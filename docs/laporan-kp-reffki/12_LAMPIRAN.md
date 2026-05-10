# LAMPIRAN

## Lampiran 1. Surat Keterangan Kerja Praktik

*[Surat keterangan pelaksanaan Kerja Praktik dari RBTV Bengkulu]*

---

## Lampiran 2. Logbook Kegiatan Kerja Praktik

| No | Tanggal | Uraian Kegiatan | Paraf Pembimbing |
|----|---------|----------------|-----------------|
| 1 | | Orientasi dan pengenalan lingkungan kerja RBTV | |
| 2 | | Observasi sistem pengelolaan aset yang berjalan | |
| 3 | | Wawancara dengan staf administrasi | |
| 4 | | Analisis kebutuhan sistem | |
| 5 | | Perancangan Use Case Diagram dan Activity Diagram | |
| 6 | | Perancangan ERD dan struktur database | |
| 7 | | Perancangan prototype antarmuka | |
| 8 | | Setup environment pengembangan (Laravel, database) | |
| 9 | | Implementasi modul autentikasi | |
| 10 | | Implementasi modul manajemen aset | |
| 11 | | Implementasi modul master data (barang, ruangan) | |
| 12 | | Implementasi fitur QR Code | |
| 13 | | Implementasi fitur maintenance | |
| 14 | | Implementasi fitur import/export | |
| 15 | | Implementasi fitur laporan | |
| 16 | | Implementasi manajemen pengguna dan audit log | |
| 17 | | Pengujian sistem dan perbaikan bug | |
| 18 | | Penyebaran kuesioner pengujian | |
| 19 | | Evaluasi dan penyempurnaan sistem | |
| 20 | | Penyusunan laporan Kerja Praktik | |

---

## Lampiran 3. Dokumentasi Kegiatan

*[Foto dokumentasi kegiatan Kerja Praktik di RBTV Bengkulu]*

---

## Lampiran 4. Tangkapan Layar Sistem SimAset

### L4.1 Halaman Login
*[Screenshot halaman login sistem SimAset]*

### L4.2 Dashboard
*[Screenshot halaman dashboard dengan statistik dan grafik]*

### L4.3 Halaman Daftar Aset
*[Screenshot halaman daftar aset dengan fitur filter dan pencarian]*

### L4.4 Halaman Tambah Aset
*[Screenshot form tambah aset baru]*

### L4.5 Halaman Detail Aset
*[Screenshot halaman detail aset dengan QR Code]*

### L4.6 QR Code Scanner
*[Screenshot halaman scanner QR Code]*

### L4.7 Batch Print QR Code
*[Screenshot halaman batch print QR Code]*

### L4.8 Halaman Maintenance
*[Screenshot halaman daftar aset maintenance]*

### L4.9 Halaman Import Data
*[Screenshot halaman import data dari Excel/CSV]*

### L4.10 Halaman Export Data
*[Screenshot halaman export data dengan filter]*

### L4.11 Halaman Laporan
*[Screenshot halaman laporan aset]*

### L4.12 Halaman Manajemen Pengguna
*[Screenshot halaman manajemen pengguna (admin only)]*

### L4.13 Halaman Audit Log
*[Screenshot halaman audit log (admin only)]*

---

## Lampiran 5. Kuesioner Pengujian

### Kuesioner User/Staff

**Identitas Responden:**
- Nama: _______________
- Status: _______________
- Jenis Kelamin: _______________
- Usia: _______________
- Perangkat yang digunakan: _______________
- Browser yang digunakan: _______________

**Petunjuk Pengisian:**
Berikan penilaian dengan memilih salah satu angka dari 1-5 untuk setiap pernyataan berikut:
- 5 = Sangat Setuju
- 4 = Setuju
- 3 = Ragu-ragu
- 2 = Tidak Setuju
- 1 = Sangat Tidak Setuju

