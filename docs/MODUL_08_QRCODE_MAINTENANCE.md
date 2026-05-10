# MODUL 8 — QR CODE DAN MAINTENANCE TRACKING
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 8.1 Pendahuluan

QR code dan maintenance tracking adalah dua fitur yang paling membedakan SimAset dari sistem pencatatan aset konvensional. QR code memungkinkan identifikasi aset yang sangat cepat — cukup pindai kode dengan kamera smartphone dan informasi aset langsung muncul di layar, tanpa perlu membuka aplikasi atau mencari di daftar. Maintenance tracking memastikan setiap proses perbaikan aset terdokumentasi dengan baik dan pihak terkait mendapat notifikasi otomatis.

Berdasarkan data aktual, AST-001 (Kamera Sony A7 di Ruang Editing) saat ini berstatus **Maintenance** — ini adalah contoh nyata penggunaan fitur maintenance tracking di sistem. File QR code yang sudah di-generate tersimpan di `public/qr_codes/` (contoh: `qr_AST-001_1777648103.png` dan `qr_BRG-002_1777492964.png`).

---

## 8.2 Arsitektur QR Code

SimAset menggunakan dua pendekatan berbeda untuk generate QR code, masing-masing untuk kebutuhan yang berbeda:

```
┌─────────────────────────────────────────────────────────────┐
│                    QR CODE SYSTEM                           │
│                                                             │
│  1. SimpleSoftwareIO\QrCode (SVG — lokal, tanpa internet)   │
│     ├── Batch print: QrCode::size(120)->format('svg')       │
│     └── Single print: QrCode::size(200)->format('svg')      │
│                                                             │
│  2. qrserver.com API (PNG — butuh internet)                 │
│     └── Generate & simpan ke public/qr_codes/               │
│         Format: qr_{kode_aset}_{timestamp}.png              │
│                                                             │
│  QR Code Content: URL ke /aset/{kode_aset}/detail           │
│  (halaman publik, dapat diakses TANPA login)                │
└─────────────────────────────────────────────────────────────┘
```

**Mengapa dua pendekatan?**
- SVG via SimpleSoftwareIO digunakan untuk halaman cetak karena kualitas vektor yang tajam di semua ukuran dan tidak memerlukan koneksi internet
- PNG via qrserver.com digunakan untuk file yang disimpan di filesystem karena format PNG lebih kompatibel untuk dicetak via printer fisik

---

## 8.3 Generate QR Code

### 8.3.1 Generate QR Code PNG (Simpan ke Filesystem)

```php
// app/Http/Controllers/AssetController.php
public function generateQr(string $kode_aset)
{
    $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

    // Cek apakah QR code sudah ada
    $qrDir = public_path('qr_codes');
    $files = file_exists($qrDir) ? glob($qrDir . '/qr_' . $kode_aset . '*.png') : [];
    if (!empty($files)) {
        return redirect()->back()->with('info', 'QR Code sudah ada.');
    }

    $success = $this->generateQrCodeImage($asset);

    return $success
        ? redirect()->back()->with('success', 'QR Code berhasil di-generate.')
        : redirect()->back()->with('error', 'Gagal generate QR Code. Pastikan koneksi internet tersedia.');
}

private function generateQrCodeImage(Asset $asset): bool
{
    try {
        $qrDir = public_path('qr_codes');
        if (!file_exists($qrDir)) mkdir($qrDir, 0755, true);

        // URL yang di-encode ke dalam QR code
        $qrData   = route('assets.detail', $asset->kode_aset);
        // Contoh: http://127.0.0.1:8000/aset/AST-001/detail

        $filename = 'qr_' . $asset->kode_aset . '_' . time() . '.png';
        $filepath = $qrDir . '/' . $filename;
        // Contoh: public/qr_codes/qr_AST-001_1777648103.png

        // Panggil API eksternal qrserver.com
        $qrUrl   = 'https://api.qrserver.com/v1/create-qr-code/?size=300x300&format=png&data='
                   . urlencode($qrData);
        $qrImage = @file_get_contents($qrUrl);

        if ($qrImage === false) return false;

        file_put_contents($filepath, $qrImage);
        return true;
    } catch (\Exception $e) {
        \Log::error('QR Code generation failed: ' . $e->getMessage());
        return false;
    }
}
```

**Catatan dari data aktual:** File `qr_AST-001_1777648103.png` dan `qr_BRG-002_1777492964.png` yang ada di `public/qr_codes/` adalah hasil dari proses generate ini.

