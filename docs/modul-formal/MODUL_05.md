# MODUL 5 - PERANCANGAN DAN IMPLEMENTASI DATABASE

## 5.1 Pendahuluan

Database merupakan komponen paling vital dalam SimAset karena seluruh data yang ditampilkan kepada pengguna bersumber dari database. Database tidak hanya berfungsi sebagai tempat penyimpanan data, tetapi juga sebagai penghubung antara proses bisnis sistem, logika aplikasi, dan antarmuka pengguna.

Perancangan database yang kurang baik dapat menyebabkan berbagai permasalahan, seperti redundansi data, inkonsistensi informasi, performa sistem yang lambat, serta kesulitan dalam pengembangan fitur lanjutan. Oleh karena itu, pada modul ini dilakukan pembahasan mendalam mengenai bagaimana database dirancang, diimplementasikan, dan diuji agar mampu mendukung kebutuhan sistem secara optimal. Modul ini juga menjelaskan pemanfaatan fitur migration dan seeder pada framework Laravel sebagai pendekatan modern dalam pengelolaan struktur dan isi database.

## 5.2 Perancangan Struktur Database

Perancangan struktur database dilakukan berdasarkan hasil analisis kebutuhan sistem dan perancangan sistem pada modul sebelumnya. Struktur database dirancang menggunakan pendekatan database relasional, di mana data disimpan dalam tabel-tabel yang saling berhubungan. Dalam perancangan ini diterapkan prinsip normalisasi database, yang bertujuan untuk:

1. Mengurangi duplikasi data.
2. Menjaga konsistensi dan integritas data.
3. Mempermudah proses pemeliharaan database.
4. Meningkatkan efisiensi penyimpanan dan pengambilan data.

Struktur database mencakup tabel-tabel utama seperti tabel users, barang, ruangan, aset, dan log_aktivitas. Setiap tabel dirancang memiliki primary key sebagai identitas unik dan foreign key sebagai penghubung antar tabel. Selain itu, struktur database dirancang agar kompatibel dengan ORM Eloquent Laravel, sehingga memudahkan pengembang dalam mengelola data melalui kode program.

> **[GAMBAR 5.1: Tampilan phpMyAdmin menampilkan daftar semua tabel di database simset_rbtv]**

## 5.3 Pembuatan Migration (Step-by-Step)

Migration digunakan untuk membuat dan mengelola struktur tabel database secara terstruktur dan terprogram. Dengan menggunakan migration, perubahan struktur database dapat dilakukan secara konsisten dan terdokumentasi dengan baik.

### 5.3.1 Migration Tabel Users

Tabel users digunakan untuk menyimpan data pengguna sistem, baik Admin maupun Staff yang memiliki hak akses pengelolaan data aset.

Langkah-langkah pembuatan migration tabel users adalah sebagai berikut:

1. Buka Terminal atau Command Prompt.
2. Jalankan perintah berikut:

```bash
php artisan make:migration create_users_table
```

3. Buka file migration yang dihasilkan pada folder database/migrations/.
4. Sesuaikan struktur tabel users sebagai berikut:

```php
Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('name', 100);
    $table->string('email', 100)->unique();
    $table->string('password');
    $table->enum('role', ['admin', 'staff'])->default('staff');
    $table->tinyInteger('is_active')->default(1);
    $table->timestamp('last_login_at')->nullable();
    $table->timestamps();
});
```

### 5.3.2 Migration Tabel Barang

Tabel barang digunakan untuk menyimpan master data jenis/tipe barang yang menjadi referensi setiap aset.

Langkah-langkah pembuatan migration tabel barang:

1. Jalankan perintah berikut:

```bash
php artisan make:migration create_barang_table
```

2. Atur struktur tabel barang sebagai berikut:

```php
Schema::create('barang', function (Blueprint $table) {
    $table->string('kode_barang', 20)->primary();
    $table->string('nama_barang', 150);
    $table->enum('kategori', [
        'Kamera','Audio','Komputer',
        'Lighting','Furniture','Peralatan Kantor'
    ]);
    $table->enum('status', ['aktif','nonaktif'])->default('aktif');
    $table->text('keterangan')->nullable();
    $table->timestamps();
    $table->softDeletes();
});
```

