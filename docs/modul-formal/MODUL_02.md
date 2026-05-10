# MODUL 2 - ANALISIS KEBUTUHAN SISTEM

## 2.1 Pendahuluan

Analisis kebutuhan sistem merupakan tahap fundamental dalam proses pengembangan SimAset. Tahapan ini bertujuan untuk memahami secara menyeluruh permasalahan yang ada, kebutuhan pengguna, serta fungsi dan kualitas sistem yang harus dipenuhi agar sistem yang dikembangkan dapat berjalan sesuai tujuan.

Tanpa analisis kebutuhan yang matang, sistem berisiko tidak sesuai dengan kebutuhan pengguna, sulit digunakan, atau bahkan tidak dimanfaatkan secara optimal. Oleh karena itu, pada modul ini dilakukan pembahasan mendalam mengenai identifikasi masalah sistem lama, analisis pengguna, kebutuhan fungsional dan non-fungsional, batasan sistem, serta metode analisis yang digunakan.

## 2.2 Tujuan Modul

Modul Analisis Kebutuhan Sistem ini disusun untuk mengidentifikasi dan mendefinisikan kebutuhan sistem secara menyeluruh sebelum dilakukan perancangan dan implementasi sistem. Tujuan dari penyusunan modul ini adalah sebagai berikut:

1. Mengidentifikasi permasalahan yang terdapat pada sistem pengelolaan aset yang berjalan sebelumnya.
2. Menganalisis kebutuhan pengguna sistem berdasarkan peran dan karakteristik pengguna.
3. Menentukan kebutuhan fungsional yang harus disediakan oleh sistem.
4. Menentukan kebutuhan non-fungsional sebagai standar kualitas sistem.
5. Menetapkan batasan sistem agar proses pengembangan tetap fokus dan terarah.
6. Menyediakan dasar yang kuat bagi tahap perancangan sistem pada modul selanjutnya.

Dengan adanya modul ini, kebutuhan sistem dapat dirumuskan secara jelas dan terstruktur sehingga meminimalkan kesalahan pada tahap pengembangan berikutnya.

## 2.3 Identifikasi Masalah Sistem Lama (Pendalaman Analisis)

Permasalahan pada sistem lama tidak hanya terletak pada ketiadaan platform digital terintegrasi, tetapi juga pada aspek pengalaman pengguna dan manajemen data. Data aset yang tersebar menyebabkan terjadinya inkonsistensi informasi, baik dari sisi kondisi aset maupun informasi lokasi penempatan.

Selain itu, sistem pencatatan yang tidak berbasis digital membuat pengelola hanya mengetahui keberadaan aset tanpa memahami kondisi terkininya. Hal ini sangat berpengaruh bagi pengelola yang bertanggung jawab atas banyak aset di berbagai ruangan. Kurangnya sistem pelacakan kondisi juga berdampak pada lambatnya penanganan kerusakan karena pengelola tidak memiliki gambaran jelas mengenai kondisi dan riwayat perbaikan setiap aset.

Dari sisi pengelola, tidak adanya sistem terpusat menyebabkan proses pembaruan data menjadi lambat dan tidak terdokumentasi dengan baik. Data aset sering kali tersimpan dalam format yang berbeda-beda, sehingga sulit untuk dikelola dan dikembangkan lebih lanjut.

Sebelum dikembangkan SimAset, pengelolaan aset barang kantor RBTV Bengkulu masih menghadapi berbagai kendala, baik dari sisi pengguna maupun pengelola sistem. Permasalahan utama yang ditemukan antara lain:

1. **Pencatatan Tidak Terpusat**
   Data aset tersebar di berbagai file spreadsheet yang dikelola secara terpisah. Kondisi ini menyulitkan pengelola dalam memperoleh informasi yang lengkap dan konsisten dalam satu platform.

2. **Tidak Ada Pelacakan Kondisi Aset**
   Sistem pencatatan lama hanya menyimpan data inventaris tanpa mekanisme untuk memantau kondisi fisik aset secara berkala. Akibatnya, kerusakan aset sering terlambat diketahui dan ditangani.