> **[GAMBAR 8.1: Contoh QR code yang di-generate untuk aset AST-001, menampilkan pola QR code dengan URL http://127.0.0.1:8000/aset/AST-001/detail]**

### 8.3.2 Generate QR Code SVG untuk Cetak

```php
// app/Http/Controllers/QrCodeController.php
public function download(string $kode_aset)
{
    $asset = Asset::with(['barang', 'ruangan'])
        ->where('kode_aset', $kode_aset)->firstOrFail();

    // Generate SVG QR code — tidak butuh internet
    $qrCode   = QrCode::size(200)->format('svg')
        ->generate(route('assets.detail', $asset->kode_aset));
    $autoPrint = true; // Trigger auto-print dialog di browser

    return view('qrcode.single', compact('asset', 'qrCode', 'autoPrint'));
}
```

> **[GAMBAR 8.2: Tampilan halaman cetak QR code individual untuk AST-001, menampilkan QR code besar dengan nama barang "Kamera Sony A7" dan kode "AST-001" di bawahnya]**

---

## 8.4 Batch Print QR Code

Fitur batch print memungkinkan mencetak QR code untuk beberapa aset sekaligus dalam satu halaman, sangat berguna saat ada banyak aset baru yang perlu diberi label QR.

```php
public function batchPrint(Request $request)
{
    $kodes = $request->input('asset_ids', []);

    // Handle comma-separated string dari GET query
    if (is_string($kodes) && !empty($kodes)) {
        $kodes = explode(',', $kodes);
    }

    if (empty($kodes)) {
        return redirect()->back()->with('error', 'Tidak ada aset yang dipilih.');
    }

    $assets = Asset::with(['barang', 'ruangan'])
        ->whereIn('kode_aset', $kodes)->get();

    $qrcodes = [];
    foreach ($assets as $asset) {
        // Generate SVG QR code untuk setiap aset
        $qrcodes[$asset->kode_aset] = QrCode::size(120)
            ->format('svg')
            ->generate(route('assets.detail', $asset->kode_aset));
    }

    return view('qrcode.batch_print', compact('assets', 'qrcodes'));
}
```

> **[GAMBAR 8.3: Tampilan halaman batch print QR code menampilkan grid QR code untuk AST-001 dan AST-002 dalam satu halaman siap cetak]**

---

## 8.5 Scanner QR Code

Halaman scanner QR code memungkinkan pengguna memindai QR code menggunakan kamera perangkat dan langsung mendapatkan informasi aset tanpa perlu mengetik kode secara manual.

### 8.5.1 Halaman Scanner

```php
// Route
Route::get('/qrcode/scanner', [QrCodeController::class, 'scanner'])->name('qrcode.scanner');
Route::get('/qrcode/search',  [QrCodeController::class, 'search'])->name('qrcode.search');
```

### 8.5.2 Endpoint AJAX untuk Pencarian

```php
public function search(Request $request)
{
    $kode = trim($request->query('code', ''));

    if (!$kode) {
        return response()->json(['success' => false, 'message' => 'Kode tidak boleh kosong']);
    }

    // Cari exact match dulu
    $asset = Asset::with(['barang', 'ruangan'])
        ->where('kode_aset', $kode)->first();

    // Jika tidak ditemukan, cari partial match
    if (!$asset) {
        $asset = Asset::with(['barang', 'ruangan'])
            ->where('kode_aset', 'like', "%{$kode}%")->first();
    }

    if (!$asset) {
        return response()->json(['success' => false, 'message' => 'Aset tidak ditemukan']);
    }

    return response()->json([
        'success' => true,
        'data'    => [
            'kode_aset'     => $asset->kode_aset,       // 'AST-001'
            'nama_barang'   => $asset->barang?->nama_barang ?? '—', // 'Kamera Sony A7'
            'kategori'      => $asset->barang?->kategori ?? '—',    // 'Kamera'
            'ruangan'       => $asset->ruangan?->nama ?? '—',       // 'Ruang Editing'
            'kondisi'       => $asset->kondisi ?? '—',  // 'Baik'
            'status'        => $asset->status ?? '—',   // 'Maintenance'
            'serial_number' => $asset->serial_number ?? '—', // 'ggG'
            'url'           => route('aset.show', $asset->kode_aset),
        ],
    ]);
}
```

> **[GAMBAR 8.4: Tampilan halaman scanner QR code dengan area kamera aktif dan panel hasil pencarian menampilkan informasi AST-001]**

---

## 8.6 Halaman Detail Publik (Akses Tanpa Login)

Halaman ini adalah tujuan dari setiap QR code yang di-generate. Halaman ini dapat diakses oleh siapapun tanpa perlu login, sehingga teknisi atau siapapun yang menemukan aset dapat langsung mengetahui informasinya hanya dengan memindai QR code.

```php
// Route — TIDAK dibungkus middleware 'auth'
Route::get('/aset/{kode_aset}/detail', [AssetController::class, 'detail'])
    ->name('assets.detail');

// Controller
public function detail(string $kode_aset)
{
    $asset = Asset::with(['barang', 'ruangan', 'creator'])
        ->where('kode_aset', $kode_aset)
        ->firstOrFail();
    return view('aset.show', compact('asset'));
}
```

**Contoh URL yang di-encode ke QR code AST-001:**
```
http://[domain]/aset/AST-001/detail
```

Saat dipindai, halaman ini menampilkan:
- Nama barang: Kamera Sony A7
- Kategori: Kamera
- Ruangan: Ruang Editing
- Kondisi: Baik
- Status: **Maintenance** (badge merah)
- Serial Number: ggG
- Tanggal Perolehan: 01 Mei 2026

---

## 8.7 Maintenance Tracking

### 8.7.1 Dashboard Maintenance

```php
// app/Http/Controllers/MaintenanceController.php
public function index(Request $request)
{
    $query = Asset::with(['barang', 'ruangan'])
        ->where('status', 'Maintenance');

    if ($request->filled('search')) {
        $s = $request->search;
        $query->where(function ($q) use ($s) {
            $q->where('kode_aset', 'like', "%{$s}%")
              ->orWhereHas('barang', fn($q2) => $q2->where('nama_barang', 'like', "%{$s}%"));
        });
    }

    if ($request->filled('kondisi')) $query->where('kondisi', $request->kondisi);

    $assets = $query->orderBy('updated_at', 'desc')->paginate(15)->withQueryString();

    // Statistik maintenance
    $totalMaintenance = Asset::where('status', 'Maintenance')->count(); // 1 (AST-001)
    $rusakBerat       = Asset::where('kondisi', 'Rusak Berat')->count(); // 0
    $rusakRingan      = Asset::where('kondisi', 'Rusak Ringan')->count(); // 0
    $totalRusak       = $rusakBerat + $rusakRingan; // 0

    return view('maintenance.index', compact(
        'assets', 'totalMaintenance', 'rusakBerat', 'rusakRingan', 'totalRusak'
    ));
}
```

**Berdasarkan data aktual:** Dashboard maintenance saat ini menampilkan 1 aset — AST-001 (Kamera Sony A7 di Ruang Editing) yang berstatus Maintenance dengan kondisi Baik.

> **[GAMBAR 8.5: Tampilan dashboard maintenance menampilkan AST-001 (Kamera Sony A7, Ruang Editing) dengan badge Maintenance dan statistik: Total Maintenance=1, Rusak Berat=0, Rusak Ringan=0]**

### 8.7.2 Set Aset ke Maintenance

```php
public function setMaintenance(Request $request, string $kode_aset)
{
    $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

    $request->validate([
        'keterangan' => 'nullable|string|max:500',
    ]);

    $asset->update([
        'status'     => 'Maintenance',
        'keterangan' => $request->keterangan ?? $asset->keterangan,
        'updated_by' => auth()->id(),
    ]);

    try {
        ActivityLogger::logAsset('Update',
            "Aset masuk maintenance: {$asset->nama_barang} ({$kode_aset})", $asset);
    } catch (\Exception $e) {}

    return redirect()->back()
        ->with('success', "Aset {$kode_aset} berhasil ditandai sebagai Maintenance.");
}
```

### 8.7.3 Selesaikan Maintenance

```php
public function complete(Request $request, string $kode_aset)
{
    $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

    $request->validate([
        'kondisi'    => 'required|in:Baik,Rusak Ringan,Rusak Berat',
        'keterangan' => 'nullable|string|max:500',
    ]);

    $asset->update([
        'status'     => 'Aktif',
        'kondisi'    => $request->kondisi,
        'keterangan' => $request->keterangan ?? $asset->keterangan,
        'updated_by' => auth()->id(),
    ]);

    try {
        ActivityLogger::logAsset('Update',
            "Maintenance selesai: {$asset->nama_barang} ({$kode_aset}) — kondisi: {$request->kondisi}",
            $asset);
    } catch (\Exception $e) {}

    // Kirim email ke semua Admin aktif
    try {
        $admins = User::where('role', 'admin')->where('is_active', 1)->get();
        // Berdasarkan data aktual: Admin Magang (magangrbtv@gmail.com)
        foreach ($admins as $admin) {
            Mail::to($admin->email)->send(new MaintenanceAlert($asset, 'selesai'));
        }
    } catch (\Exception $e) {
        // Email gagal tidak menghentikan proses
    }

    return redirect()->route('maintenance.index')
        ->with('success', "Maintenance aset {$kode_aset} selesai. Status kembali Aktif.");
}
```

> **[GAMBAR 8.6: Tampilan form selesaikan maintenance untuk AST-001 dengan dropdown pilihan kondisi akhir (Baik/Rusak Ringan/Rusak Berat) dan field keterangan]**

---

## 8.8 Email Notifikasi Maintenance

### 8.8.1 Konfigurasi Mail

Untuk development, email tidak benar-benar terkirim tetapi tercatat di `storage/logs/laravel.log`:

```env
MAIL_MAILER=log
MAIL_FROM_ADDRESS="noreply@rbtv.co.id"
MAIL_FROM_NAME="SimAset RBTV"
```

Untuk production dengan Gmail:
```env
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password  # App Password, bukan password biasa
MAIL_ENCRYPTION=tls
```

### 8.8.2 MaintenanceAlert Mail Class

```php
// app/Mail/MaintenanceAlert.php
class MaintenanceAlert extends Mailable
{
    public function __construct(
        public Asset $asset,
        public string $tipe = 'selesai'
    ) {}

    public function envelope(): Envelope
    {
        return new Envelope(
            subject: "SimAset — Maintenance {$this->tipe}: {$this->asset->kode_aset}",
        );
    }

    public function content(): Content
    {
        return new Content(
            view: 'emails.maintenance-alert',
        );
    }
}
```

Email yang dikirim ke Admin Magang (magangrbtv@gmail.com) berisi:
- Kode aset: AST-001
- Nama barang: Kamera Sony A7
- Ruangan: Ruang Editing
- Kondisi akhir: (sesuai input)
- Waktu penyelesaian

> **[GAMBAR 8.7: Contoh tampilan email notifikasi maintenance selesai yang diterima Admin, menampilkan informasi aset AST-001 dan kondisi akhir]**

---

## 8.9 Pengujian QR Code dan Maintenance

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Generate QR AST-001 (online) | Klik Generate QR | File PNG tersimpan di qr_codes/ | ✅ |
| 2 | Generate QR (offline) | Tanpa internet | Pesan error, QR tidak ter-generate | ✅ |
| 3 | Cetak QR individual AST-001 | Klik Cetak QR | Halaman cetak terbuka, auto-print | ✅ |
| 4 | Batch print AST-001 + AST-002 | Pilih 2 aset, Print QR | Halaman batch print dengan 2 QR | ✅ |
| 5 | Scan QR AST-001 | Pindai QR code | Browser buka /aset/AST-001/detail | ✅ |
| 6 | Akses detail tanpa login | GET /aset/AST-001/detail | Halaman detail tampil (publik) | ✅ |
| 7 | Scanner web — AST-001 | Input kode AST-001 | Info aset tampil (Maintenance) | ✅ |
| 8 | Scanner web — kode tidak ada | Input AST-999 | "Aset tidak ditemukan" | ✅ |
| 9 | Set AST-002 ke maintenance | Klik Set Maintenance | Status berubah ke Maintenance | ✅ |
| 10 | Dashboard maintenance | GET /maintenance | AST-001 tampil di daftar | ✅ |
| 11 | Selesaikan maintenance AST-001 | Pilih kondisi Baik, klik Selesai | Status kembali Aktif | ✅ |
| 12 | Email notifikasi | Selesaikan maintenance | Email tercatat di laravel.log | ✅ |

---

## 8.10 Kesimpulan Modul

Modul 8 ini telah membahas implementasi QR code dan maintenance tracking SimAset secara menyeluruh menggunakan data aktual. QR code menggunakan dua pendekatan (SVG lokal dan PNG via API) untuk kebutuhan yang berbeda. Halaman detail publik memungkinkan identifikasi aset tanpa login. Maintenance tracking dengan notifikasi email otomatis memastikan setiap proses perbaikan terdokumentasi dan pihak terkait selalu mendapat informasi terkini.

---

*Kembali ke: [Modul 7 — Manajemen Aset](MODUL_07_MANAJEMEN_ASET.md)*
*Lanjut ke: [Modul 9 — Import, Export, dan Laporan](MODUL_09_IMPORT_EXPORT_LAPORAN.md)*
