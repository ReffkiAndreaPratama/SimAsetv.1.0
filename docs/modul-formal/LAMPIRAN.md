# LAMPIRAN

## Lampiran 1. Tampilan Halaman Login Sistem

Lampiran ini menampilkan halaman login SimAset yang menggunakan layout dua panel — panel kiri berwarna biru tua berisi informasi sistem dan fitur unggulan, panel kanan berisi form login dengan field email dan password. Halaman ini merupakan tampilan awal yang diakses oleh Admin dan Staff sebelum masuk ke sistem.

> **[GAMBAR LAMPIRAN 1: Tampilan halaman login SimAset dengan panel kiri biru dan panel kanan form login]**

## Lampiran 2. Tampilan Dashboard

Lampiran ini menampilkan halaman dashboard SimAset yang diakses setelah berhasil login. Dashboard menampilkan 6 metric cards (Total Aset, Aktif, Maintenance, Rusak, Non-Aktif, Ruangan), grafik distribusi kondisi aset (donut chart), grafik top 5 kategori (bar chart), tabel 10 aset terbaru, aktivitas terbaru, dan tombol akses cepat.

> **[GAMBAR LAMPIRAN 2: Tampilan dashboard SimAset dengan metric cards, chart distribusi kondisi, dan tabel aset terbaru]**

## Lampiran 3. Tampilan Halaman Daftar Aset

Lampiran ini menampilkan halaman daftar aset SimAset yang berisi tabel data aset lengkap dengan filter bar (search, status, kondisi, kategori), bulk action bar, dan pagination. Setiap baris menampilkan foto thumbnail, kode aset, nama barang, kategori, ruangan, kondisi, status dengan badge berwarna, dan tombol aksi (detail, edit, QR, hapus).

> **[GAMBAR LAMPIRAN 3: Tampilan halaman daftar aset dengan filter bar, tabel data, dan badge status berwarna]**

## Lampiran 4. Tampilan Detail Aset dan QR Code

Lampiran ini menampilkan halaman detail aset AST-001 (Kamera Sony A7 di Ruang Editing) yang menampilkan seluruh informasi aset secara lengkap di kolom kiri, serta foto aset, QR Code, informasi sistem, dan aksi cepat di kolom kanan. Badge Maintenance berwarna kuning terlihat jelas pada kolom status.

> **[GAMBAR LAMPIRAN 4: Tampilan halaman detail aset AST-001 dengan badge Maintenance dan QR Code]**

## Lampiran 5. Tampilan Dashboard Maintenance

Lampiran ini menampilkan dashboard maintenance SimAset yang menampilkan daftar aset berstatus Maintenance beserta statistik (Total Maintenance, Rusak Berat, Rusak Ringan, Total Bermasalah). Terdapat tombol "Selesai" pada setiap baris untuk menandai maintenance selesai.

> **[GAMBAR LAMPIRAN 5: Tampilan dashboard maintenance dengan AST-001 dan tombol Selesai]**

## Lampiran 6. Tampilan Halaman Import dan Export

Lampiran ini menampilkan halaman import data SimAset dengan drag-drop zone untuk upload file, pilihan jenis data (Aset/Barang), dan tabel panduan format kolom. Juga ditampilkan halaman export dengan filter data dan tombol Export Excel/PDF.

> **[GAMBAR LAMPIRAN 6: Tampilan halaman import data dengan drag-drop zone dan tabel format kolom]**

## Lampiran 7. Struktur Database Sistem

Lampiran ini menampilkan struktur database simset_rbtv di phpMyAdmin yang terdiri dari tabel: users, barang, ruangan, aset, log_aktivitas, sessions, cache, cache_locks, migrations, dan password_reset_tokens.

> **[GAMBAR LAMPIRAN 7: Tampilan phpMyAdmin menampilkan daftar tabel database simset_rbtv]**

## Lampiran 8. Diagram Sistem

Lampiran ini menampilkan diagram arsitektur sistem SimAset yang menggambarkan hubungan antara Client Layer (Browser), Server Layer (Laravel 12 + MVC), Database Layer (MySQL simset_rbtv), dan External Services (qrserver.com API, SMTP Server).

> **[GAMBAR LAMPIRAN 8: Diagram arsitektur sistem SimAset lengkap dengan semua layer dan komponen]**