3. **Identifikasi Aset Lambat dan Rawan Kesalahan**
   Tanpa sistem identifikasi yang standar, aset dengan nama atau jenis yang serupa sulit dibedakan. Pengecekan aset memerlukan waktu lama karena harus mencocokkan data secara manual.

4. **Pengelolaan Data Kurang Efisien**
   Proses pengelolaan data aset masih dilakukan secara manual menggunakan spreadsheet yang tidak terintegrasi, sehingga rawan kesalahan, sulit dikontrol, dan tidak terdokumentasi dengan baik.

5. **Tidak Ada Audit Trail**
   Tidak ada mekanisme untuk mencatat siapa yang melakukan perubahan data, kapan perubahan dilakukan, dan apa yang diubah. Hal ini menyulitkan proses audit dan akuntabilitas pengelolaan aset.

Permasalahan-permasalahan tersebut menjadi dasar utama perlunya pengembangan SimAset sebagai sistem informasi manajemen aset berbasis web.

> **[GAMBAR 2.1: Diagram permasalahan sistem lama yang menggambarkan 5 masalah utama pengelolaan aset manual]**

## 2.4 Analisis Pengguna Sistem

Analisis pengguna dilakukan untuk memahami karakteristik, kebutuhan, dan pola interaksi pengguna dengan sistem. Sistem ini dirancang untuk melayani dua kelompok pengguna utama, yaitu Admin dan Staff.

### 2.4.1 Admin

Admin merupakan pihak yang memiliki peran strategis dalam pengelolaan sistem. Admin biasanya berasal dari pihak yang diberi kewenangan penuh untuk mengelola data aset dan konfigurasi sistem.

Kebutuhan admin dalam sistem ini meliputi:

1. Sistem yang mampu mengurangi beban kerja manual dalam pencatatan aset.
2. Kemudahan dalam menambahkan, mengedit, dan menghapus data aset.
3. Pengelolaan foto aset dan informasi perolehan secara akurat.
4. Dashboard yang informatif dengan statistik dan visualisasi data.
5. Struktur data yang konsisten dan terorganisir.
6. Sistem keamanan untuk membatasi akses hanya kepada pengguna berwenang.
7. Audit log untuk memantau seluruh aktivitas pengguna.
8. Sistem yang mudah dikembangkan di masa depan.

Dengan demikian, sistem harus dirancang tidak hanya fungsional, tetapi juga intuitif dan ramah bagi admin dengan berbagai latar belakang teknis.

### 2.4.2 Staff

Staff merupakan pengguna operasional yang mengelola data aset sehari-hari. Karakteristik staff sangat beragam, mulai dari yang memiliki latar belakang teknis hingga yang tidak.

Kebutuhan staff meliputi:

1. Akses pengelolaan aset yang cepat dan mudah.
2. Tampilan antarmuka yang sederhana dan menarik.
3. Informasi aset yang lengkap dan mudah dipahami.
4. Identifikasi aset melalui QR Code yang dapat dipindai.
5. Kemampuan mencatat dan menyelesaikan proses maintenance.
6. Import data massal untuk efisiensi saat penambahan banyak aset.

Penggunaan QR Code menjadi solusi utama karena mampu menggabungkan identifikasi dan akses informasi aset secara bersamaan.

## 2.5 Kebutuhan Fungsional Sistem

Kebutuhan fungsional merupakan fungsi utama yang wajib disediakan oleh sistem agar dapat berjalan sesuai dengan tujuan pengembangan. Kebutuhan fungsional sistem ini meliputi:

1. Sistem mampu menampilkan dashboard berisi statistik dan visualisasi data aset.
2. Sistem mampu menampilkan daftar aset dengan filter dan pencarian.
3. Sistem mampu menampilkan detail aset secara lengkap.
4. Sistem menyediakan fitur autentikasi untuk Admin dan Staff.
5. Sistem menyediakan CRUD (Create, Read, Update, Delete) data aset.
6. Sistem mampu mengelola master data barang dan ruangan.
7. Sistem mampu generate dan mencetak QR Code per aset.
8. Sistem mampu memindai QR Code untuk mengakses detail aset.
9. Sistem mampu menyimpan dan menampilkan foto aset.
10. Sistem mampu mencatat dan menyelesaikan proses maintenance aset.
11. Sistem mampu mengirim notifikasi email saat maintenance selesai.
12. Sistem mendukung import data massal dari file Excel/CSV.
13. Sistem mendukung export data ke Excel, PDF, dan CSV.
14. Sistem mampu menghasilkan laporan aset, per ruangan, dan maintenance.
15. Sistem mencatat seluruh aktivitas pengguna dalam audit log.
16. Admin dapat mengelola akun pengguna (tambah, ubah, hapus).

