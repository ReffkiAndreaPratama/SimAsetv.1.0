# BAB IV IMPLEMENTASI DAN PENGUJIAN

## 4.1 Tahapan dan Realisasi Kerja Praktik

### 4.1.1 Tahapan Pengembangan

Pelaksanaan Kerja Praktik ini dilakukan melalui serangkaian tahapan yang sistematis mengacu pada model pengembangan Software Development Life Cycle (SDLC) dengan pendekatan Waterfall. Setiap tahapan dirancang agar saling berkesinambungan sehingga sistem yang dikembangkan mampu memberikan solusi efektif dalam pengelolaan aset barang kantor di RBTV Bengkulu.

> **Gambar 4.1 Tahapan Pengembangan Sistem**

Adapun tahapan pengembangan yang dilaksanakan meliputi:

#### 1. Analisis Kebutuhan (Requirement Analysis)

Tahap analisis kebutuhan bertujuan untuk mengidentifikasi kebutuhan pengguna dan kebutuhan sistem yang akan dikembangkan. Pada tahap ini dilakukan:

- Observasi langsung terhadap proses pengelolaan aset yang sedang berjalan di RBTV Bengkulu.
- Wawancara dengan staf administrasi dan manajemen RBTV mengenai permasalahan yang dihadapi.
- Studi literatur terkait sistem informasi manajemen aset dan teknologi yang akan digunakan.
- Pengumpulan data mengenai jenis-jenis aset, kategori, dan alur pengelolaan aset di RBTV.

Hasil dari tahap analisis ini adalah perumusan kebutuhan fungsional dan non-fungsional sistem yang menjadi dasar perancangan.

#### 2. Perancangan Sistem (System Design)

Tahap perancangan sistem merupakan proses penerjemahan hasil analisis kebutuhan ke dalam bentuk rancangan teknis. Pada tahap ini dilakukan:

- Pemodelan sistem menggunakan UML (Use Case Diagram, Activity Diagram, Sequence Diagram, Class Diagram).
- Perancangan struktur database menggunakan ERD dan DFD.
- Perancangan antarmuka pengguna (prototype) untuk seluruh halaman sistem.
- Penentuan teknologi yang akan digunakan (Laravel 12, MySQL, Tailwind CSS, Alpine.js).

#### 3. Implementasi Sistem (Implementation)

Tahap implementasi merupakan proses realisasi rancangan sistem ke dalam bentuk perangkat lunak yang berfungsi. Sistem dikembangkan sebagai aplikasi berbasis web dengan menggunakan:

- **Backend:** Laravel 12 (PHP 8.2) dengan arsitektur MVC
- **Frontend:** Tailwind CSS + Alpine.js + Bootstrap 5
- **Database:** SQLite (development) / MySQL (production)
- **Authentication:** Laravel Breeze (session-based)
- **Export:** Maatwebsite Excel + DomPDF
- **QR Code:** SimpleSoftwareIO/simple-qrcode
- **Build Tool:** Vite

Pada tahap ini dikembangkan seluruh modul sistem secara bertahap, mulai dari autentikasi, manajemen aset, master data, QR Code, maintenance, import/export, laporan, manajemen pengguna, hingga audit log.

#### 4. Pengujian Sistem (Testing)

Tahap pengujian dilakukan untuk memastikan bahwa seluruh fitur sistem berfungsi dengan baik dan sesuai dengan kebutuhan pengguna. Pengujian dilakukan menggunakan pendekatan **Black Box Testing** dengan instrumen kuesioner skala Likert lima poin. Pengujian melibatkan dua kelompok responden: pengguna/staff dan admin.

#### 5. Evaluasi dan Penyempurnaan (Evaluation)

Tahap evaluasi dilakukan berdasarkan hasil pengujian dan umpan balik dari pengguna. Penyempurnaan dilakukan pada aspek tampilan antarmuka, performa sistem, dan kejelasan informasi yang ditampilkan.

#### 6. Dokumentasi (Documentation)

Tahap terakhir adalah penyusunan dokumentasi lengkap sistem, termasuk laporan Kerja Praktik, diagram sistem, dan panduan penggunaan.

---

### 4.1.2 Realisasi Tahapan

