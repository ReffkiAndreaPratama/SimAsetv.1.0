# BAB III IMPLEMENTASI CAPSTONE PROJECT

## 3.1 Tahapan dan Realisasi Capstone Project

### 3.1.1 Tahapan Capstone Project

Pelaksanaan Capstone Project ini dilakukan melalui serangkaian tahapan yang sistematis untuk memastikan proses pengembangan Website Pariwisata Berbasis Peta Interaktif berlangsung secara terstruktur dan sesuai dengan kebutuhan pengguna. Setiap tahapan dirancang agar saling berkesinambungan sehingga sistem yang dikembangkan mampu memberikan solusi efektif dalam penyediaan dan promosi informasi destinasi wisata pesisir dan laut di Kota Bengkulu.

Model pengembangan sistem yang digunakan mengacu pada kerangka kerja Software Development Life Cycle (SDLC) dengan pendekatan Waterfall. Metode ini dipilih karena memiliki alur kerja yang terencana dan berurutan, dimulai dari tahap analisis kebutuhan hingga dokumentasi akhir. Pendekatan ini dinilai sesuai untuk pengembangan sistem informasi berbasis web yang memiliki ruang lingkup dan kebutuhan yang jelas sejak awal.

> **Gambar 3.1 Tahapan Capstone Project**

Adapun tahapan pengembangan yang dilaksanakan meliputi langkah-langkah sebagai berikut:

#### 1. Analisis Kebutuhan (Requirement Analysis)

Tahap analisis kebutuhan bertujuan untuk mengidentifikasi kebutuhan pengguna dan kebutuhan sistem yang akan dikembangkan. Pada tahap ini dilakukan pengumpulan data melalui observasi terhadap media informasi pariwisata yang telah ada serta studi literatur terkait sistem informasi pariwisata dan pemanfaatan peta interaktif. Selain itu, dilakukan pula pengumpulan data mengenai destinasi wisata pesisir dan laut di Kota Bengkulu, termasuk lokasi, fasilitas, dan informasi pendukung lainnya.

Hasil dari tahap analisis ini adalah perumusan kebutuhan fungsional dan nonfungsional sistem. Kebutuhan fungsional mencakup fitur pencarian destinasi, tampilan peta interaktif, penayangan detail informasi destinasi, serta pengelolaan data destinasi oleh admin. Sementara itu, kebutuhan nonfungsional meliputi aspek kemudahan penggunaan, performa sistem, keamanan data, dan kompatibilitas sistem pada berbagai perangkat.

#### 2. Perancangan Sistem (System Design)

Tahap perancangan sistem merupakan proses penerjemahan hasil analisis kebutuhan ke dalam bentuk rancangan teknis sistem. Pada tahap ini dilakukan pemodelan sistem menggunakan Unified Modeling Language (UML) yang meliputi Use Case Diagram, Activity Diagram, Sequence Diagram, serta Entity Relationship Diagram (ERD) untuk menggambarkan struktur basis data.

Selain perancangan proses dan basis data, dilakukan pula perancangan antarmuka pengguna (User Interface) untuk memastikan sistem mudah dipahami dan digunakan oleh pengguna. Rancangan antarmuka mencakup tampilan halaman utama, peta interaktif, halaman detail destinasi, serta dashboard admin untuk pengelolaan data destinasi wisata.

#### 3. Implementasi Sistem (Implementation)

Tahap implementasi merupakan proses realisasi rancangan sistem ke dalam bentuk perangkat lunak yang berfungsi. Sistem dikembangkan sebagai aplikasi berbasis web dengan menggunakan framework **Laravel** sebagai backend, basis data **MySQL**, serta **Leaflet.js** sebagai library peta interaktif.

Pada tahap ini dilakukan pengembangan fitur-fitur utama sistem, antara lain pengelolaan data destinasi wisata, integrasi peta interaktif dengan marker lokasi, pencarian destinasi, serta dashboard admin. Seluruh komponen sistem diintegrasikan secara bertahap agar dapat berjalan secara terpadu dan sesuai dengan rancangan yang telah ditetapkan sebelumnya.

#### 4. Pengujian Sistem (Testing)

Tahap pengujian sistem dilakukan untuk memastikan bahwa seluruh fitur sistem berfungsi dengan baik dan sesuai dengan kebutuhan pengguna. Pengujian dilakukan menggunakan pendekatan **Black Box Testing**, di mana fokus pengujian diarahkan pada kesesuaian antara input yang diberikan pengguna dengan output yang dihasilkan oleh sistem, tanpa memperhatikan struktur kode program.

Pengujian mencakup pengujian fungsi pencarian destinasi, interaksi dengan peta interaktif, tampilan detail destinasi, serta pengelolaan data oleh admin. Hasil pengujian digunakan untuk menilai keandalan, efisiensi, dan ketepatan fungsi sistem sebelum digunakan lebih lanjut.

#### 5. Evaluasi dan Penyempurnaan (Evaluation)

