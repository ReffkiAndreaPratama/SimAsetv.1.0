# MODUL 6 - IMPLEMENTASI AUTENTIKASI DAN HAK AKSES

## 6.1 Pendahuluan

Autentikasi dan pengelolaan hak akses merupakan bagian penting dalam pengembangan SimAset karena berkaitan langsung dengan keamanan, keandalan, dan integritas data sistem. Sistem informasi yang tidak memiliki mekanisme autentikasi dan pembatasan hak akses berpotensi mengalami penyalahgunaan, seperti perubahan data tanpa izin, penghapusan data penting, atau akses ilegal ke fitur administratif.

Pada sistem ini, autentikasi diterapkan untuk semua pengguna (Admin dan Staff), sedangkan pembatasan hak akses dilakukan berdasarkan role masing-masing pengguna. Pendekatan ini dipilih untuk menjaga keseimbangan antara keamanan sistem dan kemudahan akses bagi seluruh pengelola aset. Modul ini membahas konsep autentikasi, implementasi login dan logout, pengelolaan role pengguna, penggunaan middleware sebagai mekanisme keamanan, serta pengujian hak akses secara menyeluruh.

## 6.2 Implementasi Login dan Logout

### 6.2.1 Konsep Autentikasi Sistem

Autentikasi merupakan proses verifikasi identitas pengguna berdasarkan kredensial yang dimasukkan ke dalam sistem. Kredensial tersebut berupa email dan password. Dalam SimAset, autentikasi diterapkan untuk memastikan bahwa hanya pengguna yang terdaftar dan aktif yang dapat mengakses fitur pengelolaan data.

Laravel menyediakan sistem autentikasi bawaan melalui Laravel Breeze yang mendukung pengelolaan session, enkripsi password menggunakan bcrypt, serta perlindungan terhadap serangan keamanan dasar seperti CSRF dan brute force. Password pengguna disimpan dalam bentuk terenkripsi sehingga tidak dapat dibaca secara langsung oleh pihak lain.

### 6.2.2 Alur Proses Login

Proses login dimulai ketika pengguna mengakses halaman login sistem. Pengguna kemudian memasukkan email dan password yang telah terdaftar. Sistem akan melakukan beberapa tahapan berikut:

1. Menerima input email dan password dari pengguna.
2. Melakukan validasi input untuk memastikan data tidak kosong dan format email valid.
3. Memeriksa rate limiting untuk mencegah serangan brute force (maksimal 5 percobaan per menit).
4. Membandingkan kredensial dengan data yang tersimpan di database.
5. Memverifikasi password menggunakan metode enkripsi bcrypt.
6. Melakukan session regenerate untuk mencegah session fixation attack.
7. Membuat session login jika autentikasi berhasil.
8. Mencatat aktivitas Login ke tabel log_aktivitas.
9. Mengarahkan pengguna ke halaman dashboard.

Jika proses autentikasi gagal, sistem akan menampilkan pesan kesalahan tanpa memberikan akses ke halaman sistem. Mekanisme ini bertujuan untuk mencegah akses tidak sah ke sistem.

> **[GAMBAR 6.1: Tampilan halaman login SimAset dengan panel kiri biru dan panel kanan form login]**

### 6.2.3 Alur Proses Logout

Logout berfungsi untuk mengakhiri session login yang sedang aktif. Proses logout dilakukan ketika pengguna memilih menu logout pada sidebar. Sistem akan menghapus session login, menginvalidasi token CSRF, dan mengarahkan pengguna kembali ke halaman login. Proses logout sangat penting untuk menjaga keamanan sistem, terutama ketika pengguna mengakses sistem melalui perangkat umum atau bersama. Dengan logout, risiko penyalahgunaan akses oleh pihak lain dapat diminimalkan.

## 6.3 Manajemen Role (Admin dan Staff)

Manajemen role digunakan untuk membedakan hak dan kewajiban setiap pengguna dalam sistem. Pada SimAset, diterapkan dua role utama, yaitu Admin dan Staff.

### 6.3.1 Role Admin

Admin merupakan pengguna dengan hak akses tertinggi dalam sistem. Admin bertanggung jawab dalam pengelolaan seluruh data dan fitur sistem. Hak akses Admin meliputi:

1. Mengelola data aset (tambah, ubah, hapus, batch delete).
2. Mengelola master data barang dan ruangan.
3. Generate dan mencetak QR Code aset.
4. Menandai aset masuk dan selesai maintenance.
5. Import data massal dari Excel/CSV.
6. Export data dan mencetak laporan.
7. Mengakses dashboard administrasi sistem.
8. **Mengelola akun pengguna (tambah, ubah, hapus).**
9. **Melihat audit log seluruh aktivitas pengguna.**

