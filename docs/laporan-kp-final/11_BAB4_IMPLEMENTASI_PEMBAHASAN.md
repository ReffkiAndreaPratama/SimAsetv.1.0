# BAB IV IMPLEMENTASI DAN PEMBAHASAN

## 4.1 User Interface

Bagian ini menampilkan hasil implementasi antarmuka sistem yang telah dibangun beserta penjelasan mengenai fungsi dan fitur yang tersedia pada setiap halaman.

**a. Halaman Login**

Halaman login merupakan pintu masuk utama sistem. Pengguna diwajibkan memasukkan email dan password yang terdaftar untuk dapat mengakses sistem. Sistem melakukan validasi kredensial secara server-side menggunakan mekanisme autentikasi Laravel Breeze. Apabila kredensial tidak valid, sistem menampilkan pesan kesalahan tanpa memberikan informasi spesifik mengenai field mana yang salah, sebagai langkah keamanan untuk mencegah enumerasi akun.

*(Gambar 4.1 Halaman Login)*

**b. Halaman Dashboard**

Halaman dashboard menampilkan ringkasan statistik aset secara keseluruhan dalam bentuk kartu informasi dan grafik. Informasi yang ditampilkan meliputi total aset terdaftar, jumlah aset dalam kondisi baik, rusak ringan, dan rusak berat, serta jumlah kategori barang dan ruangan yang terdaftar. Grafik distribusi kondisi aset ditampilkan dalam bentuk diagram lingkaran (pie chart) untuk memudahkan pemantauan kondisi aset secara visual.

*(Gambar 4.2 Halaman Dashboard)*

**c. Halaman Data Aset**

Halaman data aset menampilkan seluruh data aset yang tersimpan dalam sistem dalam bentuk tabel yang dilengkapi dengan fitur pencarian berdasarkan nama atau kode aset, filter berdasarkan kategori barang, kondisi, dan ruangan, serta pagination untuk memudahkan navigasi data dalam jumlah besar. Setiap baris data dilengkapi dengan tombol aksi untuk melihat detail, mengubah data, mencetak QR Code, dan menghapus aset.

*(Gambar 4.3 Halaman Data Aset)*

**d. Halaman Tambah Aset**

Halaman tambah aset menyediakan form input yang terstruktur untuk memasukkan data aset baru. Form dilengkapi dengan validasi sisi klien dan sisi server untuk memastikan kelengkapan dan kebenaran data yang dimasukkan. Pengguna dapat mengunggah foto aset langsung melalui form ini. Setelah data berhasil disimpan, sistem secara otomatis menghasilkan QR Code unik untuk aset tersebut.

*(Gambar 4.4 Halaman Tambah Aset)*

**e. Halaman Detail Aset**

Halaman detail aset menampilkan seluruh informasi lengkap mengenai suatu aset, meliputi data identitas aset, kondisi, lokasi, riwayat pemeliharaan, dan QR Code aset. Halaman ini juga menyediakan tombol untuk mencetak detail aset dan QR Code secara langsung.

*(Gambar 4.5 Halaman Detail Aset)*

**f. Halaman Manajemen Barang**

Halaman manajemen barang digunakan untuk mengelola data kategori/jenis barang yang menjadi pengelompokan aset. Administrator dapat menambah kategori baru, mengubah data kategori yang ada, serta menghapus kategori yang tidak lagi digunakan. Setiap kategori barang memiliki kode unik yang digunakan sebagai awalan kode aset.

*(Gambar 4.6 Halaman Manajemen Barang)*

**g. Halaman Manajemen Ruangan**

Halaman manajemen ruangan digunakan untuk mengelola data ruangan sebagai lokasi penempatan aset. Administrator dapat menambah, mengubah, dan menghapus data ruangan. Informasi ruangan yang tersimpan digunakan sebagai referensi dalam pencatatan lokasi aset.

*(Gambar 4.7 Halaman Manajemen Ruangan)*

**h. Halaman QR Code Scanner**

Halaman QR Code Scanner menyediakan fitur pemindaian QR Code menggunakan kamera perangkat. Ketika QR Code aset berhasil dipindai, sistem secara otomatis menampilkan halaman detail aset yang bersangkutan. Fitur ini memudahkan staf dalam melakukan verifikasi dan pengecekan kondisi aset secara langsung di lapangan tanpa perlu mencari data secara manual.

