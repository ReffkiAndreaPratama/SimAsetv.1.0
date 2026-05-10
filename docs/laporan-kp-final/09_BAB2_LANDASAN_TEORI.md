# BAB II LANDASAN TEORI

## 2.1 Tinjauan Pustaka

Beberapa penelitian terdahulu yang relevan dengan pengembangan sistem informasi manajemen aset berbasis web diuraikan sebagai berikut.

**1. Nasrul (2024)**

Nasrul (2024) dalam penelitiannya berjudul "Pengembangan Sistem Informasi Manajemen Aset Berbasis Web Menggunakan Framework Laravel" mengembangkan sistem informasi manajemen aset berbasis web menggunakan framework Laravel. Penelitian ini bertujuan untuk mengatasi permasalahan pengelolaan aset yang masih dilakukan secara manual pada instansi yang diteliti. Hasil penelitian menunjukkan bahwa sistem yang dikembangkan mampu meningkatkan efisiensi pengelolaan aset secara signifikan, dengan fitur utama meliputi pencatatan aset, pelacakan kondisi, dan pelaporan otomatis. Penelitian ini menjadi referensi utama dalam pemilihan framework Laravel sebagai teknologi pengembangan sistem pada penelitian ini. Perbedaan penelitian ini dengan penelitian Nasrul (2024) terletak pada objek penelitian dan fitur tambahan yang dikembangkan, yaitu fitur QR Code, pemindaian aset, audit log, dan manajemen pemeliharaan yang disesuaikan dengan kebutuhan spesifik RBTV Bengkulu.

**2. Kusumojati & Mediawati (2024)**

Kusumojati dan Mediawati (2024) dalam penelitiannya berjudul "Penerapan Sistem Informasi Manajemen Aset Berbasis Web dalam Organisasi" membahas penerapan sistem informasi manajemen aset berbasis web dalam lingkungan organisasi. Penelitian ini menekankan pentingnya integrasi data aset secara terpusat untuk mendukung pengambilan keputusan manajemen. Hasil penelitian menunjukkan bahwa sistem berbasis web mampu meningkatkan transparansi dan akuntabilitas pengelolaan aset organisasi. Penelitian ini memberikan kontribusi dalam perancangan fitur manajemen data terpusat pada sistem yang dikembangkan. Perbedaannya, penelitian ini lebih berfokus pada instansi penyiaran dengan kebutuhan pengelolaan aset peralatan teknis yang spesifik, serta dilengkapi dengan fitur QR Code dan audit log yang tidak dibahas dalam penelitian Kusumojati dan Mediawati (2024).

**3. Rahman & Dewi (2024)**

Rahman dan Dewi (2024) dalam penelitiannya berjudul "Pengembangan Sistem Inventaris Berbasis Web dengan Fitur Pelaporan Otomatis" mengembangkan sistem inventaris berbasis web yang dilengkapi dengan fitur pelaporan otomatis. Penelitian ini berfokus pada kemampuan sistem untuk menghasilkan laporan secara otomatis berdasarkan data yang tersimpan di database, sehingga mengurangi waktu dan tenaga yang diperlukan untuk pembuatan laporan manual. Hasil penelitian membuktikan bahwa fitur pelaporan otomatis dapat meningkatkan efisiensi kerja staf administrasi secara signifikan. Penelitian ini menjadi acuan dalam pengembangan fitur laporan otomatis pada sistem yang dikembangkan. Perbedaannya, penelitian ini mengembangkan sistem yang tidak hanya mencakup pelaporan otomatis, tetapi juga mengintegrasikan fitur impor data dari Excel, ekspor ke PDF, dan pemindaian QR Code yang belum dibahas dalam penelitian Rahman dan Dewi (2024).

**4. Anwar & Fatimah (2022)**

