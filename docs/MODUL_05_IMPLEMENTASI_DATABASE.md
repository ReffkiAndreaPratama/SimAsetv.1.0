# MODUL 5 — IMPLEMENTASI DATABASE
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 5.1 Pendahuluan

Database adalah komponen paling fundamental dalam SimAset karena seluruh data yang dikelola, ditampilkan, dan dilaporkan oleh sistem bersumber dari database. Kualitas perancangan database secara langsung menentukan kualitas sistem secara keseluruhan — database yang dirancang dengan baik akan menghasilkan query yang efisien, data yang konsisten, dan sistem yang mudah dikembangkan. Sebaliknya, database yang buruk akan menyebabkan performa lambat, data yang tidak konsisten, dan kesulitan dalam pengembangan fitur baru.

SimAset menggunakan **MySQL 8.0.30** sebagai database server dengan nama database **`simset_rbtv`**. Pengelolaan struktur database dilakukan menggunakan fitur **Migration** Laravel, yang memungkinkan perubahan struktur database dilakukan secara terprogram, terdokumentasi, dan dapat direproduksi di lingkungan manapun hanya dengan satu perintah. Data awal diisi menggunakan **Seeder** yang juga dapat dijalankan ulang kapan saja.

---

## 5.2 Struktur Database Aktual

Database `simset_rbtv` terdiri dari tabel-tabel berikut:

| Nama Tabel | Jenis | Fungsi |
|------------|-------|--------|
| users | Aplikasi | Data pengguna sistem (Admin dan Staff) |
| barang | Aplikasi | Master data jenis/tipe barang |
| ruangan | Aplikasi | Master data lokasi/ruangan |
| aset | Aplikasi | Data aset fisik (tabel utama) |
| log_aktivitas | Aplikasi | Audit trail aktivitas pengguna |
| sessions | Laravel | Data session login pengguna |
| cache | Laravel | Cache data aplikasi |
| cache_locks | Laravel | Lock untuk cache |
| migrations | Laravel | Riwayat migration yang sudah dijalankan |
| password_reset_tokens | Laravel | Token reset password |

> **[GAMBAR 5.1: Tampilan phpMyAdmin menampilkan daftar semua tabel di database simset_rbtv beserta jumlah record masing-masing]**

---

## 5.3 Implementasi Tabel Utama

### 5.3.1 Tabel `users`

Tabel `users` menyimpan data seluruh pengguna yang dapat mengakses sistem SimAset. Setiap pengguna memiliki role yang menentukan hak aksesnya — `admin` untuk pengelola sistem dan `staff` untuk pengguna operasional.

**DDL (Data Definition Language) aktual:**

```sql
CREATE TABLE `users` (
  `id`            int NOT NULL AUTO_INCREMENT,
  `name`          varchar(100) NOT NULL,
  `email`         varchar(100) NOT NULL,
  `password`      varchar(255) NOT NULL,
  `role`          enum('admin','staff') DEFAULT 'staff',
  `is_active`     tinyint(1) NOT NULL DEFAULT '1',
  `last_login_at` timestamp NULL DEFAULT NULL,
  `created_at`    timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`    timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

**Penjelasan setiap kolom:**

- `id` — Primary key dengan auto-increment. Setiap pengguna mendapat ID unik yang tidak berubah.
- `name` — Nama lengkap pengguna, maksimal 100 karakter, wajib diisi.
- `email` — Alamat email yang digunakan untuk login. Harus unik di seluruh tabel (UNIQUE KEY). Maksimal 100 karakter.
- `password` — Password yang sudah di-hash menggunakan algoritma bcrypt. Panjang hash bcrypt selalu 60 karakter, namun kolom dibuat 255 untuk mengakomodasi algoritma hash lain di masa depan.
- `role` — Peran pengguna menggunakan ENUM untuk membatasi nilai yang valid. Default 'staff' sehingga pengguna baru otomatis menjadi staff kecuali ditentukan lain.
- `is_active` — Flag aktif/nonaktif akun. 1 = aktif (dapat login), 0 = nonaktif (tidak dapat login meskipun password benar). Ini memungkinkan Admin menonaktifkan akun tanpa menghapusnya.
- `last_login_at` — Timestamp waktu login terakhir. Diperbarui setiap kali pengguna berhasil login. Berguna untuk memantau aktivitas pengguna.
- `created_at` — Waktu akun dibuat, diisi otomatis dengan CURRENT_TIMESTAMP.
- `updated_at` — Waktu akun terakhir diubah.

