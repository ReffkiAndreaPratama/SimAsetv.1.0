# MODUL 9 — IMPORT, EXPORT, DAN LAPORAN
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 9.1 Pendahuluan

Fitur import, export, dan laporan adalah komponen yang sangat meningkatkan produktivitas pengelola aset. Import memungkinkan penambahan data massal dari file Excel/CSV tanpa harus input satu per satu — sangat berguna saat ada banyak aset baru yang perlu didaftarkan sekaligus. Export memungkinkan pengambilan data dalam format yang dapat diolah lebih lanjut di Excel atau dicetak sebagai laporan formal. Laporan menghasilkan dokumen siap cetak dalam format PDF untuk keperluan administrasi dan audit.

---

## 9.2 Import Aset dari Excel/CSV

### 9.2.1 Format Template Import Aset

Template CSV yang dapat diunduh dari `/import/template?type=aset`:

| Kolom | Header | Wajib | Contoh | Keterangan |
|-------|--------|-------|--------|------------|
| A | Kode Barang | ✅ | BRG-001 | Harus ada di tabel barang |
| B | Nama Ruangan | ❌ | Ruang Editing | Harus sama persis dengan nama di tabel ruangan |
| C | Kondisi | ❌ | Baik | Baik / Rusak Ringan / Rusak Berat |
| D | Status | ❌ | Aktif | Aktif / Maintenance / Non-Aktif |
| E | Jumlah | ❌ | 1 | Angka bulat positif |
| F | Tanggal Perolehan | ❌ | 2026-05-01 | Format YYYY-MM-DD |
| G | Harga Perolehan | ❌ | 5000000 | Angka tanpa titik/koma ribuan |
| H | Sumber Perolehan | ❌ | Pembelian | Pembelian/Hibah/Sumbangan/Pinjaman/Lainnya |
| I | Keterangan | ❌ | Catatan | Teks bebas |

**Contoh isi file CSV:**
```csv
Kode Barang;Nama Ruangan;Kondisi;Status;Jumlah;Tanggal Perolehan;Harga Perolehan;Sumber Perolehan;Keterangan
BRG-001;Ruang Editing;Baik;Aktif;1;2026-05-01;15000000;Pembelian;Kamera utama studio
BRG-002;Studio 1;Baik;Aktif;2;2026-04-15;;Hibah;Mic wireless untuk anchor
BRG-001;Studio 2;Rusak Ringan;Maintenance;1;2026-03-20;;;Perlu perbaikan lensa
```

> **[GAMBAR 9.1: Tampilan halaman import aset dengan form upload file, pilihan tipe import (Aset/Barang), dan link download template]**

### 9.2.2 Proses Import di Controller

```php
// app/Http/Controllers/ImportController.php
private function validateAndCreateAsset($row, $lineNumber)
{
    try {
        // Validasi kolom A (kode_barang) wajib
        if (empty($row[0])) {
            return ['success' => false,
                    'error' => "Baris $lineNumber: Kode Barang wajib diisi"];
        }

        $kodeBarang = trim($row[0]);

        // Cek apakah barang ada di database
        $barang = Barang::where('kode_barang', $kodeBarang)->first();
        if (!$barang) {
            return ['success' => false,
                    'error' => "Baris $lineNumber: Kode Barang '$kodeBarang' tidak ditemukan"];
        }

        // Cari ruangan berdasarkan nama (kolom B)
        $ruanganId = null;
        if (!empty($row[1])) {
            $ruangan   = Ruangan::where('nama', trim($row[1]))->first();
            $ruanganId = $ruangan?->id;
            // Jika nama ruangan tidak ditemukan, ruangan_id = null (tidak error)
        }

        $kode_aset = Asset::generateKode();

        Asset::create([
            'kode_aset'         => $kode_aset,
            'kode_barang'       => $kodeBarang,
            'ruangan_id'        => $ruanganId,
            'kondisi'           => $this->normalizeKondisi(trim($row[2] ?? 'Baik')),
            'status'            => $this->normalizeStatus(trim($row[3] ?? 'Aktif')),
            'jumlah'            => intval($row[4] ?? 1),
            'tanggal_perolehan' => $this->parseDate(trim($row[5] ?? null)),
            'harga_perolehan'   => !empty($row[6])
                ? (float) str_replace(['.', ','], ['', '.'], trim($row[6]))
                : null,
            'sumber_perolehan'  => !empty($row[7]) ? trim($row[7]) : null,
            'keterangan'        => trim($row[8] ?? ''),
            'created_by'        => auth()->id(),
        ]);

        return ['success' => true];

    } catch (\Exception $e) {
        return ['success' => false, 'error' => "Baris $lineNumber: " . $e->getMessage()];
    }
}
```