Anwar dan Fatimah (2022) dalam penelitiannya berjudul "Evaluasi Usability Sistem Inventaris Berbasis Web" melakukan evaluasi terhadap aspek usability sistem inventaris berbasis web. Penelitian ini menggunakan metode pengujian berbasis kuesioner untuk mengukur tingkat kemudahan penggunaan, efisiensi, dan kepuasan pengguna terhadap sistem inventaris. Hasil penelitian menunjukkan bahwa aspek antarmuka yang intuitif dan navigasi yang mudah merupakan faktor kunci dalam penerimaan sistem oleh pengguna. Penelitian ini memberikan landasan dalam perancangan antarmuka yang ramah pengguna pada sistem yang dikembangkan. Perbedaannya, penelitian ini tidak hanya memperhatikan aspek usability antarmuka, tetapi juga mengembangkan sistem secara menyeluruh mulai dari analisis kebutuhan hingga implementasi dan pengujian pada objek penelitian yang berbeda, yaitu instansi penyiaran RBTV Bengkulu.

---

## 2.2 Dasar Teori

### 2.2.1 Definisi Sistem

Sistem adalah sekumpulan elemen atau komponen yang saling berinteraksi dan bekerja sama untuk mencapai tujuan tertentu. Menurut Laudon & Laudon (2021), sistem merupakan sekumpulan komponen yang saling berhubungan yang mengumpulkan, memproses, menyimpan, dan mendistribusikan informasi untuk mendukung pengambilan keputusan dan pengendalian dalam suatu organisasi. Setiap sistem terdiri dari masukan (input), proses (process), dan keluaran (output) yang saling berkaitan satu sama lain.

Karakteristik utama dari sebuah sistem meliputi:
- **Komponen (Components):** Bagian-bagian yang membentuk sistem dan saling berinteraksi.
- **Batas (Boundary):** Daerah yang membatasi antara sistem dengan lingkungan luarnya.
- **Lingkungan Luar (Environment):** Segala sesuatu di luar batas sistem yang mempengaruhi operasi sistem.
- **Penghubung (Interface):** Media yang menghubungkan satu subsistem dengan subsistem lainnya.
- **Masukan (Input):** Energi atau data yang dimasukkan ke dalam sistem.
- **Keluaran (Output):** Hasil dari proses yang dilakukan oleh sistem.
- **Pengolah (Process):** Bagian yang mengubah masukan menjadi keluaran.
- **Sasaran (Objective):** Tujuan yang ingin dicapai oleh sistem.

### 2.2.2 Definisi Informasi

Informasi adalah data yang telah diolah dan diorganisasikan sehingga memiliki makna dan nilai bagi penerimanya. Menurut Stair & Reynolds (2022), informasi adalah kumpulan fakta yang terorganisir sedemikian rupa sehingga memiliki nilai tambah di luar nilai fakta-fakta individual tersebut. Informasi yang berkualitas harus memenuhi beberapa kriteria, yaitu akurat (accurate), tepat waktu (timely), relevan (relevant), lengkap (complete), dan dapat dipercaya (reliable).

Kualitas informasi sangat menentukan efektivitas pengambilan keputusan dalam suatu organisasi. Informasi yang tidak akurat atau tidak tepat waktu dapat menyebabkan keputusan yang salah dan merugikan organisasi. Oleh karena itu, sistem informasi yang baik harus mampu menghasilkan informasi yang berkualitas tinggi untuk mendukung operasional dan manajemen organisasi.

### 2.2.3 Definisi Sistem Informasi

Sistem informasi adalah kombinasi dari teknologi informasi dan aktivitas manusia yang menggunakan teknologi tersebut untuk mendukung operasi dan manajemen suatu organisasi. Menurut O'Brien & Marakas (2021), sistem informasi merupakan kombinasi terorganisir dari orang, perangkat keras, perangkat lunak, jaringan komunikasi, sumber data, dan kebijakan serta prosedur yang menyimpan, mengambil, mengubah, dan mendistribusikan informasi dalam suatu organisasi.

Sistem informasi berbasis web memanfaatkan teknologi internet dan browser sebagai antarmuka pengguna, sehingga dapat diakses dari berbagai perangkat tanpa memerlukan instalasi perangkat lunak khusus. Keunggulan ini menjadikan sistem informasi berbasis web sebagai pilihan yang tepat untuk organisasi yang membutuhkan akses data secara terpusat dan real-time. Komponen utama sistem informasi meliputi perangkat keras (hardware), perangkat lunak (software), data, prosedur, dan manusia (brainware).

### 2.2.4 Manajemen Aset

