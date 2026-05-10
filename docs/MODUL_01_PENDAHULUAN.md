# MODUL 1 — PENDAHULUAN SISTEM
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu
**Modul Pengembangan | Versi 1.0 | 2026**

---

## 1.1 Deskripsi Umum Sistem

SimAset adalah sebuah sistem informasi manajemen aset berbasis web yang dikembangkan khusus untuk memenuhi kebutuhan operasional Rakyat Bengkulu Televisi (RBTV). Sistem ini dirancang untuk mengelola, memantau, dan mendokumentasikan seluruh aset barang kantor secara digital dan terpusat, menggantikan proses pencatatan manual yang selama ini dilakukan menggunakan spreadsheet yang tidak terintegrasi.

Secara umum, SimAset berfungsi sebagai pusat data aset yang dapat diakses oleh seluruh pengguna yang berwenang kapan saja dan dari mana saja melalui browser web. Sistem ini tidak hanya menyimpan data aset, tetapi juga mengintegrasikan berbagai fitur pendukung seperti pelacakan kondisi fisik aset, manajemen lokasi (ruangan), pembuatan dan pemindaian QR code, pencatatan proses maintenance, serta pelaporan komprehensif dalam berbagai format.

Keunikan utama SimAset dibandingkan sistem pencatatan konvensional terletak pada beberapa hal berikut:

- **QR Code per aset** — setiap aset yang terdaftar di sistem memiliki QR code unik yang dapat dicetak dan ditempel pada fisik aset. Siapapun yang memindai QR code tersebut menggunakan kamera smartphone akan langsung diarahkan ke halaman detail aset, sehingga identifikasi aset menjadi sangat cepat dan akurat tanpa perlu membuka aplikasi terlebih dahulu.
- **Maintenance tracking terintegrasi** — sistem mencatat dan mengelola seluruh siklus maintenance aset, mulai dari penandaan aset masuk maintenance, pemantauan aset yang sedang dalam perbaikan, hingga penyelesaian maintenance. Setiap perubahan status maintenance secara otomatis mengirimkan notifikasi email kepada seluruh admin yang aktif.
- **Audit log otomatis** — seluruh aktivitas pengguna di dalam sistem, mulai dari login, penambahan data, perubahan data, hingga penghapusan data, tercatat secara otomatis di tabel log_aktivitas. Fitur ini sangat penting untuk keperluan audit dan akuntabilitas pengelolaan aset.
- **Import/Export massal** — sistem mendukung penambahan data aset dan barang secara massal melalui file Excel atau CSV, serta mendukung ekspor data ke berbagai format (Excel dengan styling profesional, PDF siap cetak, dan CSV).

Sistem ini dikembangkan menggunakan pendekatan arsitektur MVC (Model-View-Controller) dengan framework Laravel 12, sehingga kode terstruktur dengan baik, mudah dipelihara, dan dapat dikembangkan lebih lanjut di masa depan. Antarmuka pengguna dirancang menggunakan Tailwind CSS agar responsif dan dapat diakses dari berbagai perangkat, baik desktop maupun mobile.

> **[GAMBAR 1.1: Tampilan halaman utama / dashboard SimAset yang menampilkan kartu statistik aset, grafik distribusi kondisi, dan tabel aset terbaru]**

---

## 1.2 Latar Belakang Pengembangan

### 1.2.1 Kondisi Pengelolaan Aset Sebelum SimAset

Rakyat Bengkulu Televisi (RBTV) sebagai perusahaan media memiliki berbagai peralatan bernilai tinggi yang digunakan dalam kegiatan produksi dan siaran sehari-hari. Peralatan tersebut mencakup kamera broadcast, perangkat audio profesional, komputer editing, perlengkapan studio, hingga peralatan kantor umum. Jumlah aset yang cukup banyak dan tersebar di berbagai ruangan menjadikan pengelolaan aset sebagai tantangan tersendiri.

Sebelum SimAset dikembangkan, pengelolaan aset di RBTV dilakukan secara manual menggunakan spreadsheet Microsoft Excel. Meskipun spreadsheet cukup membantu untuk pencatatan sederhana, pendekatan ini memiliki banyak keterbatasan yang semakin terasa seiring bertambahnya jumlah aset dan kompleksitas kebutuhan pengelolaan.