### 9.2.3 Normalisasi Nilai

```php
// Normalisasi kondisi — case-insensitive, support berbagai format
private function normalizeKondisi($value): string
{
    $map = [
        'baik'         => 'Baik',
        'rusak ringan' => 'Rusak Ringan',
        'rusak_ringan' => 'Rusak Ringan',
        'rusak berat'  => 'Rusak Berat',
        'rusak_berat'  => 'Rusak Berat',
    ];
    return $map[strtolower(str_replace('_', ' ', $value))] ?? 'Baik';
}

// Normalisasi status
private function normalizeStatus($value): string
{
    $map = [
        'aktif'       => 'Aktif',
        'active'      => 'Aktif',
        'maintenance' => 'Maintenance',
        'non-aktif'   => 'Non-Aktif',
        'nonaktif'    => 'Non-Aktif',
        'non aktif'   => 'Non-Aktif',
    ];
    return $map[strtolower($value)] ?? 'Aktif';
}
```

### 9.2.4 Penanganan Error per Baris

Sistem melanjutkan proses import meskipun ada baris yang error — baris yang valid tetap diimport, baris yang error dilaporkan:

```
// Contoh output setelah import file dengan 5 baris:
"Berhasil import 3 data aset.
Error: Baris 2: Kode Barang 'BRG-999' tidak ditemukan,
       Baris 4: Kode Barang wajib diisi"
```

> **[GAMBAR 9.2: Tampilan hasil import dengan pesan sukses "Berhasil import 3 data aset" dan daftar error untuk baris yang gagal]**

---

## 9.3 Import Barang dari Excel/CSV

Format template CSV untuk import barang (`/import/template?type=barang`):

| Kolom | Header | Wajib | Contoh |
|-------|--------|-------|--------|
| A | Kode Barang | ✅ | BRG-004 |
| B | Nama Barang | ✅ | Laptop Dell XPS |
| C | Kategori | ❌ | Komputer |
| D | Status | ❌ | aktif |

---

## 9.4 Export Aset ke Excel

### 9.4.1 AssetExportFile Class

```php
// app/Exports/AssetExportFile.php
class AssetExportFile implements
    FromCollection, WithHeadings, WithStyles,
    ShouldAutoSize, WithTitle, WithEvents
{
    protected $filters = [];

    public function __construct($filters = []) {
        $this->filters = $filters;
    }

    public function title(): string { return 'Data Aset'; }

    public function collection()
    {
        $query = Asset::with(['barang', 'ruangan', 'creator']);

        // Terapkan filter
        if (!empty($this->filters['status']))
            $query->where('status', $this->filters['status']);
        if (!empty($this->filters['kondisi']))
            $query->where('kondisi', $this->filters['kondisi']);
        if (!empty($this->filters['ruangan_id']))
            $query->where('ruangan_id', $this->filters['ruangan_id']);
        if (!empty($this->filters['date_from']))
            $query->whereDate('tanggal_perolehan', '>=', $this->filters['date_from']);
        if (!empty($this->filters['date_to']))
            $query->whereDate('tanggal_perolehan', '<=', $this->filters['date_to']);

        $no = 1;
        return $query->orderBy('kode_aset')->get()->map(function ($asset) use (&$no) {
            return [
                $no++,
                $asset->kode_aset,
                $asset->barang?->nama_barang ?? '-',
                $asset->barang?->kategori ?? '-',
                $asset->serial_number ?? '-',
                $asset->ruangan?->nama ?? '-',
                $asset->kondisi ?? '-',
                $asset->status ?? '-',
                $asset->tanggal_perolehan?->format('d/m/Y') ?? '-',
                $asset->harga_perolehan
                    ? 'Rp ' . number_format($asset->harga_perolehan, 0, ',', '.') : '-',
                $asset->sumber_perolehan ?? '-',
                $asset->jumlah ?? 1,
                $asset->keterangan ?? '-',
                $asset->creator?->name ?? '-',
            ];
        });
    }

    public function headings(): array
    {
        return ['No', 'Kode Aset', 'Nama Barang', 'Kategori', 'Serial Number',
                'Ruangan', 'Kondisi', 'Status', 'Tanggal Perolehan',
                'Harga Perolehan', 'Sumber Perolehan', 'Jumlah', 'Keterangan', 'Dibuat Oleh'];
    }
}
```

