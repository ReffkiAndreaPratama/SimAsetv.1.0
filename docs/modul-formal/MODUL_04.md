# MODUL 4 - PERSIAPAN LINGKUNGAN PENGEMBANGAN

## 4.1 Pendahuluan

Persiapan lingkungan pengembangan merupakan tahapan krusial dalam siklus pengembangan perangkat lunak karena menjadi fondasi sebelum proses implementasi sistem dilakukan. Lingkungan pengembangan yang tidak disiapkan dengan baik dapat menyebabkan berbagai permasalahan teknis, seperti error konfigurasi, kegagalan koneksi database, serta kesulitan dalam pengujian sistem.

Pada pengembangan SimAset, lingkungan pengembangan dirancang agar mendukung proses pengembangan berbasis web dengan framework Laravel serta integrasi fitur QR Code. Oleh karena itu, diperlukan penyiapan perangkat lunak pendukung, konfigurasi sistem, dan pengujian awal untuk memastikan seluruh komponen dapat berjalan secara optimal.

Modul ini membahas secara rinci tahapan persiapan lingkungan pengembangan, mulai dari kebutuhan perangkat lunak hingga pengujian awal sistem, sebagai dasar sebelum memasuki tahap implementasi fitur-fitur sistem.

## 4.2 Kebutuhan Perangkat Lunak

Kebutuhan perangkat lunak dalam pengembangan sistem ini disesuaikan dengan arsitektur dan teknologi yang digunakan. Perangkat lunak yang dipilih harus mampu mendukung pengembangan aplikasi web yang stabil, aman, dan mudah dikembangkan.

1. **Sistem Operasi**
   Sistem operasi berfungsi sebagai platform utama pengembangan. Sistem ini dapat dikembangkan pada sistem operasi Windows, Linux, maupun macOS. Pemilihan sistem operasi disesuaikan dengan kenyamanan dan kebutuhan pengembang.

2. **Web Server**
   Web server digunakan untuk menjalankan aplikasi web secara lokal selama proses pengembangan. Web server berfungsi menerima permintaan dari browser dan mengeksekusi aplikasi Laravel. Web server yang umum digunakan adalah Apache dan Nginx.

3. **Database Server**
   Database server digunakan untuk menyimpan seluruh data sistem, seperti data aset, master barang, master ruangan, pengguna, dan log aktivitas. Sistem ini menggunakan MySQL 8.0.30 dengan nama database simset_rbtv karena stabil, mudah digunakan, dan kompatibel dengan Laravel.

4. **Bahasa Pemrograman PHP**
   PHP digunakan sebagai bahasa pemrograman utama dalam pengembangan backend sistem. Versi PHP yang digunakan adalah 8.2 atau lebih baru, sesuai dengan kebutuhan framework Laravel 12 agar sistem dapat berjalan dengan optimal.

5. **Framework Laravel**
   Laravel 12 dipilih karena menyediakan struktur pengembangan yang rapi, menerapkan pola MVC, serta memiliki fitur keamanan dan manajemen database yang baik melalui Eloquent ORM.

6. **Node.js dan NPM**
   Node.js dan NPM digunakan untuk mengelola dependensi frontend seperti Tailwind CSS dan Alpine.js melalui Vite sebagai build tool.

7. **Code Editor dan Browser**
   Code editor seperti Visual Studio Code digunakan untuk menulis dan mengelola kode program, sedangkan web browser digunakan untuk pengujian sistem secara langsung.

## 4.3 Instalasi Web Server dan Database

Untuk mempermudah proses pengembangan, digunakan paket web server lokal seperti Laragon. Paket ini menyediakan web server (Apache/Nginx), PHP, dan MySQL dalam satu instalasi. Proses instalasi dilakukan dengan mengunduh installer dari situs resmi, kemudian menjalankan proses instalasi sesuai petunjuk. Setelah instalasi selesai, web server dan database dijalankan melalui control panel.

**Langkah-langkah instalasi Laragon:**

1. Buka link https://laragon.org/download/ untuk mengunduh Laragon versi Full.
2. Jika sudah terunduh, jalankan file installer lalu pilih lokasi instalasi file Laragon.

> **[GAMBAR 4.1: Tampilan installer Laragon saat memilih direktori instalasi]**

3. Jika sudah terinstal, buka Laragon dan klik **Start All** di pojok kiri bawah untuk menjalankan Apache/Nginx dan MySQL. Klik **Stop** jika sudah selesai menggunakannya.

> **[GAMBAR 4.2: Tampilan Laragon Control Panel setelah berhasil dijalankan dengan Apache dan MySQL berstatus Running]**

## 4.4 Instalasi Composer

Composer digunakan untuk mengelola dependensi Laravel.

**Langkah instalasi Composer:**

1. Unduh Composer dari https://getcomposer.org

> **[GAMBAR 4.3: Halaman download Composer di getcomposer.org]**

2. Jalankan installer Composer dan pastikan Composer terhubung dengan PHP Laragon. Dengan kode ini:

