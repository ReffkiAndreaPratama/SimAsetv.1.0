# MODUL 7 — MANAJEMEN DATA ASET
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 7.1 Pendahuluan

Manajemen data aset adalah inti dari SimAset. Seluruh fitur lain — QR code, maintenance, laporan — semuanya berputar di sekitar data aset yang dikelola di modul ini. Modul ini mencakup operasi CRUD (Create, Read, Update, Delete) aset secara lengkap, pengelolaan master data barang dan ruangan, serta dashboard statistik yang memberikan gambaran kondisi aset secara real-time.

Berdasarkan data aktual dari database `simset_rbtv`, saat ini terdapat 2 aset aktif (AST-001 berstatus Maintenance dan AST-002 berstatus Aktif), 2 barang aktif (BRG-001 Kamera Sony A7 dan BRG-002 Mic Wireless Rode), dan 4 ruangan (Studio 1, Studio 2, Ruang Editing, Ruang Redaksi).

---

## 7.2 Struktur Data Aset

Setiap aset dalam SimAset memiliki atribut-atribut berikut yang sesuai dengan struktur tabel `aset` di database:

| Atribut | Tipe Data | Wajib | Nilai Valid | Contoh Aktual |
|---------|-----------|-------|-------------|---------------|
| kode_aset | varchar(20) | Auto | AST-001, AST-002, ... | AST-001 |
| kode_barang | varchar(20) | ✅ | Harus ada di tabel barang | BRG-001 |
| ruangan_id | int | ✅ | Harus ada di tabel ruangan | 3 (Ruang Editing) |
| kondisi | ENUM | ✅ | Baik / Rusak Ringan / Rusak Berat | Baik |
| status | ENUM | ✅ | Aktif / Maintenance / Non-Aktif | Maintenance |
| serial_number | varchar(100) | ❌ | Unik jika diisi | ggG |
| foto | varchar(255) | ❌ | Nama file di public/foto_aset/ | 1777735186_AST-001.png |
| jumlah | int | ❌ | Min 1, default 1 | 1 |
| tanggal_perolehan | date | ✅ | Format YYYY-MM-DD | 2026-05-01 |
| harga_perolehan | decimal(15,2) | ❌ | Angka positif | NULL |
| sumber_perolehan | varchar(255) | ❌ | Pembelian/Hibah/Sumbangan/Pinjaman/Lainnya | NULL |
| keterangan | text | ❌ | Teks bebas | NULL |
| created_by | int | Auto | ID user yang menambahkan | 3 (Admin Magang) |
| updated_by | int | Auto | ID user yang terakhir mengubah | 3 |

---

## 7.3 CRUD Aset

### 7.3.1 Read — Daftar Aset (index)

Halaman daftar aset menampilkan semua aset yang aktif (tidak soft-deleted) dengan fitur filter multi-kriteria dan pagination 15 item per halaman.

```php
// app/Http/Controllers/AssetController.php
public function index(Request $request)
{
    $query = Asset::with(['barang', 'ruangan'])->orderBy('kode_aset');

    // Filter pencarian: kode aset, serial number, nama barang, kode barang, nama ruangan
    if ($request->filled('search')) {
        $s = $request->search;
        $query->where(function ($q) use ($s) {
            $q->where('kode_aset',      'like', "%{$s}%")
              ->orWhere('serial_number', 'like', "%{$s}%")
              ->orWhereHas('barang',    fn($q2) => $q2->where('nama_barang', 'like', "%{$s}%")
                                                       ->orWhere('kode_barang', 'like', "%{$s}%"))
              ->orWhereHas('ruangan',   fn($q2) => $q2->where('nama', 'like', "%{$s}%"));
        });
    }

    if ($request->filled('status'))  $query->where('status', $request->status);
    if ($request->filled('kondisi')) $query->where('kondisi', $request->kondisi);
    if ($request->filled('kategori'))
        $query->whereHas('barang', fn($q) => $q->where('kategori', $request->kategori));

    $assets = $query->paginate(15)->withQueryString();

    // Statistik keseluruhan (bukan hanya halaman ini)
    $stats = [
        'total'       => Asset::count(),       // 2
        'aktif'       => Asset::where('status', 'Aktif')->count(),       // 1
        'maintenance' => Asset::where('status', 'Maintenance')->count(), // 1
        'non_aktif'   => Asset::where('status', 'Non-Aktif')->count(),   // 0
    ];

    $kategoriList = Barang::whereHas('aset')->whereNotNull('kategori')
        ->distinct()->orderBy('kategori')->pluck('kategori');

    return view('aset.index', compact('assets', 'stats', 'kategoriList'));
}
```