Manajemen aset adalah proses sistematis untuk mengembangkan, mengoperasikan, memelihara, meningkatkan, dan melepaskan aset dengan cara yang paling efektif dari segi biaya. Menurut International Organization for Standardization (2021), manajemen aset adalah aktivitas terkoordinasi dari suatu organisasi untuk merealisasikan nilai dari aset. Standar ISO 55000 mendefinisikan aset sebagai sesuatu yang memiliki nilai potensial atau aktual bagi suatu organisasi.

Dalam konteks aset barang kantor, manajemen aset mencakup beberapa aspek penting, yaitu:
- **Pencatatan aset:** Mendokumentasikan seluruh informasi aset secara lengkap dan akurat, meliputi identitas aset, kondisi, lokasi, dan nilai aset.
- **Pelacakan aset:** Memantau lokasi, kondisi, dan status aset secara real-time untuk memastikan aset dapat digunakan secara optimal.
- **Pemeliharaan aset:** Merencanakan dan melaksanakan perawatan aset secara berkala untuk memperpanjang umur pakai aset.
- **Pelaporan aset:** Menghasilkan laporan yang akurat dan tepat waktu untuk mendukung pengambilan keputusan manajemen.
- **Penghapusan aset:** Mengelola proses penghapusan aset yang sudah tidak layak pakai sesuai dengan prosedur yang berlaku.

Pengelolaan aset yang baik akan memberikan manfaat bagi organisasi, antara lain meningkatkan efisiensi penggunaan aset, mengurangi biaya operasional, meningkatkan akuntabilitas, dan mendukung perencanaan anggaran yang lebih baik.

### 2.2.5 Laravel

Laravel adalah framework PHP open-source yang mengikuti pola arsitektur Model-View-Controller (MVC). Dikembangkan oleh Taylor Otwell dan pertama kali dirilis pada tahun 2011, Laravel telah menjadi salah satu framework PHP paling populer di dunia. Menurut Purbadian (2021), Laravel menyediakan berbagai fitur yang memudahkan pengembangan aplikasi web, seperti routing yang ekspresif, ORM yang powerful, sistem migrasi database, dan template engine yang fleksibel.

Fitur-fitur utama Laravel yang digunakan dalam pengembangan sistem ini meliputi:
- **Eloquent ORM:** Object-Relational Mapping yang memudahkan interaksi dengan database menggunakan sintaks PHP yang ekspresif.
- **Blade Templating:** Template engine yang powerful dan mudah digunakan untuk membangun antarmuka pengguna.
- **Artisan CLI:** Command-line interface untuk berbagai tugas pengembangan seperti pembuatan model, controller, dan migrasi.
- **Migration & Seeder:** Sistem manajemen skema database yang terstruktur dan dapat direproduksi.
- **Middleware:** Lapisan pemrosesan request yang fleksibel untuk autentikasi, otorisasi, dan logging.
- **Laravel Breeze:** Starter kit untuk autentikasi yang ringan dan mudah dikustomisasi.

### 2.2.6 Basis Data

Basis data (database) adalah kumpulan data yang terorganisir dan saling berhubungan yang disimpan secara elektronik dalam sistem komputer. Menurut Connolly & Begg (2021), basis data adalah kumpulan data yang terbagi secara logis, deskripsi data tersebut, yang dirancang untuk memenuhi kebutuhan informasi suatu organisasi. Sistem Manajemen Basis Data (DBMS) adalah perangkat lunak yang memungkinkan pengguna untuk mendefinisikan, membuat, memelihara, dan mengontrol akses ke basis data.

MySQL adalah sistem manajemen basis data relasional (RDBMS) open-source yang paling banyak digunakan di dunia. MySQL menggunakan bahasa SQL (Structured Query Language) untuk mengelola data dan mendukung berbagai fitur seperti transaksi, indeks, dan stored procedure. Menurut Coronel & Morris (2022), MySQL menawarkan performa tinggi, keandalan, dan kemudahan penggunaan yang menjadikannya pilihan utama untuk aplikasi web berbasis data.

### 2.2.7 ERD

Entity Relationship Diagram (ERD) adalah representasi grafis dari entitas-entitas dalam suatu sistem dan hubungan antar entitas tersebut. ERD digunakan sebagai alat perancangan basis data untuk menggambarkan struktur data dan hubungan antar data sebelum diimplementasikan ke dalam sistem basis data. Menurut Connolly & Begg (2021), ERD terdiri dari tiga komponen utama, yaitu entitas (entity), atribut (attribute), dan relasi (relationship).