Tahap evaluasi dan penyempurnaan dilakukan berdasarkan hasil pengujian sistem dan umpan balik dari pengguna. Pada tahap ini dilakukan penilaian terhadap kemudahan penggunaan sistem, kejelasan informasi yang ditampilkan, serta performa sistem secara keseluruhan.

Masukan yang diperoleh dari proses evaluasi digunakan sebagai dasar untuk melakukan perbaikan dan penyempurnaan sistem, baik dari sisi fungsionalitas maupun tampilan antarmuka. Tujuan dari tahap ini adalah memastikan sistem yang dikembangkan benar-benar sesuai dengan kebutuhan pengguna dan siap digunakan sebagai media informasi pariwisata.

#### 6. Dokumentasi dan Laporan Akhir (Documentation)

Tahap terakhir merupakan proses penyusunan dokumentasi dan laporan akhir Capstone Project. Dokumentasi yang disusun mencakup seluruh tahapan pengembangan sistem, mulai dari analisis kebutuhan, perancangan sistem, implementasi, pengujian, hingga evaluasi.

Dokumentasi ini disajikan dalam bentuk laporan Capstone Project sebagai bentuk pertanggungjawaban akademik, serta dilengkapi dengan diagram sistem, tangkapan layar (screenshot) aplikasi, dan penjelasan teknis sistem yang dikembangkan.

---

### 3.1.2 Realisasi Tahapan Capstone Project

| No | Tahapan Capstone Project | Realisasi Pelaksanaan |
|----|--------------------------|----------------------|
| 1 | Analisis Kebutuhan (Requirement Analysis) | Tim Capstone Project melakukan pengumpulan data destinasi wisata pesisir dan laut di Kota Bengkulu melalui studi literatur dan observasi sumber informasi pariwisata. Data yang dikumpulkan meliputi lokasi destinasi, fasilitas, deskripsi wisata, serta kebutuhan pengguna. Hasil analisis digunakan untuk menyusun kebutuhan fungsional dan nonfungsional sebagai dasar perancangan sistem. |
| 2 | Perancangan Sistem (System Design) | Perancangan sistem dilakukan menggunakan pemodelan UML, meliputi Use Case Diagram, Activity Diagram, Sequence Diagram, dan ERD. Selain itu, rancangan antarmuka pengguna untuk pengguna umum dan admin juga disusun. Seluruh rancangan telah melalui proses konsultasi dan perbaikan sehingga menghasilkan desain sistem yang lebih terstruktur dan mudah digunakan. |
| 3 | Implementasi Sistem (Implementation) | Sistem diimplementasikan sesuai dengan rancangan yang telah dibuat. Fitur utama seperti pengelolaan data destinasi, pencarian destinasi, peta interaktif dengan marker lokasi, serta dashboard admin berhasil diintegrasikan dengan basis data dan berjalan dengan baik. Implementasi dilakukan secara bertahap hingga membentuk sistem yang terintegrasi. |
| 4 | Pengujian Sistem (Testing) | Pengujian sistem dilakukan pada seluruh fitur utama menggunakan skenario pengujian fungsional. Hasil pengujian menunjukkan bahwa sistem berjalan sesuai dengan yang diharapkan. Beberapa kendala minor seperti tampilan pada perangkat mobile dan validasi input ditemukan, namun telah diperbaiki untuk meningkatkan kinerja sistem. |
| 5 | Evaluasi dan Penyempurnaan (Evaluation) | Evaluasi dilakukan berdasarkan hasil pengujian dan masukan pengguna. Penyempurnaan meliputi perbaikan tampilan antarmuka, penyesuaian alur pencarian destinasi, serta peningkatan kejelasan informasi pada halaman detail destinasi guna meningkatkan kenyamanan pengguna. |
| 6 | Dokumentasi dan Laporan Akhir (Documentation) | Dokumentasi pengembangan sistem disusun secara sistematis dalam laporan Capstone Project. Diagram sistem, ERD, serta tangkapan layar aplikasi dilampirkan sebagai pendukung agar sistem mudah dipahami oleh pihak akademik dan pengguna. |

---

## 3.2 Timeline Capstone Project

Pelaksanaan Capstone Project Website Pariwisata Berbasis Peta Interaktif untuk Promosi Destinasi Pesisir dan Laut Kota Bengkulu direncanakan dan direalisasikan dalam jangka waktu satu semester. Penyusunan timeline dilakukan dengan membagi aktivitas proyek ke dalam beberapa tahapan pengembangan sistem yang mengacu pada metode Waterfall, yaitu analisis kebutuhan, perancangan sistem, implementasi, pengujian, evaluasi, serta dokumentasi dan penyusunan laporan.

Timeline ini disusun untuk memastikan setiap tahapan pengembangan sistem dapat berjalan secara terstruktur, terjadwal, dan mudah dipantau baik dari sisi perencanaan maupun realisasi pelaksanaan. Setiap aktivitas memiliki bobot tertentu yang menunjukkan tingkat kontribusi terhadap keseluruhan proyek, serta penanggung jawab yang ditetapkan sesuai dengan pembagian tugas dalam tim Capstone Project.