*(Gambar 4.8 Halaman QR Code Scanner)*

**i. Halaman Batch Print QR Code**

Halaman batch print QR Code memungkinkan administrator untuk mencetak QR Code beberapa aset sekaligus dalam satu sesi. Pengguna dapat memilih aset-aset yang QR Code-nya akan dicetak, kemudian sistem menghasilkan halaman cetak yang berisi seluruh QR Code yang dipilih dalam format yang siap cetak.

*(Gambar 4.9 Halaman Batch Print QR Code)*

**j. Halaman Maintenance**

Halaman maintenance digunakan untuk mencatat dan memantau riwayat pemeliharaan aset. Setiap catatan pemeliharaan berisi informasi mengenai aset yang dipelihara, tanggal pemeliharaan, jenis pemeliharaan, biaya, dan keterangan hasil pemeliharaan. Halaman ini juga menampilkan daftar aset yang memerlukan pemeliharaan berdasarkan kondisi yang tercatat.

*(Gambar 4.10 Halaman Maintenance)*

**k. Halaman Import Data**

Halaman import data menyediakan fitur untuk mengimpor data aset dari file Excel ke dalam sistem. Pengguna dapat mengunduh template Excel yang telah disediakan, mengisi data aset sesuai format yang ditentukan, kemudian mengunggah file tersebut untuk diproses oleh sistem. Sistem melakukan validasi data yang diimpor dan menampilkan laporan hasil impor beserta informasi mengenai data yang berhasil diimpor dan data yang gagal beserta alasannya.

*(Gambar 4.11 Halaman Import Data)*

**l. Halaman Export Data**

Halaman export data menyediakan fitur untuk mengekspor data aset ke dalam format Excel atau PDF. Pengguna dapat menentukan filter data yang akan diekspor berdasarkan kategori, kondisi, atau ruangan sebelum melakukan ekspor. File hasil ekspor dapat langsung diunduh oleh pengguna.

*(Gambar 4.12 Halaman Export Data)*

**m. Halaman Laporan Aset**

Halaman laporan aset menyediakan fitur pembuatan laporan inventaris aset secara otomatis. Pengguna dapat menentukan parameter laporan yang diinginkan, kemudian sistem menghasilkan laporan yang dapat ditampilkan di layar, dicetak, atau diunduh dalam format PDF. Laporan yang dihasilkan mencakup daftar aset lengkap beserta informasi kondisi, lokasi, dan nilai aset.

*(Gambar 4.13 Halaman Laporan Aset)*

**n. Halaman Manajemen Pengguna**

Halaman manajemen pengguna hanya dapat diakses oleh administrator. Halaman ini menampilkan daftar seluruh akun pengguna yang terdaftar dalam sistem beserta informasi peran masing-masing. Administrator dapat menambah akun pengguna baru, mengubah data pengguna, mengatur ulang password, serta menonaktifkan akun pengguna yang tidak lagi aktif.

*(Gambar 4.14 Halaman Manajemen Pengguna)*

**o. Halaman Audit Log**

Halaman audit log menampilkan catatan seluruh aktivitas yang dilakukan oleh pengguna dalam sistem, meliputi informasi pengguna yang melakukan aksi, jenis aksi, deskripsi aktivitas, alamat IP, dan waktu kejadian. Fitur ini memungkinkan administrator untuk memantau dan menelusuri seluruh perubahan data yang terjadi dalam sistem sebagai bentuk akuntabilitas dan keamanan data.

*(Gambar 4.15 Halaman Audit Log)*

---

## 4.2 White-box Testing

White-box testing dilakukan untuk menguji logika internal dan struktur kode program yang telah dibangun. Pengujian ini memastikan bahwa setiap fungsi dan alur program berjalan sesuai dengan algoritma yang telah dirancang serta tidak terdapat kesalahan pada struktur kode.

Pengujian white-box pada sistem ini dilakukan dengan memeriksa alur logika pada fungsi-fungsi kritis sistem, meliputi fungsi autentikasi, fungsi validasi input, fungsi penyimpanan data, dan fungsi pembuatan laporan. Pengujian dilakukan dengan menelusuri setiap jalur eksekusi kode (path coverage) untuk memastikan tidak ada jalur yang menghasilkan output yang tidak diharapkan.