### 1.2.2 Permasalahan yang Ditemukan

Berdasarkan observasi dan analisis terhadap proses pengelolaan aset yang berjalan, ditemukan sejumlah permasalahan mendasar sebagai berikut:

**1. Pencatatan Manual yang Tidak Terstruktur**

Data aset tersebar di berbagai file spreadsheet yang dikelola secara terpisah oleh masing-masing penanggung jawab. Tidak ada sumber data tunggal yang dapat dipercaya sebagai acuan. Akibatnya, duplikasi data sering terjadi, pembaruan di satu file tidak otomatis tercermin di file lain, dan rekonsiliasi data antar departemen menjadi sangat menyulitkan.

**2. Tidak Ada Pelacakan Kondisi Aset Secara Real-Time**

Kondisi fisik setiap aset hanya dapat diketahui melalui pengecekan fisik langsung ke lokasi aset. Tidak ada mekanisme untuk mengetahui kondisi aset secara cepat tanpa harus mendatangi ruangan tempat aset berada. Akibatnya, kerusakan aset sering terlambat diketahui dan ditangani.

**3. Identifikasi Aset yang Lambat dan Rawan Kesalahan**

Tanpa sistem identifikasi yang standar, aset dengan nama atau jenis yang serupa sulit dibedakan. Pengecekan aset saat audit atau pemindahan memerlukan waktu lama karena harus mencocokkan data secara manual. Kesalahan identifikasi aset pun sering terjadi.

**4. Proses Maintenance Tidak Terdokumentasi**

Ketika sebuah aset mengalami kerusakan dan perlu diperbaiki, proses maintenance dilakukan tanpa pencatatan yang sistematis. Tidak ada riwayat perbaikan per aset, tidak ada notifikasi kepada pihak terkait, dan tidak ada cara untuk mengetahui berapa lama sebuah aset sudah dalam kondisi rusak atau sedang diperbaiki.

**5. Pembuatan Laporan Memakan Waktu Lama**

Setiap kali manajemen membutuhkan laporan kondisi aset, staf harus mengumpulkan data dari berbagai spreadsheet, merekap secara manual, dan memformat laporan. Proses ini bisa memakan waktu berjam-jam dan hasilnya sering tidak akurat karena data yang tidak up-to-date.

**6. Tidak Ada Kontrol Akses yang Jelas**

Siapapun yang memiliki akses ke file spreadsheet dapat mengubah data tanpa jejak yang jelas. Tidak ada pembatasan hak akses berdasarkan peran pengguna, dan tidak ada audit trail yang mencatat siapa mengubah apa dan kapan.

### 1.2.3 Urgensi Pengembangan Sistem

Kondisi-kondisi di atas menyebabkan berbagai dampak negatif bagi operasional RBTV, antara lain potensi kehilangan aset yang tidak terdeteksi, keterlambatan penanganan kerusakan yang berdampak pada kualitas produksi, kesulitan dalam pengambilan keputusan pengadaan aset baru karena data yang tidak akurat, serta risiko akuntabilitas yang rendah dalam pengelolaan aset.

Oleh karena itu, pengembangan SimAset sebagai sistem informasi manajemen aset berbasis web menjadi sangat mendesak dan relevan untuk mengatasi seluruh permasalahan tersebut secara komprehensif.

> **[GAMBAR 1.2: Diagram perbandingan alur pengelolaan aset sebelum dan sesudah menggunakan SimAset]**

---

## 1.3 Tujuan Pengembangan Sistem

Tujuan pengembangan SimAset dirancang secara bertahap dan berorientasi pada kebutuhan nyata operasional RBTV. Setiap tujuan ditetapkan berdasarkan permasalahan spesifik yang telah diidentifikasi pada tahap analisis.

1. **Menyediakan database aset terpusat dan terintegrasi** — seluruh data aset RBTV tersimpan dalam satu sistem yang dapat diakses secara bersamaan oleh pengguna yang berwenang, menghilangkan fragmentasi data yang selama ini terjadi.