Visualisasi timeline Capstone Project disajikan dalam bentuk tabel Gantt Chart yang menggambarkan distribusi aktivitas pada setiap minggu selama periode pelaksanaan. Selain itu, timeline juga dilengkapi dengan kurva S yang digunakan untuk menunjukkan perkembangan persentase progres proyek dari waktu ke waktu. Kurva S ini memberikan gambaran ketercapaian proyek secara kumulatif, sehingga memudahkan dalam memantau kesesuaian antara rencana dan realisasi pekerjaan.

Berdasarkan timeline dan kurva S yang disajikan, dapat dilihat bahwa progres Capstone Project mengalami peningkatan secara bertahap seiring dengan selesainya setiap tahapan pengembangan sistem. Hal ini menunjukkan bahwa pelaksanaan proyek dilakukan secara sistematis dan terkontrol sesuai dengan rencana yang telah ditetapkan sejak awal.

**Tabel 3.1 Timeline Capstone Project dengan Kurva S**

| NO | Aktivitas | Penanggung Jawab | Bobot | Bulan 1 M1 | Bulan 1 M2 | Bulan 1 M3 | Bulan 1 M4 | Bulan 2 M1 | Bulan 2 M2 | Bulan 2 M3 | Bulan 2 M4 | Bulan 3 M1 | Bulan 3 M2 | Bulan 3 M3 | Bulan 3 M4 |
|----|-----------|-----------------|-------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| I | Analisis Kebutuhan | Dzakki & Reffki | 15 | 7.5 | 7.5 | | | | | | | | | | |
| II | Perencanaan Sistem | Aulia & Dzakki | 20 | | | 10 | 10 | | | | | | | | |
| III | Implementasi Sistem | Seluruh Tim | 30 | | | | | 7.5 | 7.5 | 7.5 | 7.5 | | | | |
| IV | Pengujian Sistem | Aulia & Reffki | 15 | | | | | | | | | 7.5 | 7.5 | | |
| V | Evaluasi | Seluruh Tim | 10 | | | | | | | | | | | 5 | 5 |
| VI | Dokumentasi & Laporan | Seluruh Tim | 10 | | | | | | | | | | | | 10 |
| | **Total** | | **100** | | | | | | | | | | | | |
| | Progres Mingguan | | | 7.5 | 7.5 | 10 | 10 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 | 5 | 15 |
| | Progres Kumulatif | | | 7.5 | 15 | 25 | 35 | 42.5 | 50 | 57.5 | 65 | 72.5 | 80 | 85 | 100 |

---

## 3.3 Hasil Capstone Project

Hasil pengembangan Website Pariwisata Berbasis Peta Interaktif menunjukkan bahwa sistem telah berhasil menyediakan fitur utama yang mendukung penyajian informasi destinasi wisata pesisir secara lebih informatif, interaktif, dan mudah diakses oleh masyarakat. Seluruh komponen sistem telah diimplementasikan dalam bentuk antarmuka pengguna (user interface), peta interaktif, tabel data, serta modul manajemen yang membantu admin dalam mengelola konten wisata. Website ini dirancang untuk meningkatkan promosi wisata Kota Bengkulu melalui visualisasi lokasi berbasis peta, kemudahan akses informasi, serta pengelolaan destinasi yang efisien oleh pihak Dinas Pariwisata.

### 3.3.1 Halaman Utama

> **Gambar 3.3.1 Halaman Utama**

Dashboard Pengguna merupakan tampilan awal ketika pengguna mengakses website. Halaman ini menampilkan pesan sambutan serta tombol navigasi cepat menuju halaman Peta Interaktif dan Daftar Destinasi. Ilustrasi visual yang digunakan memberikan kesan dinamis dan modern, membuat pengguna merasa nyaman saat pertama kali mengakses sistem. Tujuannya adalah memberikan orientasi cepat dan jelas kepada pengguna mengenai fitur utama yang tersedia dalam website.

### 3.3.2 Halaman Daftar Pengguna

> **Gambar 3.3.2 Halaman Daftar Pengguna**

Halaman daftar atau *Sign Up* merupakan fitur yang digunakan oleh pengguna baru untuk membuat akun sebelum mengakses layanan tertentu pada Website Peta Interaktif Wisata Pesisir Kota Bengkulu. Pada halaman ini, pengguna diminta mengisi beberapa data dasar seperti Nama Lengkap, Email, Password, dan Konfirmasi Password. Sistem juga telah dilengkapi dengan validasi form untuk memastikan bahwa email dan password yang dimasukkan sesuai format dan cocok satu sama lain sebelum akun dapat dibuat. Dengan adanya halaman ini, proses registrasi pengguna menjadi lebih aman, terstruktur, serta memastikan bahwa setiap interaksi dalam sistem dapat dicatat sesuai identitas pengguna yang valid.

### 3.3.3 Halaman Login Pengguna