**Tabel 4.1 Hasil White-box Testing**

| No | Fungsi yang Diuji | Jalur yang Diuji | Hasil yang Diharapkan | Hasil Pengujian |
|---|---|---|---|---|
| 1 | Login | Kredensial valid | Pengguna diarahkan ke dashboard | Sesuai |
| 2 | Login | Kredensial tidak valid | Pesan kesalahan ditampilkan | Sesuai |
| 3 | Tambah Aset | Input lengkap dan valid | Data tersimpan, QR Code dibuat | Sesuai |
| 4 | Tambah Aset | Input tidak lengkap | Pesan validasi ditampilkan | Sesuai |
| 5 | Hapus Aset | Aset tidak memiliki relasi aktif | Data dihapus (soft delete) | Sesuai |
| 6 | Import Data | File Excel valid | Data berhasil diimpor | Sesuai |
| 7 | Import Data | File Excel tidak valid | Pesan kesalahan ditampilkan | Sesuai |
| 8 | Generate Laporan | Parameter filter valid | Laporan berhasil dibuat | Sesuai |
| 9 | Kontrol Akses | Pengguna tanpa hak akses | Dialihkan ke halaman 403 | Sesuai |
| 10 | Audit Log | Setiap aksi pengguna | Aktivitas tercatat di log | Sesuai |

Berdasarkan hasil white-box testing, seluruh jalur logika yang diuji menghasilkan output yang sesuai dengan yang diharapkan. Tidak ditemukan kesalahan logika pada fungsi-fungsi kritis sistem.

---

## 4.3 Black-box Testing

Black-box testing dilakukan untuk menguji fungsionalitas sistem dari perspektif pengguna berdasarkan skenario penggunaan nyata, tanpa memperhatikan struktur kode internal. Pengujian ini memastikan bahwa setiap fitur sistem berfungsi sesuai dengan kebutuhan yang telah ditetapkan.

**Tabel 4.2 Skenario Black-box Testing**

| No | Fitur | Skenario Uji | Input | Output yang Diharapkan | Hasil |
|---|---|---|---|---|---|
| 1 | Login | Login dengan data valid | Email dan password benar | Masuk ke halaman dashboard | Berhasil |
| 2 | Login | Login dengan password salah | Email benar, password salah | Pesan "Kredensial tidak sesuai" | Berhasil |
| 3 | Login | Login dengan email tidak terdaftar | Email tidak terdaftar | Pesan "Kredensial tidak sesuai" | Berhasil |
| 4 | Tambah Aset | Menambah aset dengan data lengkap | Semua field terisi | Data tersimpan, notifikasi sukses | Berhasil |
| 5 | Tambah Aset | Menambah aset tanpa nama | Field nama kosong | Pesan validasi "Nama aset wajib diisi" | Berhasil |
| 6 | Edit Aset | Mengubah kondisi aset | Kondisi diubah menjadi "Rusak Ringan" | Data kondisi berhasil diperbarui | Berhasil |
| 7 | Hapus Aset | Menghapus aset | Klik tombol hapus dan konfirmasi | Aset tidak tampil di daftar | Berhasil |
| 8 | QR Code | Mencetak QR Code aset | Klik tombol cetak QR Code | Halaman cetak QR Code terbuka | Berhasil |
| 9 | QR Code Scanner | Memindai QR Code | Arahkan kamera ke QR Code | Detail aset ditampilkan | Berhasil |
| 10 | Import | Mengimpor file Excel valid | Upload file Excel sesuai template | Data berhasil diimpor | Berhasil |
| 11 | Import | Mengimpor file bukan Excel | Upload file PDF | Pesan kesalahan format file | Berhasil |
| 12 | Export | Mengekspor data ke Excel | Klik tombol export Excel | File Excel berhasil diunduh | Berhasil |
| 13 | Export | Mengekspor data ke PDF | Klik tombol export PDF | File PDF berhasil diunduh | Berhasil |
| 14 | Laporan | Membuat laporan dengan filter | Pilih periode dan kategori | Laporan sesuai filter ditampilkan | Berhasil |
| 15 | Maintenance | Menambah catatan pemeliharaan | Isi form pemeliharaan | Catatan tersimpan di riwayat | Berhasil |
| 16 | Manajemen User | Menambah pengguna baru | Isi data pengguna baru | Akun baru berhasil dibuat | Berhasil |
| 17 | Manajemen User | Akses oleh non-admin | Staff mengakses menu user | Dialihkan ke halaman 403 | Berhasil |
| 18 | Audit Log | Melihat log aktivitas | Akses menu audit log | Daftar aktivitas ditampilkan | Berhasil |
| 19 | Logout | Keluar dari sistem | Klik tombol logout | Sesi berakhir, diarahkan ke login | Berhasil |
| 20 | Pencarian | Mencari aset berdasarkan nama | Ketik nama aset di kolom pencarian | Aset yang sesuai ditampilkan | Berhasil |