Komponen-komponen ERD meliputi:
- **Entitas (Entity):** Objek atau konsep yang memiliki keberadaan independen dalam dunia nyata, digambarkan dengan persegi panjang.
- **Atribut (Attribute):** Properti atau karakteristik dari suatu entitas, digambarkan dengan elips.
- **Relasi (Relationship):** Hubungan antara dua atau lebih entitas, digambarkan dengan belah ketupat.
- **Kardinalitas:** Menggambarkan jumlah kemunculan suatu entitas yang dapat dihubungkan dengan entitas lain, seperti one-to-one (1:1), one-to-many (1:N), dan many-to-many (M:N).

### 2.2.8 Normalisasi

Normalisasi adalah proses pengorganisasian data dalam basis data untuk mengurangi redundansi data dan meningkatkan integritas data. Proses normalisasi dilakukan dengan membagi tabel-tabel besar menjadi tabel-tabel yang lebih kecil dan mendefinisikan hubungan antar tabel tersebut. Menurut Coronel & Morris (2022), normalisasi bertujuan untuk menghilangkan anomali data yang dapat terjadi saat operasi insert, update, dan delete dilakukan pada basis data.

Tahapan normalisasi meliputi:
- **Bentuk Normal Pertama (1NF):** Setiap kolom dalam tabel harus berisi nilai atomik (tidak dapat dibagi lagi) dan setiap baris harus unik.
- **Bentuk Normal Kedua (2NF):** Memenuhi 1NF dan setiap atribut non-kunci harus bergantung penuh pada kunci primer.
- **Bentuk Normal Ketiga (3NF):** Memenuhi 2NF dan tidak ada ketergantungan transitif antara atribut non-kunci.
- **Bentuk Normal Boyce-Codd (BCNF):** Versi yang lebih ketat dari 3NF yang menghilangkan semua anomali yang tidak dapat diatasi oleh 3NF.

### 2.2.9 SQL

SQL (Structured Query Language) adalah bahasa standar yang digunakan untuk mengelola dan memanipulasi data dalam sistem manajemen basis data relasional. SQL memungkinkan pengguna untuk membuat, membaca, memperbarui, dan menghapus data dalam basis data. Menurut Connolly & Begg (2021), SQL terdiri dari beberapa sub-bahasa yang masing-masing memiliki fungsi berbeda.

Sub-bahasa SQL meliputi:
- **DDL (Data Definition Language):** Digunakan untuk mendefinisikan struktur basis data, seperti CREATE, ALTER, dan DROP.
- **DML (Data Manipulation Language):** Digunakan untuk memanipulasi data dalam basis data, seperti SELECT, INSERT, UPDATE, dan DELETE.
- **DCL (Data Control Language):** Digunakan untuk mengontrol akses ke data dalam basis data, seperti GRANT dan REVOKE.
- **TCL (Transaction Control Language):** Digunakan untuk mengelola transaksi dalam basis data, seperti COMMIT, ROLLBACK, dan SAVEPOINT.

---

## 2.3 Metode Analisis

Metode analisis yang digunakan dalam penelitian ini adalah analisis PIECES (Performance, Information, Economy, Control, Efficiency, Service). Analisis PIECES merupakan kerangka kerja yang digunakan untuk mengidentifikasi dan menganalisis permasalahan pada sistem yang sedang berjalan, sehingga dapat ditentukan kebutuhan sistem yang baru. Menurut Laudon & Laudon (2021), analisis PIECES membantu dalam mengidentifikasi kelemahan sistem lama dan merumuskan solusi yang tepat untuk sistem baru.