Setiap fungsi dirancang agar saling terintegrasi dan mendukung tujuan utama sistem.

## 2.6 Kebutuhan Non-Fungsional Sistem

Kebutuhan non-fungsional berkaitan dengan kualitas sistem secara keseluruhan, antara lain:

1. **Usability (Kemudahan Penggunaan)**
   Sistem harus mudah dipahami dan digunakan tanpa memerlukan pelatihan khusus.

2. **Performance (Kinerja Sistem)**
   Sistem harus memiliki waktu respons yang cepat, terutama dalam menampilkan daftar aset dan memproses QR Code.

3. **Compatibility (Kesesuaian Perangkat)**
   Sistem dapat diakses melalui berbagai perangkat dan browser modern.

4. **Security (Keamanan Sistem)**
   Sistem harus membatasi akses pengelolaan hanya kepada pengguna berwenang dengan mekanisme autentikasi dan otorisasi berbasis role.

5. **Maintainability & Scalability**
   Sistem mudah dipelihara dan dikembangkan untuk penambahan fitur di masa depan.

## 2.7 Batasan Sistem

Batasan sistem ditetapkan untuk menjaga fokus pengembangan dan efektivitas sistem. Batasan tersebut antara lain:

1. Sistem hanya berfungsi sebagai media pencatatan dan pemantauan aset fisik.
2. Sistem tidak menyediakan fitur pengadaan, pemesanan, atau pembayaran aset.
3. Sistem tidak mengelola aset tidak berwujud seperti lisensi software.
4. Sistem tidak menyediakan perhitungan depresiasi atau nilai buku aset secara otomatis.
5. Sistem hanya mencakup aset yang berada di lingkungan RBTV Bengkulu.
6. Generate QR Code memerlukan koneksi internet karena menggunakan API eksternal.

Batasan ini bukan merupakan kelemahan, melainkan strategi agar sistem dapat dikembangkan secara optimal sesuai tujuan awal.

## 2.8 Metode Analisis Kebutuhan

Metode analisis kebutuhan dilakukan secara sistematis agar hasil analisis dapat dipertanggungjawabkan secara akademik. Metode yang digunakan meliputi:

1. **Studi Literatur**
   Mengkaji jurnal, buku, dan referensi terkait sistem informasi manajemen aset dan pengembangan web berbasis Laravel.

2. **Observasi**
   Mengamati proses pengelolaan aset yang berjalan di RBTV Bengkulu secara langsung.

3. **Analisis Pemangku Kepentingan (Stakeholder)**
   Mengidentifikasi pihak yang terlibat langsung dan tidak langsung dalam pengelolaan aset.

4. **Analisis Kebutuhan Pengguna**
   Mengelompokkan kebutuhan berdasarkan peran Admin dan Staff.

5. **Analisis Kelayakan Sistem**
   Menilai kelayakan sistem dari sisi teknis dan operasional.

## 2.9 Kesimpulan Modul

Modul 2 ini membahas analisis kebutuhan SimAset secara menyeluruh, mulai dari identifikasi permasalahan sistem lama, analisis karakteristik dan kebutuhan pengguna, perumusan kebutuhan fungsional dan non-fungsional, hingga penetapan batasan sistem dan metode analisis yang digunakan.

Hasil analisis kebutuhan yang telah dirumuskan pada modul ini menjadi acuan utama dalam proses perancangan sistem pada modul berikutnya. Dengan analisis kebutuhan yang jelas dan terstruktur, diharapkan sistem yang dikembangkan dapat sesuai dengan kebutuhan pengguna serta berjalan secara efektif dan optimal.
