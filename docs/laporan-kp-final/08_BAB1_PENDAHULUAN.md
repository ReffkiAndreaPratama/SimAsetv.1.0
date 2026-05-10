---
# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi telah mengubah cara organisasi dalam mengelola data dan informasi operasional. Pemanfaatan sistem informasi berbasis komputer memungkinkan proses pencatatan, penyimpanan, pengolahan, serta pelaporan data dilakukan secara lebih cepat, akurat, dan terintegrasi dibandingkan dengan metode konvensional. Penggunaan sistem terkomputerisasi tidak hanya membantu meningkatkan efisiensi kerja, tetapi juga meminimalkan risiko kesalahan manusia (human error) dalam proses pencatatan dan pengolahan data. Instansi yang masih menggunakan metode pencatatan manual berpotensi mengalami berbagai permasalahan, seperti duplikasi data, kehilangan arsip, inkonsistensi informasi, serta keterlambatan dalam penyusunan laporan yang dibutuhkan untuk mendukung kegiatan operasional dan pengambilan keputusan.

RBTV Bengkulu merupakan stasiun televisi lokal yang menjalankan kegiatan operasional di bidang penyiaran, produksi program, administrasi, serta pengelolaan teknis peralatan siaran. Dalam menunjang kegiatan tersebut, RBTV Bengkulu memiliki berbagai aset barang seperti kamera, perangkat editing, komputer, peralatan jaringan, perangkat audio, serta perlengkapan kantor lainnya. Aset-aset tersebut digunakan secara rutin dalam proses produksi dan penyiaran sehingga memiliki tingkat mobilitas dan intensitas penggunaan yang cukup tinggi. Oleh karena itu, pengelolaan aset yang tertib dan terdokumentasi dengan baik sangat diperlukan untuk memastikan ketersediaan, kondisi, dan keberadaan barang tetap terpantau serta dapat digunakan secara optimal.

Berdasarkan hasil observasi selama pelaksanaan kerja praktik, proses pengelolaan aset barang di RBTV Bengkulu masih dilakukan melalui pencatatan dokumen tertulis dan file spreadsheet yang terpisah. Data aset belum tersimpan dalam satu sistem terpusat sehingga informasi terkait jumlah, lokasi penyimpanan, serta kondisi barang belum terintegrasi dengan baik. Proses pencarian data tertentu memerlukan waktu yang relatif lama karena harus memeriksa beberapa dokumen atau file secara manual. Selain itu, pembaruan kondisi barang belum terdokumentasi secara sistematis, sehingga informasi yang tersedia terkadang tidak sepenuhnya mencerminkan kondisi aktual di lapangan. Hal ini berpotensi menimbulkan kesalahan informasi dalam proses monitoring dan pelaporan.

Kondisi tersebut menimbulkan beberapa permasalahan, antara lain kesulitan dalam melakukan monitoring kondisi aset secara berkala, potensi terjadinya pencatatan ganda, serta keterlambatan dalam penyusunan laporan inventaris yang dibutuhkan oleh pihak manajemen. Apabila tidak ditangani dengan baik, permasalahan tersebut dapat mempengaruhi efektivitas pengelolaan aset serta kelancaran operasional instansi. Oleh karena itu, diperlukan suatu sistem informasi manajemen aset barang berbasis web yang mampu mengelola data aset secara terintegrasi dan terpusat, menyediakan fitur pengelompokan kategori dan kondisi barang, serta menghasilkan laporan secara otomatis dan akurat. Sistem yang dibangun diharapkan dapat membantu meningkatkan efektivitas dan efisiensi pengelolaan aset di RBTV Bengkulu serta mendukung tertib administrasi aset secara berkelanjutan.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan sebelumnya, permasalahan utama dalam kerja praktik ini berkaitan dengan sistem pengelolaan aset barang yang masih dilakukan secara manual dan belum terintegrasi. Oleh karena itu, rumusan masalah dalam kerja praktik ini dapat dirumuskan sebagai berikut:

1. Bagaimana proses pengelolaan aset barang yang sedang berjalan di RBTV Bengkulu, mulai dari pencatatan, penyimpanan data, hingga penyusunan laporan inventaris?