**Filter yang tersedia di halaman daftar aset:**
- **search** — mencari di kode aset, serial number, nama barang, kode barang, nama ruangan
- **status** — filter Aktif / Maintenance / Non-Aktif
- **kondisi** — filter Baik / Rusak Ringan / Rusak Berat
- **kategori** — filter berdasarkan kategori barang (Kamera, Audio, dll.)

> **[GAMBAR 7.1: Tampilan halaman daftar aset menampilkan AST-001 (Maintenance, badge merah) dan AST-002 (Aktif, badge hijau) dengan filter bar di atas]**

### 7.3.2 Create — Tambah Aset Baru

```php
public function store(Request $request)
{
    $request->validate([
        'kode_barang'       => 'required|exists:barang,kode_barang',
        'ruangan_id'        => 'required|exists:ruangan,id',
        'kondisi'           => 'required|in:Baik,Rusak Ringan,Rusak Berat',
        'tanggal_perolehan' => 'required|date',
        'harga_perolehan'   => 'nullable|numeric|min:0',
        'sumber_perolehan'  => 'nullable|in:Pembelian,Hibah,Sumbangan,Pinjaman,Lainnya',
        'status'            => 'required|in:Aktif,Maintenance,Non-Aktif',
        // serial_number harus unik di seluruh tabel aset
        'serial_number'     => 'nullable|string|max:100|unique:aset,serial_number',
        'jumlah'            => 'nullable|integer|min:1',
        'keterangan'        => 'nullable|string',
        'foto'              => 'nullable|image|mimes:jpeg,png,jpg,gif|max:2048',
    ]);

    $kode_aset = Asset::generateKode(); // Contoh: AST-004

    $data = [
        'kode_aset'         => $kode_aset,
        'kode_barang'       => $request->kode_barang,
        'ruangan_id'        => $request->ruangan_id,
        'serial_number'     => $request->serial_number,
        'kondisi'           => $request->kondisi,
        'jumlah'            => $request->jumlah ?? 1,
        'tanggal_perolehan' => $request->tanggal_perolehan,
        'harga_perolehan'   => $request->harga_perolehan ?: null,
        'sumber_perolehan'  => $request->sumber_perolehan ?: null,
        'status'            => $request->status,
        'keterangan'        => $request->keterangan,
        'created_by'        => auth()->id(),
    ];

    // Handle upload foto
    if ($request->hasFile('foto')) {
        $foto      = $request->file('foto');
        $nama_foto = time() . '_' . $foto->getClientOriginalName();
        $foto->move(public_path('foto_aset'), $nama_foto);
        $data['foto'] = $nama_foto;
    }

    $asset = Asset::create($data);

    try {
        ActivityLogger::logAsset('Create',
            "Menambahkan aset baru: {$asset->nama_barang} ({$kode_aset})", $asset);
    } catch (\Exception $e) {}

    return redirect()->route('aset.index')
        ->with('success', "Aset berhasil ditambahkan. Kode: {$kode_aset}");
}
```

> **[GAMBAR 7.2: Tampilan form tambah aset baru dengan dropdown barang (BRG-001 Kamera Sony A7, BRG-002 Mic Wireless Rode) dan dropdown ruangan (Studio 1, Studio 2, Ruang Editing, Ruang Redaksi)]**

### 7.3.3 Read — Detail Aset

```php
public function show(string $kode_aset)
{
    $asset = Asset::with(['barang', 'ruangan', 'creator', 'updater'])
        ->where('kode_aset', $kode_aset)
        ->firstOrFail();

    return view('aset.show', compact('asset'));
}
```

Halaman detail menampilkan semua informasi aset secara lengkap, termasuk:
- Foto aset (jika ada)
- Nama barang dan kategori (dari relasi ke tabel barang)
- Nama ruangan (dari relasi ke tabel ruangan)
- Kondisi dan status dengan badge berwarna
- Informasi perolehan (tanggal, harga, sumber)
- Serial number
- Siapa yang menambahkan (creator) dan terakhir mengubah (updater)
- Tombol aksi: Edit, Set Maintenance, Generate QR, Hapus