| No | Tahapan | Realisasi Pelaksanaan |
|----|---------|----------------------|
| 1 | Analisis Kebutuhan | Dilakukan observasi dan wawancara di RBTV Bengkulu. Data yang dikumpulkan meliputi jenis aset, alur pengelolaan, permasalahan yang dihadapi, dan kebutuhan pengguna. Hasil analisis digunakan untuk menyusun kebutuhan fungsional dan non-fungsional sebagai dasar perancangan sistem. |
| 2 | Perancangan Sistem | Perancangan dilakukan menggunakan pemodelan UML (Use Case, Activity, Sequence, Class Diagram) dan ERD. Rancangan antarmuka dibuat dalam bentuk prototype untuk seluruh halaman sistem. Seluruh rancangan dikonsultasikan dengan pembimbing lapangan dan dosen pembimbing. |
| 3 | Implementasi Sistem | Sistem diimplementasikan menggunakan Laravel 12 dengan seluruh modul yang direncanakan. Fitur utama seperti manajemen aset, QR Code, maintenance, import/export, laporan, manajemen pengguna, dan audit log berhasil diintegrasikan dan berjalan dengan baik. |
| 4 | Pengujian Sistem | Pengujian dilakukan kepada dua kelompok responden: pengguna/staff (12 responden) dan admin (1 responden). Pengujian menggunakan kuesioner dengan empat kategori: Unit Testing, Functional Testing, Accuracy Testing, dan Usability Testing. |
| 5 | Evaluasi | Evaluasi dilakukan berdasarkan hasil pengujian dan masukan pengguna. Penyempurnaan meliputi perbaikan tampilan antarmuka, optimasi performa, dan peningkatan kejelasan pesan error dan notifikasi. |
| 6 | Dokumentasi | Dokumentasi disusun secara sistematis dalam laporan Kerja Praktik, dilengkapi dengan diagram sistem, tangkapan layar aplikasi, dan panduan penggunaan. |

---

## 4.2 Timeline Kerja Praktik

Pelaksanaan Kerja Praktik direncanakan dan direalisasikan dalam jangka waktu satu semester. Penyusunan timeline mengacu pada metode Waterfall dengan pembagian aktivitas ke dalam beberapa tahapan pengembangan.

**Tabel 4.2 Timeline Kerja Praktik dengan Kurva S**

| NO | Aktivitas | Penanggung Jawab | Bobot | B1-M1 | B1-M2 | B1-M3 | B1-M4 | B2-M1 | B2-M2 | B2-M3 | B2-M4 | B3-M1 | B3-M2 | B3-M3 | B3-M4 |
|----|-----------|-----------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| I | Analisis Kebutuhan | Reffki | 15 | 7.5 | 7.5 | | | | | | | | | | |
| II | Perancangan Sistem | Reffki | 20 | | | 10 | 10 | | | | | | | | |
| III | Implementasi Sistem | Reffki | 30 | | | | | 7.5 | 7.5 | 7.5 | 7.5 | | | | |
| IV | Pengujian Sistem | Reffki | 15 | | | | | | | | | 7.5 | 7.5 | | |
| V | Evaluasi | Reffki | 10 | | | | | | | | | | | 5 | 5 |
| VI | Dokumentasi & Laporan | Reffki | 10 | | | | | | | | | | | | 10 |
| | **Total** | | **100** | | | | | | | | | | | | |
| | Progres Mingguan | | | 7.5 | 7.5 | 10 | 10 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 | 5 | 15 |
| | Progres Kumulatif | | | 7.5 | 15 | 25 | 35 | 42.5 | 50 | 57.5 | 65 | 72.5 | 80 | 85 | 100 |

---

## 4.3 Hasil Implementasi Sistem

Hasil pengembangan SimAset menunjukkan bahwa sistem telah berhasil menyediakan seluruh fitur yang direncanakan. Berikut adalah tampilan dan penjelasan setiap halaman sistem yang telah diimplementasikan.

### 4.3.1 Halaman Login

> **Gambar 4.2 Halaman Login**

Halaman Login merupakan titik masuk utama bagi pengguna untuk mengakses sistem SimAset. Pengguna diminta memasukkan email dan password yang telah terdaftar. Desain halaman dibuat minimalis, bersih, dan responsif. Elemen seperti tombol "Ingat Saya" dan "Lupa Password?" disediakan untuk meningkatkan kenyamanan pengguna. Sistem menggunakan Laravel Breeze untuk autentikasi berbasis session yang aman. Setiap percobaan login dicatat dalam audit log, termasuk login yang berhasil maupun yang gagal.

### 4.3.2 Dashboard

> **Gambar 4.3 Dashboard Utama**

Halaman Dashboard merupakan tampilan awal setelah pengguna berhasil login. Dashboard menampilkan:

- **Statistik Utama:** Total aset, aset aktif, aset maintenance, aset non-aktif, total barang, total ruangan, dan aset yang ditambahkan bulan ini.
- **Grafik Distribusi Kondisi:** Pie chart yang menampilkan distribusi kondisi aset (Baik, Rusak Ringan, Rusak Berat) menggunakan Chart.js.
- **Grafik Top 5 Kategori:** Bar chart yang menampilkan 5 kategori barang dengan jumlah aset terbanyak.
- **Aset Terbaru:** Tabel yang menampilkan 10 aset yang paling baru ditambahkan ke sistem.

Dashboard dirancang untuk memberikan gambaran cepat kepada pengguna mengenai kondisi aset secara keseluruhan, sehingga memudahkan monitoring dan pengambilan keputusan.

### 4.3.3 Manajemen Aset

> **Gambar 4.4 Halaman Daftar Aset**

Halaman Daftar Aset menampilkan seluruh aset yang terdaftar dalam sistem dalam bentuk tabel dengan pagination 15 item per halaman. Fitur yang tersedia:

- **Pencarian:** Cari aset berdasarkan kode aset, nama barang, serial number, atau ruangan.
- **Filter:** Filter berdasarkan status (Aktif/Maintenance/Non-Aktif), kondisi (Baik/Rusak Ringan/Rusak Berat), dan kategori.
- **Statistik:** Kartu statistik di bagian atas menampilkan total aset, aset aktif, maintenance, dan non-aktif.
- **Batch Delete:** Pilih multiple aset dan hapus sekaligus.
- **Batch QR Print:** Pilih multiple aset dan cetak QR Code sekaligus.

> **Gambar 4.5 Halaman Tambah Aset**

Halaman Tambah Aset menyediakan form untuk menambahkan aset baru ke sistem. Field yang tersedia:

- Kode Barang (dropdown dari master data barang aktif)
- Ruangan (dropdown dari master data ruangan)
- Kondisi (Baik/Rusak Ringan/Rusak Berat)
- Status (Aktif/Maintenance/Non-Aktif)
- Serial Number (opsional, unik)
- Jumlah
- Tanggal Perolehan
- Harga Perolehan
- Sumber Perolehan (Pembelian/Hibah/Sumbangan/Pinjaman/Lainnya)
- Foto Aset (upload gambar)
- Keterangan

Kode aset di-generate otomatis oleh sistem dengan format AST-001, AST-002, dst., menggunakan algoritma gap-filling untuk memastikan tidak ada nomor yang terlewat.

> **Gambar 4.6 Halaman Detail Aset**

Halaman Detail Aset menampilkan seluruh informasi aset secara lengkap, termasuk foto aset, QR Code, informasi barang, ruangan, kondisi, status, data perolehan, dan riwayat perubahan (dibuat oleh siapa dan kapan, diperbarui oleh siapa dan kapan). Dari halaman ini pengguna dapat melakukan edit, hapus, generate QR Code, atau menandai aset masuk maintenance.

### 4.3.4 Manajemen Barang

> **Gambar 4.7 Halaman Manajemen Barang**

Halaman Manajemen Barang digunakan untuk mengelola master data barang. Admin/Staff dapat menambah, mengedit, dan menghapus data barang. Setiap barang memiliki kode unik (format BRG-001), nama barang, kategori (Kamera/Audio/Komputer/Lighting/Furniture/Peralatan Kantor/Lainnya), status (aktif/nonaktif), dan keterangan. Fitur pencarian dan filter berdasarkan kategori dan status tersedia untuk memudahkan pengelolaan. Barang yang dihapus menggunakan soft delete sehingga data tidak hilang secara permanen.

### 4.3.5 Manajemen Ruangan

> **Gambar 4.8 Halaman Manajemen Ruangan**

Halaman Manajemen Ruangan digunakan untuk mengelola master data ruangan tempat aset ditempatkan. Setiap ruangan memiliki nama, lantai/lokasi, dan keterangan. Halaman ini juga menampilkan statistik: total ruangan, total aset, ruangan kosong (tanpa aset), dan ruangan terisi. Sistem mencegah penghapusan ruangan yang masih memiliki aset terdaftar untuk menjaga integritas data.

### 4.3.6 QR Code

> **Gambar 4.9 Halaman QR Code Scanner**

Halaman QR Code Scanner menyediakan fitur scanner berbasis web yang memanfaatkan kamera perangkat untuk memindai QR Code aset. Setelah QR Code berhasil dipindai, sistem menampilkan informasi detail aset secara real-time, meliputi kode aset, nama barang, kategori, ruangan, kondisi, status, jumlah, dan serial number. Pengguna juga dapat mengakses halaman detail aset lengkap dari hasil scan.

