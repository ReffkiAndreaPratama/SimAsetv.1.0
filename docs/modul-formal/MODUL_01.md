# MODUL 1 - PENDAHULUAN SISTEM

## 1.1 Deskripsi Umum Sistem

SimAset adalah sebuah sistem informasi manajemen aset barang kantor berbasis web yang dirancang untuk mengelola, memantau, dan mendokumentasikan seluruh aset fisik milik Rakyat Bengkulu Televisi (RBTV) secara digital dan terpusat. Sistem ini menggantikan proses pencatatan manual yang selama ini dilakukan menggunakan spreadsheet yang tidak terintegrasi.

Sistem ini mengintegrasikan data aset dengan fitur pelacakan kondisi, manajemen lokasi (ruangan), pembuatan QR Code, pencatatan maintenance, serta pelaporan komprehensif dalam satu platform yang saling terhubung. Dengan demikian, pengelola dapat memperoleh informasi aset yang akurat, real-time, dan mudah diakses kapan saja.

Keunikan utama sistem ini terletak pada pemanfaatan QR Code sebagai media identifikasi aset. Melalui QR Code tersebut, pengguna dapat memindai kode menggunakan kamera smartphone untuk langsung mengakses detail informasi aset tanpa perlu membuka aplikasi atau mencari secara manual.

> **[GAMBAR 1.1: Tampilan halaman utama / dashboard SimAset yang menampilkan kartu statistik aset, grafik distribusi kondisi, dan tabel aset terbaru]**

Sistem ini dikembangkan menggunakan pendekatan pengembangan sistem modern berbasis MVC (Model-View-Controller) dengan framework Laravel, di mana antarmuka pengguna dirancang agar responsif, ramah pengguna (user-friendly), dan dapat diakses melalui berbagai perangkat. Dengan demikian, sistem diharapkan mampu menjangkau seluruh pengelola aset di lingkungan RBTV Bengkulu.

## 1.2 Latar Belakang Pengembangan

Pengelolaan aset merupakan salah satu aspek penting dalam operasional sebuah perusahaan media seperti RBTV Bengkulu. Peralatan produksi seperti kamera broadcast, perangkat audio profesional, komputer editing, dan perlengkapan studio memiliki nilai yang tinggi dan perlu dikelola dengan baik agar dapat digunakan secara optimal dan terpantau kondisinya.

Namun, potensi pengelolaan yang baik tersebut belum sepenuhnya terwujud. Salah satu masalah yang sering muncul adalah terbatasnya sistem pencatatan aset yang terintegrasi. Banyak organisasi, termasuk RBTV, masih mengandalkan cara konvensional seperti spreadsheet Excel yang tidak terhubung satu sama lain, sehingga informasi tentang kondisi dan lokasi aset sulit diakses secara efektif.

Permasalahan serupa juga terjadi di lingkungan RBTV Bengkulu, yang dikenal memiliki banyak peralatan produksi bernilai tinggi. Meskipun memiliki aset yang banyak, pengelolaan aset belum terdigitalisasi dengan baik karena pencatatan yang terbatas dan kurang memanfaatkan teknologi digital. Informasi mengenai kondisi, lokasi, maupun riwayat maintenance aset sering kali tidak tersedia secara lengkap, sehingga menyulitkan pengelola dalam mengambil keputusan terkait pengadaan atau perbaikan aset.

Penyebab utama dari masalah ini adalah belum optimalnya pemanfaatan teknologi informasi dalam pengelolaan aset. RBTV, seperti banyak organisasi lain, masih mengandalkan cara tradisional untuk mencatat asetnya, padahal perkembangan teknologi digital membuka peluang besar untuk pengelolaan yang lebih interaktif dan efisien. Salah satu pendekatan yang relevan adalah penggunaan sistem informasi berbasis web dengan fitur QR Code. Teknologi ini memungkinkan identifikasi aset yang cepat dan akurat sehingga pengelola dapat menemukan informasi aset, riwayat maintenance, kondisi fisik, hingga lokasi penempatan dengan lebih mudah.