> **Gambar 3.3.3 Halaman Login Pengguna**

Halaman Login Akun merupakan titik masuk utama bagi pengguna untuk mengakses fitur-fitur di dalam sistem. Pengguna diminta memasukkan email dan password yang telah terdaftar untuk dapat melakukan login. Desain halaman dibuat minimalis, bersih, dan responsif, sehingga mudah dipahami oleh pengunjung dari berbagai kalangan. Elemen seperti tombol "Ingat Saya" dan "Lupa Password?" disediakan untuk meningkatkan kenyamanan dan fleksibilitas dalam proses autentikasi. Tampilan ini memastikan bahwa hanya pengguna yang terverifikasi yang dapat mengakses fitur seperti pemberian rating dan komentar pada destinasi.

### 3.3.4 Peta Interaktif

> **Gambar 3.3.4 Peta Interaktif**

Peta interaktif merupakan fitur inti dari sistem, yang memberikan visualisasi lokasi destinasi wisata pesisir di Kota Bengkulu. Pengguna dapat menelusuri lokasi wisata melalui marker yang muncul pada peta, lalu mengklik marker tersebut untuk melihat informasi singkat destinasi seperti nama, kategori, dan deskripsi awal. Fitur-fitur navigasi seperti Fit, Fokus, Refresh, dan Fullscreen disediakan untuk membantu pengguna menjelajahi peta dengan lebih nyaman. Dengan adanya peta ini, wisatawan dapat memahami posisi geografis destinasi dengan lebih jelas serta mendapatkan gambaran nyata sebelum berkunjung.

### 3.3.5 Halaman Destinasi

> **Gambar 3.3.5 Halaman Destinasi**

Halaman Destinasi merupakan fitur utama pada Website Peta Interaktif Wisata Pesisir Kota Bengkulu yang menampilkan daftar destinasi wisata pesisir yang telah diinput oleh admin. Pada halaman ini, pengguna dapat melihat informasi awal mengenai setiap destinasi, seperti nama tempat, gambar, rating, dan keterangan singkat. Setiap destinasi ditampilkan dalam bentuk card yang memuat tombol "Lihat Detail", yang memungkinkan pengguna mengakses informasi lebih lengkap seperti deskripsi destinasi, lokasi, fasilitas, dan ulasan. Halaman ini berfungsi sebagai pintu masuk utama bagi pengguna untuk menjelajahi berbagai destinasi wisata yang ada di Kota Bengkulu, sekaligus memberikan gambaran awal mengenai daya tarik wisata yang tersedia secara jelas, informatif, dan mudah diakses.

### 3.3.6 Halaman About Us

> **Gambar 3.3.6 Halaman About Us**

Halaman About Us menampilkan informasi mengenai Dinas Pariwisata Kota Bengkulu sebagai pengelola website, termasuk visi, misi, dan tujuan pengembangan platform pariwisata digital ini.

### 3.3.7 Dashboard Admin

> **Gambar 3.3.7 Dashboard Admin**

Halaman Dashboard Admin berfungsi sebagai pusat kontrol bagi pengelola dari Dinas Pariwisata. Pada bagian ini ditampilkan ringkasan statistik penting seperti jumlah destinasi wisata, jumlah pengguna terdaftar, total review, dan admin aktif. Selain itu, terdapat daftar aktivitas terbaru yang menampilkan proses penambahan pengguna maupun destinasi. Dashboard ini dirancang untuk memberikan gambaran cepat kepada admin mengenai kondisi sistem secara keseluruhan, sehingga memudahkan monitoring dan pengambilan keputusan dalam pengelolaan data wisata.

### 3.3.8 Halaman Kelola Destinasi

> **Gambar 3.3.8 Halaman Kelola Destinasi**

Halaman Kelola Destinasi digunakan admin untuk menambahkan, mengubah, dan menghapus data destinasi wisata. Admin dapat menambahkan nama destinasi, kategori (pantai, alam, kuliner, sejarah), deskripsi, koordinat latitude-longitude, serta gambar destinasi. Di bagian bawah, daftar destinasi yang sudah tersimpan ditampilkan dalam tabel untuk memudahkan pemantauan. Fitur ini mempermudah proses pembaruan data wisata sehingga informasi yang ditampilkan kepada pengguna selalu terkini dan relevan.

### 3.3.9 Halaman Kelola Pengguna

> **Gambar 3.3.9 Halaman Kelola Pengguna**

Halaman ini dirancang bagi admin untuk mengelola seluruh akun pengguna dalam sistem. Admin dapat menambah pengguna baru dengan mengisi nama, email, password, dan role (Admin/User). Selain itu, daftar pengguna yang sudah terdaftar ditampilkan dalam bentuk kartu yang berisi informasi dasar pengguna, serta tombol Edit dan Hapus untuk memudahkan pengelolaan. Fitur ini memastikan bahwa kontrol akses sistem dapat dilakukan dengan baik sesuai kebutuhan operasional.

### 3.3.10 Peta Interaktif Admin