> **Gambar 4.10 Halaman Batch Print QR Code**

Halaman Batch Print QR Code memungkinkan pengguna mencetak QR Code untuk multiple aset sekaligus. Pengguna memilih aset-aset yang diinginkan dari halaman daftar aset, kemudian sistem menampilkan halaman cetak dengan QR Code dalam format SVG yang dapat langsung dicetak. Setiap QR Code dilengkapi dengan kode aset dan nama barang untuk memudahkan identifikasi.

QR Code yang di-generate berisi URL yang mengarah ke halaman detail aset (route: assets.detail), sehingga siapapun yang memindai QR Code dapat langsung mengakses informasi aset tersebut.

### 4.3.7 Maintenance

> **Gambar 4.11 Halaman Maintenance**

Halaman Maintenance menampilkan daftar seluruh aset yang sedang dalam status Maintenance. Statistik yang ditampilkan meliputi total aset maintenance, aset rusak berat, aset rusak ringan, dan total aset rusak. Fitur pencarian dan filter berdasarkan kondisi tersedia untuk memudahkan pemantauan.

**Alur Maintenance:**
1. Staff menandai aset masuk maintenance dari halaman detail aset dengan mengisi keterangan.
2. Aset muncul di halaman Maintenance dengan status "Maintenance".
3. Setelah perbaikan selesai, staff menandai maintenance selesai dengan mengisi kondisi terkini aset.
4. Status aset kembali menjadi "Aktif" dan sistem mengirimkan notifikasi email ke seluruh admin.
5. Seluruh aktivitas maintenance dicatat dalam audit log.

### 4.3.8 Import Data

> **Gambar 4.12 Halaman Import Data**

Halaman Import Data menyediakan fitur untuk memasukkan data aset atau barang secara massal dari file Excel (.xlsx, .xls) atau CSV. Fitur yang tersedia:

- **Download Template:** Unduh template CSV yang sudah berformat sesuai untuk memudahkan pengisian data.
- **Upload File:** Upload file Excel/CSV yang berisi data aset atau barang.
- **Validasi Per Baris:** Sistem memvalidasi setiap baris data dan menampilkan laporan error jika ada data yang tidak valid.
- **Normalisasi Data:** Sistem secara otomatis menormalisasi nilai enum (kondisi, status) agar sesuai dengan format yang diterima.

Format kolom untuk import aset: Kode Barang, Nama Ruangan, Kondisi, Status, Jumlah, Tanggal Perolehan, Harga Perolehan, Sumber Perolehan, Keterangan.

### 4.3.9 Export Data

> **Gambar 4.13 Halaman Export Data**

Halaman Export Data menyediakan fitur untuk mengekspor data aset atau barang ke format Excel (.xlsx) atau PDF. Tersedia filter sebelum export:

- **Filter Aset:** Status, kondisi, ruangan, tanggal perolehan (dari-sampai), kategori, dan pencarian nama.
- **Filter Barang:** Status, kategori, dan pencarian nama.

Export Excel menggunakan library Maatwebsite Excel, sedangkan export PDF menggunakan DomPDF dengan layout landscape untuk aset dan portrait untuk barang. File yang dihasilkan diberi nama dengan timestamp untuk memudahkan identifikasi.

### 4.3.10 Laporan

> **Gambar 4.14 Halaman Laporan Aset**

Halaman Laporan menyediakan berbagai jenis laporan yang dapat diakses dan dicetak:

- **Laporan Aset:** Laporan seluruh aset dengan filter status, kondisi, dan ruangan. Dapat dicetak sebagai PDF (landscape) atau diexport sebagai CSV.
- **Laporan Per Ruangan:** Laporan aset yang dikelompokkan per ruangan. Dapat dicetak sebagai PDF (portrait) untuk setiap ruangan.
- **Laporan Maintenance:** Laporan aset yang sedang dalam status maintenance. Dapat dicetak sebagai PDF atau CSV.

Setiap laporan dilengkapi dengan header yang berisi nama instansi, judul laporan, nama pencetak, dan tanggal cetak.

### 4.3.11 Manajemen Pengguna (Admin Only)

> **Gambar 4.15 Halaman Manajemen Pengguna**

Halaman Manajemen Pengguna hanya dapat diakses oleh pengguna dengan role Admin. Fitur yang tersedia:

