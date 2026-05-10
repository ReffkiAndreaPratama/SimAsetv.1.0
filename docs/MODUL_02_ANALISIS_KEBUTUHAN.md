# MODUL 2 — ANALISIS KEBUTUHAN SISTEM
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 2.1 Pendahuluan

Analisis kebutuhan sistem merupakan tahap paling fundamental dalam seluruh siklus pengembangan perangkat lunak. Pada tahap ini, pengembang berusaha memahami secara mendalam dan menyeluruh tentang apa yang sebenarnya dibutuhkan oleh pengguna, permasalahan apa yang harus diselesaikan, dan batasan-batasan apa yang harus diperhatikan selama pengembangan berlangsung.

Tanpa analisis kebutuhan yang matang dan komprehensif, sistem yang dikembangkan berisiko tidak sesuai dengan kebutuhan pengguna yang sebenarnya, sulit digunakan karena tidak mempertimbangkan karakteristik pengguna, atau bahkan tidak dimanfaatkan secara optimal karena fitur yang dikembangkan tidak relevan dengan masalah yang ada.

Pada modul ini, analisis kebutuhan SimAset dilakukan melalui beberapa pendekatan, yaitu observasi langsung terhadap proses pengelolaan aset yang berjalan, identifikasi permasalahan pada sistem lama, analisis karakteristik dan kebutuhan pengguna berdasarkan perannya, serta perumusan kebutuhan fungsional dan non-fungsional yang harus dipenuhi oleh sistem.

---

## 2.2 Identifikasi Masalah Sistem Lama

Sebelum SimAset dikembangkan, pengelolaan aset RBTV dilakukan secara manual menggunakan spreadsheet. Berdasarkan observasi dan wawancara dengan pengguna, ditemukan sejumlah permasalahan mendasar yang menjadi justifikasi utama pengembangan sistem baru.

### 2.2.1 Informasi Aset Tidak Terpusat

Permasalahan paling mendasar adalah tidak adanya satu sumber data yang dapat dijadikan acuan tunggal. Data aset tersebar di berbagai file Excel yang dikelola secara terpisah oleh masing-masing penanggung jawab ruangan atau departemen. Kondisi ini menyebabkan inkonsistensi data yang serius — data yang sama bisa memiliki nilai berbeda di file yang berbeda, dan tidak ada mekanisme untuk mengetahui versi mana yang paling akurat dan terkini.

Ketika manajemen membutuhkan gambaran kondisi aset secara keseluruhan, staf harus mengumpulkan semua file dari berbagai sumber, menggabungkannya secara manual, dan melakukan rekonsiliasi data yang memakan waktu berjam-jam. Proses ini sangat tidak efisien dan rawan kesalahan.

### 2.2.2 Tidak Ada Visualisasi Kondisi Aset

Sistem lama hanya menyimpan data dalam bentuk teks di spreadsheet, tanpa ada mekanisme untuk memvisualisasikan kondisi aset secara keseluruhan. Tidak ada dashboard yang menampilkan berapa aset yang dalam kondisi baik, berapa yang rusak, atau berapa yang sedang dalam maintenance. Untuk mengetahui kondisi ini, seseorang harus membaca baris demi baris data di spreadsheet.

Selain itu, tidak ada cara untuk mengetahui kondisi aset secara real-time tanpa melakukan pengecekan fisik langsung ke lokasi aset. Kerusakan aset sering kali baru diketahui ketika aset tersebut sudah tidak dapat digunakan, bukan saat kerusakan pertama kali terjadi.

### 2.2.3 Identifikasi Aset Lambat dan Tidak Standar

Tanpa sistem identifikasi yang standar dan konsisten, proses identifikasi aset menjadi sangat lambat dan rawan kesalahan. Aset dengan nama atau jenis yang serupa sulit dibedakan hanya dari deskripsi teks. Saat dilakukan audit atau pemindahan aset, staf harus mencocokkan data secara manual dengan melihat fisik aset satu per satu, yang sangat memakan waktu terutama jika jumlah aset banyak.