```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

3. Setelah instalasi selesai, buka Command Prompt atau Terminal dan jalankan perintah berikut untuk memastikan Composer terpasang:

```bash
composer --version
```

Jika versi Composer muncul, maka instalasi berhasil.

## 4.5 Instalasi Framework Laravel

Framework Laravel digunakan sebagai fondasi utama dalam pengembangan sistem. Laravel menyediakan berbagai fitur bawaan seperti routing, autentikasi, dan ORM yang memudahkan pengembang. Instalasi Laravel dilakukan menggunakan Composer, yaitu dependency manager untuk PHP. Setelah Laravel terinstal, struktur dasar project akan terbentuk secara otomatis, mencakup folder aplikasi, konfigurasi, dan resource tampilan.

**Langkah-langkah:**

1. Buka terminal Laragon.

2. Arahkan ke folder root Laragon. Buka Command Prompt atau Terminal, kemudian arahkan ke direktori root Laragon dengan perintah:

```bash
cd E:\Laragon\www
```

3. Clone repository project SimAset:

```bash
git clone https://github.com/[username]/simaset-rbtv.git
cd simaset-rbtv
```

4. Instal dependensi PHP menggunakan Composer:

```bash
composer install
```

5. Instal dependensi JavaScript menggunakan NPM:

```bash
npm install
```

6. Salin file environment dan generate application key:

```bash
cp .env.example .env
php artisan key:generate
```

7. Konfigurasi file `.env` untuk koneksi database:

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=simset_rbtv
DB_USERNAME=root
DB_PASSWORD=
```

8. Jalankan migrasi dan seeder database:

```bash
php artisan migrate --seed
```

9. Build asset frontend:

```bash
npm run build
```

10. Menjalankan server Laravel:

```bash
php artisan serve
```

11. Mengakses aplikasi melalui browser. Buka web browser dan akses alamat berikut:

```
http://127.0.0.1:8000
```

12. Verifikasi instalasi. Jika halaman login SimAset berhasil ditampilkan pada browser, maka proses instalasi framework Laravel telah berhasil dan lingkungan pengembangan siap digunakan untuk tahap implementasi sistem.

> **[GAMBAR 4.4: Tampilan halaman login SimAset pertama kali diakses di browser setelah instalasi berhasil]**

## 4.6 Konfigurasi Project

Setelah Laravel berhasil diinstal, dilakukan konfigurasi project agar sistem dapat berjalan sesuai kebutuhan. Konfigurasi ini meliputi pengaturan koneksi database, pengaturan environment aplikasi, serta penyesuaian parameter sistem.

Pengaturan koneksi database dilakukan dengan menentukan nama database (simset_rbtv), username, dan password yang sesuai. Selain itu, pengaturan timezone (Asia/Jakarta) dan locale (id) dilakukan agar sistem menyesuaikan dengan wilayah operasional. Konfigurasi mail juga perlu disesuaikan — untuk development gunakan driver `log`, untuk production gunakan SMTP.

Konfigurasi project yang tepat akan memastikan aplikasi dapat berjalan stabil dan meminimalkan kesalahan pada tahap implementasi.

## 4.7 Struktur Folder Project

Laravel memiliki struktur folder yang dirancang secara terorganisir untuk mendukung pengembangan berbasis MVC. Struktur ini memisahkan logika aplikasi, tampilan, dan konfigurasi sistem.

```
simaset-rbtv/
├── app/
│   ├── Exports/          ← Kelas export Excel
│   ├── Helpers/          ← ActivityLogger, ImageHelper
│   ├── Http/
│   │   ├── Controllers/  ← 13 controller utama
│   │   ├── Middleware/   ← RoleMiddleware, SecurityHeaders, LogActivity
│   │   └── Requests/     ← Form request validation
│   ├── Imports/          ← Kelas import Excel
│   ├── Mail/             ← AkunBaruMail, MaintenanceAlert
│   └── Models/           ← Asset, Barang, Ruangan, User, ActivityLog
├── database/
│   ├── migrations/       ← 14 file migration
│   └── seeders/          ← AdminSeeder, StaffSeeder, BarangSeeder
├── public/
│   ├── foto_aset/        ← Upload foto aset
│   └── qr_codes/         ← File QR Code yang di-generate
├── resources/
│   ├── css/              ← app.css (Tailwind)
│   ├── js/               ← app.js (Alpine.js)
│   └── views/            ← Blade templates
├── routes/
│   ├── web.php           ← Route web utama
│   └── auth.php          ← Route autentikasi (Breeze)
├── .env                  ← Environment variables
├── composer.json         ← Dependensi PHP
└── package.json          ← Dependensi JavaScript
```

Struktur folder yang rapi memudahkan pengembang dalam memahami dan memelihara kode program.

> **[GAMBAR 4.5: Tampilan struktur folder project SimAset di Visual Studio Code Explorer]**

## 4.8 Pengujian Awal Lingkungan

Pengujian awal lingkungan pengembangan dilakukan untuk memastikan bahwa seluruh komponen sistem telah berjalan dengan baik. Pengujian ini meliputi menjalankan server Laravel, mengakses aplikasi melalui browser, serta memastikan koneksi database berjalan normal. Selain itu, dilakukan pengecekan terhadap error konfigurasi dan validasi struktur folder.

Langkah pengujian awal:

1. Jalankan `php artisan serve` dan akses `http://127.0.0.1:8000`.
2. Login dengan akun Admin: magangrbtv@gmail.com / Magang123.
3. Pastikan dashboard tampil dengan data statistik aset.
4. Cek koneksi database dengan `php artisan db:show`.
5. Cek status migrasi dengan `php artisan migrate:status`.

Jika sistem dapat dijalankan tanpa kendala, maka lingkungan pengembangan dinyatakan siap untuk tahap implementasi fitur sistem. Pengujian awal ini bertujuan untuk mencegah permasalahan teknis yang dapat menghambat proses pengembangan pada tahap selanjutnya.

## 4.9 Kesimpulan Modul

Modul 4 membahas persiapan lingkungan pengembangan SimAset secara menyeluruh. Dengan lingkungan pengembangan yang telah disiapkan dan diuji dengan baik, proses implementasi sistem dapat dilakukan secara lebih terstruktur dan efisien. Lingkungan pengembangan yang stabil menjadi fondasi utama dalam menghasilkan sistem informasi yang berkualitas, mudah dikembangkan, dan siap digunakan pada tahap implementasi berikutnya.
