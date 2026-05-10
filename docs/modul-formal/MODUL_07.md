# MODUL 7 - MANAJEMEN DATA ASET BARANG KANTOR

## 7.1 Pendahuluan

Manajemen data aset barang kantor merupakan proses pengelolaan seluruh informasi aset fisik yang tersimpan dalam sistem, mulai dari tahap pencatatan aset baru, pembaruan kondisi, pemantauan lokasi, hingga penyajian kepada pengguna. Dalam SimAset, data aset menjadi komponen utama yang menentukan kualitas informasi yang diterima oleh pengelola.

Data aset yang dikelola secara baik akan menghasilkan informasi yang akurat, konsisten, dan mudah dipahami. Sebaliknya, pengelolaan data yang kurang terstruktur dapat menimbulkan kesalahan informasi, duplikasi data, serta menurunkan kepercayaan pengguna terhadap sistem. Oleh karena itu, sistem ini dirancang dengan mekanisme manajemen data yang terkontrol, sistematis, dan mudah digunakan oleh Admin maupun Staff.

Modul ini membahas secara rinci implementasi manajemen data aset, meliputi proses CRUD data aset, pengelolaan master data barang dan ruangan, upload foto aset, serta pengujian modul manajemen data.

## 7.2 CRUD Data Aset

CRUD (Create, Read, Update, Delete) merupakan konsep dasar dalam pengelolaan data yang memungkinkan pengguna untuk mengatur seluruh data aset secara penuh dan terkontrol. Implementasi CRUD pada sistem ini menjadi inti dari proses manajemen data aset barang kantor.

### 7.2.1 Create (Menambahkan Data Aset)

Proses penambahan data aset dilakukan oleh Admin atau Staff melalui halaman form input yang tersedia pada sistem. Form ini dirancang dengan tampilan yang sederhana dan terstruktur agar memudahkan pengguna dalam memasukkan data.

Data yang dimasukkan pada proses ini meliputi:

1. Jenis barang (dipilih dari master data barang)
2. Ruangan penempatan (dipilih dari master data ruangan)
3. Kondisi aset (Baik / Rusak Ringan / Rusak Berat)
4. Status aset (Aktif / Maintenance / Non-Aktif)
5. Tanggal perolehan
6. Harga perolehan (opsional)
7. Sumber perolehan (Pembelian / Hibah / Sumbangan / Pinjaman / Lainnya)
8. Serial number (opsional, harus unik)
9. Jumlah unit (default 1)
10. Foto aset (opsional, format JPG/PNG/GIF, maksimal 2MB)
11. Keterangan tambahan (opsional)

Sebelum data disimpan ke dalam database, sistem melakukan validasi server-side terhadap setiap input. Validasi meliputi pengecekan field wajib, format data, keunikan serial number, serta batasan ukuran dan format file foto. Validasi ini bertujuan untuk mencegah kesalahan input yang dapat mempengaruhi akurasi data aset pada sistem.

Sistem juga secara otomatis men-generate kode aset unik menggunakan algoritma gap-filling. Algoritma ini mencari nomor terkecil yang belum dipakai, sehingga jika AST-003 dihapus dan ditambah aset baru, kode yang digunakan adalah AST-003 (mengisi celah), bukan AST-004.

Setelah data dinyatakan valid, sistem akan menyimpan data ke dalam database, mencatat aktivitas Create ke log_aktivitas, dan menampilkan notifikasi bahwa proses penambahan data berhasil dilakukan.

> **[GAMBAR 7.1: Tampilan form tambah aset baru dengan 4 section card (Informasi Barang, Lokasi & Waktu, Kondisi & Status, Foto Aset)]**

### 7.2.2 Read (Menampilkan Data Aset)

Fungsi Read digunakan untuk menampilkan data aset yang telah tersimpan dalam database. Data aset ditampilkan pada dua konteks dalam sistem.

Pada halaman daftar aset, data ditampilkan dalam bentuk tabel yang berisi daftar aset lengkap dengan informasi singkat (kode, nama barang, kategori, ruangan, kondisi, status). Tampilan ini dilengkapi dengan filter multi-kriteria (search, status, kondisi, kategori) dan pagination 15 item per halaman untuk memudahkan pengguna dalam mencari dan mengelola data.

Pada halaman detail aset, data ditampilkan secara lengkap termasuk foto aset, QR Code, informasi perolehan, dan informasi sistem (dibuat oleh, diperbarui oleh, waktu). Setiap aset juga dapat diakses melalui pemindaian QR Code tanpa perlu login.

> **[GAMBAR 7.2: Tampilan halaman daftar aset dengan filter bar, tabel data, dan badge status berwarna]**

### 7.2.3 Update (Memperbarui Data Aset)

Fungsi Update digunakan untuk memperbarui data aset yang telah tersimpan dalam sistem. Pembaruan data dapat dilakukan ketika terdapat perubahan informasi, seperti perubahan kondisi, perpindahan ruangan, atau koreksi data perolehan.

Pengguna dapat mengakses fitur update melalui tombol edit pada daftar data aset atau halaman detail aset. Sistem akan menampilkan form edit yang berisi data lama untuk kemudian diperbarui sesuai kebutuhan. Proses pembaruan data ini juga dilengkapi dengan validasi input yang sama dengan proses tambah data. Setelah data berhasil diperbarui, perubahan akan langsung tercermin pada halaman sistem dan aktivitas Update dicatat ke log_aktivitas.