**Contoh data yang ditampilkan untuk AST-001:**
- Nama Barang: Kamera Sony A7 (BRG-001)
- Kategori: Kamera
- Ruangan: Ruang Editing (Lantai 1)
- Kondisi: Baik
- Status: **Maintenance** (badge merah)
- Serial Number: ggG
- Tanggal Perolehan: 01 Mei 2026
- Ditambahkan oleh: Admin Magang

> **[GAMBAR 7.3: Tampilan halaman detail aset AST-001 (Kamera Sony A7 di Ruang Editing) dengan badge Maintenance berwarna merah dan semua informasi lengkap]**

### 7.3.4 Update — Edit Aset

```php
public function update(Request $request, string $kode_aset)
{
    $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

    $request->validate([
        // ... validasi sama dengan store
        // serial_number unique tapi exclude kode_aset saat ini
        'serial_number' => 'nullable|string|max:100|unique:aset,serial_number,'
                           . $asset->kode_aset . ',kode_aset',
        'foto'          => 'nullable|image|mimes:jpeg,png,jpg,gif|max:2048',
    ]);

    $data = [/* ... field yang diupdate ... */
        'updated_by' => auth()->id(),
    ];

    // Handle foto baru: hapus foto lama, simpan foto baru
    if ($request->hasFile('foto')) {
        if ($asset->foto && file_exists(public_path('foto_aset/' . $asset->foto))) {
            unlink(public_path('foto_aset/' . $asset->foto));
        }
        $foto = $request->file('foto');
        $nama_foto = time() . '_' . $foto->getClientOriginalName();
        $foto->move(public_path('foto_aset'), $nama_foto);
        $data['foto'] = $nama_foto;
    }

    // Handle hapus foto tanpa upload baru
    if ($request->input('remove_photo') == '1' && $asset->foto) {
        if (file_exists(public_path('foto_aset/' . $asset->foto))) {
            unlink(public_path('foto_aset/' . $asset->foto));
        }
        $data['foto'] = null;
    }

    $asset->update($data);

    ActivityLogger::logAsset('Update',
        "Mengupdate aset: {$asset->nama_barang} ({$kode_aset})", $asset);

    return redirect()->route('aset.show', $kode_aset)
        ->with('success', 'Data aset berhasil diperbarui.');
}
```

**Catatan dari data aktual:** Log id=17 (`Update: Mengupdate aset: Kamera Sony A7 (AST-001)`) adalah hasil dari operasi update ini, yang mengubah status AST-001 menjadi Maintenance pada 2026-05-02 07:42:40.

### 7.3.5 Delete — Hapus Aset (Soft Delete)

```php
public function destroy(string $kode_aset)
{
    $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();
    $nama  = $asset->nama_barang;
    $asset->delete(); // Soft delete: hanya set deleted_at

    ActivityLogger::logAsset('Delete',
        "Menghapus aset: {$nama} ({$kode_aset})", $asset);

    return redirect()->route('aset.index')
        ->with('success', "Aset '{$nama}' ({$kode_aset}) berhasil dihapus.");
}
```

**Catatan dari data aktual:** Log id=20 (`Delete: Menghapus aset: printer epson l200 (AST-003)`) adalah hasil dari operasi ini pada 2026-05-02 08:19:54. AST-003 sekarang memiliki `deleted_at = '2026-05-02 08:19:54'` dan tidak muncul di daftar aset normal.

> **[GAMBAR 7.4: Tampilan modal konfirmasi hapus aset dengan pesan "Apakah Anda yakin ingin menghapus aset AST-001?"]**

---

## 7.4 Batch Delete

Fitur batch delete memungkinkan penghapusan beberapa aset sekaligus dari halaman daftar dengan mencentang checkbox di setiap baris.

```php
public function batchDestroy(Request $request)
{
    $kodes = $request->input('kodes', []);
    $count = 0;

    foreach ($kodes as $kode) {
        $asset = Asset::where('kode_aset', $kode)->first();
        if ($asset) {
            $asset->delete();
            $count++;
            try {
                ActivityLogger::logAsset('Delete',
                    "Batch delete: {$asset->nama_barang} ({$kode})", $asset);
            } catch (\Exception $e) {}
        }
    }

    return redirect()->route('aset.index')
        ->with('success', "Berhasil menghapus {$count} aset.");
}
```

---

## 7.5 Upload dan Manajemen Foto Aset

Foto aset disimpan di direktori `public/foto_aset/` dengan nama file format `{timestamp}_{nama_file_asli}`.

