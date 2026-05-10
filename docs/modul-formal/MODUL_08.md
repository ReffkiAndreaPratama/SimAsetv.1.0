# MODUL 8 - IMPLEMENTASI QR CODE DAN MAINTENANCE TRACKING

## 8.1 Pendahuluan

QR Code dan maintenance tracking merupakan dua fitur unggulan SimAset yang membedakannya dari sistem pencatatan aset konvensional. QR Code memungkinkan identifikasi aset yang sangat cepat — cukup pindai kode dengan kamera smartphone dan informasi aset langsung muncul di layar tanpa perlu membuka aplikasi atau mencari secara manual. Maintenance tracking memastikan setiap proses perbaikan aset terdokumentasi dengan baik dan pihak terkait mendapat notifikasi otomatis.

Modul ini membahas secara mendalam implementasi QR Code dalam sistem, mulai dari generate QR Code, pencetakan individual dan batch, scanner berbasis web, hingga halaman detail aset publik. Selain itu, modul ini juga membahas implementasi maintenance tracking lengkap dengan notifikasi email otomatis.

## 8.2 Generate dan Cetak QR Code

Generate QR Code merupakan langkah awal dalam implementasi fitur identifikasi aset. Pada sistem ini digunakan dua pendekatan untuk generate QR Code:

1. **SimpleSoftwareIO QrCode** — untuk generate QR Code dalam format SVG, digunakan di halaman cetak karena kualitas vektor yang tajam di semua ukuran dan tidak memerlukan koneksi internet.
2. **qrserver.com API** — untuk generate QR Code dalam format PNG, disimpan di filesystem public/qr_codes/ (memerlukan koneksi internet).

QR Code dipilih sebagai media identifikasi karena:

1. Dapat dipindai menggunakan kamera smartphone standar tanpa aplikasi khusus.
2. Menyimpan URL yang mengarah langsung ke halaman detail aset.
3. Dapat dicetak dalam berbagai ukuran tanpa kehilangan kualitas (format SVG).
4. Mudah ditempel pada fisik aset sebagai label identifikasi.

Proses generate QR Code dilakukan melalui beberapa tahapan, yaitu:

1. Pengguna membuka halaman detail aset dan klik tombol "Generate QR".
2. Sistem memanggil API qrserver.com dengan URL halaman detail aset sebagai konten.
3. File PNG QR Code disimpan di public/qr_codes/qr_{kode_aset}_{timestamp}.png.
4. QR Code ditampilkan di halaman detail aset.

> **[GAMBAR 8.1: Tampilan halaman QR Code aset AST-001 dengan QR Code yang sudah di-generate dan tombol Download, Cetak, dan Lihat Label]**

## 8.3 Penampilan QR Code per Aset

Setiap aset yang terdaftar dalam sistem dapat memiliki QR Code unik yang mengarah ke URL halaman detail aset publik. QR Code ditampilkan di halaman detail aset pada kolom kanan bersama foto aset dan informasi sistem.

Jika QR Code belum di-generate, sistem menampilkan placeholder dengan tombol "Generate QR Code". Jika sudah di-generate, sistem menampilkan gambar QR Code beserta tombol untuk mengunduh (format PNG), mencetak, atau melihat label cetak.

Penempatan QR Code yang akurat sangat penting untuk memastikan informasi aset dapat diakses dengan cepat oleh pengelola di lapangan.

## 8.4 Scanner QR Code Berbasis Web

Selain memindai QR Code menggunakan kamera smartphone secara langsung, sistem juga menyediakan halaman scanner QR Code berbasis web yang dapat diakses melalui menu QR Scanner di sidebar.

Halaman scanner menyediakan tiga metode pencarian aset:

1. **Kamera** — membuka kamera perangkat dan memindai QR Code secara real-time menggunakan library jsQR.
2. **Upload gambar** — mengunggah foto QR Code untuk dipindai secara otomatis.
3. **Input manual** — memasukkan kode aset secara manual (contoh: AST-001).

Setelah aset ditemukan, sistem menampilkan informasi singkat aset (kode, nama barang, kategori, ruangan, kondisi, status) beserta tombol untuk melihat detail lengkap.

> **[GAMBAR 8.2: Tampilan halaman QR Scanner dengan area kamera aktif dan panel hasil pencarian menampilkan informasi aset]**

## 8.5 Halaman Detail Aset Publik

Halaman detail aset publik adalah tujuan dari setiap QR Code yang di-generate. Halaman ini dapat diakses oleh siapapun tanpa perlu login, sehingga teknisi atau siapapun yang menemukan aset dapat langsung mengetahui informasinya hanya dengan memindai QR Code.

URL halaman detail publik: `/aset/{kode_aset}/detail`

Contoh: Memindai QR Code aset AST-001 akan membuka halaman yang menampilkan:
- Nama barang: Kamera Sony A7
- Kategori: Kamera
- Ruangan: Ruang Editing
- Kondisi: Baik
- Status: Maintenance
- Serial Number: ggG
- Tanggal Perolehan: 01 Mei 2026