Masalah ini penting untuk diselesaikan karena pengelolaan aset yang baik berpotensi memperpanjang umur pakai peralatan, menghemat biaya pengadaan, serta meningkatkan akuntabilitas pengelolaan barang milik organisasi. Tanpa inovasi sistem, RBTV berisiko mengalami kehilangan aset yang tidak terdeteksi, keterlambatan penanganan kerusakan, dan kesulitan dalam pelaporan aset kepada manajemen.

Sebagai solusi, beberapa alternatif dapat ditawarkan. Pertama, membangun sistem informasi manajemen aset berbasis web yang menyajikan informasi detail tentang setiap aset di RBTV, meliputi kondisi, lokasi, riwayat maintenance, dan foto dokumentasi. Kedua, mengintegrasikan fitur QR Code untuk memudahkan identifikasi aset secara cepat menggunakan kamera smartphone. Ketiga, menyediakan fitur import/export massal agar pengelola lebih mudah mengelola data dalam jumlah besar. Dari berbagai alternatif tersebut, solusi yang paling tepat adalah pengembangan SimAset sebagai sistem informasi manajemen aset berbasis web yang terintegrasi dengan fitur QR Code dan audit log. Solusi ini dipilih karena lebih praktis, mudah diakses oleh pengelola, dan efektif dalam meningkatkan akuntabilitas pengelolaan aset di RBTV Bengkulu.

## 1.3 Tujuan Pengembangan Sistem

Tujuan pengembangan sistem ini dirancang secara bertahap dan berorientasi pada kebutuhan pengguna serta pengelola sistem, yaitu:

1. Menyediakan sistem informasi manajemen aset yang terpusat dan terintegrasi.
2. Menyajikan informasi aset dalam bentuk visual yang informatif melalui dashboard.
3. Meningkatkan kualitas pencatatan dan pemantauan kondisi aset barang kantor.
4. Mempermudah identifikasi aset melalui fitur QR Code yang dapat dipindai.
5. Mendukung transformasi digital pengelolaan aset di lingkungan RBTV Bengkulu.
6. Menjadi sarana pembelajaran dalam pengembangan sistem informasi manajemen aset berbasis web.

## 1.4 Ruang Lingkup Sistem

Agar pengembangan sistem tetap terarah, ruang lingkup sistem ditetapkan sebagai berikut:

1. Sistem difokuskan pada pengelolaan aset fisik barang kantor RBTV Bengkulu.
2. Sistem menyajikan data aset dalam bentuk teks, gambar, dan QR Code.
3. Sistem menyediakan modul pengelolaan data aset oleh admin dan staff.
4. Sistem mendukung akses publik terbatas untuk melihat detail aset melalui QR Code.
5. Sistem belum mencakup fitur depresiasi aset, integrasi keuangan, atau pengadaan aset.

Ruang lingkup ini disesuaikan dengan tujuan utama sistem sebagai media pencatatan dan pemantauan aset, bukan sebagai sistem layanan pengadaan atau keuangan.

## 1.5 Manfaat Sistem

Manfaat sistem ini dapat dirasakan oleh berbagai pihak, antara lain:

1. **Manfaat bagi Pengelola Aset (Admin dan Staff)**
   Pengelola dapat mencatat, memantau, dan memperbarui data aset secara mudah dan cepat melalui antarmuka web yang intuitif.

2. **Manfaat bagi Teknisi dan Tim Maintenance**
   Teknisi dapat mengidentifikasi aset dengan cepat melalui pemindaian QR Code dan mencatat riwayat maintenance secara terstruktur.

3. **Manfaat bagi Manajemen RBTV**
   Manajemen dapat memperoleh laporan kondisi aset secara real-time melalui dashboard dan laporan yang dapat dicetak kapan saja.

4. **Manfaat bagi Dunia Akademik**
   Sistem ini dapat dijadikan contoh implementasi nyata pengembangan sistem informasi manajemen aset berbasis web menggunakan Laravel.

## 1.6 Aktor Sistem (Admin dan Staff)

Aktor sistem didefinisikan untuk membatasi hak akses dan tanggung jawab dalam sistem, yaitu:

1. **Admin**
   Admin bertanggung jawab dalam mengelola seluruh data yang terdapat dalam sistem, termasuk pengelolaan akun pengguna dan pemantauan audit log. Admin memiliki akses untuk menambah, mengubah, dan menghapus data aset serta memastikan keakuratan informasi yang disajikan.