**Data aktual dari database:**

```sql
INSERT INTO `users` VALUES
(2, 'Staff RBTV', 'staff@rbtv.id', 'hashed_password', 'staff', 1, NULL,
 '2026-04-29 13:37:42', NULL),
(3, 'Admin Magang', 'magangrbtv@gmail.com',
 '$2y$12$FpZbPJ0q6w6scnV9B9muyeauUKa6DXG7khyLw/ZpRDWsNXSlfPBG.', 'admin', 1,
 '2026-05-02 13:03:44', '2026-04-29 06:50:07', '2026-05-02 13:03:44'),
(4, 'reffki', 'reffkip@gmail.com',
 '$2y$12$3oqH5om5HD3C0peGUJcp1eHKrVdTqU85N0wKrKZGwr8NH5L1TZ.Ne', 'staff', 1,
 '2026-05-02 11:04:07', '2026-05-02 06:20:29', '2026-05-02 11:04:07');
```

> **[GAMBAR 5.2: Tampilan data tabel users di phpMyAdmin menampilkan 3 pengguna aktual]**

### 5.3.2 Tabel `barang`

Tabel `barang` adalah master data yang mendefinisikan jenis-jenis barang yang dapat dijadikan aset. Setiap aset yang terdaftar di sistem harus merujuk ke salah satu barang di tabel ini. Tabel ini mendukung soft delete melalui kolom `deleted_at`.

**DDL aktual:**

```sql
CREATE TABLE `barang` (
  `kode_barang` varchar(20) NOT NULL,
  `nama_barang` varchar(150) NOT NULL,
  `kategori`    enum('Kamera','Audio','Komputer','Lighting',
                     'Furniture','Peralatan Kantor') NOT NULL,
  `status`      enum('aktif','nonaktif') DEFAULT 'aktif',
  `keterangan`  text,
  `created_at`  timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`  timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at`  timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

**Penjelasan kolom penting:**

- `kode_barang` — Primary key bertipe string dengan format BRG-XXX (BRG-001, BRG-002, dst.). Tidak menggunakan auto-increment karena kode di-generate secara programatik dengan algoritma gap-filling.
- `kategori` — Menggunakan ENUM untuk memastikan konsistensi kategorisasi. Nilai yang valid: Kamera, Audio, Komputer, Lighting, Furniture, Peralatan Kantor.
- `deleted_at` — Kolom soft delete. NULL berarti barang aktif, terisi timestamp berarti sudah dihapus (soft deleted) dan tidak akan muncul di query normal.

**Data aktual dari database:**

```sql
INSERT INTO `barang` VALUES
('BRG-001', 'Kamera Sony A7', 'Kamera', 'aktif', NULL,
 '2026-04-29 13:37:42', '2026-05-02 08:19:09', NULL),
('BRG-002', 'Mic Wireless Rode', 'Audio', 'aktif', NULL,
 '2026-04-29 13:37:42', NULL, NULL),
('BRG-003', 'printer epson l200', 'Peralatan Kantor', 'aktif', NULL,
 '2026-05-02 08:18:44', '2026-05-02 08:19:59', '2026-05-02 08:19:59');