- **Daftar Pengguna:** Menampilkan seluruh pengguna yang terdaftar beserta role dan status aktif.
- **Tambah Pengguna:** Form untuk menambah pengguna baru dengan validasi password (min 8 karakter, huruf besar, huruf kecil, angka).
- **Edit Pengguna:** Ubah nama, email, role, dan status aktif pengguna.
- **Hapus Pengguna:** Hapus pengguna (tidak dapat menghapus akun sendiri).
- **Kirim Email Notifikasi:** Opsi untuk mengirimkan email berisi informasi akun ke pengguna baru.

### 4.3.12 Audit Log (Admin Only)

> **Gambar 4.16 Halaman Audit Log**

Halaman Audit Log hanya dapat diakses oleh pengguna dengan role Admin. Halaman ini menampilkan seluruh aktivitas yang dilakukan oleh pengguna dalam sistem, meliputi:

- Login dan Logout
- Create, Update, Delete data aset
- Create, Update, Delete data barang
- Create, Update, Delete data ruangan
- Aktivitas maintenance

Setiap entri log mencatat: nama pengguna, jenis aktivitas, deskripsi detail, alamat IP, browser/device, dan waktu aktivitas. Tersedia filter berdasarkan pengguna, jenis aktivitas (module), dan pencarian teks.

---

## 4.4 Pengujian Sistem

### 4.4.1 Analisis Metode Pengujian

Teknik analisis data yang digunakan dalam pengujian ini adalah analisis deskriptif kuantitatif. Data diperoleh melalui kuesioner menggunakan skala Likert lima poin, yang memungkinkan peneliti untuk mengukur persepsi, pengalaman, dan tingkat kepuasan pengguna terhadap sistem SimAset secara objektif. Penggunaan skala Likert lima poin dipilih karena terbukti efektif dalam penelitian modern yang menilai kualitas dan usability aplikasi digital.

Skor penilaian yang digunakan terdiri dari kategori Sangat Setuju (SS) hingga Sangat Tidak Setuju (STS) dengan rentang nilai 1-5.

**Tabel 4.3 Kategori Skor Penilaian**

| Jawaban | Skor |
|---------|------|
| Sangat Setuju (SS) | 5 |
| Setuju (S) | 4 |
| Ragu-ragu (Rr) | 3 |
| Tidak Setuju (TS) | 2 |
| Sangat Tidak Setuju (STS) | 1 |

Data hasil kuesioner dianalisis menggunakan rumus rata-rata:

`
x̄ = Σx / n
`

Keterangan:
- x̄ = rata-rata skor
- Σx = total skor jawaban
- n = jumlah responden

**Tabel 4.4 Kategori Interval Skala Likert**

| Rentang Nilai | Kategori |
|---------------|----------|
| 4,01 – 5,00 | Sangat Layak |
| 3,01 – 4,00 | Layak |
| 2,01 – 3,00 | Kurang Layak |
| 1,00 – 2,00 | Tidak Layak |

Kuesioner disusun berdasarkan empat jenis pengujian:
- **Unit Testing:** Menguji fungsi dasar sistem (kemudahan akses, stabilitas halaman, navigasi).
- **Functional Testing:** Menguji fungsionalitas fitur utama (manajemen aset, QR Code, maintenance, import/export).
- **Accuracy Testing:** Menguji keakuratan data yang ditampilkan sistem.
- **Usability Testing:** Menguji kemudahan penggunaan dan kenyamanan antarmuka.

---

### 4.4.2 Data Pengujian Dengan Kuesioner

#### 1. User/Staff (Pengguna Umum)

Pengujian sistem dilakukan melalui penyebaran kuesioner kepada pengguna/staff dengan tujuan untuk mengetahui tingkat kelayakan, kemudahan penggunaan, serta efektivitas sistem SimAset. Responden terdiri dari **12 orang** yang berasal dari staf RBTV Bengkulu dan mahasiswa yang berperan sebagai pengguna sistem.

**Tabel 4.5 Data Responden User/Staff**

| No | Nama | Status | Jenis Kelamin | Usia | Perangkat | Browser |
|----|------|--------|--------------|------|-----------|---------|
| 1 | Responden 1 | Staf RBTV | Laki-laki | 26-30 Tahun | Laptop/PC | Google Chrome |
| 2 | Responden 2 | Staf RBTV | Perempuan | 26-30 Tahun | Laptop/PC | Google Chrome |
| 3 | Responden 3 | Staf RBTV | Laki-laki | 31-35 Tahun | Laptop/PC | Microsoft Edge |
| 4 | Responden 4 | Staf RBTV | Perempuan | 26-30 Tahun | Smartphone | Google Chrome |
| 5 | Responden 5 | Staf RBTV | Laki-laki | 26-30 Tahun | Laptop/PC | Google Chrome |
| 6 | Responden 6 | Mahasiswa | Perempuan | 20-25 Tahun | Laptop/PC | Google Chrome |
| 7 | Responden 7 | Mahasiswa | Laki-laki | 20-25 Tahun | Smartphone | Google Chrome |
| 8 | Responden 8 | Mahasiswa | Perempuan | 20-25 Tahun | Laptop/PC | Microsoft Edge |
| 9 | Responden 9 | Mahasiswa | Laki-laki | 20-25 Tahun | Smartphone | Google Chrome |
| 10 | Responden 10 | Mahasiswa | Perempuan | 20-25 Tahun | Laptop/PC | Google Chrome |
| 11 | Responden 11 | Mahasiswa | Laki-laki | 20-25 Tahun | Smartphone | Safari |
| 12 | Responden 12 | Mahasiswa | Perempuan | 20-25 Tahun | Laptop/PC | Google Chrome |

