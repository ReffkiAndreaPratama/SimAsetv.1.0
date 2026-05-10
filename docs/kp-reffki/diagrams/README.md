# Diagram Sistem — SimAset RBTV Bengkulu

Semua diagram UML dan ERD untuk Sistem Informasi Manajemen Aset (SimAset) RBTV Bengkulu.  
Format: **PlantUML** (`.puml`) — dibuat berdasarkan **kode aktual** dan **SQL dump aktual** database `simset_rbtv`.

---

## Daftar Diagram

| No | File | Jenis | Deskripsi |
|----|------|-------|-----------|
| 01 | `01_ERD.puml` | **ERD** | Semua tabel aktual dari SQL dump: `users`, `barang`, `ruangan`, `aset`, `log_aktivitas`, `sessions`, `password_reset_tokens`, `cache`, `cache_locks`, `migrations` — dengan tipe data persis, constraint FK aktual, index, dan data contoh |
| 02 | `02_UseCase.puml` | **Use Case** | Dua aktor (Admin & Staff), semua use case dari routes/web.php, relasi `<<include>>` dan `<<extend>>` |
| 03 | `03_Activity_Login.puml` | **Activity** | Login & Logout — termasuk cek `is_active`, rate limiting (5x/menit), session regeneration, update `last_login_at`, log aktivitas |
| 04 | `04_Activity_Aset.puml` | **Activity** | Manajemen Aset CRUD lengkap dengan swimlane |
| 05 | `05_Activity_Maintenance.puml` | **Activity** | Set Maintenance + Selesaikan Maintenance + kirim email ke semua Admin aktif |
| 06 | `06_Activity_QRCode.puml` | **Activity** | Generate QR (via qrserver.com API), Scan QR, Batch Print |
| 07 | `07_Activity_LaporanExport.puml` | **Activity** | Laporan PDF/Excel/CSV, per ruangan, maintenance |
| 08 | `08_Sequence_Login.puml` | **Sequence** | Login detail: Router → AuthCtrl → LoginRequest → RateLimiter → User Model → cek is_active → Auth::attempt → Session → ActivityLogger → DB |
| 09 | `09_Sequence_TambahAset.puml` | **Sequence** | Tambah Aset: form → validasi → generateKode gap-filling → simpan foto → Asset::create → ActivityLogger |
| 10 | `10_Sequence_Maintenance.puml` | **Sequence** | Set Maintenance + Selesai + loop kirim email ke semua Admin aktif |
| 11 | `11_Sequence_ScanQR.puml` | **Sequence** | Generate QR via API eksternal + Scan + tampilkan detail (route publik) |
| 12 | `12_Sequence_ManajemenUser.puml` | **Sequence** | CRUD Pengguna (Admin Only) + kirim email akun baru |
| 13 | `13_ClassDiagram.puml` | **Class** | Semua Model, Controller (termasuk Auth/Breeze), Middleware, Helper, Mail, Export, Import, Notification |
| 14 | `14_Activity_ImportExport.puml` | **Activity** | Import data dari Excel/CSV (Aset & Barang) |
| 15 | `15_Activity_ManajemenUser.puml` | **Activity** | Manajemen Pengguna Admin (CRUD + Audit Log) |

---

## Struktur Database Aktual (dari SQL Dump)

Database: **`simset_rbtv`** | MySQL 8.0.30 | phpMyAdmin 5.2.3

### Tabel Utama Aplikasi