### 5.3.3 Migration Tabel Ruangan

Tabel ruangan digunakan untuk menyimpan data lokasi/ruangan tempat aset ditempatkan.

Langkah-langkah pembuatan migration tabel ruangan:

1. Jalankan perintah:

```bash
php artisan make:migration create_ruangan_table
```

2. Sesuaikan struktur tabel ruangan sebagai berikut:

```php
Schema::create('ruangan', function (Blueprint $table) {
    $table->id();
    $table->string('nama', 100);
    $table->string('lantai', 50)->nullable();
    $table->text('keterangan')->nullable();
    $table->timestamp('created_at')->useCurrent();
});
```

### 5.3.4 Migration Tabel Aset

Tabel aset merupakan tabel utama yang menyimpan seluruh data aset fisik barang kantor RBTV.

Langkah-langkah pembuatan migration tabel aset:

1. Jalankan perintah:

```bash
php artisan make:migration create_aset_table
```

2. Sesuaikan struktur tabel aset sebagai berikut:

```php
Schema::create('aset', function (Blueprint $table) {
    $table->string('kode_aset', 20)->primary();
    $table->string('kode_barang', 20);
    $table->integer('ruangan_id')->nullable();
    $table->enum('kondisi', ['Baik','Rusak Ringan','Rusak Berat'])
          ->default('Baik');
    $table->enum('status', ['Aktif','Maintenance','Non-Aktif'])
          ->default('Aktif');
    $table->string('serial_number', 100)->nullable();
    $table->string('foto', 255)->nullable();
    $table->integer('jumlah')->default(1);
    $table->date('tanggal_perolehan')->nullable();
    $table->decimal('harga_perolehan', 15, 2)->nullable();
    $table->string('sumber_perolehan')->nullable();
    $table->text('keterangan')->nullable();
    $table->integer('created_by')->nullable();
    $table->integer('updated_by')->nullable();
    $table->timestamps();
    $table->softDeletes();

    $table->foreign('kode_barang')
          ->references('kode_barang')->on('barang')
          ->onDelete('restrict')->onUpdate('cascade');
    $table->foreign('ruangan_id')
          ->references('id')->on('ruangan')
          ->onDelete('set null')->onUpdate('cascade');
});
```

### 5.3.5 Migration Tabel Log Aktivitas

Tabel log_aktivitas digunakan untuk menyimpan audit trail seluruh aktivitas pengguna.

```php
Schema::create('log_aktivitas', function (Blueprint $table) {
    $table->bigIncrements('id');
    $table->unsignedBigInteger('user_id')->nullable();
    $table->string('aktivitas');
    $table->text('keterangan')->nullable();
    $table->string('ip_address', 45)->nullable();
    $table->text('user_agent')->nullable();
    $table->timestamps();

    $table->foreign('user_id')
          ->references('id')->on('users')
          ->onDelete('set null');
});
```

## 5.4 Menjalankan Migration

Setelah seluruh file migration dibuat dan disesuaikan, jalankan perintah berikut untuk membuat tabel pada database:

```bash
php artisan migrate
```

Jika tidak terdapat error pada proses migrasi, maka seluruh tabel database berhasil dibuat sesuai dengan perancangan sistem.

> **[GAMBAR 5.2: Tampilan terminal saat php artisan migrate berjalan dan berhasil membuat semua tabel]**

## 5.5 Pembuatan Seeder (Data Awal)

Seeder digunakan untuk mengisi data awal ke dalam database, seperti akun Admin, Staff, dan data contoh barang serta ruangan.

### 5.5.1 Membuat Seeder Admin

1. Jalankan perintah berikut:

```bash
php artisan make:seeder AdminSeeder
```

2. Pada file seeder, isi data admin sebagai berikut:

```php
User::updateOrCreate(
    ['email' => 'magangrbtv@gmail.com'],
    [
        'name'      => 'Admin Magang',
        'password'  => Hash::make('Magang123'),
        'role'      => 'admin',
        'is_active' => true,
    ]
);
```