2. Apa saja kelemahan dan kendala yang terdapat pada sistem pengelolaan aset yang saat ini digunakan, khususnya dalam hal pencarian data, pembaruan kondisi barang, dan ketepatan penyajian informasi?

3. Bagaimana merancang dan membangun Sistem Informasi Manajemen Aset Barang berbasis web yang sesuai dengan kebutuhan operasional RBTV Bengkulu serta mampu mengatasi kelemahan sistem sebelumnya?

4. Bagaimana hasil implementasi sistem yang dibangun dapat membantu meningkatkan efektivitas, efisiensi, dan akurasi dalam proses pengelolaan aset barang di RBTV Bengkulu?

---

## 1.3 Batasan Masalah

Agar penelitian lebih terarah, terfokus, dan tidak melebar dari tujuan yang telah ditetapkan, maka ruang lingkup penelitian ini dibatasi pada hal-hal berikut:

1. Sistem yang dikembangkan hanya mencakup pengelolaan aset barang operasional dan perlengkapan kantor yang digunakan dalam kegiatan penyiaran dan administrasi di RBTV Bengkulu. Penelitian ini tidak membahas pengelolaan aset tetap lainnya di luar ruang lingkup kerja praktik.

2. Sistem meliputi fitur autentikasi pengguna (login dan logout), pengelolaan data aset, pengelolaan kategori aset, pengelolaan kondisi aset, serta pembuatan dan penampilan laporan aset secara terstruktur. Fitur yang dikembangkan difokuskan pada kebutuhan dasar pengelolaan dan monitoring aset.

3. Sistem dikembangkan berbasis web menggunakan framework Laravel sebagai kerangka kerja pengembangan aplikasi dan MySQL sebagai sistem manajemen basis data. Bahasa pemrograman yang digunakan adalah PHP dengan arsitektur Model-View-Controller (MVC).

4. Sistem digunakan oleh administrator dan staf internal RBTV Bengkulu yang memiliki hak akses tertentu sesuai peran masing-masing. Penelitian ini tidak membahas penggunaan sistem oleh pihak eksternal.

5. Sistem tidak membahas perhitungan penyusutan nilai aset secara akuntansi, manajemen keuangan, maupun integrasi dengan sistem akuntansi yang mungkin digunakan oleh instansi.

6. Implementasi sistem dilakukan pada lingkungan jaringan internal instansi (intranet) dan tidak terhubung dengan sistem eksternal atau layanan berbasis internet publik.

---

## 1.4 Tujuan Penelitian

Tujuan yang ingin dicapai dalam pelaksanaan kerja praktik ini adalah sebagai berikut:

1. Mengidentifikasi dan menganalisis sistem pengelolaan aset barang yang sedang berjalan di RBTV Bengkulu, termasuk proses pencatatan, penyimpanan data, serta penyusunan laporan inventaris yang dilakukan secara manual.

2. Merancang Sistem Informasi Manajemen Aset Barang berbasis web yang sesuai dengan kebutuhan operasional RBTV Bengkulu, dengan memperhatikan permasalahan dan kelemahan yang ditemukan pada sistem sebelumnya.

3. Mengimplementasikan sistem yang mampu menyimpan, mengelola, dan menampilkan data aset secara terpusat dan terstruktur dalam basis data, sehingga memudahkan proses pencarian, pembaruan kondisi, dan pelaporan aset.

4. Melakukan pengujian terhadap sistem yang telah dibangun untuk memastikan seluruh fungsi berjalan sesuai dengan kebutuhan pengguna serta dapat digunakan secara efektif dalam mendukung pengelolaan aset barang di RBTV Bengkulu.

---

## 1.5 Metode Penelitian

### 1.5.1 Metode Pengumpulan Data

**1. Observasi**

Observasi dilakukan secara langsung di RBTV Bengkulu untuk memahami alur kerja pengelolaan aset barang yang sedang berjalan. Kegiatan observasi meliputi pengamatan terhadap proses pencatatan barang, penyimpanan data aset, pembaruan kondisi barang, serta penyusunan laporan inventaris. Melalui observasi ini diperoleh gambaran nyata mengenai prosedur yang digunakan dan kendala yang dihadapi dalam pengelolaan aset.

