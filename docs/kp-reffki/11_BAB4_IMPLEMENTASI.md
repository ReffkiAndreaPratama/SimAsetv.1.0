# BAB IV IMPLEMENTASI DAN PEMBAHASAN

## 4.1 User Interface

User Interface (antarmuka pengguna) merupakan bagian dari sistem yang berfungsi sebagai media interaksi antara pengguna dengan sistem. Antarmuka yang baik harus mampu menyajikan informasi secara jelas, mudah dipahami, serta mudah digunakan oleh pengguna. Oleh karena itu, perancangan antarmuka dalam sistem ini dilakukan dengan mempertimbangkan aspek kemudahan penggunaan (usability), kejelasan informasi, serta konsistensi tampilan.

Pada sistem informasi manajemen aset yang dikembangkan, antarmuka dirancang menggunakan framework Bootstrap sehingga memiliki tampilan yang responsif dan dapat diakses melalui berbagai perangkat. Struktur antarmuka dibuat sederhana agar pengguna dapat dengan mudah memahami alur penggunaan sistem.

Berikut adalah beberapa tampilan utama dalam sistem:

**1. Halaman Login**

Halaman login merupakan halaman awal yang digunakan oleh pengguna untuk masuk ke dalam sistem. Pengguna diminta untuk memasukkan email dan password yang telah terdaftar. Sistem akan melakukan proses autentikasi untuk memastikan bahwa pengguna memiliki hak akses.

> **Gambar 4.1 Halaman Login**

**2. Halaman Dashboard**

Dashboard merupakan halaman utama setelah pengguna berhasil login. Halaman ini menampilkan ringkasan informasi seperti jumlah aset, jumlah kategori, jumlah barang masuk dan keluar, serta grafik statistik. Dashboard berfungsi sebagai pusat informasi yang memudahkan pengguna dalam memonitor kondisi aset.

> **Gambar 4.2 Halaman Dashboard**

**3. Halaman Data Aset**

Halaman ini digunakan untuk menampilkan data aset yang tersimpan dalam sistem. Pengguna dapat melakukan operasi CRUD (Create, Read, Update, Delete) terhadap data aset. Selain itu, tersedia fitur pencarian dan pagination untuk mempermudah pengelolaan data.

> **Gambar 4.3 Halaman Data Aset**

> **Gambar 4.4 Halaman Tambah Aset**

> **Gambar 4.5 Halaman Detail Aset**

**4. Halaman Manajemen Barang dan Ruangan**

Halaman ini digunakan untuk mengelola master data barang dan ruangan. Pengguna dapat menambah, mengedit, dan menghapus data barang serta ruangan yang digunakan sebagai referensi dalam pengelolaan aset.

> **Gambar 4.6 Halaman Manajemen Barang**

> **Gambar 4.7 Halaman Manajemen Ruangan**

**5. Halaman QR Code Scanner**

Halaman ini digunakan untuk melakukan pemindaian QR Code guna menampilkan informasi aset secara cepat. Pengguna dapat menggunakan kamera perangkat untuk memindai QR Code yang tertempel pada aset, dan sistem akan menampilkan detail informasi aset tersebut secara langsung.

> **Gambar 4.8 Halaman QR Code Scanner**

> **Gambar 4.9 Halaman Batch Print QR Code**

**6. Halaman Maintenance**

Halaman maintenance digunakan untuk memantau dan mengelola aset yang sedang dalam proses perbaikan. Staff dapat menandai aset masuk maintenance dan menandai selesai setelah perbaikan dilakukan.

> **Gambar 4.10 Halaman Maintenance**

**7. Halaman Import dan Export Data**

Halaman ini digunakan untuk melakukan import data aset dari file Excel atau CSV, serta export data ke format Excel dan PDF.

> **Gambar 4.11 Halaman Import Data**

> **Gambar 4.12 Halaman Export Data**

**8. Halaman Laporan**

Halaman laporan digunakan untuk menghasilkan laporan aset dalam format PDF. Pengguna dapat memilih jenis laporan sesuai kebutuhan, termasuk laporan per ruangan dan laporan maintenance.

> **Gambar 4.13 Halaman Laporan Aset**

**9. Halaman Manajemen Pengguna dan Audit Log**

Halaman manajemen pengguna hanya dapat diakses oleh admin untuk mengelola akun pengguna. Halaman audit log menampilkan seluruh riwayat aktivitas pengguna dalam sistem.