```

**Catatan penting:** BRG-003 (printer epson l200) memiliki `deleted_at = '2026-05-02 08:19:59'`, artinya sudah di-soft delete. Barang ini tidak akan muncul di query normal (`Barang::all()`) tetapi masih ada di database dan dapat dilihat dengan `Barang::withTrashed()->get()`.

> **[GAMBAR 5.3: Tampilan data tabel barang di phpMyAdmin, termasuk BRG-003 yang sudah soft-deleted dengan deleted_at terisi]**

### 5.3.3 Tabel `ruangan`

Tabel `ruangan` menyimpan data lokasi/ruangan tempat aset ditempatkan. Berbeda dengan tabel barang dan aset, tabel ruangan tidak menggunakan soft delete karena ada validasi di controller yang mencegah penghapusan ruangan yang masih memiliki aset.

**DDL aktual:**

```sql
CREATE TABLE `ruangan` (
  `id`         int NOT NULL AUTO_INCREMENT,
  `nama`       varchar(100) NOT NULL,
  `lantai`     varchar(50) DEFAULT NULL,
  `keterangan` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

**Data aktual dari database:**

```sql
INSERT INTO `ruangan` VALUES
(1, 'Studio 1', 'Lantai 1', NULL, '2026-04-29 13:37:42'),
(2, 'Studio 2', 'Lantai 2', NULL, '2026-04-29 13:37:42'),
(3, 'Ruang Editing', 'Lantai 1', NULL, '2026-04-29 13:37:42'),
(4, 'Ruang Redaksi', '5', NULL, '2026-05-02 15:18:23');
```

**Catatan:** Ruang Editing (id=3) adalah ruangan yang paling aktif digunakan — AST-001 (Kamera Sony A7, Maintenance) dan AST-002 (Kamera Sony A7, Aktif) keduanya berada di ruangan ini.

> **[GAMBAR 5.4: Tampilan data tabel ruangan di phpMyAdmin dengan 4 ruangan aktual]**

### 5.3.4 Tabel `aset`

Tabel `aset` adalah tabel utama dan terpenting dalam sistem SimAset. Setiap baris mewakili satu unit aset fisik yang merupakan instance dari barang tertentu yang ditempatkan di ruangan tertentu.

**DDL aktual:**

```sql
CREATE TABLE `aset` (
  `kode_aset`         varchar(20) NOT NULL,
  `kode_barang`       varchar(20) NOT NULL,
  `ruangan_id`        int DEFAULT NULL,
  `kondisi`           enum('Baik','Rusak Ringan','Rusak Berat') DEFAULT 'Baik',
  `status`            enum('Aktif','Maintenance','Non-Aktif') DEFAULT 'Aktif',
  `serial_number`     varchar(100) DEFAULT NULL,
  `foto`              varchar(255) DEFAULT NULL,
  `jumlah`            int DEFAULT '1',
  `tanggal_perolehan` date DEFAULT NULL,
  `harga_perolehan`   decimal(15,2) DEFAULT NULL,
  `sumber_perolehan`  varchar(255) DEFAULT NULL,
  `keterangan`        text,
  `created_by`        int DEFAULT NULL,
  `updated_by`        int DEFAULT NULL,
  `created_at`        timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`        timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at`        timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`kode_aset`),
  KEY `idx_kode_barang` (`kode_barang`),
  KEY `idx_ruangan_id` (`ruangan_id`),
  KEY `idx_status` (`status`),
  CONSTRAINT `fk_aset_barang`
    FOREIGN KEY (`kode_barang`) REFERENCES `barang` (`kode_barang`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_aset_ruangan`
    FOREIGN KEY (`ruangan_id`) REFERENCES `ruangan` (`id`)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

**Penjelasan index yang ada:**

- `PRIMARY KEY (kode_aset)` — Index utama untuk pencarian berdasarkan kode aset
- `KEY idx_kode_barang (kode_barang)` — Index untuk mempercepat query filter berdasarkan barang
- `KEY idx_ruangan_id (ruangan_id)` — Index untuk mempercepat query filter berdasarkan ruangan
- `KEY idx_status (status)` — Index untuk mempercepat query filter berdasarkan status (sangat sering digunakan di dashboard dan maintenance)

**Data aktual dari database:**

```sql
INSERT INTO `aset` VALUES
('AST-001', 'BRG-001', 3, 'Baik', 'Maintenance', 'ggG', NULL, 1,
 '2026-05-01', NULL, NULL, NULL, 3, 3,
 '2026-05-01 05:59:30', '2026-05-02 07:42:40', NULL),
('AST-002', 'BRG-001', 3, 'Baik', 'Aktif', 'hgfx', NULL, 1,
 '2026-05-01', NULL, NULL, NULL, 3, NULL,
 '2026-05-01 08:04:45', '2026-05-01 08:04:45', NULL),
('AST-003', 'BRG-003', 4, 'Baik', 'Aktif', 'l201', '1777735186_AST-001.png', 1,
 '2026-05-02', NULL, NULL, NULL, 3, 3,
 '2026-05-02 08:19:31', '2026-05-02 08:19:54', '2026-05-02 08:19:54');
```

**Analisis data aktual:**

| Kode | Barang | Ruangan | Kondisi | Status | Serial | Foto | Deleted |
|------|--------|---------|---------|--------|--------|------|---------|
| AST-001 | Kamera Sony A7 | Ruang Editing | Baik | **Maintenance** | ggG | - | Tidak |
| AST-002 | Kamera Sony A7 | Ruang Editing | Baik | Aktif | hgfx | - | Tidak |
| AST-003 | printer epson l200 | Ruang Redaksi | Baik | Aktif | l201 | Ada | **Ya** |

> **[GAMBAR 5.5: Tampilan data tabel aset di phpMyAdmin menampilkan AST-001 (Maintenance), AST-002 (Aktif), dan AST-003 (soft-deleted)]**

### 5.3.5 Tabel `log_aktivitas`

Tabel ini menyimpan seluruh audit trail aktivitas pengguna. Berdasarkan data aktual, tabel ini sudah memiliki 39 record yang mencakup berbagai jenis aktivitas.

**DDL aktual:**

```sql
CREATE TABLE `log_aktivitas` (
  `id`         bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id`    bigint UNSIGNED DEFAULT NULL,
  `aktivitas`  varchar(255) NOT NULL,
  `keterangan` text,
  `ip_address` varchar(45) DEFAULT NULL,
  `user_agent` text,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  AUTO_INCREMENT=40;
```

**Contoh data aktual (record penting):**

| id | user_id | aktivitas | keterangan | created_at |
|----|---------|-----------|------------|------------|
| 1 | 3 | Create | Menambahkan aset baru: Kamera Sony A7 (AST-002) | 2026-05-01 08:04:46 |
| 17 | 3 | Update | Mengupdate aset: Kamera Sony A7 (AST-001) | 2026-05-02 07:42:40 |
| 18 | 3 | Create | Menambahkan aset baru: printer epson l200 (AST-003) | 2026-05-02 08:19:32 |
| 19 | 3 | Update | Mengupdate aset: printer epson l200 (AST-003) | 2026-05-02 08:19:46 |
| 20 | 3 | Delete | Menghapus aset: printer epson l200 (AST-003) | 2026-05-02 08:19:54 |
| 23 | 4 | Login | User berhasil login: reffki (reffkip@gmail.com) | 2026-05-02 09:55:38 |

> **[GAMBAR 5.6: Tampilan data tabel log_aktivitas di phpMyAdmin menampilkan 39 record aktivitas]**

---

## 5.4 Relasi Antar Tabel

SimAset memiliki dua foreign key constraint yang didefinisikan secara eksplisit di database, plus relasi implisit melalui kolom `created_by` dan `updated_by`.

### 5.4.1 FK: `fk_aset_barang` (RESTRICT delete, CASCADE update)

```sql
CONSTRAINT `fk_aset_barang`
  FOREIGN KEY (`kode_barang`) REFERENCES `barang` (`kode_barang`)
  ON DELETE RESTRICT ON UPDATE CASCADE
```

**ON DELETE RESTRICT** berarti barang tidak dapat dihapus (hard delete) jika masih ada aset yang merujuk ke barang tersebut. Ini adalah pilihan yang tepat karena mencegah "orphan records" — aset yang tidak memiliki barang induk. Namun perlu diperhatikan bahwa SimAset menggunakan soft delete untuk barang, sehingga `DELETE` yang dimaksud di sini adalah hard delete (yang tidak pernah dilakukan secara normal).

**ON UPDATE CASCADE** berarti jika `kode_barang` di tabel barang diubah, semua aset yang merujuk ke barang tersebut akan otomatis diperbarui. Ini jarang terjadi karena kode barang biasanya tidak berubah.

**Contoh nyata:** BRG-001 (Kamera Sony A7) tidak dapat di-hard-delete karena AST-001 dan AST-002 masih merujuk ke BRG-001.

### 5.4.2 FK: `fk_aset_ruangan` (SET NULL delete, CASCADE update)

```sql
CONSTRAINT `fk_aset_ruangan`
  FOREIGN KEY (`ruangan_id`) REFERENCES `ruangan` (`id`)
  ON DELETE SET NULL ON UPDATE CASCADE
```

**ON DELETE SET NULL** berarti jika sebuah ruangan dihapus, kolom `ruangan_id` pada semua aset yang berada di ruangan tersebut akan di-set menjadi NULL. Ini lebih aman daripada RESTRICT karena aset tidak ikut terhapus — hanya informasi lokasinya yang hilang. Namun di level aplikasi, ada validasi tambahan di `RuanganController::destroy()` yang mencegah penghapusan ruangan yang masih memiliki aset.

**Contoh nyata:** Jika Ruang Editing (id=3) dihapus, maka `ruangan_id` pada AST-001 dan AST-002 akan menjadi NULL. Namun karena ada validasi di controller, penghapusan ini tidak akan diizinkan selama masih ada aset di ruangan tersebut.

### 5.4.3 Relasi Implisit (Tidak Ada FK di Database)

Kolom `created_by` dan `updated_by` di tabel `aset` merujuk ke `users.id`, namun tidak ada foreign key constraint eksplisit di database. Relasi ini dikelola di level aplikasi melalui Eloquent:

```php
// Di Model Asset
public function creator() {
    return $this->belongsTo(User::class, 'created_by');
}
public function updater() {
    return $this->belongsTo(User::class, 'updated_by');
}
```

Demikian juga kolom `user_id` di `log_aktivitas` — tidak ada FK eksplisit di database, tetapi ada relasi Eloquent di model.

> **[GAMBAR 5.7: Diagram relasi tabel di phpMyAdmin (Designer view) menampilkan FK antara aset-barang dan aset-ruangan]**

---

## 5.5 Implementasi Model Eloquent

### 5.5.1 Model Asset

```php
<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Asset extends Model
{
    use SoftDeletes;

    protected $table      = 'aset';
    protected $primaryKey = 'kode_aset';
    public    $incrementing = false;   // PK bukan auto-increment
    protected $keyType    = 'string';  // PK bertipe string

    protected $fillable = [
        'kode_aset', 'kode_barang', 'ruangan_id', 'kondisi', 'status',
        'serial_number', 'foto', 'jumlah', 'tanggal_perolehan',
        'harga_perolehan', 'sumber_perolehan', 'keterangan',
        'created_by', 'updated_by',
    ];

    protected $casts = [
        'tanggal_perolehan' => 'date',
        'harga_perolehan'   => 'decimal:2',
        'jumlah'            => 'integer',
        'created_at'        => 'datetime',
        'updated_at'        => 'datetime',
        'deleted_at'        => 'datetime',
    ];

    // Relasi ke Barang (Many-to-One)
    public function barang() {
        return $this->belongsTo(Barang::class, 'kode_barang', 'kode_barang');
    }

    // Relasi ke Ruangan (Many-to-One)
    public function ruangan() {
        return $this->belongsTo(Ruangan::class, 'ruangan_id');
    }

    // Relasi ke User pembuat
    public function creator() {
        return $this->belongsTo(User::class, 'created_by');
    }

    // Relasi ke User pengupdate
    public function updater() {
        return $this->belongsTo(User::class, 'updated_by');
    }

    // Accessor: ambil nama barang dari relasi
    public function getNamaBarangAttribute(): string {
        return $this->barang?->nama_barang ?? '—';
    }

    // Auto-generate kode aset dengan algoritma gap-filling
    public static function generateKode(): string
    {
        $existing = self::withTrashed()
            ->pluck('kode_aset')
            ->map(fn($k) => (int) str_replace('AST-', '', $k))
            ->filter(fn($n) => $n > 0)
            ->sort()
            ->values();

        $next = 1;
        foreach ($existing as $num) {
            if ($num > $next) break;
            if ($num === $next) $next++;
        }

        return 'AST-' . str_pad($next, 3, '0', STR_PAD_LEFT);
    }
}
```

### 5.5.2 Model Barang

```php
class Barang extends Model
{
    use SoftDeletes;

    protected $table      = 'barang';
    protected $primaryKey = 'kode_barang';
    public    $incrementing = false;
    protected $keyType    = 'string';

    protected $fillable = [
        'kode_barang', 'nama_barang', 'kategori', 'status', 'keterangan',
    ];

    // Relasi ke Aset (One-to-Many)
    public function aset() {
        return $this->hasMany(Asset::class, 'kode_barang', 'kode_barang');
    }

    // Auto-generate kode barang dengan gap-filling
    public static function generateKode(): string
    {
        $existing = self::withTrashed()
            ->pluck('kode_barang')
            ->map(fn($k) => (int) str_replace('BRG-', '', $k))
            ->filter(fn($n) => $n > 0)
            ->sort()->values();

        $next = 1;
        foreach ($existing as $num) {
            if ($num > $next) break;
            if ($num === $next) $next++;
        }

        return 'BRG-' . str_pad($next, 3, '0', STR_PAD_LEFT);
    }
}
```

### 5.5.3 Model Ruangan

```php
class Ruangan extends Model
{
    protected $table    = 'ruangan';
    protected $fillable = ['nama', 'lantai', 'keterangan'];

    // Relasi ke Aset (One-to-Many)
    public function assets() {
        return $this->hasMany(Asset::class, 'ruangan_id');
    }
}
```

### 5.5.4 Model ActivityLog

```php
class ActivityLog extends Model
{
    protected $table    = 'log_aktivitas';
    protected $fillable = [
        'user_id', 'aktivitas', 'keterangan', 'ip_address', 'user_agent',
    ];

    public function user() {
        return $this->belongsTo(User::class, 'user_id');
    }
}
```

---

## 5.6 Algoritma Auto-Generate Kode (Gap-Filling)

Salah satu fitur paling menarik dari SimAset adalah algoritma auto-generate kode dengan **gap-filling**. Algoritma ini memastikan kode yang digunakan selalu merupakan nomor terkecil yang tersedia, mengisi "celah" yang ditinggalkan oleh record yang sudah dihapus.

### 5.6.1 Mengapa Gap-Filling?

Tanpa gap-filling, jika AST-003 dihapus dan kemudian ditambah aset baru, kode yang digunakan adalah AST-004 (nomor berikutnya). Ini menyebabkan "lubang" di urutan kode (AST-001, AST-002, AST-004) yang terlihat tidak rapi dan membingungkan.

Dengan gap-filling, kode AST-003 yang sudah dihapus akan digunakan kembali untuk aset baru, sehingga urutan tetap rapi (AST-001, AST-002, AST-003).

### 5.6.2 Contoh dengan Data Aktual

Berdasarkan data aktual di database:
- AST-001 → ada (Maintenance)
- AST-002 → ada (Aktif)
- AST-003 → ada tapi soft-deleted (deleted_at = '2026-05-02 08:19:54')

Jika sekarang ditambah aset baru, `generateKode()` akan:

```
1. withTrashed()->pluck('kode_aset')
   → ['AST-001', 'AST-002', 'AST-003']

2. map: str_replace('AST-', '', kode) → cast ke int
   → [1, 2, 3]

3. sort() → [1, 2, 3]

4. Loop gap-filling:
   - num=1, next=1 → cocok, next++ → next=2
   - num=2, next=2 → cocok, next++ → next=3
   - num=3, next=3 → cocok, next++ → next=4

5. Hasil: 'AST-' + str_pad(4, 3, '0') = 'AST-004'
```

Dalam kasus ini, karena AST-003 sudah digunakan (meskipun soft-deleted), kode baru adalah AST-004. Ini adalah perilaku yang benar — kode dari record yang sudah dihapus tidak digunakan ulang untuk mencegah konflik data historis.

### 5.6.3 Implementasi Lengkap

```php
public static function generateKode(): string
{
    // withTrashed() memastikan kode dari record soft-deleted
    // tidak digunakan ulang
    $existing = self::withTrashed()
        ->pluck('kode_aset')
        ->map(fn($k) => (int) str_replace('AST-', '', $k))
        ->filter(fn($n) => $n > 0)  // filter nilai non-numerik
        ->sort()
        ->values();  // re-index array

    $next = 1;
    foreach ($existing as $num) {
        if ($num > $next) break;   // celah ditemukan
        if ($num === $next) $next++;
    }

    // str_pad memastikan format 3 digit: 001, 002, ..., 099, 100, 101
    return 'AST-' . str_pad($next, 3, '0', STR_PAD_LEFT);
}
```

---

## 5.7 Soft Delete

Soft delete adalah mekanisme di mana record yang "dihapus" tidak benar-benar dihapus dari database, melainkan hanya ditandai dengan timestamp di kolom `deleted_at`. Record dengan `deleted_at` yang terisi tidak akan muncul dalam query normal, tetapi masih ada di database dan dapat dipulihkan.

### 5.7.1 Tabel yang Menggunakan Soft Delete

| Tabel | Soft Delete | Alasan |
|-------|-------------|--------|
| aset | ✅ Ya | Mencegah kehilangan data aset yang dihapus tidak sengaja |
| barang | ✅ Ya | Menjaga integritas referensial dengan aset |
| users | ❌ Tidak | Pengguna dihapus permanen (ada validasi tidak bisa hapus diri sendiri) |
| ruangan | ❌ Tidak | Ada validasi tidak bisa hapus ruangan berisi aset |

### 5.7.2 Contoh dari Data Aktual

**BRG-003 (printer epson l200)** — soft deleted pada 2026-05-02 08:19:59:
- Tidak muncul di `Barang::all()` atau `Barang::where(...)->get()`
- Muncul di `Barang::withTrashed()->get()`
- Kode BRG-003 tidak akan digunakan ulang oleh `generateKode()`

**AST-003** — soft deleted pada 2026-05-02 08:19:54:
- Tidak muncul di daftar aset normal
- Foto `1777735186_AST-001.png` masih ada di `public/foto_aset/`
- Log aktivitas Delete (id=20) tetap ada di `log_aktivitas`

---

## 5.8 Seeder Data Awal

### 5.8.1 AdminSeeder

```php
class AdminSeeder extends Seeder
{
    public function run(): void
    {
        // updateOrCreate aman dijalankan berulang kali
        User::updateOrCreate(
            ['email' => 'admin@rbtv.co.id'],
            ['name' => 'Admin RBTV', 'password' => Hash::make('Admin123'),
             'role' => 'admin', 'is_active' => true]
        );
        User::updateOrCreate(
            ['email' => 'magangrbtv@gmail.com'],
            ['name' => 'Magang RBTV', 'password' => Hash::make('Magang123'),
             'role' => 'admin', 'is_active' => true]
        );
    }
}
```

### 5.8.2 StaffSeeder

```php
class StaffSeeder extends Seeder
{
    public function run(): void
    {
        User::updateOrCreate(
            ['email' => 'staff@rbtv.co.id'],
            ['name' => 'Staff RBTV', 'password' => Hash::make('Staff123'),
             'role' => 'staff', 'is_active' => true]
        );
    }
}
```

---

## 5.9 Pengujian Database

### 5.9.1 Verifikasi via Tinker

```bash
php artisan tinker
```

```php
// Cek jumlah record
App\Models\User::count();    // 3
App\Models\Barang::count();  // 2 (BRG-003 soft-deleted tidak dihitung)
App\Models\Ruangan::count(); // 4
App\Models\Asset::count();   // 2 (AST-003 soft-deleted tidak dihitung)

// Cek soft-deleted
App\Models\Barang::withTrashed()->count();  // 3
App\Models\Asset::withTrashed()->count();   // 3

// Cek relasi
$aset = App\Models\Asset::with(['barang','ruangan','creator'])->first();
$aset->kode_aset;           // 'AST-001'
$aset->barang->nama_barang; // 'Kamera Sony A7'
$aset->ruangan->nama;       // 'Ruang Editing'
$aset->creator->name;       // 'Admin Magang'
$aset->status;              // 'Maintenance'

// Cek generate kode
App\Models\Asset::generateKode(); // 'AST-004' (karena AST-001,002,003 sudah ada)
App\Models\Barang::generateKode(); // 'BRG-004' (karena BRG-001,002,003 sudah ada)
```

### 5.9.2 Verifikasi FK Constraint

```sql
-- Coba hapus BRG-001 yang masih dirujuk AST-001 dan AST-002
DELETE FROM barang WHERE kode_barang = 'BRG-001';
-- Error: Cannot delete or update a parent row: a foreign key constraint fails
-- (fk_aset_barang: RESTRICT delete) ✓ Benar!

-- Coba hapus Ruang Editing (id=3) yang masih dirujuk AST-001 dan AST-002
DELETE FROM ruangan WHERE id = 3;
-- Ini akan berhasil di level database (SET NULL),
-- tapi dicegah di level aplikasi oleh RuanganController::destroy()
```

---

## 5.10 Kesimpulan Modul

Modul 5 ini telah membahas implementasi database SimAset secara sangat mendalam menggunakan data aktual dari database `simset_rbtv`. Setiap tabel dijelaskan dengan DDL yang tepat sesuai SQL dump, penjelasan setiap kolom, constraint yang ada, dan contoh data nyata.

Relasi antar tabel melalui dua FK constraint (`fk_aset_barang` dengan RESTRICT delete dan `fk_aset_ruangan` dengan SET NULL delete) memastikan integritas referensial data. Algoritma gap-filling untuk auto-generate kode memastikan urutan kode yang rapi. Soft delete pada tabel aset dan barang mencegah kehilangan data yang tidak disengaja.

Database yang dirancang dan diimplementasikan dengan baik ini menjadi fondasi yang kuat untuk seluruh fitur sistem yang dibahas pada modul-modul berikutnya.

---

*Kembali ke: [Modul 4 — Persiapan Lingkungan](MODUL_04_PERSIAPAN_LINGKUNGAN.md)*
*Lanjut ke: [Modul 6 — Autentikasi dan Hak Akses](MODUL_06_AUTENTIKASI_HAK_AKSES.md)*