> **Gambar 3.3.10 Peta Interaktif Admin**

Halaman ini memungkinkan admin melihat langsung posisi marker destinasi pada peta dalam mode pengelolaan. Admin dapat memastikan bahwa koordinat yang diinputkan sudah benar serta marker muncul di lokasi yang sesuai. Tampilan ini juga memberikan kemudahan dalam melakukan pengecekan visual tanpa harus masuk ke tampilan publik. Dengan fitur tambahan seperti zoom, fullscreen, dan fokus, admin dapat memvalidasi lokasi destinasi secara lebih efisien dan akurat.

---

## 3.4 Pengujian Hasil Capstone Project

### 3.4.1 Analisis Metode Pengujian Hasil

Teknik analisis data yang digunakan dalam penelitian ini adalah analisis deskriptif kuantitatif. Data diperoleh melalui kuesioner menggunakan skala Likert lima poin, yang memungkinkan peneliti untuk mengukur persepsi, pengalaman, dan tingkat kepuasan pengguna terhadap sistem secara objektif. Penggunaan skala Likert lima poin dipilih karena terbukti efektif dalam penelitian modern yang menilai kualitas dan usability aplikasi digital. Dalam penelitian Fajaria & Tania (2023) menunjukkan bahwa instrumen penilaian berbasis skala Likert dan SUS (System Usability Scale) sangat relevan untuk mengevaluasi sistem informasi berbasis web, terutama dalam menilai kemudahan penggunaan, kejelasan tampilan, serta fungsi sistem secara keseluruhan. Temuan ini memperkuat dasar metodologis bahwa kuesioner Likert merupakan teknik yang valid dan reliabel untuk analisis kelayakan sistem digital.

Skor penilaian yang digunakan terdiri dari kategori Sangat Setuju (SS) hingga Sangat Tidak Setuju (STS) dengan rentang nilai 1-5.

**Tabel 3.4.1 Kategori Skor Penilaian**

| Jawaban | Skor |
|---------|------|
| Sangat Setuju (SS) | 5 |
| Setuju (S) | 4 |
| Ragu-ragu (Rr) | 3 |
| Tidak Setuju (TS) | 2 |
| Sangat Tidak Setuju (STS) | 1 |

Data hasil kuesioner kemudian dianalisis menggunakan rumus rata-rata:

`
x̄ = Σx / n
`

Keterangan:
- x̄ = rata-rata skor
- Σx = total skor jawaban
- n = jumlah responden

Untuk menginterpretasikan tingkat kelayakan sistem, digunakan kategori interval berdasarkan skala Likert lima poin. Penentuan interval ini mengacu pada Widyastuti (2022).

**Tabel 3.4.2 Kategori Interval Skala Likert**

| Rentang Nilai | Kategori |
|---------------|----------|
| 4,01 – 5,00 | Sangat Layak |
| 3,01 – 4,00 | Layak |
| 2,01 – 3,00 | Kurang Layak |
| 1,00 – 2,00 | Tidak Layak |

---

### 3.4.2 Data Pengujian Dengan Kuesioner

#### 1. User (Public)

Pengujian sistem dilakukan melalui penyebaran kuesioner kepada pengguna publik dengan tujuan untuk mengetahui tingkat kelayakan, kemudahan penggunaan, serta efektivitas Website Pariwisata Berbasis Peta Interaktif untuk Promosi Destinasi Pesisir dan Laut Kota Bengkulu. Responden pada pengujian ini terdiri dari **12 orang pengguna**, yang berasal dari kalangan mahasiswa dan masyarakat umum yang berpotensi atau memiliki minat terhadap pariwisata daerah.

Kuesioner disusun berdasarkan empat jenis pengujian, yaitu Unit Testing, Functional Testing, Accuracy Testing, dan Usability Testing, yang masing-masing dirancang untuk menilai aspek penggunaan yang berbeda.

**Tabel 3.4.3 Data User Responden**

| Waktu | Nama | Status | Jenis Kelamin | Usia | Asal | Perangkat | Browser |
|-------|------|--------|--------------|------|------|-----------|---------|
| 11/12/2025 00:05 | Fernando Torres | Masyarakat Umum | Laki-laki | < 20 Tahun | Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 12:37 | Angelika Simanjuntak | Mahasiswa | Perempuan | 20-25 Tahun | Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 12:40 | Fauziah Syafitri | Mahasiswa | Perempuan | 20-25 Tahun | Luar Kota Bengkulu | Laptop/PC | Microsoft Edge |
| 11/12/2025 12:50 | Ajs Saputra Hidayah | Mahasiswa | Laki-laki | 20-25 Tahun | Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 12:57 | Ehrizal Dwi Sapustra | Mahasiswa | Laki-laki | 20-25 Tahun | Luar Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 13:03 | Hanifa Wulandari | Mahasiswa | Perempuan | 20-25 Tahun | Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 13:06 | Anisah Labilbah | Mahasiswa | Perempuan | < 20 Tahun | Kota Bengkulu | Laptop/PC | Microsoft Edge |
| 11/12/2025 13:10 | Ahmad Ali | Masyarakat Umum | Laki-laki | 26-30 Tahun | Luar Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 13:20 | Patrialis Akbar | Mahasiswa | Laki-laki | 20-25 Tahun | Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 13:35 | Anisa Iaye Fadila | Mahasiswa | Perempuan | 20-25 Tahun | Luar Kota Bengkulu | Smartphone | Google Chrome |
| 11/12/2025 13:57 | Dila | Mahasiswa | Perempuan | 20-25 Tahun | Kota Bengkulu | Smartphone | Safari |
| 11/12/2025 14:01 | Perdian Pebri Teriyadi | Mahasiswa | Laki-laki | 20-25 Tahun | Kota Bengkulu | Smartphone | Google Chrome |