### 9.4.2 Styling Excel

File Excel yang dihasilkan memiliki styling profesional:
- **Header row**: Background biru tua (#1A3470), teks putih, bold
- **Data rows**: Zebra striping (baris genap abu-abu muda #F8FAFC, ganjil putih)
- **Border**: Tipis antar sel, tebal di outline tabel
- **Freeze pane**: Baris header tetap terlihat saat scroll
- **Baris total**: Di bagian bawah dengan background biru tua
- **Auto-size kolom**: Lebar kolom menyesuaikan konten

> **[GAMBAR 9.3: Contoh file Excel hasil export aset dengan header biru tua, zebra striping, dan baris total di bagian bawah]**

---

## 9.5 Export Aset ke CSV

CSV export menggunakan beberapa teknik khusus untuk kompatibilitas dengan Excel Indonesia:

```php
public function exportAset(Request $request)
{
    $assets   = $query->get();
    $filename = 'laporan_aset_' . date('d-m-Y') . '.csv';

    $callback = function () use ($assets) {
        $handle = fopen('php://output', 'w');

        // UTF-8 BOM — agar Excel membaca karakter Indonesia dengan benar
        fprintf($handle, chr(0xEF) . chr(0xBB) . chr(0xBF));

        // Header laporan
        fputcsv($handle, ['LAPORAN DATA ASET BARANG KANTOR'], ';');
        fputcsv($handle, ['Rakyat Bengkulu Televisi (RBTV) — SimAset v1.0'], ';');
        fputcsv($handle, [''], ';');
        fputcsv($handle, ['Dicetak oleh', auth()->user()?->name], ';');
        fputcsv($handle, ['Tanggal cetak', date('d-m-Y H:i')], ';');
        fputcsv($handle, ['Total aset', $assets->count() . ' record'], ';');
        fputcsv($handle, [''], ';');

        // Header kolom
        fputcsv($handle, ['No', 'Kode Aset', 'Nama Barang', 'Kategori',
                          'Ruangan', 'Kondisi', 'Status', 'Jumlah',
                          'Tanggal Perolehan', 'Harga Perolehan', 'Sumber',
                          'Serial Number', 'Keterangan', 'Dibuat Oleh'], ';');

        // Data
        $no = 1;
        foreach ($assets as $item) {
            fputcsv($handle, [
                $no++, $item->kode_aset,
                $item->barang?->nama_barang ?? '-',
                $item->barang?->kategori ?? '-',
                $item->ruangan?->nama ?? '-',
                $item->kondisi ?? '-', $item->status ?? '-',
                $item->jumlah ?? 1,
                $item->tanggal_perolehan
                    ? \Carbon\Carbon::parse($item->tanggal_perolehan)->format('d-m-Y') : '-',
                $item->harga_perolehan
                    ? 'Rp ' . number_format($item->harga_perolehan, 0, ',', '.') : '-',
                $item->sumber_perolehan ?? '-',
                $item->serial_number ?? '-',
                $item->keterangan ?? '-',
                $item->creator?->name ?? '-',
            ], ';');
        }

        fclose($handle);
    };

    return response()->stream($callback, 200, [
        'Content-Type'        => 'text/csv; charset=UTF-8',
        'Content-Disposition' => "attachment; filename=\"{$filename}\"",
    ]);
}
```

**Teknik khusus yang digunakan:**
- **UTF-8 BOM** (`chr(0xEF).chr(0xBB).chr(0xBF)`) — agar Excel membaca karakter Indonesia (ä, é, dll.) dengan benar
- **Delimiter titik koma (`;`)** — lebih kompatibel dengan Excel versi Indonesia yang menggunakan koma sebagai desimal
- **`response()->stream()`** — streaming data langsung ke browser tanpa menyimpan file sementara, efisien untuk data besar

---

## 9.6 Laporan PDF

### 9.6.1 Laporan Aset (PDF Landscape)

```php
public function cetakAset(Request $request)
{
    $query = Asset::with(['barang', 'ruangan'])->orderBy('kode_aset');

    // Filter opsional
    if ($request->filled('ruangan_id')) $query->where('ruangan_id', $request->ruangan_id);
    if ($request->filled('kondisi'))    $query->where('kondisi', $request->kondisi);
    if ($request->filled('status'))     $query->where('status', $request->status);

    $assets = $query->get();
    $pdf = Pdf::loadView('laporan.aset_pdf', compact('assets'))
        ->setPaper('a4', 'landscape'); // Landscape untuk tabel yang lebar
    return $pdf->download('laporan_aset_' . date('d-m-Y') . '.pdf');
}
```

> **[GAMBAR 9.4: Contoh laporan aset PDF landscape dengan header RBTV, tabel data aset, dan footer tanggal cetak]**

### 9.6.2 Laporan Per Ruangan (PDF Portrait)

```php
public function laporanRuangan(int $id)
{
    $ruangan = Ruangan::with(['assets.barang'])->findOrFail($id);
    $assets  = $ruangan->assets()->with('barang')->orderBy('kode_aset')->get();

    $pdf = Pdf::loadView('laporan.ruangan_pdf', compact('ruangan', 'assets'))
        ->setPaper('a4', 'portrait');

    $namaFile = 'laporan_ruangan_'
        . \Illuminate\Support\Str::slug($ruangan->nama) . '_'
        . date('d-m-Y') . '.pdf';
    return $pdf->download($namaFile);
}
```

**Contoh nyata:** Laporan untuk Ruang Editing (id=3) akan menampilkan:
- Nama ruangan: Ruang Editing (Lantai 1)
- Daftar aset: AST-001 (Kamera Sony A7, Maintenance) dan AST-002 (Kamera Sony A7, Aktif)
- Total: 2 aset

> **[GAMBAR 9.5: Contoh laporan per ruangan PDF untuk Ruang Editing menampilkan AST-001 dan AST-002]**

### 9.6.3 Laporan Maintenance (PDF dan CSV)

```php
public function exportMaintenancePdf()
{
    $assets = Asset::with(['barang', 'ruangan'])
        ->where('status', 'Maintenance')
        ->orderBy('updated_at', 'desc')
        ->get();
    // Berdasarkan data aktual: hanya AST-001 (Kamera Sony A7)

    $pdf = Pdf::loadView('laporan.maintenance_pdf', compact('assets'))
        ->setPaper('a4', 'portrait');
    return $pdf->download('laporan_maintenance_' . date('d-m-Y') . '.pdf');
}
```

> **[GAMBAR 9.6: Contoh laporan maintenance PDF menampilkan AST-001 (Kamera Sony A7, Ruang Editing, kondisi Baik, status Maintenance)]**

---

## 9.7 Pengujian Import, Export, dan Laporan

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Import aset valid | CSV dengan BRG-001, Ruang Editing | Aset tersimpan dengan kode baru | ✅ |
| 2 | Import aset kode barang tidak ada | BRG-999 di kolom A | Error "Kode Barang tidak ditemukan" | ✅ |
| 3 | Import file format salah | File .pdf | Error "File harus berformat Excel atau CSV" | ✅ |
| 4 | Import barang kode duplikat | BRG-001 (sudah ada) | Error "Kode Barang sudah ada" | ✅ |
| 5 | Download template aset | GET /import/template?type=aset | File CSV template terunduh | ✅ |
| 6 | Export aset Excel tanpa filter | GET /export/aset/excel | File .xlsx dengan AST-001 dan AST-002 | ✅ |
| 7 | Export aset Excel filter Maintenance | status=Maintenance | File .xlsx hanya AST-001 | ✅ |
| 8 | Export aset PDF | GET /export/aset/pdf | File .pdf terunduh | ✅ |
| 9 | Export CSV maintenance | GET /laporan/maintenance/csv | File .csv dengan AST-001 | ✅ |
| 10 | Laporan per ruangan Ruang Editing | GET /laporan/ruangan/3 | PDF dengan AST-001 dan AST-002 | ✅ |
| 11 | Buka CSV di Excel | Buka file .csv | Karakter Indonesia terbaca benar | ✅ |

---

## 9.8 Kesimpulan Modul

Modul 9 ini telah membahas implementasi import, export, dan laporan SimAset secara menyeluruh. Import dengan validasi per baris memungkinkan penambahan data massal yang efisien. Export Excel dengan styling profesional dan PDF siap cetak memenuhi kebutuhan pelaporan formal. Teknik khusus seperti UTF-8 BOM dan delimiter titik koma memastikan kompatibilitas dengan Excel Indonesia.

---

*Kembali ke: [Modul 8 — QR Code dan Maintenance](MODUL_08_QRCODE_MAINTENANCE.md)*
*Lanjut ke: [Modul 10 — Audit Log dan Manajemen Pengguna](MODUL_10_AUDIT_LOG_USER.md)*