> **Gambar 4.14 Halaman Manajemen Pengguna**

> **Gambar 4.15 Halaman Audit Log**

Dari segi implementasi kode, antarmuka dibangun menggunakan Blade Template pada Laravel yang memungkinkan pengelolaan tampilan menjadi lebih terstruktur dan dinamis.

Dengan adanya antarmuka yang dirancang dengan baik, sistem dapat digunakan dengan mudah oleh pengguna serta meningkatkan efisiensi dalam pengelolaan aset.

---

## 4.2 White-box Testing

White-box testing merupakan metode pengujian perangkat lunak yang dilakukan dengan cara menganalisis struktur internal program, termasuk logika, alur kontrol, serta jalur eksekusi kode. Tujuan dari pengujian ini adalah untuk memastikan bahwa setiap bagian dari kode program telah berjalan sesuai dengan logika yang dirancang serta bebas dari kesalahan (error).

Dalam penelitian ini, white-box testing dilakukan pada beberapa modul utama sistem informasi manajemen aset yang dikembangkan menggunakan framework Laravel. Pengujian difokuskan pada fungsi-fungsi inti seperti proses penyimpanan data, pembaruan data, penghapusan data, serta validasi input pengguna.

Pendekatan yang digunakan dalam white-box testing meliputi pengujian terhadap alur logika program (control flow) serta pengujian jalur independen (independent path). Setiap jalur program diuji untuk memastikan bahwa semua kemungkinan kondisi telah ditangani dengan benar.

### 4.2.1 Pengujian Modul Barang Masuk

Sebagai contoh, pengujian dilakukan pada fungsi penyimpanan data barang masuk. Proses yang terjadi dalam modul ini adalah sebagai berikut:

1. Sistem menerima input dari pengguna berupa data barang masuk
2. Sistem melakukan validasi terhadap data input
3. Sistem mencari data barang berdasarkan ID
4. Sistem menyimpan data barang masuk ke dalam database
5. Sistem memperbarui jumlah stok barang
6. Sistem mencatat aktivitas ke dalam audit trail

Dari alur tersebut, dapat dibuat jalur logika sebagai berikut:

- Jalur 1: Input valid → data disimpan → stok bertambah → sukses
- Jalur 2: Input tidak valid → proses dihentikan → muncul error

Pengujian dilakukan dengan mencoba berbagai kondisi input untuk memastikan bahwa setiap jalur berjalan dengan benar.

### 4.2.2 Pengujian Modul Barang Keluar

Pada modul barang keluar, pengujian difokuskan pada validasi stok barang. Alur prosesnya adalah:

1. Sistem menerima input data barang keluar
2. Sistem memeriksa jumlah stok barang
3. Jika stok mencukupi, maka data disimpan dan stok dikurangi
4. Jika stok tidak mencukupi, maka sistem menampilkan pesan error

Jalur pengujian:

- Jalur 1: Stok cukup → proses berhasil
- Jalur 2: Stok tidak cukup → proses ditolak

Pengujian ini bertujuan untuk memastikan bahwa sistem mampu menjaga konsistensi data.

### 4.2.3 Pengujian Validasi Input

Pengujian juga dilakukan pada validasi input untuk memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan aturan yang telah ditentukan. Beberapa validasi yang dilakukan antara lain:

- Field tidak boleh kosong
- Format data harus sesuai
- Data harus sesuai dengan tipe yang ditentukan

Jika input tidak valid, sistem akan menampilkan pesan kesalahan dan tidak melanjutkan proses penyimpanan.

### 4.2.4 Hasil Pengujian

Berdasarkan hasil pengujian white-box testing yang telah dilakukan, dapat disimpulkan bahwa:

- Seluruh fungsi utama dalam sistem berjalan sesuai dengan logika yang dirancang
- Tidak ditemukan kesalahan pada alur program utama
- Validasi input berjalan dengan baik
- Sistem mampu menangani kondisi normal maupun kondisi error

Dengan demikian, sistem dinyatakan telah memenuhi aspek pengujian dari sisi internal program dan siap untuk dilakukan pengujian lebih lanjut dari sisi pengguna.

---

## 4.3 Black-box Testing

Black-box testing merupakan metode pengujian perangkat lunak yang dilakukan dengan menguji fungsi sistem tanpa melihat struktur internal kode program. Pengujian ini berfokus pada apakah sistem telah berjalan sesuai dengan kebutuhan fungsional yang telah ditentukan. Dalam metode ini, penguji hanya memperhatikan input yang diberikan dan output yang dihasilkan oleh sistem.