**Tabel 3.4.4 Unit Testing User**

| Unit Testing | Rata-rata Skor |
|-------------|---------------|
| "Website mudah dipahami saat pertama kali digunakan." | 4.6 |
| "Navigasi menu mudah digunakan dan tidak membingungkan." | 4.7 |
| "Saya dapat menemukan informasi destinasi dengan mudah." | 4.7 |
| "Website berjalan lancar tanpa error saat berpindah halaman." | 4.5 |
| "Informasi awal pada website muncul dengan benar." | 4.6 |
| **Jumlah** | **23.1** |
| **Rata-rata Poin** | **4.62** |
| **Kriteria** | **Sangat Layak** |

Berdasarkan hasil Unit Testing, rata-rata skor sebesar **4.62** menunjukkan bahwa website dinilai sangat layak dari sisi penggunaan dasar. Pengguna merasa bahwa website mudah dipahami, navigasi dapat digunakan tanpa kendala, informasi mudah ditemukan, dan halaman dapat diakses tanpa gangguan error.

**Tabel 3.4.5 Functional Testing User**

| Functional Testing | Rata-rata Skor |
|-------------------|---------------|
| "Peta interaktif pada website mudah dipahami dan digunakan." | 4.7 |
| "Marker lokasi destinasi wisata mudah dikenali dan diklik." | 4.6 |
| "Informasi yang muncul saat marker diklik jelas dan informatif." | 4.7 |
| "Website membantu saya mengetahui lokasi destinasi dengan cepat." | 4.6 |
| "Peta interaktif bekerja sesuai fungsi tanpa kendala." | 4.8 |
| **Jumlah** | **23.4** |
| **Rata-rata Poin** | **4.68** |
| **Kriteria** | **Sangat Layak** |

Rata-rata skor **4.68** menunjukkan bahwa fitur peta interaktif bekerja dengan sangat baik. Pengguna dapat mengakses marker dengan mudah, memahami informasi destinasi, serta menemukan lokasi wisata secara cepat.

**Tabel 3.4.6 Accuracy Testing User**

| Accuracy Testing | Rata-rata Skor |
|-----------------|---------------|
| "Informasi destinasi wisata yang ditampilkan lengkap dan jelas." | 4.6 |
| "Deskripsi, lokasi, dan fasilitas destinasi mudah dipahami." | 4.7 |
| "Informasi sesuai dengan kebutuhan saya sebagai pengguna." | 4.6 |
| "Marker pada peta menunjukkan lokasi destinasi dengan tepat." | 4.5 |
| "Informasi yang muncul akurat dan konsisten." | 4.6 |
| **Jumlah** | **23.0** |
| **Rata-rata Poin** | **4.60** |
| **Kriteria** | **Sangat Layak** |

Dengan skor rata-rata **4.60**, pengguna menilai bahwa informasi wisata yang disajikan oleh website telah akurat, lengkap, dan sesuai dengan kondisi di lapangan.

**Tabel 3.4.7 Usability Testing User**

| Usability Testing | Rata-rata Skor |
|------------------|---------------|
| "Tampilan website mudah dimengerti." | 4.5 |
| "Menu seperti Beranda dan Destinasi mudah ditemukan." | 4.6 |
| "Website membantu saya mencari informasi lebih efisien." | 4.7 |
| "Saya merasa nyaman menggunakan website ini." | 4.6 |
| "Secara keseluruhan website mudah digunakan." | 4.7 |
| **Jumlah** | **23.1** |
| **Rata-rata Poin** | **4.62** |
| **Kriteria** | **Sangat Layak** |

Rata-rata skor **4.62** menunjukkan bahwa pengguna merasa website sangat mudah digunakan. Tampilan dinilai jelas, navigasi tidak membingungkan, dan website memberikan pengalaman penggunaan yang cepat, nyaman, dan responsif.

**Tabel 3.4.8 Rekapitulasi Hasil Testing User**

| Jenis Testing | Rata-rata Skor |
|--------------|---------------|
| Unit Testing | 4.62 |
| Functional Testing | 4.68 |
| Accuracy Testing | 4.60 |
| Usability Testing | 4.62 |
| **Jumlah** | **18.52** |
| **Rata-rata Hasil** | **4.63** |
| **Kriteria Hasil** | **Sangat Layak** |

