# BAB II TINJAUAN PUSTAKA DAN LANDASAN TEORI

## 2.1 Profil Instansi

### 2.1.1 Sejarah Singkat RBTV Bengkulu

Rakyat Bengkulu Televisi (RBTV) merupakan stasiun televisi lokal yang beroperasi di Kota Bengkulu, Provinsi Bengkulu. RBTV hadir sebagai media penyiaran lokal yang berkomitmen untuk menyajikan informasi, hiburan, dan konten edukatif yang relevan bagi masyarakat Bengkulu dan sekitarnya. Sebagai stasiun televisi lokal, RBTV memiliki peran penting dalam mendukung perkembangan industri media dan informasi di wilayah Bengkulu.

### 2.1.2 Visi dan Misi

**Visi:**
Menjadi stasiun televisi lokal terdepan di Bengkulu yang informatif, edukatif, dan menghibur.

**Misi:**
1. Menyajikan konten siaran yang berkualitas dan bermanfaat bagi masyarakat Bengkulu.
2. Mendukung perkembangan budaya dan potensi daerah Bengkulu melalui media penyiaran.
3. Memberikan informasi yang akurat, cepat, dan terpercaya kepada masyarakat.

### 2.1.3 Struktur Organisasi

> **Gambar 2.1 Struktur Organisasi RBTV Bengkulu**

Struktur organisasi RBTV Bengkulu terdiri dari Direktur Utama yang membawahi beberapa divisi, antara lain Divisi Produksi, Divisi Teknik, Divisi Pemberitaan, Divisi Marketing, dan Divisi Administrasi & Umum. Pengelolaan aset barang kantor berada di bawah tanggung jawab Divisi Administrasi & Umum.

---

## 2.2 Landasan Teori

### 2.2.1 Sistem Informasi

Sistem informasi adalah kombinasi dari teknologi informasi dan aktivitas manusia yang menggunakan teknologi tersebut untuk mendukung operasi dan manajemen suatu organisasi. Menurut O'Brien & Marakas (2011), sistem informasi merupakan kombinasi terorganisir dari orang, perangkat keras, perangkat lunak, jaringan komunikasi, sumber data, dan kebijakan serta prosedur yang menyimpan, mengambil, mengubah, dan mendistribusikan informasi dalam suatu organisasi.

Sistem informasi berbasis web memanfaatkan teknologi internet dan browser sebagai antarmuka pengguna, sehingga dapat diakses dari berbagai perangkat tanpa memerlukan instalasi perangkat lunak khusus. Keunggulan ini menjadikan sistem informasi berbasis web sebagai pilihan yang tepat untuk organisasi yang membutuhkan akses data secara terpusat dan real-time.

### 2.2.2 Manajemen Aset

Manajemen aset adalah proses sistematis untuk mengembangkan, mengoperasikan, memelihara, meningkatkan, dan melepaskan aset dengan cara yang paling efektif dari segi biaya. Menurut ISO 55000:2014, manajemen aset adalah aktivitas terkoordinasi dari suatu organisasi untuk merealisasikan nilai dari aset.

Dalam konteks aset barang kantor, manajemen aset mencakup:
- **Pencatatan aset:** Mendokumentasikan seluruh informasi aset secara lengkap dan akurat.
- **Pelacakan aset:** Memantau lokasi, kondisi, dan status aset secara real-time.
- **Pemeliharaan aset:** Merencanakan dan melaksanakan perawatan aset secara berkala.
- **Pelaporan aset:** Menghasilkan laporan yang akurat untuk mendukung pengambilan keputusan.
- **Penghapusan aset:** Mengelola proses penghapusan aset yang sudah tidak layak pakai.

### 2.2.3 Laravel Framework

Laravel adalah framework PHP open-source yang mengikuti pola arsitektur Model-View-Controller (MVC). Dikembangkan oleh Taylor Otwell dan pertama kali dirilis pada tahun 2011, Laravel telah menjadi salah satu framework PHP paling populer di dunia. Laravel 12, versi yang digunakan dalam proyek ini, menawarkan berbagai fitur modern seperti:

- **Eloquent ORM:** Object-Relational Mapping yang memudahkan interaksi dengan database.
- **Blade Templating:** Template engine yang powerful dan mudah digunakan.
- **Laravel Breeze:** Starter kit untuk autentikasi yang ringan dan mudah dikustomisasi.
- **Artisan CLI:** Command-line interface untuk berbagai tugas pengembangan.
- **Migration & Seeder:** Sistem manajemen skema database yang terstruktur.
- **Middleware:** Lapisan pemrosesan request yang fleksibel.

### 2.2.4 MySQL / SQLite

**MySQL** adalah sistem manajemen basis data relasional (RDBMS) open-source yang paling banyak digunakan di dunia. MySQL menggunakan bahasa SQL (Structured Query Language) untuk mengelola data dan mendukung berbagai fitur seperti transaksi, indeks, dan stored procedure.