**A. Unit Testing**
1. Sistem mudah dipahami saat pertama kali digunakan. (1-2-3-4-5)
2. Navigasi menu mudah digunakan dan tidak membingungkan. (1-2-3-4-5)
3. Saya dapat menemukan fitur yang dibutuhkan dengan mudah. (1-2-3-4-5)
4. Sistem berjalan lancar tanpa error saat berpindah halaman. (1-2-3-4-5)
5. Informasi yang ditampilkan pada halaman utama muncul dengan benar. (1-2-3-4-5)

**B. Functional Testing**
6. Fitur manajemen aset (tambah, edit, hapus) berjalan sesuai fungsi. (1-2-3-4-5)
7. Fitur QR Code (generate, scan, cetak) berfungsi dengan baik. (1-2-3-4-5)
8. Fitur import data dari Excel/CSV berjalan sesuai yang diharapkan. (1-2-3-4-5)
9. Fitur export data ke Excel dan PDF menghasilkan file yang benar. (1-2-3-4-5)
10. Fitur laporan menampilkan data yang sesuai dengan filter yang dipilih. (1-2-3-4-5)

**C. Accuracy Testing**
11. Data aset yang ditampilkan lengkap dan akurat. (1-2-3-4-5)
12. Informasi kondisi dan status aset ditampilkan dengan benar. (1-2-3-4-5)
13. Data yang diinput tersimpan dan ditampilkan kembali dengan benar. (1-2-3-4-5)
14. Filter dan pencarian menghasilkan data yang sesuai. (1-2-3-4-5)
15. Laporan yang dihasilkan akurat dan sesuai dengan data di sistem. (1-2-3-4-5)

**D. Usability Testing**
16. Tampilan antarmuka sistem mudah dimengerti. (1-2-3-4-5)
17. Menu dan tombol penting mudah ditemukan. (1-2-3-4-5)
18. Sistem membantu saya menyelesaikan pekerjaan lebih efisien. (1-2-3-4-5)
19. Saya merasa nyaman menggunakan sistem ini. (1-2-3-4-5)
20. Secara keseluruhan sistem mudah digunakan. (1-2-3-4-5)

---

## Lampiran 6. Source Code Utama

### L6.1 Model Asset (app/Models/Asset.php)

```php
class Asset extends Model
{
    use SoftDeletes;

    protected $table      = 'aset';
    protected $primaryKey = 'kode_aset';
    public    $incrementing = false;
    protected $keyType    = 'string';

    // ... (lihat source code lengkap di repository)

    public static function generateKode(): string
    {
        $existing = self::withTrashed()
            ->pluck('kode_aset')
            ->map(fn($k) => (int) str_replace('AST-', '', $k))
            ->filter(fn($n) => $n > 0)
            ->sort()->values();

        $next = 1;
        foreach ($existing as $num) {
            if ($num > $next) break;
            if ($num === $next) $next++;
        }
        return 'AST-' . str_pad($next, 3, '0', STR_PAD_LEFT);
    }
}
```

### L6.2 Middleware SecurityHeaders (app/Http/Middleware/SecurityHeaders.php)

```php
class SecurityHeaders
{
    public function handle(Request $request, Closure $next)
    {
        $response = $next($request);
        $response->headers->set('X-Content-Type-Options', 'nosniff');
        $response->headers->set('X-Frame-Options', 'DENY');
        $response->headers->set('X-XSS-Protection', '1; mode=block');
        $response->headers->set('Referrer-Policy', 'strict-origin-when-cross-origin');
        $response->headers->set('Content-Security-Policy', "frame-ancestors 'self';");
        return $response;
    }
}
```

### L6.3 QR Code Controller (app/Http/Controllers/QrCodeController.php)

```php
public function batchPrint(Request $request)
{
    $kodes = $request->input('asset_ids', []);
    $assets = Asset::with(['barang', 'ruangan'])
        ->whereIn('kode_aset', $kodes)->get();

    $qrcodes = [];
    foreach ($assets as $asset) {
        $qrcodes[$asset->kode_aset] = QrCode::size(120)
            ->format('svg')
            ->generate(route('assets.detail', $asset->kode_aset));
    }
    return view('qrcode.batch_print', compact('assets', 'qrcodes'));
}
```