2. **Meningkatkan akurasi dan konsistensi data aset** — melalui validasi otomatis pada setiap input data, auto-generate kode unik untuk setiap aset dan barang, serta mekanisme soft delete yang mencegah kehilangan data secara tidak sengaja.

3. **Mempercepat identifikasi aset di lapangan** — melalui QR code yang dicetak dan ditempel pada fisik aset, siapapun dapat mengidentifikasi aset hanya dengan memindai kode menggunakan kamera smartphone, tanpa perlu membuka aplikasi atau mencari di daftar manual.

4. **Memudahkan pengelolaan dan pemantauan maintenance** — sistem menyediakan dashboard khusus maintenance yang menampilkan seluruh aset yang sedang dalam perbaikan, beserta fitur untuk menandai aset masuk dan selesai maintenance, dilengkapi notifikasi email otomatis.

5. **Menghasilkan laporan aset secara otomatis** — laporan aset keseluruhan, laporan per ruangan, dan laporan maintenance dapat dihasilkan kapan saja dalam format PDF siap cetak atau Excel untuk analisis lebih lanjut.

6. **Meningkatkan keamanan dan akuntabilitas pengelolaan data** — melalui sistem autentikasi berbasis session, role-based access control yang membedakan hak akses Admin dan Staff, serta audit log yang mencatat seluruh aktivitas pengguna secara otomatis.

7. **Mendukung pengambilan keputusan manajemen** — dashboard dengan statistik real-time dan visualisasi data (chart distribusi kondisi, distribusi kategori) memberikan gambaran kondisi aset secara cepat kepada manajemen.

8. **Menjadi sarana pembelajaran pengembangan sistem informasi** — sebagai proyek kerja praktik, sistem ini juga bertujuan menjadi contoh implementasi nyata pengembangan sistem informasi berbasis web menggunakan Laravel.

---

## 1.4 Ruang Lingkup Sistem

Agar pengembangan sistem tetap terarah dan dapat diselesaikan dalam waktu yang tersedia, ruang lingkup SimAset ditetapkan sebagai berikut:

**Yang termasuk dalam ruang lingkup:**

1. Manajemen aset fisik — CRUD (Create, Read, Update, Delete) data aset lengkap dengan foto, kondisi fisik, status operasional, informasi perolehan (tanggal, harga, sumber), dan serial number
2. Master data barang — pengelolaan jenis/tipe barang yang menjadi referensi untuk setiap aset
3. Master data ruangan — pengelolaan lokasi/ruangan tempat aset ditempatkan
4. QR code — generate, cetak individual, batch print, dan scanner QR code
5. Maintenance tracking — pencatatan aset masuk maintenance, pemantauan, dan penyelesaian maintenance
6. Import massal — import data aset dan barang dari file Excel/CSV
7. Export dan laporan — export ke Excel (dengan styling), PDF, dan CSV; laporan aset, per ruangan, dan maintenance
8. Dashboard — statistik dan visualisasi data aset secara real-time
9. Manajemen pengguna — CRUD user dengan role Admin/Staff (khusus Admin)
10. Audit log — pencatatan seluruh aktivitas pengguna (khusus Admin)

**Yang tidak termasuk dalam ruang lingkup:**

- Sistem pengadaan atau pembelian aset baru
- Integrasi dengan sistem keuangan atau akuntansi
- Perhitungan depresiasi atau nilai buku aset
- Manajemen aset tidak berwujud (lisensi software, hak cipta, dll.)
- Aplikasi mobile native (Android/iOS)
- Navigasi rute menuju lokasi aset secara real-time

---

## 1.5 Manfaat Sistem

Manfaat SimAset dapat dirasakan oleh berbagai pihak yang terlibat dalam pengelolaan aset RBTV:

**Bagi Pengelola Aset (Admin dan Staff):**
- Kemudahan pencatatan aset baru dengan form yang terstruktur dan validasi otomatis
- Identifikasi aset yang sangat cepat melalui pemindaian QR code
- Notifikasi email otomatis untuk setiap perubahan status maintenance
- Laporan siap cetak yang dapat dihasilkan kapan saja tanpa perlu rekap manual
- Import data massal yang menghemat waktu saat penambahan banyak aset sekaligus