### 2.2.4 Proses Maintenance Tidak Terdokumentasi

Ketika sebuah aset mengalami kerusakan dan perlu diperbaiki, proses maintenance dilakukan tanpa pencatatan yang sistematis. Tidak ada riwayat perbaikan per aset yang dapat ditelusuri, tidak ada notifikasi kepada pihak terkait saat aset masuk atau selesai maintenance, dan tidak ada cara untuk mengetahui berapa lama sebuah aset sudah dalam kondisi rusak atau sedang diperbaiki. Akibatnya, aset yang rusak kadang terlupakan dan tidak segera ditangani.

### 2.2.5 Pembuatan Laporan Tidak Efisien

Setiap kali manajemen membutuhkan laporan kondisi aset, staf harus mengumpulkan data dari berbagai spreadsheet, merekap secara manual, memformat laporan sesuai kebutuhan, dan mencetaknya. Proses ini bisa memakan waktu berjam-jam dan hasilnya sering tidak akurat karena data yang tidak up-to-date. Format laporan pun tidak konsisten karena dibuat secara manual setiap kali.

### 2.2.6 Tidak Ada Kontrol Akses dan Audit Trail

Siapapun yang memiliki akses ke file spreadsheet dapat mengubah data tanpa jejak yang jelas. Tidak ada pembatasan hak akses berdasarkan peran pengguna, sehingga staf yang seharusnya hanya bisa melihat data bisa saja mengubah atau menghapus data secara tidak sengaja atau disengaja. Tidak ada audit trail yang mencatat siapa mengubah apa dan kapan, sehingga jika terjadi kesalahan data, sangat sulit untuk menelusuri penyebabnya.

> **[GAMBAR 2.1: Diagram fishbone (Ishikawa) yang menggambarkan akar permasalahan pengelolaan aset manual di RBTV]**

---

## 2.3 Analisis Pengguna Sistem

Analisis pengguna dilakukan untuk memahami karakteristik, kebutuhan spesifik, dan pola interaksi masing-masing kelompok pengguna dengan sistem. Pemahaman yang baik tentang pengguna sangat penting agar sistem yang dikembangkan benar-benar sesuai dengan kebutuhan dan kemampuan mereka.

### 2.3.1 Admin

Admin merupakan pengguna dengan tanggung jawab penuh atas pengelolaan sistem. Berdasarkan data aktual dari database, Admin di RBTV adalah pengelola yang memiliki pemahaman teknis yang cukup dan bertanggung jawab atas akurasi seluruh data aset.

**Karakteristik Admin:**
- Memiliki pemahaman teknis yang memadai tentang sistem informasi
- Bertanggung jawab atas akurasi dan kelengkapan seluruh data aset
- Perlu memantau aktivitas seluruh pengguna untuk memastikan tidak ada penyalahgunaan
- Sering membuat laporan untuk kebutuhan manajemen
- Perlu mengelola akun pengguna (menambah staff baru, menonaktifkan akun yang tidak aktif)

**Kebutuhan spesifik Admin:**
- Dashboard yang informatif dengan statistik lengkap dan visualisasi data yang mudah dipahami
- Kemampuan mengelola seluruh data aset, barang, dan ruangan dengan mudah
- Akses ke audit log untuk memantau aktivitas seluruh pengguna
- Kemampuan mengelola akun pengguna termasuk pengiriman email notifikasi akun baru
- Laporan komprehensif dalam berbagai format yang dapat dihasilkan kapan saja
- Notifikasi email untuk kejadian penting seperti maintenance selesai

### 2.3.2 Staff

Staff adalah pengguna operasional yang berinteraksi dengan sistem setiap hari untuk mengelola data aset. Staff mungkin tidak memiliki latar belakang teknis yang kuat, sehingga antarmuka sistem harus dirancang sesederhana dan seintuitif mungkin.

**Karakteristik Staff:**
- Mungkin tidak memiliki latar belakang teknis yang kuat
- Bekerja dengan data aset secara rutin setiap hari
- Perlu antarmuka yang sederhana, intuitif, dan tidak membingungkan
- Sering bekerja di lapangan dan perlu mengidentifikasi aset dengan cepat
- Perlu menambahkan data aset baru secara berkala