> **[GAMBAR 8.3: Tampilan halaman detail aset publik AST-001 yang dapat diakses tanpa login melalui pemindaian QR Code]**

## 8.6 Maintenance Tracking

Maintenance tracking merupakan fitur yang memungkinkan pengelola untuk mencatat dan memantau proses perbaikan aset secara terstruktur. Fitur ini mencakup dua sub-proses utama: menandai aset masuk maintenance dan menandai maintenance selesai.

**Menandai Aset Masuk Maintenance:**

Pengguna membuka halaman detail aset dan klik tombol "Set Maintenance". Sistem akan memperbarui status aset menjadi Maintenance, mencatat aktivitas ke log_aktivitas, dan menampilkan aset di dashboard maintenance.

**Dashboard Maintenance:**

Dashboard maintenance menampilkan seluruh aset yang sedang berstatus Maintenance beserta informasi kondisi, ruangan, keterangan, dan waktu terakhir diperbarui. Dashboard dilengkapi dengan filter pencarian dan kondisi, serta statistik (total maintenance, rusak berat, rusak ringan).

Berdasarkan data aktual: AST-001 (Kamera Sony A7 di Ruang Editing) saat ini berstatus Maintenance.

> **[GAMBAR 8.4: Tampilan dashboard maintenance menampilkan AST-001 dengan statistik Total Maintenance=1]**

**Menandai Maintenance Selesai:**

Pengguna membuka dashboard maintenance dan klik tombol "Selesai" pada baris aset yang selesai diperbaiki. Sistem menampilkan modal konfirmasi dengan pilihan kondisi akhir (Baik / Rusak Ringan / Rusak Berat) dan field keterangan opsional.

Setelah dikonfirmasi, sistem akan:
1. Memperbarui status aset kembali menjadi Aktif.
2. Memperbarui kondisi aset sesuai input.
3. Mencatat aktivitas Update ke log_aktivitas.
4. Mengirim email notifikasi ke semua Admin aktif.

> **[GAMBAR 8.5: Tampilan modal konfirmasi selesaikan maintenance dengan pilihan kondisi akhir]**

## 8.7 Notifikasi Email Maintenance

Sistem mengirimkan email notifikasi secara otomatis kepada seluruh Admin aktif ketika proses maintenance selesai. Email ini berisi informasi lengkap aset yang selesai diperbaiki, termasuk kode aset, nama barang, kategori, ruangan, kondisi akhir, dan tautan menuju halaman detail aset.

Konfigurasi email di file .env:

```env
# Development (email tidak terkirim, tercatat di storage/logs/laravel.log)
MAIL_MAILER=log

# Production (SMTP Gmail)
MAIL_MAILER=smtp
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS="noreply@rbtv.co.id"
MAIL_FROM_NAME="SimAset RBTV"
```

> **[GAMBAR 8.6: Contoh tampilan email notifikasi maintenance selesai yang diterima Admin dengan informasi aset lengkap]**

## 8.8 Pengujian Fitur QR Code dan Maintenance

Pengujian fitur QR Code dan maintenance dilakukan untuk memastikan bahwa seluruh fungsi berjalan dengan baik dan sesuai dengan perancangan sistem.

| No | Skenario | Hasil yang Diharapkan | Hasil |
|----|----------|-----------------------|-------|
| 1 | Generate QR Code (online) | File PNG tersimpan di qr_codes/ | Berhasil |
| 2 | Generate QR Code (offline) | Pesan error, QR tidak ter-generate | Berhasil |
| 3 | Cetak QR individual | Halaman cetak terbuka, auto-print | Berhasil |
| 4 | Batch print QR | Halaman batch print dengan grid QR | Berhasil |
| 5 | Scan QR Code | Browser buka halaman detail aset | Berhasil |
| 6 | Akses detail tanpa login | Halaman detail tampil (publik) | Berhasil |
| 7 | Set aset ke maintenance | Status berubah ke Maintenance | Berhasil |
| 8 | Selesaikan maintenance | Status kembali Aktif, email terkirim | Berhasil |

## 8.9 Kesimpulan Modul

Modul 8 membahas implementasi QR Code dan maintenance tracking SimAset secara menyeluruh. QR Code menggunakan dua pendekatan (SVG lokal dan PNG via API) untuk kebutuhan yang berbeda. Halaman detail publik memungkinkan identifikasi aset tanpa login. Maintenance tracking dengan notifikasi email otomatis memastikan setiap proses perbaikan terdokumentasi dan pihak terkait selalu mendapat informasi terkini.

Kedua fitur ini secara signifikan meningkatkan efisiensi pengelolaan aset dibandingkan sistem manual konvensional. Modul ini menjadi dasar sebelum pembahasan dashboard dan fitur import/export pada modul berikutnya.