**Bagi Manajemen RBTV:**
- Visibilitas kondisi seluruh aset secara real-time melalui dashboard
- Data yang akurat dan terpercaya sebagai dasar pengambilan keputusan pengadaan
- Audit trail yang lengkap untuk akuntabilitas pengelolaan aset
- Penghematan waktu yang signifikan dalam pembuatan laporan periodik

**Bagi Teknisi dan Tim Maintenance:**
- Informasi detail aset yang dapat diakses langsung dari QR code tanpa perlu login
- Pencatatan riwayat maintenance yang terstruktur dan mudah ditelusuri
- Notifikasi email saat maintenance selesai sehingga tidak ada informasi yang terlewat

**Bagi Dunia Akademik:**
- Contoh implementasi nyata pengembangan sistem informasi berbasis web menggunakan Laravel 12
- Referensi teknis untuk pengembangan sistem serupa di organisasi lain

---

## 1.6 Aktor Sistem

Sistem SimAset melibatkan dua aktor utama yang memiliki hak akses berbeda. Pembagian peran ini penting untuk menjaga keamanan sistem dan memastikan bahwa setiap pengguna hanya dapat mengakses fitur yang sesuai dengan tanggung jawabnya.

### 1.6.1 Admin

Admin adalah pengguna dengan hak akses tertinggi dalam sistem. Admin bertanggung jawab atas pengelolaan seluruh data, konfigurasi sistem, dan pemantauan aktivitas pengguna. Dalam konteks RBTV, Admin biasanya adalah penanggung jawab aset atau supervisor yang memiliki kewenangan penuh atas sistem.

**Hak akses Admin mencakup:**
- Seluruh fitur operasional yang dimiliki Staff
- Manajemen pengguna: menambah, mengubah, menonaktifkan, dan menghapus akun pengguna
- Melihat dan memfilter audit log seluruh aktivitas pengguna di sistem
- Menerima notifikasi email saat ada aset yang selesai maintenance

**Data akun Admin yang tersedia di sistem (dari database aktual):**

| ID | Nama | Email | Role |
|----|------|-------|------|
| 3 | Admin Magang | magangrbtv@gmail.com | admin |

### 1.6.2 Staff

Staff adalah pengguna operasional yang mengelola data aset sehari-hari. Staff memiliki akses ke seluruh fitur operasional sistem, namun tidak dapat mengakses fitur manajemen pengguna dan audit log yang bersifat administratif.

**Hak akses Staff mencakup:**
- Mengelola data aset (tambah, lihat, edit, hapus, batch delete)
- Mengelola master data barang dan ruangan
- Generate, cetak, dan scan QR code
- Menandai aset masuk dan selesai maintenance
- Import data dari Excel/CSV
- Export data dan mencetak laporan
- Mengedit profil sendiri

**Data akun Staff yang tersedia di sistem (dari database aktual):**

| ID | Nama | Email | Role |
|----|------|-------|------|
| 2 | Staff RBTV | staff@rbtv.id | staff |
| 4 | reffki | reffkip@gmail.com | staff |

> **[GAMBAR 1.3: Diagram aktor sistem yang menunjukkan perbedaan hak akses antara Admin dan Staff dengan panah ke masing-masing fitur yang dapat diakses]**

---

## 1.7 Gambaran Umum Alur Sistem

Alur kerja SimAset secara umum dapat digambarkan sebagai berikut. Setiap pengguna, baik Admin maupun Staff, harus melalui proses autentikasi (login) sebelum dapat mengakses fitur apapun di dalam sistem. Setelah berhasil login, pengguna akan diarahkan ke halaman dashboard yang menampilkan ringkasan statistik aset.

**Alur utama pengelolaan aset:**