**2. Studi Pustaka**

Studi pustaka dilakukan dengan mempelajari buku, jurnal ilmiah, serta referensi lain yang berkaitan dengan sistem informasi, manajemen aset, perancangan sistem berbasis web, dan metode pengujian perangkat lunak. Studi pustaka bertujuan untuk memperkuat landasan teori serta menjadi acuan dalam proses analisis, perancangan, dan pengembangan sistem.

### 1.5.2 Metode Analisis

Metode analisis yang digunakan dalam kerja praktik ini adalah analisis deskriptif terhadap sistem pengelolaan aset yang sedang berjalan di RBTV Bengkulu. Analisis deskriptif dilakukan dengan menggambarkan secara sistematis proses pencatatan, penyimpanan, pembaruan kondisi, serta penyusunan laporan aset yang saat ini digunakan oleh instansi.

Tahap analisis dilakukan dengan mengidentifikasi alur proses pengelolaan aset, mengevaluasi kelemahan sistem manual yang digunakan, serta mengkaji kendala yang dihadapi dalam proses pencarian data dan penyusunan laporan. Selain itu, dilakukan identifikasi kebutuhan sistem baru berdasarkan permasalahan yang ditemukan selama observasi.

Hasil analisis ini digunakan sebagai dasar dalam menentukan solusi yang diusulkan dan menjadi acuan dalam tahap perancangan sistem, sehingga sistem yang dibangun dapat sesuai dengan kebutuhan operasional RBTV Bengkulu.

### 1.5.3 Metode Perancangan

Metode perancangan sistem pada kerja praktik ini dilakukan menggunakan pendekatan Unified Modeling Language (UML) sebagai alat bantu pemodelan sistem. UML digunakan untuk menggambarkan struktur, alur proses, serta hubungan antar komponen sistem sebelum tahap implementasi dilakukan. Penggunaan pemodelan ini bertujuan untuk memberikan gambaran yang jelas mengenai sistem yang akan dibangun sehingga dapat meminimalkan kesalahan pada tahap pengembangan.

Diagram yang digunakan dalam perancangan sistem meliputi:

1. **Use Case Diagram**, yang digunakan untuk menggambarkan interaksi antara aktor (administrator dan pengguna) dengan sistem. Diagram ini menunjukkan fungsi-fungsi utama yang tersedia dalam sistem serta batasan hak akses masing-masing pengguna.

2. **Activity Diagram**, yang digunakan untuk menggambarkan alur proses atau aktivitas yang terjadi dalam sistem, seperti proses login, pengelolaan data aset, dan pembuatan laporan.

3. **Class Diagram**, yang digunakan untuk menggambarkan struktur data sistem, atribut yang dimiliki setiap kelas, serta relasi antar entitas dalam basis data.

Melalui pemodelan ini, rancangan sistem dapat divisualisasikan secara sistematis sebelum diterapkan ke dalam bentuk aplikasi berbasis web.

### 1.5.4 Metode Pengembangan

Metode pengembangan sistem yang digunakan dalam kerja praktik ini adalah model Waterfall. Model Waterfall merupakan metode pengembangan perangkat lunak yang dilakukan secara bertahap dan terstruktur, di mana setiap tahapan harus diselesaikan sebelum melanjutkan ke tahap berikutnya. Model ini dipilih karena sesuai dengan kebutuhan pengembangan sistem yang memiliki ruang lingkup dan spesifikasi yang telah ditentukan sejak awal berdasarkan hasil observasi dan analisis.

Tahapan dalam model Waterfall yang diterapkan pada penelitian ini meliputi:

1. Analisis Kebutuhan, yaitu tahap identifikasi kebutuhan sistem berdasarkan permasalahan yang ditemukan pada sistem pengelolaan aset yang berjalan.

2. Perancangan Sistem, yaitu tahap penyusunan desain sistem menggunakan pemodelan UML serta perancangan struktur basis data dan antarmuka pengguna.

3. Implementasi, yaitu tahap pengkodean sistem ke dalam bentuk aplikasi berbasis web menggunakan framework Laravel dan database MySQL.