**Tabel 4.6 Unit Testing User/Staff**

| Unit Testing | Rata-rata Skor |
|-------------|---------------|
| "Sistem mudah dipahami saat pertama kali digunakan." | 4.6 |
| "Navigasi menu mudah digunakan dan tidak membingungkan." | 4.7 |
| "Saya dapat menemukan fitur yang dibutuhkan dengan mudah." | 4.6 |
| "Sistem berjalan lancar tanpa error saat berpindah halaman." | 4.5 |
| "Informasi yang ditampilkan pada halaman utama muncul dengan benar." | 4.6 |
| **Jumlah** | **23.0** |
| **Rata-rata Poin** | **4.60** |
| **Kriteria** | **Sangat Layak** |

Berdasarkan hasil Unit Testing, rata-rata skor sebesar **4.60** menunjukkan bahwa sistem dinilai sangat layak dari sisi penggunaan dasar. Pengguna merasa bahwa sistem mudah dipahami, navigasi dapat digunakan tanpa kendala, dan halaman dapat diakses tanpa gangguan error.

**Tabel 4.7 Functional Testing User/Staff**

| Functional Testing | Rata-rata Skor |
|-------------------|---------------|
| "Fitur manajemen aset (tambah, edit, hapus) berjalan sesuai fungsi." | 4.7 |
| "Fitur QR Code (generate, scan, cetak) berfungsi dengan baik." | 4.6 |
| "Fitur import data dari Excel/CSV berjalan sesuai yang diharapkan." | 4.5 |
| "Fitur export data ke Excel dan PDF menghasilkan file yang benar." | 4.7 |
| "Fitur laporan menampilkan data yang sesuai dengan filter yang dipilih." | 4.6 |
| **Jumlah** | **23.1** |
| **Rata-rata Poin** | **4.62** |
| **Kriteria** | **Sangat Layak** |

Rata-rata skor **4.62** menunjukkan bahwa fitur-fitur utama sistem berjalan dengan sangat baik. Pengguna dapat menggunakan seluruh fitur operasional tanpa kendala berarti.

**Tabel 4.8 Accuracy Testing User/Staff**

| Accuracy Testing | Rata-rata Skor |
|-----------------|---------------|
| "Data aset yang ditampilkan lengkap dan akurat." | 4.6 |
| "Informasi kondisi dan status aset ditampilkan dengan benar." | 4.7 |
| "Data yang diinput tersimpan dan ditampilkan kembali dengan benar." | 4.6 |
| "Filter dan pencarian menghasilkan data yang sesuai." | 4.5 |
| "Laporan yang dihasilkan akurat dan sesuai dengan data di sistem." | 4.6 |
| **Jumlah** | **23.0** |
| **Rata-rata Poin** | **4.60** |
| **Kriteria** | **Sangat Layak** |

Dengan skor rata-rata **4.60**, pengguna menilai bahwa data yang disajikan oleh sistem telah akurat, lengkap, dan konsisten.

**Tabel 4.9 Usability Testing User/Staff**

| Usability Testing | Rata-rata Skor |
|------------------|---------------|
| "Tampilan antarmuka sistem mudah dimengerti." | 4.5 |
| "Menu dan tombol penting mudah ditemukan." | 4.6 |
| "Sistem membantu saya menyelesaikan pekerjaan lebih efisien." | 4.7 |
| "Saya merasa nyaman menggunakan sistem ini." | 4.6 |
| "Secara keseluruhan sistem mudah digunakan." | 4.7 |
| **Jumlah** | **23.1** |
| **Rata-rata Poin** | **4.62** |
| **Kriteria** | **Sangat Layak** |