1. Admin atau Staff melakukan login menggunakan email dan password yang terdaftar
2. Sistem memverifikasi kredensial dan membuat session login
3. Pengguna diarahkan ke dashboard yang menampilkan statistik aset terkini
4. Sebelum menambah aset, pastikan master data barang dan ruangan sudah tersedia
5. Tambah aset baru melalui form — sistem otomatis generate kode unik (AST-001, AST-002, dst.)
6. Generate QR code untuk aset yang baru ditambahkan, cetak, dan tempel pada fisik aset
7. Saat perlu mengidentifikasi aset, cukup pindai QR code dengan kamera smartphone
8. Jika aset mengalami kerusakan, tandai sebagai Maintenance — sistem kirim email notifikasi ke Admin
9. Setelah aset selesai diperbaiki, tandai maintenance selesai — status kembali Aktif
10. Export laporan sesuai kebutuhan (PDF untuk cetak, Excel untuk analisis, CSV untuk backup)
11. Admin dapat memantau seluruh aktivitas melalui halaman Audit Log

**Alur khusus Admin:**
- Mengelola akun pengguna (tambah Staff baru, nonaktifkan akun, reset password)
- Memantau audit log untuk mendeteksi aktivitas yang tidak wajar

> **[GAMBAR 1.4: Flowchart alur kerja utama SimAset dari login hingga logout, mencakup semua modul utama]**

---

## 1.8 Tech Stack dan Dependensi

SimAset dibangun menggunakan teknologi-teknologi modern yang sudah teruji dan banyak digunakan di industri. Pemilihan teknologi ini mempertimbangkan faktor kemudahan pengembangan, ketersediaan dokumentasi, komunitas yang aktif, dan kompatibilitas antar komponen.

| Komponen | Teknologi | Versi | Fungsi |
|----------|-----------|-------|--------|
| Backend Framework | Laravel | 12.x | Framework PHP utama, routing, ORM, auth |
| Bahasa Pemrograman | PHP | 8.2+ | Bahasa server-side |
| Database | MySQL | 8.0 | Penyimpanan data utama |
| Frontend CSS | Tailwind CSS | 3.x | Styling antarmuka yang responsif |
| Frontend JS | Alpine.js | 3.x | Interaktivitas ringan (modal, dropdown) |
| Build Tool | Vite | 7.x | Kompilasi dan bundling asset frontend |
| Autentikasi | Laravel Breeze | 2.x | Scaffolding login, register, reset password |
| Export Excel | Maatwebsite Excel | 3.x | Export data ke file .xlsx dengan styling |
| Export PDF | DomPDF (barryvdh) | 3.x | Generate file PDF dari Blade template |
| QR Code | SimpleSoftwareIO | 4.x | Generate QR code dalam format SVG/PNG |
| Image Processing | Intervention Image | 4.x | Resize dan manipulasi foto aset |
| Charts | Chart.js | - | Visualisasi data di dashboard |

**Dependensi PHP (composer.json):**
```json
{
  "require": {
    "php": "^8.2",
    "barryvdh/laravel-dompdf": "^3.1",
    "intervention/image": "^4.0",
    "laravel/framework": "^12.0",
    "laravel/tinker": "^2.10.1",
    "maatwebsite/excel": "^3.1",
    "simplesoftwareio/simple-qrcode": "^4.2"
  }
}
```

**Dependensi JavaScript (package.json):**
```json
{
  "devDependencies": {
    "@tailwindcss/vite": "^4.0.0",
    "alpinejs": "^3.4.2",
    "axios": "^1.11.0",
    "laravel-vite-plugin": "^2.0.0",
    "tailwindcss": "^3.1.0",
    "vite": "^7.0.7"
  }
}
```

---

## 1.9 Ringkasan Modul

Modul 1 ini telah memberikan gambaran menyeluruh tentang SimAset sebagai sistem informasi manajemen aset RBTV Bengkulu. Dimulai dari deskripsi umum sistem yang menjelaskan apa itu SimAset dan apa keunggulannya, dilanjutkan dengan latar belakang pengembangan yang menjelaskan mengapa sistem ini perlu dibuat berdasarkan permasalahan nyata yang ditemukan di lapangan.