Berdasarkan hasil black-box testing, seluruh skenario pengujian menghasilkan output yang sesuai dengan yang diharapkan. Sistem dapat berjalan dengan baik dan memenuhi seluruh kebutuhan fungsional yang telah ditetapkan.

---

## 4.4 Implementasi

### 4.4.1 Manual Program

Manual program menjelaskan cara penggunaan sistem informasi manajemen aset barang RBTV Bengkulu secara lengkap untuk setiap fitur yang tersedia.

**a. Login ke Sistem**

1. Buka browser dan akses alamat sistem melalui jaringan intranet instansi.
2. Pada halaman login, masukkan alamat email dan password yang telah terdaftar.
3. Klik tombol "Masuk" untuk mengakses sistem.
4. Apabila berhasil, sistem akan menampilkan halaman dashboard.

**b. Mengelola Data Aset**

1. Klik menu "Data Aset" pada navigasi utama.
2. Sistem menampilkan daftar seluruh aset yang terdaftar.
3. Untuk menambah aset baru, klik tombol "Tambah Aset".
4. Isi seluruh field yang tersedia pada form tambah aset, meliputi kode aset, nama aset, kategori barang, ruangan, kondisi, tahun perolehan, harga perolehan, sumber perolehan, dan keterangan.
5. Unggah foto aset apabila tersedia.
6. Klik tombol "Simpan" untuk menyimpan data aset.
7. Untuk mengubah data aset, klik ikon edit pada baris aset yang bersangkutan.
8. Untuk menghapus aset, klik ikon hapus dan konfirmasi penghapusan pada dialog yang muncul.

**c. Menggunakan QR Code**

1. Setiap aset yang tersimpan secara otomatis memiliki QR Code unik.
2. Untuk mencetak QR Code satu aset, klik ikon QR Code pada baris aset yang bersangkutan.
3. Untuk mencetak QR Code beberapa aset sekaligus, pilih aset-aset yang diinginkan menggunakan checkbox, kemudian klik tombol "Cetak QR Code Terpilih".
4. Untuk memindai QR Code, akses menu "QR Scanner" dan izinkan akses kamera browser.
5. Arahkan kamera ke QR Code aset untuk menampilkan detail aset secara langsung.

**d. Mengimpor Data Aset**

1. Klik menu "Import Data" pada navigasi utama.
2. Unduh template Excel yang tersedia dengan mengklik tombol "Unduh Template".
3. Isi data aset pada template Excel sesuai format yang telah ditentukan.
4. Kembali ke halaman import, klik tombol "Pilih File" dan pilih file Excel yang telah diisi.
5. Klik tombol "Import" untuk memproses file.
6. Sistem menampilkan laporan hasil impor beserta informasi data yang berhasil dan gagal diimpor.

**e. Mengekspor Data dan Membuat Laporan**

1. Untuk mengekspor data, klik menu "Export Data" dan pilih format yang diinginkan (Excel atau PDF).
2. Tentukan filter data yang akan diekspor apabila diperlukan.
3. Klik tombol "Export" untuk mengunduh file.
4. Untuk membuat laporan inventaris, klik menu "Laporan Aset".
5. Tentukan parameter laporan (periode, kategori, kondisi, ruangan).
6. Klik tombol "Buat Laporan" untuk menampilkan laporan.
7. Laporan dapat dicetak atau diunduh dalam format PDF.

**f. Mengelola Pemeliharaan Aset**