**Kebutuhan spesifik Staff:**
- Form input yang mudah dipahami dengan label yang jelas dan pesan error yang informatif
- Kemampuan mencari dan memfilter aset dengan cepat menggunakan berbagai kriteria
- Fitur QR code untuk identifikasi aset yang cepat tanpa perlu membuka laptop
- Kemampuan mencatat dan menyelesaikan maintenance dengan langkah yang sederhana
- Import data massal untuk efisiensi saat ada penambahan banyak aset sekaligus

---

## 2.4 Kebutuhan Fungsional Sistem

Kebutuhan fungsional adalah deskripsi lengkap tentang fungsi-fungsi yang harus disediakan oleh sistem agar dapat memenuhi tujuan pengembangannya. Setiap kebutuhan fungsional dirumuskan berdasarkan permasalahan yang telah diidentifikasi dan kebutuhan pengguna yang telah dianalisis.

### 2.4.1 Modul Autentikasi dan Keamanan

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-AUTH-01 | Sistem menyediakan halaman login dengan input email dan password | Tinggi |
| F-AUTH-02 | Sistem memvalidasi kredensial pengguna dan menampilkan pesan error yang jelas jika gagal | Tinggi |
| F-AUTH-03 | Sistem membuat session login yang aman setelah autentikasi berhasil | Tinggi |
| F-AUTH-04 | Sistem menyediakan fitur logout yang menghapus session secara aman | Tinggi |
| F-AUTH-05 | Sistem menyediakan fitur lupa password dengan pengiriman link reset via email | Sedang |
| F-AUTH-06 | Sistem membatasi akses seluruh halaman hanya untuk pengguna yang sudah login | Tinggi |
| F-AUTH-07 | Sistem membatasi akses fitur manajemen pengguna dan audit log hanya untuk Admin | Tinggi |
| F-AUTH-08 | Sistem mencatat waktu login terakhir setiap pengguna | Sedang |
| F-AUTH-09 | Sistem menerapkan rate limiting untuk mencegah serangan brute force | Tinggi |

### 2.4.2 Modul Manajemen Aset

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-ASET-01 | Sistem menampilkan daftar aset dengan pagination (15 item per halaman) | Tinggi |
| F-ASET-02 | Sistem menyediakan filter aset berdasarkan kata kunci, status, kondisi, dan kategori | Tinggi |
| F-ASET-03 | Sistem menyediakan form tambah aset dengan validasi server-side yang lengkap | Tinggi |
| F-ASET-04 | Sistem auto-generate kode aset unik (AST-001, AST-002, dst.) dengan algoritma gap-filling | Tinggi |
| F-ASET-05 | Sistem mendukung upload foto aset dengan validasi format dan ukuran file | Sedang |
| F-ASET-06 | Sistem menampilkan halaman detail aset yang lengkap termasuk relasi ke barang dan ruangan | Tinggi |
| F-ASET-07 | Sistem menyediakan form edit aset dengan validasi yang sama seperti form tambah | Tinggi |
| F-ASET-08 | Sistem mendukung soft delete aset (data tidak benar-benar dihapus dari database) | Tinggi |
| F-ASET-09 | Sistem mendukung batch delete untuk menghapus beberapa aset sekaligus | Sedang |
| F-ASET-10 | Sistem mencatat created_by dan updated_by untuk setiap perubahan data aset | Tinggi |
| F-ASET-11 | Sistem menampilkan statistik aset (total, aktif, maintenance, non-aktif) di dashboard | Tinggi |
| F-ASET-12 | Sistem menyimpan informasi harga perolehan dan sumber perolehan aset | Sedang |

