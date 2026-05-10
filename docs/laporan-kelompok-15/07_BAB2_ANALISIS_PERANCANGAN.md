# BAB II ANALISIS KEBUTUHAN DAN PERANCANGAN

## 2.1 Analisis Kebutuhan

### 2.1.1 Proses Pengambilan Data (Requirement Gathering)

Untuk mengidentifikasi kebutuhan sistem, tim melaksanakan pengumpulan informasi dari dua sumber berbeda:

#### 1. Data Primer

**Observasi Lapangan** dilakukan di berbagai spot wisata pantai di Kota Bengkulu, termasuk Pantai Panjang, Pantai Tapak Paderi, dan Pantai Zakat. Hasil pengamatan menunjukkan bahwa banyak tempat wisata hanya dilengkapi dengan papan informasi fisik tanpa adanya media digital yang dapat diakses oleh pengunjung sebelum mereka datang.

**Wawancara Singkat** dengan pengunjung lokal dan dari luar daerah. Dari diskusi ini terungkap bahwa para wisatawan kerap mengalami kesulitan dalam memperoleh informasi mendetail mengenai lokasi, fasilitas, serta akses transportasi menuju tempat wisata.

**Diskusi** dengan pelaku usaha lokal seperti pedagang dan penyedia layanan wisata. Mereka menyatakan bahwa promosi wisata melalui platform digital masih sangat terbatas, yang mengakibatkan jumlah kunjungan wisatawan tidak stabil.

#### 2. Data Sekunder

- Laporan dan artikel dari Dinas Pariwisata Kota Bengkulu menunjukkan bahwa jumlah kunjungan wisatawan masih mengalami perubahan yang tidak tetap karena kurangnya pemasaran digital.
- Penelitian jurnal mengenai sistem informasi berbasis peta interaktif yang membuktikan bahwa teknologi tersebut efektif dalam meningkatkan akses terhadap informasi publik, seperti pada sistem informasi lokasi SPBU Pertamina di Padang yang memanfaatkan Leaflet.js.
- Sumber mengenai pengembangan aplikasi peta 3D dan Augmented Reality yang menunjukkan bahwa pariwisata berbasis digital semakin penting untuk menarik minat para pengunjung.

---

### 2.1.2 Proses Analisis Kebutuhan (Requirement Analysis)

Data yang terkumpul dianalisis dengan tujuan memahami kebutuhan utama pengguna dan nilai bisnis yang ingin dicapai. Beberapa metode yang digunakan antara lain:

- **Persona:** Dibuat tiga persona utama, yaitu *wisatawan lokal*, *wisatawan luar daerah*, dan *pengelola destinasi*. Hasilnya menunjukkan bahwa wisatawan membutuhkan informasi yang cepat, akurat, dan mudah diakses, sedangkan pengelola ingin media digital yang efektif untuk mempromosikan destinasi mereka.

- **User Journey Map:** Menggambarkan alur pengguna mulai dari mencari informasi wisata → menemukan website → melihat detail destinasi. Dari alur ini, kebutuhan utama yang muncul adalah fitur *peta interaktif* yang bisa menampilkan lokasi destinasi secara jelas.

- **Empathy Map:** Mengidentifikasi pengalaman wisatawan ketika mencari informasi destinasi. Wisatawan sering merasa "bingung" karena informasi tersebar di banyak sumber, "frustrasi" karena sulit menemukan detail destinasi, dan "butuh" platform tunggal yang menampilkan seluruh informasi penting tentang wisata pesisir.

Dari analisis tersebut, kebutuhan dengan nilai bisnis tertinggi adalah peta interaktif yang menampilkan titik destinasi dan detailnya, karena inilah yang paling berkaitan dengan masalah utama: keterbatasan informasi dan promosi digital destinasi wisata pesisir.

---

### 2.1.3 Daftar Kebutuhan

Berdasarkan hasil analisis, kebutuhan sistem dirumuskan sebagai berikut:

#### 1. Kebutuhan Fungsional

- Menampilkan daftar destinasi wisata pesisir di Kota Bengkulu.
- Menampilkan peta interaktif dengan titik lokasi destinasi.
- Menyediakan detail destinasi berupa deskripsi, foto, fasilitas, dan daya tarik utama.
- Menyediakan fitur pencarian dan filter berdasarkan kategori (misalnya pantai, budaya, kuliner).

#### 2. Kebutuhan Non-Fungsional

- Website dapat diakses melalui perangkat desktop maupun mobile.
- Antarmuka sederhana, informatif, dan ramah pengguna (user-friendly).
- Performa sistem cepat dalam menampilkan data peta dan gambar.
- Keamanan website dijaga untuk mencegah manipulasi data.

---

## 2.2 Perancangan

