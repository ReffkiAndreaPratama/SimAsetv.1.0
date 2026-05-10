# MODUL 9 - DASHBOARD, IMPORT, EXPORT, DAN LAPORAN

## 9.1 Pendahuluan

Dashboard, import, export, dan laporan merupakan komponen penting yang mendukung efisiensi operasional SimAset. Dashboard memberikan gambaran kondisi aset secara real-time kepada pengelola. Import memungkinkan penambahan data massal tanpa harus input satu per satu. Export memungkinkan pengambilan data dalam format yang dapat diolah lebih lanjut. Laporan menghasilkan dokumen siap cetak untuk keperluan administrasi dan audit.

Modul ini membahas secara mendalam perancangan dan implementasi dashboard, fitur import/export, serta berbagai jenis laporan yang tersedia dalam sistem.

## 9.2 Dashboard Admin dan Staff

Dashboard merupakan halaman utama yang diakses oleh pengguna setelah berhasil melakukan login. Dashboard ini dirancang sebagai pusat informasi yang menampilkan ringkasan data penting secara cepat dan mudah dipahami.

### 9.2.1 Tujuan Dashboard

Dashboard memiliki beberapa tujuan utama, antara lain:

1. Menyediakan ringkasan statistik aset secara real-time.
2. Memudahkan pengelola dalam memantau kondisi seluruh aset.
3. Memberikan akses cepat ke fitur pengelolaan data.
4. Menyajikan informasi sistem secara visual dan ringkas melalui grafik.

Dengan adanya dashboard, pengelola tidak perlu membuka setiap menu satu per satu untuk mengetahui kondisi sistem.

### 9.2.2 Komponen Utama Dashboard

Dashboard terdiri dari beberapa komponen utama, yaitu:

1. **Alert Maintenance** — banner peringatan yang muncul jika ada aset berstatus Maintenance, dengan tautan langsung ke dashboard maintenance.

2. **Metric Cards (6 kartu)** — menampilkan statistik utama:
   - Total Aset
   - Aset Aktif
   - Aset Maintenance
   - Kondisi Rusak
   - Non-Aktif
   - Total Ruangan

3. **Chart Distribusi Kondisi** — grafik donut yang menampilkan proporsi kondisi aset (Baik, Rusak Ringan, Rusak Berat) menggunakan Chart.js.

4. **Chart Top 5 Kategori** — grafik bar yang menampilkan 5 kategori aset dengan jumlah terbanyak.

5. **Tabel Recent Assets** — tabel 10 aset terbaru dengan filter kondisi dan tombol "Lihat Semua".

6. **Aktivitas Terbaru** — daftar 6 aktivitas pengguna terbaru dari log_aktivitas.

7. **Akses Cepat** — grid tombol untuk akses cepat ke fitur yang sering digunakan.

Setiap komponen dashboard dirancang agar mudah dibaca dan diakses oleh pengelola.

> **[GAMBAR 9.1: Tampilan dashboard SimAset dengan metric cards, chart distribusi kondisi, dan tabel aset terbaru]**

### 9.2.3 Alur Penggunaan Dashboard

Setelah login, pengguna diarahkan ke dashboard. Dari halaman ini, pengguna dapat:

1. Melihat ringkasan statistik aset secara real-time.
2. Mengakses menu pengelolaan data melalui sidebar atau tombol akses cepat.
3. Memantau aktivitas terbaru yang terjadi di sistem.
4. Melakukan navigasi ke modul lain dalam sistem.

Alur ini dirancang agar pengelola dapat bekerja secara efisien tanpa proses yang rumit.

## 9.3 Import Data Massal

### 9.3.1 Import Data Aset

Fitur import aset memungkinkan penambahan data aset secara massal dari file Excel (.xlsx, .xls) atau CSV. Halaman import menyediakan panduan format kolom yang harus diikuti beserta tombol download template.

**Format file import aset (9 kolom):**

| Kolom | Keterangan | Status |
|-------|------------|--------|
| A: Kode Barang | Harus ada di master barang | Wajib |
| B: Nama Ruangan | Nama ruangan penempatan | Opsional |
| C: Kondisi | Baik / Rusak Ringan / Rusak Berat | Opsional |
| D: Status | Aktif / Maintenance / Non-Aktif | Opsional |
| E: Jumlah | Angka bulat positif | Opsional |
| F: Tanggal Perolehan | Format YYYY-MM-DD | Opsional |
| G: Harga Perolehan | Angka tanpa titik/koma ribuan | Opsional |
| H: Sumber Perolehan | Pembelian/Hibah/Sumbangan/Pinjaman/Lainnya | Opsional |
| I: Keterangan | Teks bebas | Opsional |

Sistem memproses file baris per baris, memvalidasi setiap baris, dan melaporkan error per baris tanpa menghentikan proses import secara keseluruhan. Baris yang valid tetap diimport meskipun ada baris lain yang error.

> **[GAMBAR 9.2: Tampilan halaman import data dengan drag-drop zone, pilihan jenis data, dan tabel format kolom]**

### 9.3.2 Import Master Barang