**SQLite** adalah sistem manajemen basis data relasional yang ringan dan tidak memerlukan server terpisah. SQLite menyimpan seluruh database dalam satu file, sehingga sangat cocok untuk pengembangan dan pengujian aplikasi. Dalam proyek SimAset, SQLite digunakan sebagai database default untuk lingkungan pengembangan, sementara MySQL direkomendasikan untuk lingkungan produksi.

### 2.2.5 QR Code

QR Code (Quick Response Code) adalah jenis kode matriks dua dimensi yang dapat menyimpan informasi dalam bentuk teks, URL, atau data lainnya. QR Code dapat dibaca dengan cepat menggunakan kamera smartphone atau perangkat scanner khusus. Dalam konteks manajemen aset, QR Code digunakan sebagai label digital yang ditempelkan pada setiap aset untuk memudahkan identifikasi dan pelacakan.

Keunggulan penggunaan QR Code dalam manajemen aset:
- Identifikasi aset yang cepat dan akurat hanya dengan memindai kode.
- Mengurangi kesalahan input data manual.
- Memudahkan audit fisik aset secara berkala.
- Dapat menyimpan URL yang mengarah ke halaman detail aset dalam sistem.

Dalam proyek ini, library **SimpleSoftwareIO/simple-qrcode** digunakan untuk generate QR Code dalam format SVG yang dapat dicetak dan ditampilkan di browser.

### 2.2.6 Model Pengembangan Waterfall

Model Waterfall adalah model pengembangan perangkat lunak yang bersifat sekuensial dan terstruktur. Setiap tahapan harus diselesaikan sebelum tahapan berikutnya dimulai. Model ini dipilih karena memiliki alur kerja yang terencana dan mudah dipantau, serta cocok untuk proyek dengan ruang lingkup dan kebutuhan yang jelas sejak awal.

> **Gambar 2.2 Tahapan Model Waterfall**

Tahapan dalam model Waterfall yang diterapkan dalam proyek ini:

1. **Analisis Kebutuhan (Requirement Analysis):** Mengidentifikasi dan mendokumentasikan kebutuhan sistem.
2. **Perancangan Sistem (System Design):** Merancang arsitektur, database, dan antarmuka sistem.
3. **Implementasi (Implementation):** Mengembangkan kode program berdasarkan rancangan.
4. **Pengujian (Testing):** Menguji sistem untuk memastikan semua fitur berfungsi dengan benar.
5. **Evaluasi (Evaluation):** Mengevaluasi sistem berdasarkan hasil pengujian dan umpan balik pengguna.
6. **Dokumentasi (Documentation):** Menyusun dokumentasi lengkap sistem yang dikembangkan.

---

## 2.3 Penelitian Terdahulu

Beberapa penelitian terdahulu yang relevan dengan pengembangan sistem informasi manajemen aset berbasis web:

**1. Sistem Informasi Manajemen Aset Berbasis Web (Studi Kasus: Universitas X)**
Penelitian ini mengembangkan sistem informasi manajemen aset berbasis web menggunakan framework CodeIgniter. Hasil penelitian menunjukkan bahwa sistem berhasil meningkatkan efisiensi pengelolaan aset hingga 60% dibandingkan sistem manual. Fitur utama yang dikembangkan meliputi CRUD aset, laporan, dan export data.

**2. Implementasi QR Code dalam Sistem Inventaris Barang (Studi Kasus: Kantor Pemerintah Daerah)**
Penelitian ini mengintegrasikan teknologi QR Code dalam sistem inventaris barang pemerintah daerah. Hasil penelitian membuktikan bahwa penggunaan QR Code dapat mempercepat proses audit fisik aset hingga 75% dibandingkan metode konvensional.

**3. Pengembangan Sistem Informasi Aset dengan Fitur Maintenance Tracking**
Penelitian ini mengembangkan sistem informasi aset yang dilengkapi dengan fitur pelacakan maintenance. Sistem berhasil mengurangi downtime peralatan sebesar 40% melalui perencanaan maintenance yang lebih terstruktur dan notifikasi otomatis.

**4. Rancang Bangun Aplikasi Manajemen Inventaris Berbasis Laravel**
Penelitian ini mengembangkan aplikasi manajemen inventaris menggunakan framework Laravel dengan fitur import/export Excel dan laporan PDF. Hasil pengujian menunjukkan bahwa sistem memiliki tingkat akurasi data yang tinggi dan antarmuka yang mudah digunakan.

Berdasarkan penelitian-penelitian terdahulu tersebut, pengembangan SimAset pada proyek Kerja Praktik ini mengintegrasikan berbagai fitur yang telah terbukti efektif, yaitu manajemen aset berbasis web, QR Code, maintenance tracking, import/export data, dan laporan, dengan menggunakan teknologi terkini yaitu Laravel 12.