```
users
  id INT PK AUTO_INCREMENT
  name VARCHAR(100) NOT NULL
  email VARCHAR(100) UNIQUE NOT NULL
  password VARCHAR(255) NOT NULL  ← bcrypt hash
  role ENUM('admin','staff') DEFAULT 'staff'
  is_active TINYINT(1) NOT NULL DEFAULT 1
  last_login_at TIMESTAMP NULL
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  updated_at TIMESTAMP NULL

barang
  kode_barang VARCHAR(20) PK  ← Format: BRG-001
  nama_barang VARCHAR(150) NOT NULL
  kategori ENUM('Kamera','Audio','Komputer','Lighting','Furniture','Peralatan Kantor') NOT NULL
  status ENUM('aktif','nonaktif') DEFAULT 'aktif'
  keterangan TEXT NULL
  created_at TIMESTAMP
  updated_at TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP
  deleted_at TIMESTAMP NULL  ← Soft Delete

ruangan
  id INT PK AUTO_INCREMENT
  nama VARCHAR(100) NOT NULL
  lantai VARCHAR(50) NULL
  keterangan TEXT NULL
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  ← TIDAK ADA updated_at di tabel aktual

aset
  kode_aset VARCHAR(20) PK  ← Format: AST-001
  kode_barang VARCHAR(20) NOT NULL  ← FK → barang (RESTRICT del, CASCADE upd)
  ruangan_id INT NULL  ← FK → ruangan (SET NULL del, CASCADE upd)
  kondisi ENUM('Baik','Rusak Ringan','Rusak Berat') DEFAULT 'Baik'
  status ENUM('Aktif','Maintenance','Non-Aktif') DEFAULT 'Aktif'
  serial_number VARCHAR(100) NULL
  foto VARCHAR(255) NULL
  jumlah INT DEFAULT 1
  tanggal_perolehan DATE NULL
  harga_perolehan DECIMAL(15,2) NULL
  sumber_perolehan VARCHAR(255) NULL
  keterangan TEXT NULL
  created_by INT NULL  ← ref users.id (NO FK constraint di DB)
  updated_by INT NULL  ← ref users.id (NO FK constraint di DB)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  updated_at TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP
  deleted_at TIMESTAMP NULL  ← Soft Delete
  INDEX: idx_kode_barang, idx_ruangan_id, idx_status

log_aktivitas
  id BIGINT UNSIGNED PK AUTO_INCREMENT
  user_id BIGINT UNSIGNED NULL  ← ref users.id (NO FK constraint di DB)
  aktivitas VARCHAR(255) NOT NULL  ← Login/Logout/Create/Update/Delete
  keterangan TEXT NULL
  ip_address VARCHAR(45) NULL
  user_agent TEXT NULL
  created_at TIMESTAMP NULL
  updated_at TIMESTAMP NULL
```

### Tabel Framework Laravel

```
sessions          ← Laravel session driver
password_reset_tokens  ← Fitur lupa password
cache             ← Laravel cache driver
cache_locks       ← Laravel cache locks
migrations        ← Riwayat migrasi
```

### FK Constraints Aktual (hanya 2)

```sql
-- Dari ALTER TABLE aset:
CONSTRAINT fk_aset_barang
  FOREIGN KEY (kode_barang) REFERENCES barang(kode_barang)
  ON DELETE RESTRICT ON UPDATE CASCADE

CONSTRAINT fk_aset_ruangan
  FOREIGN KEY (ruangan_id) REFERENCES ruangan(id)
  ON DELETE SET NULL ON UPDATE CASCADE
```

> **Catatan:** `created_by`, `updated_by` di tabel `aset` dan `user_id` di `log_aktivitas` **tidak memiliki FK constraint** di database aktual — hanya referensi logis di level aplikasi.

---

## Data Aktual

| Tabel | Jumlah Record |
|-------|--------------|
| users | 3 (id: 2,3,4) |
| barang | 3 (1 soft-deleted: BRG-003) |
| ruangan | 4 (Studio 1, Studio 2, Ruang Editing, Ruang Redaksi) |
| aset | 3 (1 soft-deleted: AST-003) |
| log_aktivitas | 39 (35 Login, 2 Create, 2 Update, 1 Delete) |

---

## Aktor & Hak Akses

| Fitur | Staff | Admin |
|-------|:-----:|:-----:|
| Dashboard (statistik, grafik) | ✅ | ✅ |
| Manajemen Aset (CRUD + batch) | ✅ | ✅ |
| Manajemen Barang (CRUD) | ✅ | ✅ |
| Manajemen Ruangan (CRUD) | ✅ | ✅ |
| QR Code (generate, scan, batch print) | ✅ | ✅ |
| Maintenance (set & selesai) | ✅ | ✅ |
| Import Excel/CSV | ✅ | ✅ |
| Export Excel/PDF | ✅ | ✅ |
| Laporan (PDF, per ruangan, maintenance) | ✅ | ✅ |
| Edit Profil & Ganti Password | ✅ | ✅ |
| **Kelola Pengguna (CRUD)** | ❌ | ✅ |
| **Audit Log (log_aktivitas)** | ❌ | ✅ |
| Terima email notifikasi maintenance | ❌ | ✅ |

---

## Cara Render Diagram

### Opsi 1: PlantUML Online (Paling Mudah)
1. Buka [https://www.plantuml.com/plantuml/uml/](https://www.plantuml.com/plantuml/uml/)
2. Copy-paste isi file `.puml`
3. Klik "Submit"

### Opsi 2: VS Code Extension
1. Install extension **PlantUML** (jcmeyer.plantuml)
2. Buka file `.puml`
3. Tekan `Alt+D` untuk preview

### Opsi 3: Command Line
```bash
java -jar plantuml.jar docs/diagrams/01_ERD.puml
# Render semua sekaligus:
java -jar plantuml.jar docs/diagrams/*.puml
```