### 2.4.3 Modul Master Data Barang

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-BRG-01 | Sistem menampilkan daftar barang dengan pagination dan filter | Tinggi |
| F-BRG-02 | Sistem menyediakan form tambah barang dengan validasi | Tinggi |
| F-BRG-03 | Sistem auto-generate kode barang unik (BRG-001, BRG-002, dst.) | Tinggi |
| F-BRG-04 | Sistem mendukung kategori barang: Kamera, Audio, Komputer, Lighting, Furniture, Peralatan Kantor | Tinggi |
| F-BRG-05 | Sistem mendukung soft delete barang | Tinggi |
| F-BRG-06 | Sistem menampilkan jumlah aset yang terdaftar untuk setiap barang | Sedang |

### 2.4.4 Modul Master Data Ruangan

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-RNG-01 | Sistem menampilkan daftar ruangan beserta jumlah aset di masing-masing ruangan | Tinggi |
| F-RNG-02 | Sistem menyediakan form tambah dan edit ruangan dengan validasi | Tinggi |
| F-RNG-03 | Sistem mencegah penghapusan ruangan yang masih memiliki aset terdaftar | Tinggi |
| F-RNG-04 | Sistem menampilkan detail ruangan beserta daftar lengkap aset di dalamnya | Sedang |
| F-RNG-05 | Sistem menampilkan statistik ruangan (total, kosong, terisi) | Sedang |

### 2.4.5 Modul QR Code

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-QR-01 | Sistem dapat generate QR code untuk setiap aset yang terdaftar | Tinggi |
| F-QR-02 | QR code yang di-generate mengarah ke URL halaman detail aset yang dapat diakses publik | Tinggi |
| F-QR-03 | Sistem mendukung cetak QR code individual dengan tampilan yang rapi | Tinggi |
| F-QR-04 | Sistem mendukung batch print QR code untuk beberapa aset sekaligus | Sedang |
| F-QR-05 | Sistem menyediakan halaman scanner QR code berbasis web | Sedang |
| F-QR-06 | Halaman detail aset dapat diakses tanpa login (untuk kemudahan identifikasi di lapangan) | Tinggi |

### 2.4.6 Modul Maintenance

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-MNT-01 | Sistem menampilkan dashboard khusus yang menampilkan semua aset berstatus Maintenance | Tinggi |
| F-MNT-02 | Sistem menyediakan fitur untuk menandai aset masuk maintenance dengan keterangan | Tinggi |
| F-MNT-03 | Sistem menyediakan fitur untuk menandai maintenance selesai dengan kondisi akhir | Tinggi |
| F-MNT-04 | Sistem mengirim email notifikasi ke semua Admin aktif saat maintenance selesai | Sedang |
| F-MNT-05 | Sistem menampilkan statistik maintenance (total, rusak berat, rusak ringan) | Sedang |

### 2.4.7 Modul Import

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-IMP-01 | Sistem mendukung import data aset dari file Excel (.xlsx, .xls) dan CSV | Tinggi |
| F-IMP-02 | Sistem mendukung import data barang dari file Excel dan CSV | Tinggi |
| F-IMP-03 | Sistem menyediakan template file import yang dapat diunduh | Tinggi |
| F-IMP-04 | Sistem memvalidasi setiap baris data import dan melaporkan error per baris | Tinggi |
| F-IMP-05 | Sistem melanjutkan proses import meskipun ada baris yang error (tidak berhenti total) | Sedang |

### 2.4.8 Modul Export dan Laporan

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-EXP-01 | Sistem mendukung export data aset ke Excel dengan styling profesional | Tinggi |
| F-EXP-02 | Sistem mendukung export data aset ke PDF siap cetak | Tinggi |
| F-EXP-03 | Sistem mendukung export data aset ke CSV | Sedang |
| F-EXP-04 | Sistem mendukung export data barang ke Excel dan PDF | Sedang |
| F-EXP-05 | Sistem mendukung filter data sebelum export (status, kondisi, ruangan, tanggal, kategori) | Tinggi |
| F-LAP-01 | Sistem menghasilkan laporan aset per ruangan dalam format PDF | Tinggi |
| F-LAP-02 | Sistem menghasilkan laporan maintenance dalam format PDF dan CSV | Tinggi |
| F-LAP-03 | Laporan mencantumkan informasi pembuat laporan dan tanggal cetak | Sedang |