Pada penelitian ini, black-box testing dilakukan dengan cara menguji setiap fitur utama dalam sistem informasi manajemen aset yang telah dikembangkan. Pengujian dilakukan oleh pengguna (penulis) dengan memasukkan berbagai jenis data untuk memastikan bahwa sistem memberikan respon yang sesuai.

### 4.3.1 Tujuan Pengujian

Tujuan dari pengujian black-box adalah:

- Memastikan setiap fungsi dalam sistem berjalan dengan baik
- Memastikan sistem mampu menerima dan memproses input dengan benar
- Memastikan output yang dihasilkan sesuai dengan yang diharapkan
- Menemukan kesalahan atau bug pada sistem

### 4.3.2 Skenario Pengujian

Pengujian dilakukan pada beberapa modul utama dalam sistem, yaitu:

**Tabel 4.1 Skenario Black-box Testing**

| No | Modul | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|-------|-------------------|----------------------|-------|
| 1 | Login | Input email & password benar | Berhasil login | Berhasil |
| 2 | Login | Input salah | Gagal login | Berhasil |
| 3 | Data Aset | Tambah data aset | Data tersimpan | Berhasil |
| 4 | Data Aset | Edit data aset | Data terupdate | Berhasil |
| 5 | Data Aset | Hapus data | Data terhapus | Berhasil |
| 6 | Barang Masuk | Input data | Stok bertambah | Berhasil |
| 7 | Barang Keluar | Input data valid | Stok berkurang | Berhasil |
| 8 | Barang Keluar | Stok tidak cukup | Muncul error | Berhasil |
| 9 | Laporan | Generate laporan | File PDF muncul | Berhasil |
| 10 | QR Code | Scan QR | Data tampil | Berhasil |

### 4.3.3 Hasil Pengujian

Berdasarkan hasil pengujian yang telah dilakukan, seluruh fitur utama dalam sistem berjalan sesuai dengan yang diharapkan. Sistem mampu menerima input dengan baik, memproses data secara benar, serta menghasilkan output yang sesuai.

Tidak ditemukan kesalahan yang signifikan dalam proses pengujian. Sistem juga mampu menangani kondisi normal maupun kondisi error dengan baik, seperti saat input data tidak valid atau ketika stok tidak mencukupi.

### 4.3.4 Analisis Hasil

Dari hasil pengujian black-box, dapat disimpulkan bahwa:

- Sistem telah memenuhi kebutuhan fungsional
- Seluruh modul dapat berjalan dengan baik
- Sistem mudah digunakan oleh pengguna
- Tidak ditemukan bug yang mengganggu penggunaan sistem

Dengan demikian, sistem informasi manajemen aset yang dikembangkan dinyatakan layak untuk digunakan dalam mendukung pengelolaan aset di RBTV Bengkulu.

---

## 4.4 Implementasi

Implementasi merupakan tahap penerapan sistem yang telah dikembangkan agar dapat digunakan oleh pengguna. Pada tahap ini dijelaskan bagaimana sistem dijalankan, digunakan, serta bagaimana pengguna dapat berinteraksi dengan sistem dalam kegiatan sehari-hari.

Sistem informasi manajemen aset yang dikembangkan berbasis web sehingga dapat diakses melalui browser tanpa memerlukan instalasi aplikasi khusus pada perangkat pengguna. Sistem ini dirancang agar mudah digunakan oleh berbagai jenis pengguna, seperti admin dan staff.

Implementasi sistem mencakup penggunaan fitur-fitur utama yang telah dibangun, mulai dari login hingga pengelolaan data aset dan pembuatan laporan.

### 4.4.1 Manual Program

Manual program merupakan panduan penggunaan sistem bagi pengguna. Panduan ini bertujuan untuk membantu pengguna dalam memahami cara menggunakan sistem dengan benar.

Berikut adalah langkah-langkah penggunaan sistem:

**1. Login ke Sistem**
- Pengguna membuka halaman login melalui browser
- Memasukkan email dan password
- Klik tombol login
- Jika data benar, pengguna akan diarahkan ke dashboard

**2. Mengakses Dashboard**
- Setelah login, pengguna akan melihat halaman dashboard
- Dashboard menampilkan ringkasan data aset
- Pengguna dapat melihat statistik dan informasi penting