2. **Staff**
   Staff berperan sebagai pengguna operasional yang mengelola data aset sehari-hari. Staff memiliki akses ke seluruh fitur operasional (aset, barang, ruangan, QR Code, maintenance, import, export, laporan) namun tidak dapat mengakses manajemen pengguna dan audit log.

Pembagian peran ini penting untuk menjaga keamanan sistem dan keandalan data.

**Akun default yang tersedia dalam sistem:**

| Role  | Nama         | Email                    | Password  |
|-------|--------------|--------------------------|-----------|
| Admin | Admin Magang | magangrbtv@gmail.com     | Magang123 |
| Staff | Staff RBTV   | staff@rbtv.id            | Staff123  |
| Staff | reffki       | reffkip@gmail.com        | (sesuai)  |

> **[GAMBAR 1.2: Diagram aktor sistem yang menunjukkan perbedaan hak akses antara Admin dan Staff]**

## 1.7 Gambaran Umum Alur Sistem

Alur sistem dimulai dari akses pengguna ke halaman login. Pada tahap ini, baik Admin maupun Staff harus melakukan autentikasi menggunakan email dan password yang terdaftar. Setelah berhasil login, pengguna diarahkan ke halaman dashboard yang menampilkan ringkasan statistik aset.

Admin dan Staff dapat langsung mengelola data aset, barang, dan ruangan. Setiap aset yang terdaftar dapat di-generate QR Code-nya untuk kemudian dicetak dan ditempel pada fisik aset. Saat perlu mengidentifikasi aset, cukup pindai QR Code menggunakan kamera smartphone untuk melihat detail aset secara langsung.

Jika aset mengalami kerusakan, pengelola dapat menandai aset tersebut masuk ke status Maintenance. Sistem akan mengirimkan notifikasi email kepada seluruh Admin aktif. Setelah aset selesai diperbaiki, pengelola menandai maintenance selesai dan status aset kembali menjadi Aktif.

Admin harus melalui proses autentikasi sebelum mengakses fitur manajemen pengguna dan audit log. Setelah login, admin dapat mengelola akun pengguna dan memantau seluruh aktivitas yang terjadi di sistem. Setiap perubahan data akan tersimpan dalam basis data dan langsung tercermin pada tampilan sistem.

Alur ini memastikan bahwa data yang disajikan kepada pengguna selalu merupakan data terbaru yang telah diverifikasi oleh pengelola.

> **[GAMBAR 1.3: Flowchart alur kerja utama SimAset dari login hingga logout]**

## 1.8 Tujuan Modul

Modul Pendahuluan Sistem ini disusun untuk memberikan pemahaman awal mengenai SimAset yang akan dikembangkan. Tujuan dari penyusunan modul ini adalah sebagai berikut:

1. Memberikan gambaran umum mengenai konsep dan karakteristik sistem informasi manajemen aset berbasis web.
2. Menjelaskan latar belakang pengembangan sistem serta permasalahan yang melatarbelakanginya.
3. Menjabarkan tujuan pengembangan sistem secara jelas dan terstruktur.
4. Menentukan ruang lingkup dan batasan sistem agar proses pengembangan tetap terarah.
5. Mengidentifikasi aktor yang terlibat beserta peran dan hak akses masing-masing dalam sistem.
6. Memberikan gambaran umum alur kerja sistem sebagai dasar pemahaman sebelum masuk ke tahap analisis kebutuhan.

Modul ini diharapkan dapat menjadi dasar konseptual bagi pengembang dan pembaca dalam memahami sistem secara menyeluruh sebelum melanjutkan ke modul-modul berikutnya.

## 1.9 Ringkasan Modul

Modul 1 ini membahas pendahuluan SimAset, mulai dari deskripsi umum sistem, latar belakang pengembangan, tujuan dan manfaat sistem, ruang lingkup pengembangan, hingga identifikasi aktor yang terlibat dan gambaran umum alur sistem. Pembahasan pada modul ini memberikan landasan awal yang penting untuk memahami konteks, tujuan, dan batasan sistem yang dikembangkan.

Pemahaman terhadap modul ini menjadi dasar yang sangat penting sebelum melanjutkan ke Modul 2, yang akan membahas analisis kebutuhan sistem secara lebih mendalam sebagai acuan dalam proses perancangan dan implementasi sistem.