Berisi rancangan-rancangan solusi Capstone Project berdasarkan kebutuhan yang sudah didapatkan di sub-bab 2.1. Rancangan solusi diharapkan dibuat lengkap tidak hanya berpusat pada rancangan antarmuka saja.

### 2.2.1 Use Case Diagram

> **Gambar 2.1 Use Case Diagram**

Diagram use case menunjukkan bahwa sistem memiliki dua aktor utama, yaitu **User** dan **Admin Web**, yang masing-masing berinteraksi dengan fitur berbeda. User dapat melakukan login untuk mengakses fungsi seperti melihat peta interaktif serta melihat detail data lokasi wisata. Proses login juga mencakup kemungkinan kegagalan autentikasi. Sementara itu, Admin Web memiliki hak penuh untuk mengelola data lokasi dan destinasi peta interaktif, meliputi proses *create*, *read*, *update*, dan *delete* (CRUD). Setiap aktivitas admin seperti pengelolaan data lokasi dan destinasi peta interaktif hanya dapat diakses setelah proses login berhasil diverifikasi oleh sistem. Secara keseluruhan, diagram ini menggambarkan batasan fitur antara user biasa dan admin, serta alur dependensi antar use case melalui relasi *include* dan *extend*.

---

### 2.2.2 Activity Diagram

> **Gambar 2.2 Activity Diagram**

Gambar activity diagram pertama untuk admin menggambarkan alur aktivitas saat mengelola data lokasi. Proses dimulai ketika admin membuka halaman login dan memasukkan username serta password. Sistem kemudian melakukan verifikasi; jika gagal, admin dikembalikan ke halaman login. Jika berhasil, admin diarahkan ke halaman menu utama, lalu memilih menu manajemen data lokasi. Pada tahap ini admin dapat memilih tindakan tambah, edit, lihat, atau hapus data lokasi. Setelah tindakan dipilih, sistem menyimpan perubahan data, dan admin dapat menutup sesi dengan melakukan logout. Diagram ini menunjukkan alur kerja lengkap dalam pengelolaan data lokasi oleh admin.

> **Gambar 2.3 Activity Diagram Manajemen Destinasi**

Gambar activity diagram kedua untuk admin menjelaskan alur aktivitas dalam pengelolaan destinasi peta interaktif. Admin memulai dengan login kemudian memasukkan informasi autentikasi seperti biasa. Setelah verifikasi berhasil, admin mengakses menu utama dan memilih fitur manajemen destinasi peta interaktif. Pada tahap ini admin dapat menambah, mengedit, melihat, atau menghapus data destinasi. Setiap tindakan dikelola melalui percabangan aktivitas dan setelah selesai, sistem menyimpan data destinasi yang telah diperbarui. Admin kemudian dapat keluar dari sistem melalui proses logout. Diagram ini menekankan bahwa pengelolaan destinasi peta memiliki struktur proses serupa dengan pengelolaan data lokasi, namun berbeda pada objek data yang dikelola.

> **Gambar 2.4 User Activity Diagram Lihat Peta**

Gambar activity diagram untuk user menggambarkan alur aktivitas saat menggunakan fitur peta interaktif. User membuka sistem dan melakukan login dengan memasukkan username serta password. Setelah sistem memverifikasi, user diarahkan ke menu utama dan dapat memilih untuk melihat peta interaktif. Sistem kemudian menampilkan peta sesuai kebutuhan user dan proses selesai ketika user memutuskan untuk logout. Diagram ini menunjukkan bahwa peran user dalam sistem bersifat informatif dan tidak memiliki akses untuk mengubah data.

> **Gambar 2.5 User Activity Diagram Lihat Data Lokasi**

Gambar terakhir menggambarkan alur pengguna dalam mengakses data lokasi wisata. Seperti sebelumnya, user melakukan login dan diverifikasi oleh sistem. Jika berhasil, user masuk ke menu utama dan memilih untuk melihat data lokasi. Sistem kemudian menampilkan data lokasi yang diinginkan. Setelah selesai mengakses informasi, user dapat keluar dari sistem melalui proses logout. Diagram ini menunjukkan fokus user yang hanya pada konsumsi informasi, bukan pengelolaan data.

> **Gambar 2.6 User Activity Diagram Cari Lokasi**

Activity Diagram ini menjelaskan alur aktivitas user saat melakukan pencarian lokasi dalam sistem. User memulai proses dengan melakukan login, lalu mengisi username dan password. Sistem kemudian memverifikasi data login tersebut. Jika login gagal, user diarahkan kembali ke halaman login, namun jika berhasil user masuk ke halaman menu utama. Pada tahap ini, user memilih fitur pencarian lokasi. Sistem kemudian memproses permintaan dan menampilkan lokasi yang dicari. Setelah memperoleh informasi yang dibutuhkan, user dapat keluar dari sistem melalui fitur logout. Diagram ini menekankan proses pencarian lokasi sebagai fitur tambahan yang dapat diakses user setelah login berhasil.