Secara keseluruhan, hasil pengujian terhadap 12 responden menunjukkan bahwa Website Pariwisata Berbasis Peta Interaktif Kota Bengkulu dinilai **sangat layak** untuk digunakan. Rata-rata skor keseluruhan sebesar **4.63** mengindikasikan bahwa website memiliki performa yang sangat baik, baik dari sisi fungsi dasar, fitur peta interaktif, ketepatan informasi, maupun pengalaman penggunaan.

---

#### 2. Petugas/Admin

Responden dalam pengujian ini adalah Admin Website Pariwisata Kota Bengkulu, yaitu pihak yang bertanggung jawab dalam proses pengelolaan data destinasi wisata, verifikasi informasi, dan pemeliharaan konten pada sistem. Sebagai admin yang berinteraksi langsung dengan dashboard pengelolaan, responden memiliki pemahaman yang baik mengenai alur kerja sistem sehingga penilaiannya dapat menjadi acuan yang valid untuk menilai performa fitur admin.

**Tabel 3.4.9 Unit Testing Petugas/Admin**

| Unit Testing | Skor |
|-------------|------|
| Sistem berhasil menyimpan data destinasi setiap kali saya menekan tombol "Tambah Destinasi". | 4 |
| Fitur Edit pada data destinasi selalu memperbarui informasi dengan benar. | 5 |
| Fungsi Delete menghapus data destinasi tanpa menyebabkan error pada data lainnya. | 5 |
| Upload foto destinasi berhasil dan gambar tampil dengan benar pada halaman destinasi. | 4 |
| Sistem berhasil memvalidasi input dan menampilkan pesan error saat form tidak lengkap. | 4 |
| **Jumlah** | **22** |
| **Rata-rata** | **4.4** |
| **Kriteria** | **Sangat Layak** |

**Tabel 3.4.10 Functional Testing Petugas/Admin**

| Functional Testing | Skor |
|-------------------|------|
| Fitur manajemen data destinasi berjalan sesuai fungsi (Tambah/Edit/Hapus). | 4 |
| Sistem menampilkan daftar destinasi sesuai urutan penginputan admin. | 5 |
| Fitur upload foto destinasi berfungsi sesuai alur kerja yang diharapkan. | 4 |
| Informasi destinasi langsung diperbarui pada tampilan publik setelah admin melakukan perubahan. | 5 |
| Sistem dapat menampilkan detail destinasi dengan benar setelah admin menginput data. | 5 |
| **Jumlah** | **23** |
| **Rata-rata** | **4.6** |
| **Kriteria** | **Sangat Layak** |

**Tabel 3.4.11 Accuracy Testing Petugas/Admin**

| Accuracy Testing | Skor |
|-----------------|------|
| Informasi destinasi yang ditampilkan sesuai dengan data yang saya inputkan. | 4 |
| Marker pada peta menunjukkan lokasi destinasi dengan akurat. | 5 |
| Perubahan data pada dashboard langsung diperbarui dengan benar pada tampilan peta. | 5 |
| Foto destinasi ditampilkan dengan ukuran dan kualitas yang sesuai. | 4 |
| Deskripsi destinasi tampil lengkap dan tidak terjadi kesalahan pemanggilan data. | 4 |
| **Jumlah** | **22** |
| **Rata-rata** | **4.4** |
| **Kriteria** | **Sangat Layak** |

**Tabel 3.4.12 Usability Testing Petugas/Admin**

| Usability Testing | Skor |
|------------------|------|
| Tampilan halaman admin mudah dipahami untuk pengelolaan data destinasi. | 5 |
| Alur kerja mulai dari input, edit, hingga publikasi destinasi mudah diikuti. | 4 |
| Tombol dan menu penting (Tambah, Edit, Hapus, Upload Foto) mudah ditemukan. | 5 |
| Proses pengelolaan data destinasi terasa cepat dan efisien. | 5 |
| Secara keseluruhan, dashboard admin nyaman digunakan untuk operasional harian. | 5 |
| **Jumlah** | **24** |
| **Rata-rata** | **4.8** |
| **Kriteria** | **Sangat Layak** |

Usability Testing menghasilkan rata-rata **4.8**, yang merupakan skor tertinggi. Hal ini menunjukkan bahwa dashboard admin sangat mudah digunakan, memiliki struktur navigasi yang jelas, serta mendukung efisiensi kerja dalam pengelolaan destinasi wisata.

**Tabel 3.4.13 Rekapitulasi Hasil Testing Petugas/Admin**

| Kategori Pengujian | Skor Rata-rata |
|-------------------|---------------|
| Unit Testing | 4.4 |
| Functional Testing | 4.6 |
| Accuracy Testing | 4.4 |
| Usability Testing | 4.8 |
| **Jumlah Total Skor** | **18.2** |
| **Rata-rata Hasil** | **4.55** |
| **Kriteria Keseluruhan** | **Sangat Layak** |