3. Jalankan seeder dengan perintah:

```bash
php artisan db:seed --class=AdminSeeder
```

### 5.5.2 Membuat Seeder Staff

```php
User::updateOrCreate(
    ['email' => 'staff@rbtv.id'],
    [
        'name'      => 'Staff RBTV',
        'password'  => Hash::make('Staff123'),
        'role'      => 'staff',
        'is_active' => true,
    ]
);
```

### 5.5.3 Membuat Seeder Barang dan Ruangan

Seeder BarangSeeder membuat data awal yang realistis untuk RBTV, meliputi:

- 4 ruangan: Studio 1, Studio 2, Ruang Editing, Ruang Redaksi
- Master barang: Kamera Sony A7 (BRG-001), Mic Wireless Rode (BRG-002)
- Contoh aset: AST-001 (Kamera Sony A7 di Ruang Editing, status Maintenance), AST-002 (Kamera Sony A7 di Ruang Editing, status Aktif)

Jalankan semua seeder sekaligus:

```bash
php artisan db:seed
```

Atau reset dan jalankan ulang dari awal:

```bash
php artisan migrate:fresh --seed
```

> **[GAMBAR 5.3: Tampilan data tabel aset di phpMyAdmin menampilkan AST-001 (Maintenance) dan AST-002 (Aktif)]**

## 5.6 Relasi Antar Tabel

Relasi antar tabel merupakan aspek penting dalam perancangan database karena menentukan bagaimana data saling terhubung. Relasi yang dirancang dalam sistem ini mencerminkan proses bisnis pengelolaan aset.

Beberapa relasi utama dalam database adalah sebagai berikut:

1. **Relasi Barang – Aset**
   Relasi ini bersifat one-to-many, di mana satu barang (jenis) dapat memiliki banyak aset (unit fisik). Relasi ini menggunakan FK RESTRICT on delete, sehingga barang tidak dapat dihapus jika masih ada aset yang merujuk.

2. **Relasi Ruangan – Aset**
   Setiap aset ditempatkan di satu ruangan, sementara satu ruangan dapat memiliki banyak aset. Relasi ini menggunakan FK SET NULL on delete, sehingga jika ruangan dihapus, kolom ruangan_id pada aset menjadi NULL.

3. **Relasi Users – Log Aktivitas**
   Satu pengguna dapat memiliki banyak log aktivitas. Relasi ini menggunakan FK SET NULL on delete untuk menjaga integritas log meskipun akun pengguna dihapus.

Perancangan relasi ini bertujuan untuk menjaga integritas data dan mendukung fleksibilitas sistem dalam menampilkan informasi.

## 5.7 Pengujian Database

Pengujian database dilakukan untuk memastikan bahwa struktur dan data database telah dibuat dengan benar. Pengujian dilakukan dengan langkah-langkah berikut:

1. Membuka phpMyAdmin atau MySQL Workbench.
2. Memastikan seluruh tabel berhasil dibuat sesuai migration.
3. Memastikan data Admin dan Staff berhasil ditambahkan ke tabel users.
4. Memastikan data barang dan ruangan berhasil dibuat oleh seeder.
5. Memastikan relasi antar tabel berjalan dengan baik.

Jika seluruh pengujian berhasil, maka database dinyatakan siap digunakan pada tahap implementasi sistem selanjutnya.

> **[GAMBAR 5.4: Tampilan phpMyAdmin menampilkan relasi antar tabel di database simset_rbtv]**

## 5.8 Kesimpulan Modul

Modul 5 membahas perancangan dan implementasi database SimAset secara mendalam. Dengan database yang dirancang menggunakan prinsip relasional, normalisasi data, serta diimplementasikan menggunakan migration dan seeder Laravel, sistem memiliki fondasi data yang kuat dan terstruktur.

Database yang baik akan memudahkan proses pengelolaan data, meningkatkan performa sistem, serta membuka peluang pengembangan fitur lanjutan pada modul berikutnya.