Rata-rata skor **4.62** menunjukkan bahwa pengguna merasa sistem sangat mudah digunakan. Tampilan dinilai jelas, navigasi tidak membingungkan, dan sistem memberikan pengalaman penggunaan yang nyaman dan responsif.

**Tabel 4.10 Rekapitulasi Hasil Testing User/Staff**

| Jenis Testing | Rata-rata Skor |
|--------------|---------------|
| Unit Testing | 4.60 |
| Functional Testing | 4.62 |
| Accuracy Testing | 4.60 |
| Usability Testing | 4.62 |
| **Jumlah** | **18.44** |
| **Rata-rata Hasil** | **4.61** |
| **Kriteria Hasil** | **Sangat Layak** |

Secara keseluruhan, hasil pengujian terhadap 12 responden user/staff menunjukkan bahwa sistem SimAset dinilai **sangat layak** untuk digunakan. Rata-rata skor keseluruhan sebesar **4.61** mengindikasikan bahwa sistem memiliki performa yang sangat baik dari sisi fungsi dasar, fungsionalitas fitur, ketepatan data, maupun pengalaman penggunaan.

---

#### 2. Admin

Responden dalam pengujian ini adalah Admin sistem SimAset di RBTV Bengkulu, yaitu pihak yang bertanggung jawab dalam pengelolaan data aset, manajemen pengguna, dan pemantauan audit log. Sebagai admin yang berinteraksi langsung dengan seluruh fitur sistem, penilaiannya dapat menjadi acuan yang valid untuk menilai performa fitur admin.

**Tabel 4.11 Unit Testing Admin**

| Unit Testing | Skor |
|-------------|------|
| Sistem berhasil menyimpan data aset setiap kali tombol "Simpan" ditekan. | 5 |
| Fitur Edit pada data aset selalu memperbarui informasi dengan benar. | 5 |
| Fungsi Delete (soft delete) menghapus data tanpa menyebabkan error pada data lainnya. | 5 |
| Upload foto aset berhasil dan gambar tampil dengan benar pada halaman detail. | 4 |
| Sistem berhasil memvalidasi input dan menampilkan pesan error saat form tidak lengkap. | 4 |
| **Jumlah** | **23** |
| **Rata-rata** | **4.6** |
| **Kriteria** | **Sangat Layak** |

**Tabel 4.12 Functional Testing Admin**

| Functional Testing | Skor |
|-------------------|------|
| Fitur manajemen aset (CRUD, batch delete) berjalan sesuai fungsi. | 5 |
| Fitur QR Code (generate, batch print, scanner) berfungsi dengan baik. | 4 |
| Fitur maintenance (set, complete, notifikasi email) berjalan sesuai alur. | 5 |
| Fitur import/export data berjalan sesuai yang diharapkan. | 4 |
| Fitur manajemen pengguna dan audit log berfungsi dengan benar. | 5 |
| **Jumlah** | **23** |
| **Rata-rata** | **4.6** |
| **Kriteria** | **Sangat Layak** |

**Tabel 4.13 Accuracy Testing Admin**

| Accuracy Testing | Skor |
|-----------------|------|
| Data aset yang ditampilkan sesuai dengan data yang diinputkan. | 5 |
| Audit log mencatat seluruh aktivitas pengguna dengan akurat. | 5 |
| Data yang diimport dari Excel/CSV tersimpan dengan benar di database. | 4 |
| File export (Excel/PDF) berisi data yang akurat dan lengkap. | 4 |
| Laporan yang dihasilkan konsisten dengan data di sistem. | 5 |
| **Jumlah** | **23** |
| **Rata-rata** | **4.6** |
| **Kriteria** | **Sangat Layak** |

**Tabel 4.14 Usability Testing Admin**

| Usability Testing | Skor |
|------------------|------|
| Tampilan dashboard admin mudah dipahami untuk monitoring sistem. | 5 |
| Alur kerja pengelolaan aset (input, edit, hapus, export) mudah diikuti. | 5 |
| Tombol dan menu penting mudah ditemukan di seluruh halaman. | 5 |
| Proses pengelolaan data terasa cepat dan efisien. | 4 |
| Secara keseluruhan, sistem nyaman digunakan untuk operasional harian. | 5 |
| **Jumlah** | **24** |
| **Rata-rata** | **4.8** |
| **Kriteria** | **Sangat Layak** |

Usability Testing menghasilkan rata-rata **4.8**, yang merupakan skor tertinggi. Hal ini menunjukkan bahwa sistem sangat mudah digunakan oleh admin, memiliki struktur navigasi yang jelas, dan mendukung efisiensi kerja dalam pengelolaan aset.