**3. Mengelola Data Aset**
- Pilih menu data aset
- Klik tombol tambah untuk menambahkan data baru
- Isi form yang tersedia
- Klik simpan untuk menyimpan data
- Pengguna juga dapat mengedit dan menghapus data

**4. Input Barang Masuk**
- Pilih menu barang masuk
- Isi data barang masuk
- Sistem akan menambahkan stok secara otomatis

**5. Input Barang Keluar**
- Pilih menu barang keluar
- Isi data barang keluar
- Sistem akan mengurangi stok secara otomatis

**6. Scan QR Code**
- Pilih menu scan QR
- Arahkan kamera ke QR Code aset
- Sistem akan menampilkan informasi aset

**7. Generate Laporan**
- Pilih menu laporan
- Pilih jenis laporan
- Klik generate
- Sistem akan menampilkan atau mengunduh file PDF

Dengan adanya manual program ini, pengguna dapat dengan mudah memahami cara menggunakan sistem tanpa mengalami kesulitan.

### 4.4.2 Manual Instalasi (Opsional)

Manual instalasi merupakan panduan untuk menginstal dan menjalankan sistem pada perangkat baru. Berikut langkah-langkah instalasi sistem:

**1. Persiapan**
- Install Laragon atau XAMPP
- Install PHP dan MySQL
- Install Composer

**2. Setup Project**

```bash
composer install
cp .env.example .env
php artisan key:generate
```

**3. Setup Database**
- Buat database baru di MySQL
- Atur konfigurasi database pada file .env

```bash
php artisan migrate
```

**4. Menjalankan Sistem**

```bash
php artisan serve
```

- Akses sistem melalui browser: `http://127.0.0.1:8000`

Dengan mengikuti langkah-langkah tersebut, sistem dapat dijalankan pada lingkungan lokal.

---

## 4.5 Pemeliharaan (Opsional)

Pemeliharaan sistem merupakan tahap yang dilakukan setelah sistem diimplementasikan dan digunakan oleh pengguna. Tujuan dari pemeliharaan adalah untuk memastikan sistem tetap berjalan dengan baik, memperbaiki kesalahan yang mungkin muncul, serta menyesuaikan sistem dengan kebutuhan pengguna yang terus berkembang.

Pemeliharaan sistem sangat penting karena dalam penggunaan nyata, sistem dapat mengalami berbagai perubahan kondisi, baik dari sisi pengguna, data, maupun lingkungan teknologi. Oleh karena itu, sistem perlu dilakukan pemeliharaan secara berkala agar tetap optimal.

Dalam penelitian ini, pemeliharaan sistem dilakukan dalam beberapa bentuk, yaitu:

### 4.5.1 Pemeliharaan Korektif (Corrective Maintenance)

Pemeliharaan korektif dilakukan untuk memperbaiki kesalahan atau bug yang ditemukan setelah sistem digunakan. Kesalahan tersebut dapat berupa error pada program, kesalahan logika, maupun kesalahan dalam proses pengolahan data.

### 4.5.2 Pemeliharaan Adaptif (Adaptive Maintenance)

Pemeliharaan adaptif dilakukan untuk menyesuaikan sistem dengan perubahan lingkungan, seperti pembaruan sistem operasi, perubahan kebutuhan pengguna, atau penyesuaian teknologi yang digunakan.

### 4.5.3 Pemeliharaan Perfektif (Perfective Maintenance)

Pemeliharaan perfektif dilakukan untuk meningkatkan kinerja sistem serta menambah fitur baru yang dapat meningkatkan kualitas sistem. Contohnya adalah penambahan fitur notifikasi atau pengembangan aplikasi mobile.

### 4.5.4 Pemeliharaan Preventif (Preventive Maintenance)

Pemeliharaan preventif dilakukan untuk mencegah terjadinya kerusakan sistem di masa depan. Kegiatan ini meliputi backup data secara berkala, monitoring sistem, serta pengecekan keamanan sistem.

Dalam sistem informasi manajemen aset yang dikembangkan, pemeliharaan dilakukan dengan cara melakukan backup database secara berkala, memantau performa sistem, memperbaiki bug yang ditemukan, serta melakukan update sistem jika diperlukan.

Dengan adanya proses pemeliharaan yang baik, sistem diharapkan dapat digunakan dalam jangka panjang serta tetap mampu memenuhi kebutuhan pengguna.