Tujuan pengembangan yang terukur dan spesifik telah ditetapkan, ruang lingkup sistem telah dibatasi dengan jelas agar pengembangan tetap terarah, manfaat sistem bagi berbagai pihak telah diidentifikasi, dan dua aktor utama sistem (Admin dan Staff) beserta hak aksesnya masing-masing telah didefinisikan.

Pemahaman yang baik terhadap modul ini menjadi fondasi yang sangat penting sebelum melanjutkan ke Modul 2, yang akan membahas analisis kebutuhan sistem secara lebih mendalam dan terstruktur sebagai acuan dalam proses perancangan dan implementasi.

---

*Lanjut ke: [Modul 2 — Analisis Kebutuhan Sistem](MODUL_02_ANALISIS_KEBUTUHAN.md)*

---

## 1.10 Gambaran Semua Halaman Sistem

Berikut adalah daftar lengkap semua halaman yang tersedia di SimAset:

| No | URL | Halaman | Akses | Keterangan |
|----|-----|---------|-------|------------|
| 1 | /login | Halaman Login | Publik | Form login dua panel |
| 2 | /forgot-password | Lupa Password | Publik | Request reset via email |
| 3 | /reset-password | Reset Password | Publik | Form password baru |
| 4 | /dashboard | Dashboard | Auth | Statistik + chart + recent assets |
| 5 | /aset | Daftar Aset | Auth | Tabel aset + filter + bulk action |
| 6 | /aset/create | Tambah Aset | Auth | Form 4 section |
| 7 | /aset/{kode} | Detail Aset | Auth | Info lengkap + QR + foto |
| 8 | /aset/{kode}/edit | Edit Aset | Auth | Form edit dengan preview foto |
| 9 | /aset/{kode}/qr | QR Code Aset | Auth | Tampilkan/generate QR |
| 10 | /aset/{kode}/detail | Detail Publik | **Publik** | Dari scan QR, tanpa login |
| 11 | /barang | Daftar Barang | Auth | Tabel master barang |
| 12 | /barang/create | Tambah Barang | Auth | Form tambah barang |
| 13 | /barang/{kode} | Detail Barang | Auth | Info + daftar aset terkait |
| 14 | /barang/{kode}/edit | Edit Barang | Auth | Form edit barang |
| 15 | /ruangan | Daftar Ruangan | Auth | Tabel ruangan + stats |
| 16 | /ruangan/create | Tambah Ruangan | Auth | Form tambah ruangan |
| 17 | /ruangan/{id} | Detail Ruangan | Auth | Info + daftar aset di ruangan |
| 18 | /ruangan/{id}/edit | Edit Ruangan | Auth | Form edit ruangan |
| 19 | /qrcode/scanner | QR Scanner | Auth | Kamera + upload + manual |
| 20 | /qrcode/batch-print | Batch Print QR | Auth | Grid QR code siap cetak |
| 21 | /qrcode/{kode}/download | Cetak QR Single | Auth | Label QR individual |
| 22 | /maintenance | Dashboard Maintenance | Auth | Daftar aset maintenance |
| 23 | /import/aset | Import Aset | Auth | Upload file + format guide |
| 24 | /import/barang | Import Barang | Auth | Upload file + format guide |
| 25 | /export/aset | Export Aset | Auth | Filter + tombol export |
| 26 | /export/barang | Export Barang | Auth | Filter + tombol export |
| 27 | /laporan | Laporan & Export | Auth | Hub semua laporan |
| 28 | /laporan/assets | Laporan Aset | Auth | Tabel laporan dengan filter |
| 29 | /profile | Edit Profil | Auth | Form profil + ganti password |
| 30 | /users | Kelola Pengguna | **Admin** | Daftar + CRUD user |
| 31 | /users/create | Tambah Pengguna | **Admin** | Form + kirim email |
| 32 | /users/{id}/edit | Edit Pengguna | **Admin** | Form edit user |
| 33 | /audit-log | Log Aktivitas | **Admin** | Tabel 39 record + filter |

> **[GAMBAR 1.5: Sitemap SimAset menampilkan hierarki semua halaman dan hubungan antar halaman]**