4. Pengujian, yaitu tahap pemeriksaan dan evaluasi sistem untuk memastikan seluruh fungsi berjalan sesuai dengan kebutuhan yang telah ditentukan.

5. Pemeliharaan, yaitu tahap perbaikan atau penyesuaian sistem apabila ditemukan kesalahan atau kebutuhan pengembangan lebih lanjut setelah sistem diterapkan.

Pendekatan ini memungkinkan proses pengembangan dilakukan secara sistematis dan terkontrol sehingga hasil akhir sistem dapat sesuai dengan kebutuhan operasional RBTV Bengkulu.

### 1.5.5 Metode Testing

Pengujian sistem dilakukan untuk memastikan bahwa aplikasi yang dibangun dapat berjalan sesuai dengan kebutuhan pengguna serta bebas dari kesalahan logika maupun kesalahan fungsi. Pada penelitian ini, metode pengujian yang digunakan terdiri dari dua pendekatan, yaitu:

1. **White-box Testing**, yaitu metode pengujian yang dilakukan dengan memeriksa struktur internal dan logika program. Pengujian ini bertujuan untuk memastikan bahwa setiap fungsi dan alur program berjalan sesuai dengan algoritma yang telah dirancang serta tidak terdapat kesalahan pada struktur kode.

2. **Black-box Testing**, yaitu metode pengujian yang dilakukan dengan menguji fungsionalitas sistem berdasarkan skenario penggunaan tanpa melihat struktur kode program. Pengujian ini berfokus pada kesesuaian antara input yang diberikan dan output yang dihasilkan oleh sistem.

Dengan menggunakan kedua metode tersebut, sistem diharapkan dapat berjalan secara optimal dan sesuai dengan kebutuhan operasional RBTV Bengkulu.

---

## 1.6 Tempat dan Waktu Kerja Praktik

Kerja Praktik dilaksanakan di Rakyat Bengkulu Televisi Bengkulu yang berlokasi di Kota Bengkulu, Provinsi Bengkulu. RBTV Bengkulu merupakan stasiun televisi lokal yang bergerak di bidang penyiaran dan produksi program siaran.

Pelaksanaan kerja praktik berlangsung selama tiga bulan, terhitung sejak tanggal 19 Januari 2026 sampai dengan 17 April 2026. Selama periode tersebut, kegiatan yang dilakukan meliputi observasi sistem yang berjalan, analisis permasalahan, perancangan sistem, serta pengembangan dan pengujian aplikasi yang dirancang untuk mendukung pengelolaan aset barang di instansi tersebut.

---

## 1.7 Sistematika Penulisan

Sistematika penulisan laporan kerja praktik ini disusun untuk memberikan gambaran mengenai isi setiap bab yang terdapat dalam laporan. Adapun sistematika penulisan laporan ini adalah sebagai berikut:

**BAB I PENDAHULUAN**

Bab ini berisi latar belakang masalah, rumusan masalah, batasan masalah, tujuan penelitian, metode penelitian, tempat dan waktu pelaksanaan kerja praktik, serta sistematika penulisan laporan.

**BAB II LANDASAN TEORI**

Bab ini memuat tinjauan pustaka dan teori-teori yang mendukung penelitian, termasuk konsep sistem informasi, manajemen aset, pemodelan sistem, basis data, serta metode pengembangan dan pengujian sistem.

**BAB III ANALISIS DAN PERANCANGAN**

Bab ini berisi deskripsi singkat instansi, analisis sistem yang berjalan, identifikasi permasalahan, analisis kebutuhan sistem, serta perancangan sistem yang diusulkan menggunakan pemodelan yang sesuai.

**BAB IV IMPLEMENTASI DAN PEMBAHASAN**

Bab ini menjelaskan proses implementasi sistem yang telah dirancang, hasil pengujian sistem, serta pembahasan terhadap hasil implementasi berdasarkan kebutuhan pengguna.

**BAB V PENUTUP**

Bab ini berisi kesimpulan yang diperoleh dari hasil penelitian serta saran yang dapat diberikan untuk pengembangan sistem di masa mendatang.