1. Klik menu "Maintenance" pada navigasi utama.
2. Sistem menampilkan daftar riwayat pemeliharaan aset.
3. Untuk menambah catatan pemeliharaan baru, klik tombol "Tambah Pemeliharaan".
4. Pilih aset yang dipelihara, isi tanggal pemeliharaan, jenis pemeliharaan, biaya, dan keterangan.
5. Klik tombol "Simpan" untuk menyimpan catatan pemeliharaan.

**g. Mengelola Pengguna (Administrator)**

1. Klik menu "Manajemen Pengguna" pada navigasi utama (hanya tersedia untuk administrator).
2. Sistem menampilkan daftar seluruh akun pengguna yang terdaftar.
3. Untuk menambah pengguna baru, klik tombol "Tambah Pengguna".
4. Isi nama, email, password, dan peran pengguna (admin/staff).
5. Klik tombol "Simpan" untuk membuat akun pengguna baru.
6. Sistem secara otomatis mengirimkan email notifikasi kepada pengguna baru.

### 4.4.2 Manual Instalasi

Berikut adalah langkah-langkah instalasi sistem informasi manajemen aset pada server instansi.

**Persyaratan Server:**
- PHP 8.1 atau lebih baru
- MySQL 8.0 atau lebih baru
- Composer
- Web server Apache atau Nginx

**Langkah Instalasi:**

1. Salin seluruh file proyek ke direktori web server (misalnya `/var/www/html/sima-rbtv`).
2. Buka terminal dan masuk ke direktori proyek.
3. Jalankan perintah `composer install` untuk menginstal seluruh dependensi PHP.
4. Salin file `.env.example` menjadi `.env` dan sesuaikan konfigurasi database (DB_HOST, DB_DATABASE, DB_USERNAME, DB_PASSWORD).
5. Jalankan perintah `php artisan key:generate` untuk menghasilkan application key.
6. Buat database baru di MySQL sesuai nama yang dikonfigurasi pada file `.env`.
7. Jalankan perintah `php artisan migrate` untuk membuat struktur tabel database.
8. Jalankan perintah `php artisan db:seed` untuk mengisi data awal (akun administrator).
9. Atur permission direktori `storage` dan `bootstrap/cache` agar dapat ditulis oleh web server.
10. Konfigurasi virtual host pada web server untuk mengarahkan domain ke direktori `public` proyek.
11. Akses sistem melalui browser menggunakan alamat yang telah dikonfigurasi.

---

## 4.5 Pemeliharaan

Pemeliharaan sistem dilakukan untuk memastikan sistem dapat terus berjalan dengan baik dan optimal setelah diimplementasikan. Kegiatan pemeliharaan yang perlu dilakukan meliputi:

1. **Pemeliharaan Korektif (Corrective Maintenance):** Perbaikan terhadap kesalahan atau bug yang ditemukan setelah sistem digunakan. Setiap laporan kesalahan dari pengguna ditindaklanjuti dengan identifikasi penyebab dan perbaikan kode program yang bersangkutan.

2. **Pemeliharaan Adaptif (Adaptive Maintenance):** Penyesuaian sistem terhadap perubahan lingkungan teknologi, seperti pembaruan versi PHP, Laravel, atau MySQL. Pembaruan dilakukan secara berkala untuk memastikan sistem tetap kompatibel dengan teknologi terbaru dan terlindungi dari celah keamanan.

3. **Pemeliharaan Perfektif (Perfective Maintenance):** Peningkatan kinerja sistem dan penambahan fitur baru berdasarkan masukan dari pengguna. Pengembangan fitur dilakukan secara bertahap sesuai dengan prioritas kebutuhan instansi.

4. **Pemeliharaan Preventif (Preventive Maintenance):** Tindakan pencegahan untuk menghindari masalah yang mungkin terjadi di masa depan, meliputi pencadangan (backup) basis data secara berkala, pemantauan log sistem, dan pemeriksaan rutin terhadap performa server.

Untuk mendukung kegiatan pemeliharaan, disarankan agar instansi melakukan pencadangan basis data secara otomatis setiap hari dan menyimpan salinan cadangan di lokasi yang terpisah dari server utama. Selain itu, pemantauan terhadap kapasitas penyimpanan server perlu dilakukan secara berkala mengingat sistem menyimpan foto aset yang dapat memerlukan ruang penyimpanan yang cukup besar seiring bertambahnya jumlah aset yang terdaftar.