**Contoh dari data aktual:** AST-003 memiliki foto `1777735186_AST-001.png` yang tersimpan di `public/foto_aset/`. Meskipun AST-003 sudah di-soft delete, file foto masih ada di filesystem.

**Validasi upload:**
```php
'foto' => 'nullable|image|mimes:jpeg,png,jpg,gif|max:2048'
// Format: JPEG, PNG, JPG, GIF
// Ukuran maksimal: 2MB (2048 KB)
```

**Menampilkan foto di Blade template:**
```blade
@if($asset->foto)
    <img src="{{ asset('foto_aset/' . $asset->foto) }}"
         alt="Foto {{ $asset->nama_barang }}"
         class="w-full h-48 object-cover rounded-lg">
@else
    <div class="w-full h-48 bg-gray-100 flex items-center justify-center rounded-lg">
        <span class="text-gray-400 text-sm">Tidak ada foto</span>
    </div>
@endif
```

---

## 7.6 Master Data Barang

### 7.6.1 Kategori yang Tersedia

Berdasarkan ENUM di tabel `barang`, kategori yang valid adalah:
- **Kamera** — contoh: BRG-001 Kamera Sony A7
- **Audio** — contoh: BRG-002 Mic Wireless Rode
- **Komputer** — laptop, PC, monitor
- **Lighting** — lampu studio, softbox
- **Furniture** — meja, kursi, rak
- **Peralatan Kantor** — contoh: BRG-003 printer epson l200 (soft-deleted)

### 7.6.2 Validasi Tambah/Edit Barang

```php
$request->validate([
    'nama_barang' => 'required|string|max:150',
    'kategori'    => 'required|in:Kamera,Audio,Komputer,Lighting,Furniture,Peralatan Kantor',
    'status'      => 'required|in:aktif,nonaktif',
    'keterangan'  => 'nullable|string|max:1000',
]);
```

### 7.6.3 Proteksi Hapus Barang

Barang tidak dapat di-hard-delete jika masih ada aset yang merujuk (FK RESTRICT). Di level aplikasi, soft delete digunakan sehingga barang hanya ditandai sebagai dihapus tanpa benar-benar menghapus record.

> **[GAMBAR 7.5: Tampilan halaman daftar barang menampilkan BRG-001 (Kamera Sony A7, Kamera) dan BRG-002 (Mic Wireless Rode, Audio) dengan badge status Aktif]**

---

## 7.7 Master Data Ruangan

### 7.7.1 Validasi Tambah/Edit Ruangan

```php
$request->validate([
    'nama'       => 'required|string|max:255',
    'lantai'     => 'nullable|string|max:50',
    'keterangan' => 'nullable|string|max:1000',
]);
```

### 7.7.2 Proteksi Hapus Ruangan Berisi Aset

```php
public function destroy(Ruangan $ruangan)
{
    $jumlahAset = $ruangan->assets()->count();
    if ($jumlahAset > 0) {
        return redirect()->route('ruangan.index')
            ->with('error',
                "Ruangan '{$ruangan->nama}' tidak bisa dihapus karena masih " .
                "memiliki {$jumlahAset} aset terdaftar.");
    }
    $nama = $ruangan->nama;
    $ruangan->delete();
    return redirect()->route('ruangan.index')
        ->with('success', "Ruangan '{$nama}' berhasil dihapus.");
}
```

**Contoh nyata:** Ruang Editing (id=3) tidak dapat dihapus karena masih memiliki 2 aset (AST-001 dan AST-002). Jika dicoba, akan muncul pesan error: "Ruangan 'Ruang Editing' tidak bisa dihapus karena masih memiliki 2 aset terdaftar."

> **[GAMBAR 7.6: Tampilan halaman daftar ruangan dengan 4 ruangan aktual, menampilkan jumlah aset di masing-masing ruangan (Ruang Editing: 2 aset)]**

---

## 7.8 Dashboard Statistik