### 7.2.4 Delete (Menghapus Data Aset)

Fungsi Delete digunakan untuk menghapus data aset yang tidak lagi relevan atau tidak digunakan. Penghapusan data menggunakan mekanisme soft delete, di mana data tidak benar-benar dihapus dari database melainkan hanya ditandai dengan timestamp di kolom deleted_at. Hal ini memastikan kode aset yang sudah digunakan tidak akan dipakai ulang.

Sistem menyediakan konfirmasi dialog (menggunakan SweetAlert2) sebelum proses penghapusan dilakukan untuk mencegah kesalahan penghapusan data. Sistem juga mendukung batch delete untuk menghapus beberapa aset sekaligus dari halaman daftar.

> **[GAMBAR 7.3: Tampilan dialog konfirmasi hapus aset menggunakan SweetAlert2]**

## 7.3 Pengelolaan Master Data Barang

Master data barang berfungsi sebagai referensi jenis/tipe barang yang dapat dijadikan aset. Setiap aset yang terdaftar harus merujuk ke salah satu barang di master data ini.

Pengelolaan master data barang meliputi:

- Tambah barang baru dengan auto-generate kode (BRG-001, BRG-002, dst.)
- Edit nama, kategori, status, dan keterangan barang
- Hapus barang (soft delete, tidak bisa dihapus jika masih ada aset yang merujuk)
- Filter berdasarkan kategori dan status
- Export ke Excel

Kategori barang yang tersedia: Kamera, Audio, Komputer, Lighting, Furniture, Peralatan Kantor.

> **[GAMBAR 7.4: Tampilan halaman daftar master barang dengan filter kategori dan kolom jumlah aset]**

## 7.4 Pengelolaan Master Data Ruangan

Master data ruangan berfungsi sebagai referensi lokasi penempatan aset. Setiap aset yang terdaftar dapat ditempatkan di salah satu ruangan yang tersedia.

Pengelolaan master data ruangan meliputi:

- Tambah ruangan baru dengan nama dan lantai
- Edit data ruangan
- Hapus ruangan (tidak bisa dihapus jika masih ada aset di dalamnya)
- Statistik: total ruangan, terisi, kosong

Data ruangan aktual: Studio 1 (Lantai 1), Studio 2 (Lantai 2), Ruang Editing (Lantai 1), Ruang Redaksi (lantai 5).

> **[GAMBAR 7.5: Tampilan halaman daftar ruangan dengan statistik dan badge jumlah aset per ruangan]**

## 7.5 Upload dan Manajemen Foto Aset

Foto aset berfungsi sebagai dokumentasi visual yang mendukung identifikasi aset secara fisik. Sistem ini menyediakan fitur upload dan manajemen foto aset yang dapat dikelola oleh Admin maupun Staff.

Pengguna dapat mengunggah satu foto untuk setiap aset. Foto yang diunggah disimpan di direktori public/foto_aset/ dengan nama file format {timestamp}_{nama_file_asli}. Manajemen foto meliputi proses unggah, penampilan, penggantian, dan penghapusan foto. Sistem memastikan bahwa format (JPG/PNG/GIF) dan ukuran foto (maksimal 2MB) sesuai dengan ketentuan agar tidak mengganggu performa sistem.

## 7.6 Kategori dan Deskripsi Aset

Pengelompokan data aset berdasarkan kategori barang bertujuan untuk memudahkan pengguna dalam mencari dan memahami jenis aset yang tersedia. Setiap aset secara otomatis mendapatkan kategori dari master data barang yang dipilih. Deskripsi aset (keterangan) berfungsi untuk memberikan penjelasan tambahan mengenai kondisi atau catatan khusus aset. Pengelolaan kategori dan deskripsi yang baik akan meningkatkan kualitas informasi dan pengalaman pengguna dalam menggunakan sistem.

## 7.7 Pengujian Modul Data Aset

Pengujian modul manajemen data aset dilakukan untuk memastikan bahwa seluruh fitur CRUD dan pengelolaan data berjalan dengan baik. Pengujian dilakukan dengan berbagai skenario penggunaan, seperti penambahan aset baru, pembaruan kondisi, penghapusan aset, dan filter data. Hasil pengujian menunjukkan bahwa modul manajemen data aset dapat berjalan sesuai dengan perancangan dan mampu mengelola data aset secara efektif.

| No | Skenario | Hasil yang Diharapkan | Hasil |
|----|----------|-----------------------|-------|
| 1 | Tambah aset valid | Aset tersimpan, kode auto-generated | Berhasil |
| 2 | Tambah aset serial duplikat | Error "serial number sudah terdaftar" | Berhasil |
| 3 | Upload foto format salah | Error "format tidak valid" | Berhasil |
| 4 | Edit aset | Data terupdate, log Update tercatat | Berhasil |
| 5 | Hapus aset | Soft delete, tidak muncul di daftar | Berhasil |
| 6 | Hapus ruangan berisi aset | Error "masih memiliki aset" | Berhasil |

## 7.8 Kesimpulan Modul

Modul 7 membahas manajemen data aset barang kantor secara menyeluruh, mulai dari proses CRUD data aset dengan validasi lengkap, pengelolaan master data barang dan ruangan, upload foto, hingga auto-generate kode dengan algoritma gap-filling. Modul ini menjadi fondasi utama dalam penyajian informasi aset yang akurat dan interaktif pada modul selanjutnya.