---

### 2.2.3 Sequence Diagram

> **Gambar 2.7 Sequence Diagram Admin**

Sequence Diagram Admin menggambarkan alur interaksi antara aktor Admin Web, halaman Login, halaman Utama, modul Manajemen Data Lokasi, modul Manajemen Destinasi Peta Interaktif, dan Database. Proses dimulai ketika admin memasukkan username dan password, lalu sistem melakukan validasi. Setelah login berhasil, halaman utama ditampilkan dan admin dapat memilih untuk mengelola data lokasi. Aktivitas yang dilakukan mencakup *create*, *read*, *update*, dan *delete* data lokasi yang masing-masing berinteraksi dengan database untuk mengambil atau menyimpan perubahan data. Setelah selesai mengelola data lokasi, admin juga dapat mengakses modul manajemen destinasi peta interaktif yang memiliki alur serupa, yaitu *create*, *read*, *update*, dan *delete* data destinasi peta. Semua perubahan data destinasi juga disimpan di database sebelum admin mengakhiri sesi. Diagram ini menunjukkan bagaimana setiap modul berkomunikasi secara terstruktur dan bergantian sesuai kebutuhan admin.

> **Gambar 2.8 User Sequence Diagram**

Sequence Diagram User menggambarkan alur komunikasi antara user dengan berbagai komponen sistem, yaitu modul Login, Halaman Utama, Lihat Peta Interaktif, Lihat Data Lokasi, Cari dan Filter Lokasi, serta Database. Proses diawali ketika user memasukkan username dan password untuk login. Setelah validasi berhasil, sistem menampilkan halaman utama, kemudian user dapat memilih untuk melihat peta interaktif. Sistem mengambil data peta dari database dan menampilkannya kepada user. User juga dapat melihat data lokasi dengan alur serupa, yaitu sistem mengambil data dari database dan menampilkannya. Selain itu, user dapat melakukan pencarian dan filter lokasi, di mana sistem memproses kata kunci dan mengambil data yang sesuai dari database. Diagram ini menggambarkan bagaimana sistem merespons berbagai permintaan user secara berurutan dan terstruktur.

---

### 2.2.4 Class Diagram

> **Gambar 2.9 Class Diagram**

Class diagram tersebut menggambarkan struktur logis dari sistem pariwisata berbasis peta interaktif, termasuk kelas-kelas utama, atribut, fungsi, serta hubungan antar entitas. Kelas **User** berperan sebagai aktor utama yang memiliki atribut identitas seperti userID, username, password, telepon, dan email, serta method untuk login, logout, melihat peta interaktif, dan melakukan pencarian lokasi. Kelas **AdminWeb** memiliki struktur serupa, tetapi dilengkapi dengan kemampuan untuk mengelola data lokasi dan destinasi peta interaktif. Modul **Login** berfungsi sebagai penghubung proses autentikasi antara user/admin dengan sistem. Kelas **LihatPetaInteraktif** dan **LihatDataLokasi** menangani fungsi tampilan data terkait peta serta detail lokasi, sedangkan kelas **CariFilterLokasi** mengelola pencarian lokasi berdasarkan kata kunci. Selain itu, kelas **ManajemenDataLokasi** dan **ManajemenDestinasiPetaInteraktif** berfungsi untuk melakukan proses CRUD pada data wisata. Diagram ini memperlihatkan hubungan asosiasi dan kardinalitas yang menunjukkan bagaimana kelas-kelas tersebut saling bergantung dan berinteraksi dalam sistem.

---

### 2.2.5 Entity Relationship Diagram

> **Gambar 2.10 ERD**

ERD menggambarkan hubungan antara entitas Admin, User, dan Lokasi dalam sistem informasi pariwisata. Entitas Lokasi memiliki atribut seperti Id_Lokasi, Nama_Lokasi, Kategori, Deskripsi, dan Letak Lokasi (lat-long). Lokasi memiliki dua jenis hubungan yaitu: hubungan **Kelola** dengan Admin dan hubungan **Akses** dengan User. Hubungan *Kelola* menunjukkan bahwa seorang admin dapat mengelola banyak lokasi (1:m), sementara setiap lokasi dikelola oleh satu admin. Hubungan *Akses* menunjukkan bahwa user dapat mengakses banyak lokasi, dan setiap lokasi dapat diakses oleh banyak user (m:m). Entitas Admin dan User masing-masing memiliki atribut identitas seperti nama, username, password, dan kontak. Model ERD ini memberikan gambaran struktur basis data dan keterkaitan antar entitas dalam proses pengelolaan serta penyajian data lokasi wisata.

---

### 2.2.6 Data Flow Diagram

> **Gambar 2.11 Data Flow Diagram Level 0**