### 2.4.9 Modul Dashboard

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-DSH-01 | Dashboard menampilkan total aset, aset aktif, non-aktif, maintenance, dan rusak | Tinggi |
| F-DSH-02 | Dashboard menampilkan total barang dan total ruangan | Sedang |
| F-DSH-03 | Dashboard menampilkan jumlah aset yang ditambahkan pada bulan berjalan | Sedang |
| F-DSH-04 | Dashboard menampilkan grafik distribusi kondisi aset | Sedang |
| F-DSH-05 | Dashboard menampilkan grafik distribusi 5 kategori aset terbanyak | Sedang |
| F-DSH-06 | Dashboard menampilkan tabel 10 aset yang paling baru ditambahkan | Sedang |

### 2.4.10 Modul Manajemen Pengguna (Admin Only)

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-USR-01 | Sistem menampilkan daftar semua pengguna beserta role dan status aktifnya | Tinggi |
| F-USR-02 | Sistem menyediakan form tambah pengguna dengan validasi password yang kuat | Tinggi |
| F-USR-03 | Sistem dapat mengirim email notifikasi berisi kredensial ke pengguna baru (opsional) | Sedang |
| F-USR-04 | Sistem mendukung edit data pengguna termasuk perubahan password | Tinggi |
| F-USR-05 | Sistem mendukung aktivasi dan deaktivasi akun pengguna | Tinggi |
| F-USR-06 | Sistem mencegah Admin menghapus akun miliknya sendiri | Tinggi |

### 2.4.11 Modul Audit Log (Admin Only)

| Kode | Kebutuhan Fungsional | Prioritas |
|------|---------------------|-----------|
| F-AUD-01 | Sistem mencatat seluruh aktivitas pengguna secara otomatis (login, CRUD, maintenance) | Tinggi |
| F-AUD-02 | Setiap log mencatat: user, jenis aktivitas, keterangan detail, IP address, user agent, waktu | Tinggi |
| F-AUD-03 | Sistem menampilkan audit log dengan filter berdasarkan user, jenis aktivitas, dan kata kunci | Sedang |
| F-AUD-04 | Audit log hanya dapat diakses oleh pengguna dengan role Admin | Tinggi |

---

## 2.5 Kebutuhan Non-Fungsional Sistem

Kebutuhan non-fungsional berkaitan dengan kualitas sistem secara keseluruhan, bukan tentang fungsi spesifik yang harus ada. Kebutuhan ini sama pentingnya dengan kebutuhan fungsional karena menentukan apakah sistem akan benar-benar dapat digunakan dengan baik dalam kondisi nyata.

### 2.5.1 Keamanan (Security)

Sistem harus menerapkan berbagai mekanisme keamanan untuk melindungi data aset yang sensitif:
- Autentikasi berbasis session dengan CSRF protection bawaan Laravel
- Password pengguna di-hash menggunakan algoritma bcrypt sebelum disimpan ke database
- Role-based access control yang membatasi akses fitur berdasarkan peran pengguna
- Security headers HTTP: X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy
- Validasi input server-side di semua form untuk mencegah SQL injection dan XSS
- Soft delete untuk mencegah kehilangan data secara permanen akibat kesalahan

### 2.5.2 Kemudahan Penggunaan (Usability)

Sistem harus mudah dipahami dan digunakan oleh pengguna dengan berbagai latar belakang teknis:
- Antarmuka yang konsisten di semua halaman dengan navigasi yang intuitif
- Pesan error yang jelas dan spesifik per field saat validasi gagal
- Pesan sukses yang informatif setelah setiap operasi berhasil
- Konfirmasi dialog sebelum operasi yang tidak dapat dibatalkan (hapus, batch delete)
- Label dan placeholder yang informatif pada setiap field form

### 2.5.3 Kinerja (Performance)