Berdasarkan seluruh kategori pengujian, dashboard admin pada Website Pariwisata Berbasis Peta Interaktif memiliki rata-rata skor **4.55** dengan kategori **Sangat Layak**. Hal ini menunjukkan bahwa sistem telah memenuhi kebutuhan operasional pengelolaan destinasi wisata, stabil digunakan, akurat dalam menampilkan data, serta memiliki kenyamanan penggunaan yang sangat baik bagi petugas/admin.

---

### 3.4.3 Analisis Pengujian Data Hasil Capstone Project

Pengujian sistem dilakukan menggunakan metode analisis deskriptif kuantitatif dengan instrumen kuesioner skala Likert lima poin. Metode ini diterapkan secara konsisten pada dua kelompok responden, yaitu pengguna publik dan admin/pengelola sistem. Penggunaan metode yang sama memungkinkan hasil penilaian dibandingkan secara objektif antara persepsi pengguna umum dan penilaian teknis dari admin.

#### 1. Analisis Berdasarkan Kuesioner Pengguna Publik

Pengujian kepada pengguna publik dilakukan dengan melibatkan 12 responden yang menjawab 16 butir pertanyaan yang mewakili empat jenis pengujian. Berdasarkan hasil yang diperoleh, rata-rata skor keseluruhan pengguna publik adalah **4.63**, sehingga termasuk kategori **Sangat Layak** (interval 4.01-5.00).

Pengguna memberikan penilaian sangat baik pada aspek:
- Kemudahan memahami website
- Kemudahan menemukan informasi wisata
- Kejelasan tampilan peta interaktif
- Kecepatan website dalam menampilkan data wisata
- Kenyamanan penggunaan website secara keseluruhan

Beberapa skor tertinggi diperoleh pada indikator kemudahan navigasi, informasi marker yang jelas, dan kepuasan penggunaan sistem, masing-masing berada pada kisaran **4.6-4.8**.

Meski demikian, terdapat sedikit catatan terkait peningkatan visualisasi tampilan destinasi tertentu, seperti ukuran foto dan kerapian layout informasi, yang dapat disempurnakan dalam pengembangan berikutnya.

#### 2. Analisis Berdasarkan Kuesioner Pengelola/Admin

Hasil pengujian admin adalah sebagai berikut:
- **Unit Testing: rata-rata 4.4** — Admin menilai fungsi dasar seperti tambah data, edit data, hapus data, upload foto, serta validasi form berjalan baik tanpa error.
- **Functional Testing: rata-rata 4.6** — Seluruh alur operasional admin berjalan sesuai kebutuhan.
- **Accuracy Testing: rata-rata 4.4** — Admin menilai data destinasi, marker, foto, dan deskripsi tampil akurat dan konsisten.
- **Usability Testing: rata-rata 4.8** — Dashboard admin sangat mudah digunakan, tombol penting mudah ditemukan, dan alur kerja pengelolaan data dinilai sangat efisien.

Total skor keseluruhan admin adalah **18.2**, dengan rata-rata **4.55**, termasuk kategori **Sangat Layak**.

#### 3. Sintesis Analisis Pengguna Publik dan Pengelola/Admin

**Tabel 3.4.14 Perbandingan Publik dan Admin**

| Kelompok | Rata-rata Kelulusan Sistem | Kategori |
|----------|--------------------------|----------|
| Pengguna Publik | 4.63 | Sangat Layak |
| Admin/Pengelola | 4.55 | Sangat Layak |

Baik pengguna publik maupun pengelola memberikan penilaian kategori **Sangat Layak**, yang berarti sistem telah memenuhi standar kelayakan baik dari sisi pengalaman pengguna maupun performa teknis admin.

Fokus penilaian berbeda antar kelompok:
- **Pengguna Publik** menyoroti kemudahan navigasi, informasi wisata yang jelas, performa peta interaktif, dan kenyamanan penggunaan.
- **Admin** menekankan akurasi data, stabilitas proses input/edit/hapus destinasi, serta efisiensi kerja di dashboard.

Kesamaan dari keduanya adalah bahwa sistem bekerja sangat baik, cepat, stabil, dan memperlancar akses informasi wisata pesisir.

#### 4. Kesimpulan Akhir Analisis Pengujian

Berdasarkan pengujian dua kelompok responden dengan instrumen yang sama, dapat disimpulkan bahwa Website Pariwisata Berbasis Peta Interaktif Kota Bengkulu memiliki tingkat kelayakan yang sangat tinggi.

Sistem dinilai:
- Cepat
- Akurat
- Mudah digunakan
- Stabil
- Mendukung kebutuhan pengguna baik publik maupun admin

Rata-rata nilai keseluruhan berada di kategori **Sangat Layak**, sehingga sistem siap diimplementasikan secara luas sebagai portal informasi pariwisata pesisir. Meskipun demikian, beberapa peningkatan minor pada aspek tampilan visual dan penataan konten dapat dilakukan untuk penyempurnaan pada tahap pengembangan berikutnya.