**Tabel 4.15 Rekapitulasi Hasil Testing Admin**

| Kategori Pengujian | Skor Rata-rata |
|-------------------|---------------|
| Unit Testing | 4.6 |
| Functional Testing | 4.6 |
| Accuracy Testing | 4.6 |
| Usability Testing | 4.8 |
| **Jumlah Total Skor** | **18.6** |
| **Rata-rata Hasil** | **4.65** |
| **Kriteria Keseluruhan** | **Sangat Layak** |

Berdasarkan seluruh kategori pengujian, sistem SimAset memiliki rata-rata skor **4.65** dengan kategori **Sangat Layak** dari perspektif admin. Hal ini menunjukkan bahwa sistem telah memenuhi kebutuhan operasional pengelolaan aset, stabil digunakan, akurat dalam menampilkan data, serta memiliki kenyamanan penggunaan yang sangat baik.

---

### 4.4.3 Analisis Pengujian Data Hasil

Pengujian sistem dilakukan menggunakan metode analisis deskriptif kuantitatif dengan instrumen kuesioner skala Likert lima poin. Metode ini diterapkan secara konsisten pada dua kelompok responden, yaitu pengguna/staff dan admin. Penggunaan metode yang sama memungkinkan hasil penilaian dibandingkan secara objektif.

#### 1. Analisis Berdasarkan Kuesioner User/Staff

Pengujian kepada pengguna/staff dilakukan dengan melibatkan 12 responden yang menjawab 20 butir pertanyaan yang mewakili empat jenis pengujian. Berdasarkan hasil yang diperoleh, rata-rata skor keseluruhan adalah **4.61**, sehingga termasuk kategori **Sangat Layak** (interval 4.01-5.00).

Pengguna memberikan penilaian sangat baik pada aspek:
- Kemudahan memahami dan menggunakan sistem
- Fungsionalitas fitur manajemen aset dan QR Code
- Keakuratan data yang ditampilkan
- Efisiensi dan kenyamanan penggunaan sistem

Beberapa skor tertinggi diperoleh pada indikator kemudahan navigasi, fungsionalitas fitur utama, dan kepuasan penggunaan sistem, masing-masing berada pada kisaran **4.6-4.7**.

#### 2. Analisis Berdasarkan Kuesioner Admin

Hasil pengujian admin menunjukkan rata-rata skor **4.65** dengan kategori **Sangat Layak**. Admin memberikan penilaian tertinggi pada aspek usability (4.8), yang menunjukkan bahwa dashboard admin sangat mudah digunakan dan mendukung efisiensi kerja operasional.

#### 3. Sintesis Analisis User/Staff dan Admin

**Tabel 4.16 Perbandingan Hasil Pengujian User dan Admin**

| Kelompok | Rata-rata Skor | Kategori |
|----------|---------------|----------|
| User/Staff (12 responden) | 4.61 | Sangat Layak |
| Admin (1 responden) | 4.65 | Sangat Layak |

Baik pengguna/staff maupun admin memberikan penilaian kategori **Sangat Layak**, yang berarti sistem telah memenuhi standar kelayakan dari sisi pengalaman pengguna maupun performa teknis.

Fokus penilaian berbeda antar kelompok:
- **User/Staff** menyoroti kemudahan navigasi, fungsionalitas fitur operasional, dan kenyamanan penggunaan sehari-hari.
- **Admin** menekankan akurasi data, stabilitas fitur CRUD, kelengkapan audit log, dan efisiensi kerja di dashboard.

Kesamaan dari keduanya adalah bahwa sistem bekerja sangat baik, cepat, stabil, dan memperlancar proses pengelolaan aset di RBTV Bengkulu.

#### 4. Kesimpulan Akhir Analisis Pengujian

Berdasarkan pengujian dua kelompok responden, dapat disimpulkan bahwa sistem SimAset memiliki tingkat kelayakan yang sangat tinggi. Sistem dinilai:
- Cepat dan responsif
- Akurat dalam menampilkan dan menyimpan data
- Mudah digunakan oleh pengguna dari berbagai latar belakang
- Stabil dan tidak mengalami error yang berarti
- Mendukung kebutuhan operasional pengelolaan aset di RBTV Bengkulu

Rata-rata nilai keseluruhan berada di kategori **Sangat Layak**, sehingga sistem siap diimplementasikan secara penuh di RBTV Bengkulu. Beberapa peningkatan minor yang dapat dilakukan pada pengembangan berikutnya meliputi peningkatan visualisasi grafik dashboard, penambahan fitur notifikasi in-app, dan pengembangan aplikasi mobile.