Fitur import barang memungkinkan penambahan master data barang secara massal. Format file import barang lebih sederhana dengan 4 kolom: Kode Barang (wajib, harus unik), Nama Barang (wajib), Kategori (opsional), dan Status (opsional).

## 9.4 Export Data

### 9.4.1 Export ke Excel

Sistem mendukung export data aset dan barang ke format Excel (.xlsx) dengan styling profesional. File Excel yang dihasilkan memiliki:

- Header berwarna biru tua (#1A3470) dengan teks putih dan bold
- Zebra striping pada baris data (baris genap abu-abu muda, ganjil putih)
- Border tipis antar sel dan border tebal di outline tabel
- Freeze pane di baris header agar tetap terlihat saat scroll
- Baris total di bagian bawah
- Auto-size kolom sesuai konten

Halaman export menyediakan filter sebelum download: status, kondisi, ruangan, kategori, kata kunci nama barang, dan rentang tanggal perolehan.

> **[GAMBAR 9.3: Contoh file Excel hasil export aset dengan header biru tua, zebra striping, dan baris total]**

### 9.4.2 Export ke PDF

Sistem mendukung export data aset ke format PDF menggunakan library DomPDF. PDF yang dihasilkan dalam orientasi landscape untuk mengakomodasi tabel yang lebar, dilengkapi dengan header organisasi (RBTV), judul laporan, dan footer dengan tanggal cetak.

### 9.4.3 Export ke CSV

Sistem mendukung export data ke format CSV dengan beberapa teknik khusus untuk kompatibilitas dengan Excel Indonesia:

- **UTF-8 BOM** di awal file agar Excel membaca karakter Indonesia dengan benar
- **Delimiter titik koma (;)** yang lebih kompatibel dengan Excel versi Indonesia
- Header laporan di bagian atas file (nama organisasi, tanggal cetak, total record)

## 9.5 Laporan

### 9.5.1 Laporan Aset

Laporan aset menampilkan seluruh data aset dengan filter opsional (ruangan, kondisi, status). Laporan dapat dilihat di halaman web, dicetak sebagai PDF landscape, atau diexport sebagai CSV.

### 9.5.2 Laporan Per Ruangan

Laporan per ruangan menghasilkan dokumen PDF yang menampilkan daftar aset di ruangan tertentu. Laporan ini tersedia untuk setiap ruangan yang memiliki aset. Contoh: laporan Ruang Editing menampilkan AST-001 (Maintenance) dan AST-002 (Aktif).

> **[GAMBAR 9.4: Contoh laporan per ruangan PDF untuk Ruang Editing menampilkan AST-001 dan AST-002]**

### 9.5.3 Laporan Maintenance

Laporan maintenance menampilkan seluruh aset yang sedang berstatus Maintenance. Laporan tersedia dalam format PDF dan CSV. Berdasarkan data aktual, laporan ini menampilkan AST-001 (Kamera Sony A7, Ruang Editing, kondisi Baik).

## 9.6 Statistik dan Ringkasan Data

Statistik dan ringkasan data digunakan untuk menyajikan informasi sistem dalam bentuk visual yang mudah dipahami. Fitur ini terutama bermanfaat bagi pengelola untuk memahami kondisi dan perkembangan data aset.

Beberapa statistik yang ditampilkan antara lain:

1. Jumlah total aset, aktif, maintenance, non-aktif, dan rusak.
2. Distribusi kondisi aset dalam bentuk grafik donut.
3. Top 5 kategori aset dalam bentuk grafik bar.
4. Jumlah aset yang ditambahkan pada bulan berjalan.

Statistik ini membantu pengelola dalam melakukan evaluasi dan pengambilan keputusan terkait pengelolaan aset.

## 9.7 Pengujian Dashboard, Import, Export, dan Laporan

| No | Skenario | Hasil yang Diharapkan | Hasil |
|----|----------|-----------------------|-------|
| 1 | Tampilkan dashboard | Statistik dan chart tampil | Berhasil |
| 2 | Import aset valid | Aset tersimpan | Berhasil |
| 3 | Import file format salah | Error validasi format | Berhasil |
| 4 | Export aset Excel | File .xlsx terunduh dengan styling | Berhasil |
| 5 | Export aset PDF | File .pdf terunduh | Berhasil |
| 6 | Export CSV maintenance | File .csv dengan UTF-8 BOM | Berhasil |
| 7 | Laporan per ruangan | PDF dengan daftar aset ruangan | Berhasil |

## 9.8 Kesimpulan Modul

Modul 9 membahas perancangan dan implementasi dashboard, import, export, dan laporan SimAset secara menyeluruh. Dashboard memberikan visibilitas kondisi aset secara real-time. Import dengan validasi per baris memungkinkan penambahan data massal yang efisien. Export Excel dengan styling profesional dan PDF siap cetak memenuhi kebutuhan pelaporan formal.

Dengan perancangan dashboard dan fitur data yang baik, sistem mampu memberikan pengalaman pengguna yang optimal serta mendukung pengelolaan data aset secara efektif.