DFD level 0 menunjukkan gambaran umum aliran data pada sistem "Website Peta Interaktif Pariwisata Pesisir Kota Bengkulu". Sistem digambarkan sebagai satu proses besar yang berinteraksi dengan dua entitas eksternal, yaitu Admin dan User. Admin memberikan input berupa akses data user dan data pariwisata, serta menerima keluaran berupa laporan data user dan laporan data pariwisata. User memberikan input berupa permintaan akses informasi pariwisata dan menerima keluaran berupa informasi pariwisata yang ditampilkan oleh sistem. Diagram ini memperlihatkan bahwa sistem berfungsi sebagai pusat pemrosesan data yang menjembatani kebutuhan informasi antara admin dan user dalam layanan pariwisata berbasis peta interaktif.

> **Gambar 2.12 Data Flow Diagram Level 1**

Diagram DFD Level 1 merinci proses internal sistem berdasarkan konteks diagram sebelumnya menjadi tiga proses utama. **Proses 1.0** Mencari Informasi Pariwisata menangani permintaan user terhadap informasi pariwisata dan mengambil data dari penyimpanan data pariwisata untuk kemudian dikembalikan kepada user. **Proses 2.0** Laporan Data User memungkinkan admin membuat laporan data user dengan mengambil informasi dari penyimpanan data user. Selanjutnya, **Proses 3.0** Laporan Data Pariwisata digunakan admin untuk menghasilkan laporan data pariwisata, memanfaatkan data yang tersimpan pada basis data pariwisata. Diagram ini memperjelas bagaimana data mengalir dalam sistem untuk memenuhi kebutuhan baik dari sisi user maupun admin.

---

### 2.2.7 User Interface (Prototype)

> **Gambar 2.13 Prototype Dashboard/Peta Interaktif User**

Gambar pertama menampilkan halaman beranda dari website peta interaktif pariwisata Kota Bengkulu. Pada halaman ini pengguna disambut dengan teks selamat datang serta visualisasi peta interaktif yang menampilkan lokasi-lokasi penting seperti hotel, pantai, mall, dan titik wisata lainnya. Navigasi utama berada di bagian atas dengan menu Beranda, Data Pariwisata, Tentang, Kontak, serta tombol Login. Peta yang ditampilkan dapat digunakan untuk menjelajahi wilayah pesisir Kota Bengkulu secara langsung. Halaman ini berfungsi sebagai pintu masuk utama bagi pengguna untuk memahami gambaran umum lokasi pariwisata sebelum menggunakan fitur lainnya.

> **Gambar 2.14 Prototype Halaman Login**

Gambar kedua menunjukkan halaman login yang digunakan oleh user maupun admin untuk mengakses fitur yang membutuhkan autentikasi. Tampilan terdiri dari form email dan kata sandi, serta tombol Login di bagian tengah halaman. Desainnya dibuat sederhana dan fokus agar pengguna mudah memasukkan informasi akun. Selain itu, terdapat pilihan "Daftar" bagi pengguna baru yang belum memiliki akun. Halaman ini berperan penting sebagai mekanisme keamanan untuk memastikan hanya pengguna yang terdaftar yang dapat mengakses fitur lanjutan seperti pengelolaan data atau melihat detail informasi tertentu.

> **Gambar 2.15 Halaman Data Pengguna**

Gambar ketiga merupakan tampilan halaman Data Pengguna yang hanya dapat diakses oleh admin. Dalam halaman ini, admin dapat melihat daftar pengguna yang terdaftar dalam sistem. Tabel menampilkan informasi berupa latitude, longitude, dan nama lokasi terkait aktivitas pengguna. Pada bagian kanan terdapat kolom aksi dengan tombol edit berwarna hijau dan tombol hapus berwarna merah untuk memudahkan admin melakukan pengelolaan data. Tersedia juga tombol "Tambah Pengguna" untuk menambahkan data baru. Halaman ini memudahkan admin dalam memonitor, memperbarui, serta menghapus data pengguna yang terkait dengan aktivitas dalam sistem.

> **Gambar 2.16 Halaman Data Pariwisata**

Gambar keempat menampilkan halaman Data Lokasi Pariwisata Pesisir Kota Bengkulu. Halaman ini digunakan untuk menampilkan dan mengelola informasi titik-titik lokasi wisata seperti latitude, longitude, dan nama lokasi. Admin dapat mencari lokasi tertentu melalui kolom pencarian yang tersedia dan melakukan tindakan edit atau hapus pada setiap baris data melalui tombol aksi yang disediakan. Selain itu, terdapat tombol "Tambah Pariwisata" untuk menambahkan lokasi wisata baru ke dalam sistem. Halaman ini berfungsi untuk mempermudah proses pemutakhiran data lokasi sehingga informasi pariwisata yang ditampilkan pada peta interaktif selalu akurat dan terbaru.