```php
// app/Http/Controllers/DashboardController.php
public function index()
{
    // Statistik berdasarkan data aktual
    $totalAset       = Asset::count();       // 2
    $asetAktif       = Asset::where('status', 'Aktif')->count();       // 1
    $asetNonaktif    = Asset::where('status', 'Non-Aktif')->count();   // 0
    $asetMaintenance = Asset::where('status', 'Maintenance')->count(); // 1
    $asetRusak       = Asset::whereIn('kondisi', ['Rusak Ringan', 'Rusak Berat'])->count(); // 0
    $totalBarang     = Barang::count();   // 2
    $totalRuangan    = Ruangan::count();  // 4

    $now = Carbon::now();
    $asetBulanIni = Asset::whereMonth('created_at', $now->month)
        ->whereYear('created_at', $now->year)->count(); // 2 (AST-001 dan AST-002 dibuat Mei 2026)

    // Data untuk chart distribusi kondisi
    $kondisiDistribusi = Asset::select('kondisi', DB::raw('count(*) as total'))
        ->whereNotNull('kondisi')->groupBy('kondisi')->get();
    // Hasil: [{'kondisi': 'Baik', 'total': 2}]

    // Data untuk chart top 5 kategori
    $kategoriDistribusi = Asset::select('barang.kategori', DB::raw('count(*) as total'))
        ->join('barang', 'aset.kode_barang', '=', 'barang.kode_barang')
        ->whereNotNull('barang.kategori')
        ->groupBy('barang.kategori')
        ->orderByDesc('total')->limit(5)->get();
    // Hasil: [{'kategori': 'Kamera', 'total': 2}]

    $recentAssets = Asset::with(['barang', 'ruangan'])
        ->orderByDesc('created_at')->take(10)->get();

    return view('dashboard', compact(
        'totalAset', 'asetAktif', 'asetNonaktif', 'asetMaintenance', 'asetRusak',
        'totalBarang', 'totalRuangan', 'asetBulanIni',
        'kondisiDistribusi', 'kategoriDistribusi', 'recentAssets'
    ));
}
```

> **[GAMBAR 7.7: Tampilan dashboard SimAset dengan 6 summary cards (Total Aset: 2, Aktif: 1, Maintenance: 1, Non-Aktif: 0, Rusak: 0, Bulan Ini: 2) dan chart distribusi kondisi]**

---

## 7.9 Pengujian Manajemen Aset

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Lihat daftar aset | GET /aset | AST-001 dan AST-002 tampil | ✅ |
| 2 | Filter status Maintenance | status=Maintenance | Hanya AST-001 tampil | ✅ |
| 3 | Filter status Aktif | status=Aktif | Hanya AST-002 tampil | ✅ |
| 4 | Cari "Kamera" | search=Kamera | AST-001 dan AST-002 tampil | ✅ |
| 5 | Tambah aset valid | BRG-001, Ruang Editing, Baik, Aktif, 2026-05-04 | Aset tersimpan dengan kode AST-004 | ✅ |
| 6 | Tambah aset tanpa barang | kode_barang kosong | Error validasi | ✅ |
| 7 | Tambah aset serial duplikat | serial_number=ggG (sudah dipakai AST-001) | Error "sudah terdaftar" | ✅ |
| 8 | Upload foto valid | File .jpg < 2MB | Foto tersimpan di public/foto_aset/ | ✅ |
| 9 | Upload foto format salah | File .pdf | Error "format tidak valid" | ✅ |
| 10 | Lihat detail AST-001 | GET /aset/AST-001 | Detail lengkap tampil, status Maintenance | ✅ |
| 11 | Edit AST-002 | Ubah kondisi ke Rusak Ringan | Data terupdate, log Update tercatat | ✅ |
| 12 | Hapus aset | DELETE /aset/AST-002 | Soft delete, tidak muncul di daftar | ✅ |
| 13 | Hapus Ruang Editing | DELETE /ruangan/3 | Error "masih memiliki 2 aset" | ✅ |
| 14 | Hapus Studio 1 (kosong) | DELETE /ruangan/1 | Ruangan terhapus | ✅ |

---

## 7.10 Kesimpulan Modul

Modul 7 ini telah membahas implementasi manajemen data aset SimAset secara menyeluruh menggunakan data aktual dari database. CRUD aset diimplementasikan dengan validasi yang ketat, auto-generate kode gap-filling, upload foto, dan pencatatan audit log otomatis. Master data barang dan ruangan dikelola dengan proteksi yang tepat untuk menjaga integritas data. Dashboard statistik memberikan gambaran kondisi aset secara real-time.

---

*Kembali ke: [Modul 6 — Autentikasi dan Hak Akses](MODUL_06_AUTENTIKASI_HAK_AKSES.md)*
*Lanjut ke: [Modul 8 — QR Code dan Maintenance](MODUL_08_QRCODE_MAINTENANCE.md)*