Sistem harus memberikan respons yang cepat meskipun data yang dikelola cukup banyak:
- Pagination untuk membatasi jumlah data yang ditampilkan per halaman (15 item)
- Eager loading pada semua query yang melibatkan relasi untuk menghindari N+1 query problem
- Filter dan pencarian yang responsif tanpa perlu reload halaman penuh
- Waktu respons halaman yang wajar (di bawah 3 detik) untuk koneksi internet standar

### 2.5.4 Keandalan (Reliability)

Sistem harus dapat diandalkan untuk menjaga integritas data:
- Validasi data yang ketat di sisi server untuk mencegah data tidak valid masuk ke database
- Soft delete untuk mencegah kehilangan data yang tidak disengaja
- Error handling yang baik dengan pesan yang informatif dan logging error untuk debugging
- Transaksi database untuk operasi yang melibatkan beberapa tabel sekaligus

### 2.5.5 Pemeliharaan (Maintainability)

Sistem harus mudah dipelihara dan dikembangkan lebih lanjut:
- Kode terstruktur mengikuti pola MVC Laravel yang sudah teruji
- Migration untuk manajemen struktur database yang terdokumentasi dan dapat direproduksi
- Seeder untuk data awal yang dapat dijalankan ulang kapan saja
- Komentar kode yang informatif pada bagian-bagian yang kompleks

### 2.5.6 Kompatibilitas (Compatibility)

Sistem harus dapat diakses dari berbagai perangkat dan browser:
- Antarmuka responsif yang dapat diakses dari desktop, tablet, dan smartphone
- Kompatibel dengan browser modern: Chrome, Firefox, Edge, dan Safari
- File export Excel kompatibel dengan Microsoft Excel dan LibreOffice Calc
- QR code dapat dipindai oleh aplikasi scanner standar di smartphone

---

## 2.6 Batasan Sistem

Batasan sistem ditetapkan secara eksplisit untuk menjaga fokus pengembangan dan memastikan sistem dapat diselesaikan dalam waktu yang tersedia. Batasan ini bukan merupakan kelemahan, melainkan strategi agar sistem dapat dikembangkan secara optimal sesuai tujuan awal.

1. Sistem hanya mengelola aset fisik yang dapat diidentifikasi secara fisik, bukan aset tidak berwujud
2. Sistem tidak menyediakan fitur pemesanan, reservasi, atau peminjaman aset
3. Sistem tidak terintegrasi dengan sistem keuangan, akuntansi, atau ERP manapun
4. Sistem tidak menghitung depresiasi atau nilai buku aset secara otomatis
5. Sistem tidak menyediakan navigasi rute menuju lokasi aset secara real-time
6. Generate QR code memerlukan koneksi internet karena menggunakan API eksternal (qrserver.com)
7. Notifikasi email memerlukan konfigurasi SMTP yang valid di file .env
8. Sistem hanya mencakup aset yang berada di lingkungan RBTV Bengkulu

---

## 2.7 Kesimpulan Modul

Modul 2 ini telah mengidentifikasi dan mendefinisikan kebutuhan sistem SimAset secara menyeluruh dan terstruktur. Enam permasalahan utama pada sistem lama telah diidentifikasi sebagai justifikasi pengembangan sistem baru. Karakteristik dan kebutuhan spesifik dua kelompok pengguna (Admin dan Staff) telah dianalisis secara mendalam.

Kebutuhan fungsional sistem telah dirumuskan dalam 11 modul dengan total lebih dari 50 kebutuhan spesifik yang terukur dan dapat diverifikasi. Kebutuhan non-fungsional yang mencakup keamanan, kemudahan penggunaan, kinerja, keandalan, pemeliharaan, dan kompatibilitas juga telah ditetapkan sebagai standar kualitas sistem.

Hasil analisis kebutuhan yang komprehensif ini menjadi acuan utama dalam proses perancangan sistem pada Modul 3, memastikan bahwa setiap keputusan desain yang diambil benar-benar berakar pada kebutuhan nyata pengguna.

---

*Kembali ke: [Modul 1 — Pendahuluan](MODUL_01_PENDAHULUAN.md)*
*Lanjut ke: [Modul 3 — Perancangan Sistem](MODUL_03_PERANCANGAN_SISTEM.md)*