Admin memiliki peran strategis dalam menjaga kualitas dan keakuratan data aset yang ditampilkan kepada pengguna.

### 6.3.2 Role Staff

Staff merupakan pengguna operasional yang mengelola data aset sehari-hari. Staff memiliki akses ke seluruh fitur operasional namun tidak dapat mengakses fitur administratif.

Hak akses Staff meliputi:

1. Mengelola data aset (tambah, ubah, hapus, batch delete).
2. Mengelola master data barang dan ruangan.
3. Generate dan mencetak QR Code aset.
4. Menandai aset masuk dan selesai maintenance.
5. Import data massal dari Excel/CSV.
6. Export data dan mencetak laporan.
7. Mengedit profil sendiri.

Staff tidak memiliki hak untuk mengelola akun pengguna atau melihat audit log. Pembatasan ini bertujuan untuk menjaga integritas data dan keamanan sistem.

## 6.4 Middleware dan Keamanan Akses

Middleware merupakan mekanisme Laravel yang digunakan untuk menyaring dan mengontrol setiap permintaan yang masuk ke sistem sebelum diteruskan ke controller. Middleware memainkan peran penting dalam pengelolaan hak akses sistem.

### 6.4.1 Fungsi Middleware

Middleware digunakan untuk:

1. Memastikan hanya pengguna yang telah login dapat mengakses halaman sistem (middleware `auth`).
2. Mencegah pengguna dengan role Staff mengakses halaman admin (middleware `role:admin`).
3. Mengalihkan pengguna ke halaman login jika belum terautentikasi.
4. Menambahkan security headers ke setiap response (SecurityHeaders middleware).
5. Mencatat aktivitas pengguna secara otomatis (LogActivity middleware).

Dengan middleware, kontrol akses sistem dapat dilakukan secara terpusat dan konsisten.

### 6.4.2 Implementasi Middleware pada Sistem

Dalam sistem ini, middleware diterapkan pada route yang berkaitan dengan pengelolaan data dan dashboard. Setiap permintaan menuju route yang dilindungi akan diperiksa status autentikasinya terlebih dahulu. Jika pengguna belum login, sistem akan otomatis mengarahkan pengguna ke halaman login. Jika pengguna tidak memiliki role yang sesuai, sistem akan mengembalikan HTTP 403 Forbidden.

```php
// Route untuk semua pengguna yang sudah login
Route::middleware(['auth'])->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index']);
    Route::resource('aset', AssetController::class);
    // ...
});

// Route khusus Admin
Route::middleware('role:admin')->group(function () {
    Route::resource('users', UserController::class);
    Route::get('/audit-log', [AuditLogController::class, 'index']);
});
```

Pendekatan ini memastikan bahwa fitur sensitif hanya dapat diakses oleh pengguna yang berwenang.

## 6.5 Pengujian Hak Akses

Pengujian hak akses dilakukan untuk memastikan bahwa mekanisme autentikasi dan pembatasan akses berjalan sesuai dengan perancangan sistem. Pengujian dilakukan menggunakan beberapa skenario penggunaan sistem.

Skenario pengujian meliputi:

1. Login Admin dengan kredensial yang valid.
2. Login Staff dengan kredensial yang valid.
3. Login dengan kredensial yang tidak valid.
4. Akses halaman dashboard tanpa login.
5. Akses halaman manajemen pengguna menggunakan akun Staff.
6. Akses halaman audit log menggunakan akun Staff.
7. Logout dan pengujian session berakhir.
8. Akses kembali halaman sistem setelah logout.

Hasil pengujian menunjukkan bahwa sistem mampu membedakan hak akses Admin dan Staff dengan baik serta mencegah akses ilegal ke fitur administratif.

> **[GAMBAR 6.2: Tampilan pesan error HTTP 403 saat Staff mencoba mengakses halaman manajemen pengguna]**

## 6.6 Kesimpulan Modul

Modul 6 membahas implementasi autentikasi dan hak akses pada SimAset secara mendalam. Dengan penerapan autentikasi login dan logout menggunakan Laravel Breeze, manajemen role pengguna melalui RoleMiddleware, serta penggunaan SecurityHeaders dan LogActivity middleware, sistem memiliki mekanisme keamanan yang memadai untuk melindungi data dan fitur penting.

Implementasi autentikasi dan hak akses ini memastikan bahwa pengelolaan data aset hanya dilakukan oleh pengguna yang berwenang, sementara fitur administratif hanya dapat diakses oleh Admin. Modul ini menjadi fondasi penting sebelum pengembangan modul lanjutan yang berfokus pada manajemen data dan fitur interaktif sistem.