Komponen analisis PIECES meliputi:
- **Performance (Kinerja):** Menganalisis kinerja sistem yang sedang berjalan, meliputi throughput (jumlah pekerjaan yang dapat diselesaikan dalam waktu tertentu) dan response time (waktu yang dibutuhkan untuk merespons permintaan).
- **Information (Informasi):** Menganalisis kualitas informasi yang dihasilkan oleh sistem, meliputi akurasi, relevansi, kelengkapan, dan ketepatan waktu informasi.
- **Economy (Ekonomi):** Menganalisis biaya dan manfaat sistem, meliputi biaya operasional, biaya pemeliharaan, dan nilai ekonomis dari sistem.
- **Control (Kontrol):** Menganalisis pengendalian dan keamanan sistem, meliputi kontrol akses, validasi data, dan audit trail.
- **Efficiency (Efisiensi):** Menganalisis efisiensi penggunaan sumber daya sistem, meliputi penggunaan waktu, tenaga, dan peralatan.
- **Service (Layanan):** Menganalisis kualitas layanan yang diberikan oleh sistem kepada pengguna, meliputi kemudahan penggunaan, keandalan, dan fleksibilitas sistem.

---

## 2.4 Langkah-langkah Pengembangan Aplikasi

Pengembangan sistem informasi manajemen aset ini menggunakan model pengembangan Waterfall. Model Waterfall adalah model pengembangan perangkat lunak yang bersifat sekuensial dan terstruktur, di mana setiap tahapan harus diselesaikan sebelum tahapan berikutnya dimulai. Menurut Pressman (2021), model Waterfall dipilih karena memiliki alur kerja yang terencana dan mudah dipantau, serta cocok untuk proyek dengan ruang lingkup dan kebutuhan yang jelas sejak awal.

Tahapan dalam model Waterfall yang diterapkan dalam pengembangan sistem ini adalah sebagai berikut:

**Tahap 1: Analisis Kebutuhan (Requirement Analysis)**

Tahap pertama adalah analisis kebutuhan, yaitu proses mengidentifikasi dan mendokumentasikan kebutuhan sistem yang akan dikembangkan. Pada tahap ini dilakukan observasi langsung terhadap proses pengelolaan aset yang sedang berjalan, wawancara dengan pengguna sistem, dan studi literatur terkait sistem informasi manajemen aset. Hasil dari tahap ini adalah spesifikasi kebutuhan fungsional dan non-fungsional sistem yang menjadi dasar perancangan.

**Tahap 2: Perancangan Sistem (System Design)**

Tahap kedua adalah perancangan sistem, yaitu proses menerjemahkan hasil analisis kebutuhan ke dalam bentuk rancangan teknis. Pada tahap ini dilakukan perancangan arsitektur sistem, perancangan basis data menggunakan ERD, perancangan alur sistem menggunakan flowchart dan diagram UML, serta perancangan antarmuka pengguna (prototype). Hasil dari tahap ini adalah dokumen perancangan sistem yang lengkap dan terperinci.

**Tahap 3: Implementasi (Implementation)**

Tahap ketiga adalah implementasi, yaitu proses merealisasikan rancangan sistem ke dalam bentuk perangkat lunak yang berfungsi. Pada tahap ini dilakukan penulisan kode program menggunakan framework Laravel dan MySQL sebagai basis data. Setiap modul sistem dikembangkan secara bertahap sesuai dengan rancangan yang telah dibuat. Hasil dari tahap ini adalah sistem informasi manajemen aset yang siap untuk diuji.

**Tahap 4: Pengujian (Testing)**

Tahap keempat adalah pengujian, yaitu proses memverifikasi dan memvalidasi sistem untuk memastikan bahwa seluruh fitur berfungsi dengan benar sesuai dengan kebutuhan yang telah ditetapkan. Pengujian dilakukan menggunakan metode white-box testing untuk menguji logika internal program dan black-box testing untuk menguji fungsionalitas sistem dari perspektif pengguna. Hasil dari tahap ini adalah laporan pengujian yang menunjukkan tingkat kelayakan sistem.

**Tahap 5: Pemeliharaan (Maintenance)**

Tahap kelima adalah pemeliharaan, yaitu proses menjaga dan meningkatkan sistem setelah sistem diimplementasikan dan digunakan oleh pengguna. Pemeliharaan meliputi perbaikan bug yang ditemukan setelah sistem digunakan (corrective maintenance), penyesuaian sistem dengan perubahan lingkungan teknologi (adaptive maintenance), peningkatan kinerja dan penambahan fitur baru (perfective maintenance), serta pencegahan masalah yang mungkin terjadi di masa depan (preventive maintenance).
