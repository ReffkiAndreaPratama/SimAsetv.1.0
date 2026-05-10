# BAB II LANDASAN TEORI

## 2.1 Tinjauan Pustaka

Tinjauan pustaka merupakan bagian penting dalam suatu penelitian yang bertujuan untuk mengkaji penelitian-penelitian terdahulu yang relevan dengan topik yang dibahas. Melalui tinjauan pustaka, peneliti dapat memahami perkembangan penelitian di bidang yang sama, mengetahui metode yang telah digunakan, serta mengidentifikasi kelebihan dan kekurangan dari penelitian sebelumnya. Selain itu, tinjauan pustaka juga berfungsi untuk menunjukkan posisi penelitian yang dilakukan sehingga memiliki kontribusi yang jelas terhadap pengembangan ilmu pengetahuan. Dalam bidang sistem informasi manajemen aset, berbagai penelitian telah dilakukan untuk meningkatkan efisiensi dan efektivitas pengelolaan aset melalui pemanfaatan teknologi informasi. Sistem manual yang sebelumnya digunakan dalam banyak organisasi memiliki berbagai keterbatasan, seperti kesulitan dalam pencatatan data, lambatnya proses pencarian informasi, serta tingginya risiko kesalahan dan duplikasi data. Oleh karena itu, banyak penelitian yang berfokus pada pengembangan sistem berbasis web untuk mengatasi permasalahan tersebut.

Penelitian yang dilakukan oleh Nasrul (2024) mengembangkan sistem informasi manajemen aset berbasis web menggunakan framework Laravel. Sistem tersebut dirancang untuk menggantikan proses manual dengan sistem terkomputerisasi yang mampu mengelola data aset secara terstruktur. Fitur yang dikembangkan meliputi penambahan data, pengubahan data, penghapusan data, serta pencarian data aset. Hasil penelitian menunjukkan bahwa sistem yang dikembangkan mampu meningkatkan efisiensi kerja serta mempermudah pengelolaan data aset. Selain itu, penggunaan Laravel sebagai framework memberikan kemudahan dalam pengembangan sistem karena struktur kode yang terorganisir dengan baik. Namun, penelitian tersebut masih memiliki keterbatasan karena belum mengakomodasi kebutuhan analisis sistem secara mendalam serta belum dilengkapi dengan fitur audit trail untuk mencatat aktivitas pengguna. Hal ini menjadi kekurangan yang dapat dikembangkan lebih lanjut pada penelitian berikutnya.

Penelitian lain yang dilakukan oleh Kusumojati dan Mediawati (2024) membahas penerapan sistem informasi manajemen aset berbasis web dalam suatu organisasi. Penelitian tersebut menekankan bahwa sistem berbasis web memiliki keunggulan dalam hal aksesibilitas dan integrasi data. Dengan sistem berbasis web, data dapat disimpan secara terpusat dan diakses oleh banyak pengguna secara bersamaan. Hal ini memungkinkan proses pengelolaan aset menjadi lebih efektif dan efisien. Selain itu, sistem berbasis web juga mendukung proses pelaporan secara otomatis sehingga informasi dapat disajikan dengan cepat dan akurat. Namun, penelitian tersebut masih bersifat konseptual dan belum menjelaskan implementasi teknis secara rinci.

Rahman dan Dewi (2024) mengembangkan sistem inventaris berbasis web yang dilengkapi dengan fitur pelaporan otomatis dan monitoring data secara real-time. Sistem tersebut mampu meningkatkan efisiensi kerja serta mengurangi kesalahan pencatatan. Akan tetapi, penelitian ini lebih berfokus pada pengelolaan stok dan belum menyesuaikan kebutuhan pengelolaan aset pada instansi yang memiliki karakteristik berbeda.

Anwar dan Fatimah (2022) melakukan penelitian mengenai evaluasi usability sistem inventaris berbasis web. Penelitian tersebut menunjukkan bahwa sistem berbasis web mampu meningkatkan kemudahan penggunaan serta efisiensi dalam pengelolaan data. Namun, penelitian ini hanya berfokus pada aspek evaluasi penggunaan dan tidak membahas proses perancangan serta implementasi sistem secara menyeluruh.

Berdasarkan beberapa penelitian yang telah diuraikan, dapat disimpulkan bahwa sistem informasi manajemen aset berbasis web memiliki peran penting dalam meningkatkan efisiensi, akurasi, dan efektivitas pengelolaan data aset. Namun, masih terdapat beberapa kekurangan yang dapat dikembangkan, antara lain belum adanya fitur audit trail, kurangnya penyesuaian sistem dengan kebutuhan instansi tertentu, serta belum optimalnya pemanfaatan teknologi seperti QR Code. Penelitian ini bertujuan untuk mengembangkan sistem informasi manajemen aset berbasis web yang dilengkapi dengan fitur audit trail dan QR Code serta disesuaikan dengan kebutuhan operasional RBTV Bengkulu. Dengan demikian, sistem yang dikembangkan diharapkan mampu meningkatkan efisiensi, transparansi, serta akurasi dalam pengelolaan aset.

---

## 2.2 Dasar Teori

Dasar teori merupakan landasan konseptual yang digunakan dalam penelitian untuk menjelaskan berbagai konsep yang berkaitan dengan sistem yang dikembangkan. Bagian ini berfungsi sebagai acuan dalam memahami permasalahan, menganalisis kebutuhan sistem, serta merancang dan mengimplementasikan solusi yang sesuai. Dengan adanya dasar teori yang kuat, penelitian yang dilakukan memiliki pijakan ilmiah yang jelas sehingga hasil yang diperoleh dapat dipertanggungjawabkan secara akademik.

Dalam penelitian ini, dasar teori yang digunakan meliputi konsep sistem, informasi, sistem informasi, manajemen aset, serta teknologi pendukung seperti framework Laravel dan basis data. Konsep-konsep tersebut saling berkaitan dan menjadi fondasi dalam pengembangan sistem informasi manajemen aset berbasis web. Konsep sistem digunakan untuk memahami bagaimana suatu proses pengelolaan aset dapat diorganisasikan dalam suatu alur yang terstruktur, mulai dari input, proses, hingga menghasilkan output berupa informasi. Sementara itu, konsep informasi digunakan untuk menjelaskan bagaimana data yang diolah dapat memberikan nilai tambah dan digunakan sebagai dasar pengambilan keputusan.

Sistem informasi merupakan integrasi dari berbagai komponen seperti manusia, perangkat keras, perangkat lunak, dan basis data yang bekerja secara bersama-sama untuk menghasilkan informasi. Dalam penelitian ini, sistem informasi digunakan untuk mengelola data aset secara terpusat sehingga mempermudah proses pencatatan, pencarian, serta pelaporan data. Selain itu, konsep manajemen aset juga menjadi bagian penting dalam penelitian ini. Manajemen aset mencakup proses pengelolaan aset mulai dari perencanaan, pengadaan, penggunaan, pemeliharaan, hingga penghapusan. Dengan adanya sistem informasi yang mendukung manajemen aset, diharapkan pengelolaan aset dapat dilakukan secara lebih efektif dan efisien.

Dalam pengembangan sistem, digunakan framework Laravel sebagai teknologi utama. Laravel dipilih karena memiliki struktur yang terorganisir serta menyediakan berbagai fitur yang mempermudah pengembangan aplikasi web. Selain itu, penggunaan basis data juga menjadi komponen penting dalam sistem, karena berfungsi untuk menyimpan dan mengelola data secara terstruktur. Dengan mengacu pada dasar teori tersebut, sistem yang dikembangkan diharapkan mampu memberikan solusi terhadap permasalahan pengelolaan aset yang masih dilakukan secara manual. Selain itu, dasar teori ini juga menjadi acuan dalam tahap analisis, perancangan, hingga implementasi sistem yang dilakukan dalam penelitian ini.

### 2.2.1 Definisi Sistem

Sistem merupakan suatu kesatuan yang terdiri dari berbagai komponen yang saling berinteraksi dan bekerja sama untuk mencapai tujuan tertentu. Dalam konteks teknologi informasi, sistem tidak hanya dipahami sebagai kumpulan elemen yang berdiri sendiri, tetapi sebagai suatu mekanisme terintegrasi yang mampu mengolah data menjadi informasi melalui serangkaian proses yang terstruktur dan berkelanjutan.

Menurut Laudon dan Laudon (2021), sistem adalah sekumpulan komponen yang saling berhubungan yang berfungsi untuk mengumpulkan, memproses, menyimpan, dan mendistribusikan informasi guna mendukung pengambilan keputusan serta pengendalian dalam suatu organisasi. Definisi ini menekankan bahwa sistem memiliki peran penting dalam mengelola data secara sistematis sehingga menghasilkan informasi yang berguna.

Sejalan dengan itu, O'Brien dan Marakas (2021) menyatakan bahwa sistem informasi merupakan kombinasi dari manusia, perangkat keras, perangkat lunak, jaringan komunikasi, dan sumber daya data yang bekerja secara bersama-sama untuk mengumpulkan, mengolah, dan menyebarkan informasi dalam organisasi. Hal ini menunjukkan bahwa sistem tidak hanya terdiri dari komponen teknis, tetapi juga melibatkan interaksi manusia sebagai pengguna sistem.

Secara umum, sistem memiliki beberapa karakteristik utama, yaitu:

1. Komponen (Components) — Sistem terdiri dari berbagai elemen yang saling berinteraksi, seperti manusia, perangkat keras, perangkat lunak, dan prosedur.
2. Batasan Sistem (Boundary) — Batasan sistem merupakan garis pemisah antara sistem dengan lingkungan luar.
3. Lingkungan (Environment) — Lingkungan adalah segala sesuatu di luar sistem yang dapat mempengaruhi jalannya sistem.
4. Masukan (Input) — Input adalah data yang dimasukkan ke dalam sistem untuk diproses.
5. Proses (Process) — Proses merupakan kegiatan pengolahan data menjadi informasi.
6. Keluaran (Output) — Output adalah hasil dari proses yang berupa informasi.
7. Pengendalian (Control) — Pengendalian digunakan untuk menjaga agar sistem berjalan sesuai dengan tujuan.
8. Umpan Balik (Feedback) — Feedback digunakan untuk mengevaluasi hasil sistem dan melakukan perbaikan.

Perkembangan teknologi informasi telah menyebabkan perubahan dari sistem manual menjadi sistem berbasis komputer. Sistem berbasis komputer memiliki keunggulan dalam hal kecepatan, akurasi, serta efisiensi dalam pengolahan data. Hal ini sangat penting dalam organisasi yang membutuhkan pengelolaan data dalam jumlah besar.

Dalam penelitian ini, konsep sistem diterapkan dalam pengelolaan aset berbasis web. Sistem menerima input berupa data aset, data barang masuk, dan data barang keluar. Data tersebut kemudian diproses melalui aplikasi berbasis Laravel sehingga menghasilkan output berupa informasi aset, laporan inventaris, serta status kondisi aset.

Selain itu, sistem juga dilengkapi dengan mekanisme pengendalian berupa validasi data dan pengaturan hak akses pengguna untuk menjaga keamanan data. Umpan balik diperoleh dari hasil pengujian sistem dan penggunaan oleh pengguna, yang kemudian digunakan sebagai dasar untuk pengembangan sistem lebih lanjut.

Dengan demikian, penerapan konsep sistem dalam penelitian ini diharapkan mampu meningkatkan efektivitas dan efisiensi dalam pengelolaan aset serta menghasilkan informasi yang akurat dan dapat digunakan sebagai dasar dalam pengambilan keputusan.

### 2.2.1 Definisi Informasi

Informasi merupakan hasil dari pengolahan data yang memiliki makna dan dapat digunakan sebagai dasar dalam pengambilan keputusan. Dalam sistem informasi, data yang masih bersifat mentah akan diolah melalui suatu proses tertentu sehingga menghasilkan informasi yang memiliki nilai guna bagi pengguna. Oleh karena itu, informasi tidak hanya sekadar kumpulan data, tetapi merupakan data yang telah diproses sehingga memiliki konteks dan arti yang jelas.

Menurut Laudon dan Laudon (2021), informasi adalah data yang telah dibentuk menjadi suatu bentuk yang memiliki arti dan berguna bagi manusia. Definisi ini menekankan bahwa informasi memiliki nilai tambah dibandingkan data mentah karena telah melalui proses pengolahan. Sejalan dengan itu, Stair dan Reynolds (2022) menyatakan bahwa informasi merupakan sekumpulan fakta yang diorganisasikan dan diproses sedemikian rupa sehingga memiliki nilai bagi penerimanya. Dengan demikian, informasi berperan penting dalam membantu individu maupun organisasi dalam memahami kondisi yang terjadi serta menentukan tindakan yang tepat.

Agar informasi dapat digunakan secara efektif, informasi harus memiliki kualitas yang baik. Menurut Stair dan Reynolds (2022), terdapat beberapa karakteristik utama informasi yang berkualitas, yaitu:

1. Akurat (Accuracy) — Informasi harus bebas dari kesalahan dan dapat dipercaya. Informasi yang tidak akurat dapat menyebabkan kesalahan dalam pengambilan keputusan.
2. Relevan (Relevance) — Informasi harus sesuai dengan kebutuhan pengguna sehingga dapat memberikan manfaat dalam pengambilan keputusan.
3. Tepat Waktu (Timeliness) — Informasi harus tersedia pada saat dibutuhkan agar tidak kehilangan nilai kegunaannya.
4. Lengkap (Completeness) — Informasi harus mencakup seluruh data yang diperlukan sehingga tidak menimbulkan kesalahpahaman.
5. Mudah Dipahami (Understandability) — Informasi harus disajikan dalam bentuk yang mudah dipahami oleh pengguna.

Dalam suatu sistem informasi, informasi merupakan output utama yang dihasilkan dari proses pengolahan data. Data yang dimasukkan ke dalam sistem akan diproses menggunakan aturan atau logika tertentu sehingga menghasilkan informasi yang berguna. Oleh karena itu, kualitas informasi sangat dipengaruhi oleh kualitas data yang digunakan serta proses pengolahan yang dilakukan oleh sistem.

Dalam konteks manajemen aset, informasi memiliki peran yang sangat penting dalam mendukung kegiatan operasional dan pengambilan keputusan. Informasi yang dihasilkan meliputi data aset, kondisi aset, lokasi aset, serta laporan penggunaan aset. Informasi tersebut digunakan oleh pihak manajemen untuk melakukan monitoring, evaluasi, serta perencanaan pengelolaan aset di masa yang akan datang.

Selain itu, informasi juga berperan dalam meningkatkan transparansi dalam pengelolaan aset. Dengan adanya sistem informasi yang terintegrasi, setiap perubahan data dapat dicatat dan dilacak sehingga meminimalkan risiko terjadinya kesalahan atau manipulasi data. Hal ini sangat penting terutama dalam organisasi yang memiliki banyak aset dan pengguna.

Dalam penelitian ini, sistem informasi yang dikembangkan bertujuan untuk menghasilkan informasi yang akurat, relevan, dan terstruktur mengenai aset yang dimiliki oleh RBTV Bengkulu. Informasi tersebut dihasilkan melalui pengolahan data yang dilakukan secara otomatis oleh sistem berbasis web. Dengan adanya sistem ini, pengguna dapat memperoleh informasi secara cepat tanpa harus melakukan pencarian data secara manual.

Selain itu, sistem juga menyediakan informasi dalam bentuk laporan yang dihasilkan secara otomatis berdasarkan data yang tersimpan dalam database. Laporan ini dapat digunakan sebagai bahan evaluasi serta dasar dalam pengambilan keputusan oleh pihak manajemen.

Dengan demikian, informasi yang dihasilkan oleh sistem informasi manajemen aset diharapkan mampu meningkatkan efektivitas pengelolaan aset serta mendukung pengambilan keputusan yang lebih tepat dan akurat.

### 2.2.1 Definisi Sistem Informasi

Sistem informasi merupakan suatu sistem yang dirancang untuk mengolah data menjadi informasi yang berguna bagi pengguna. Sistem ini mengintegrasikan berbagai komponen seperti manusia, perangkat keras, perangkat lunak, jaringan komunikasi, serta basis data yang bekerja secara bersama-sama untuk mendukung kegiatan operasional dan pengambilan keputusan dalam suatu organisasi.

Menurut Laudon dan Laudon (2021), sistem informasi adalah sekumpulan komponen yang saling berhubungan yang berfungsi untuk mengumpulkan, memproses, menyimpan, dan mendistribusikan informasi guna mendukung pengambilan keputusan serta pengendalian dalam organisasi. Definisi ini menunjukkan bahwa sistem informasi memiliki peran strategis dalam membantu organisasi mengelola data dan menghasilkan informasi yang berkualitas.

Sejalan dengan itu, Stair dan Reynolds (2022) menyatakan bahwa sistem informasi merupakan suatu kumpulan elemen yang saling berinteraksi untuk mengumpulkan, memanipulasi, menyimpan, dan menyebarkan data serta informasi. Dengan adanya sistem informasi, proses pengolahan data dapat dilakukan secara lebih cepat, akurat, dan efisien dibandingkan dengan sistem manual.

Sistem informasi memiliki beberapa komponen utama yang saling mendukung, yaitu:

1. Perangkat Keras (Hardware) — Perangkat keras merupakan komponen fisik yang digunakan untuk menjalankan sistem, seperti komputer, server, dan perangkat input/output.
2. Perangkat Lunak (Software) — Perangkat lunak adalah program atau aplikasi yang digunakan untuk mengolah data menjadi informasi.
3. Basis Data (Database) — Basis data merupakan tempat penyimpanan data yang terstruktur sehingga mudah diakses dan dikelola.
4. Prosedur (Procedures) — Prosedur adalah langkah-langkah atau aturan yang digunakan dalam pengoperasian sistem.
5. Pengguna (User) — Pengguna merupakan pihak yang menggunakan sistem untuk memperoleh informasi.

Selain komponen, sistem informasi juga memiliki fungsi utama, yaitu mengumpulkan data dari berbagai sumber, mengolah data menjadi informasi, menyimpan data secara terstruktur, dan menyajikan informasi kepada pengguna.

Dalam perkembangan teknologi, sistem informasi telah mengalami transformasi dari sistem manual menjadi sistem berbasis komputer dan web. Sistem berbasis web memungkinkan akses data dilakukan secara real-time dan dari berbagai lokasi, sehingga meningkatkan fleksibilitas dan efisiensi dalam pengelolaan informasi.

Dalam konteks penelitian ini, sistem informasi digunakan untuk mengelola data aset secara terpusat dalam suatu aplikasi berbasis web. Sistem ini memungkinkan pengguna untuk melakukan pencatatan data aset, memantau kondisi aset, serta menghasilkan laporan secara otomatis. Dengan adanya sistem ini, proses pengelolaan aset menjadi lebih terstruktur dan efisien.

Selain itu, sistem informasi yang dikembangkan juga dilengkapi dengan fitur audit trail yang berfungsi untuk mencatat setiap aktivitas pengguna. Hal ini bertujuan untuk meningkatkan transparansi dan keamanan data. Sistem juga memanfaatkan teknologi QR Code untuk mempermudah proses pencarian dan identifikasi aset.

Dengan demikian, penerapan sistem informasi dalam penelitian ini diharapkan mampu meningkatkan efektivitas pengelolaan aset serta mendukung pengambilan keputusan yang lebih cepat dan akurat.

### 2.2.4 Manajemen Aset

Manajemen aset merupakan suatu proses pengelolaan aset yang dilakukan secara sistematis dan terstruktur sepanjang siklus hidup aset. Proses ini mencakup perencanaan, pengadaan, penggunaan, pemeliharaan, hingga penghapusan aset. Manajemen aset bertujuan untuk memastikan bahwa aset yang dimiliki oleh suatu organisasi dapat digunakan secara optimal serta memberikan nilai manfaat yang maksimal.

Menurut International Organization for Standardization dalam standar ISO 55000 (2021), manajemen aset adalah aktivitas terkoordinasi dari suatu organisasi untuk merealisasikan nilai dari aset. Definisi ini menekankan bahwa pengelolaan aset tidak hanya berfokus pada pencatatan aset, tetapi juga pada bagaimana aset tersebut dapat memberikan manfaat yang maksimal bagi organisasi.

Sejalan dengan itu, Too dan Weaver (2021) menyatakan bahwa manajemen aset merupakan pendekatan sistematis dalam mengelola aset fisik maupun non-fisik dengan tujuan meningkatkan kinerja dan efisiensi organisasi. Dengan demikian, manajemen aset tidak hanya berfungsi sebagai alat administrasi, tetapi juga sebagai strategi dalam pengelolaan sumber daya.

Secara umum, siklus hidup aset (asset lifecycle) dalam manajemen aset terdiri dari beberapa tahapan utama, yaitu:

1. Perencanaan (Planning) — Tahap ini dilakukan untuk menentukan kebutuhan aset berdasarkan tujuan dan aktivitas organisasi.
2. Pengadaan (Acquisition) — Tahap pengadaan meliputi proses pembelian atau perolehan aset yang dibutuhkan.
3. Penggunaan (Utilization) — Aset digunakan sesuai dengan fungsinya untuk mendukung kegiatan operasional organisasi.
4. Pemeliharaan (Maintenance) — Tahap ini bertujuan untuk menjaga kondisi aset agar tetap dalam keadaan baik dan dapat digunakan secara optimal.
5. Penghapusan (Disposal) — Aset yang sudah tidak digunakan atau tidak layak pakai akan dihapus dari daftar aset.

Dalam praktiknya, manajemen aset memiliki beberapa fungsi utama, antara lain mengelola data aset secara terstruktur, memantau kondisi aset, mengoptimalkan penggunaan aset, mengurangi risiko kehilangan atau kerusakan, serta mendukung pengambilan keputusan.

Dalam sistem manual, pengelolaan aset seringkali menghadapi berbagai kendala seperti kesulitan dalam pencatatan data, keterbatasan dalam pencarian informasi, serta risiko kesalahan dan duplikasi data. Oleh karena itu, diperlukan sistem informasi yang dapat mendukung proses manajemen aset secara lebih efektif dan efisien.

Dalam penelitian ini, konsep manajemen aset diterapkan dalam sistem informasi berbasis web yang dikembangkan untuk mengelola aset di RBTV Bengkulu. Sistem ini memungkinkan pencatatan data aset dilakukan secara terpusat, sehingga memudahkan proses pencarian dan pengelolaan data. Selain itu, sistem juga menyediakan fitur untuk memantau kondisi aset serta mencatat transaksi barang masuk dan keluar.

Sistem yang dikembangkan juga dilengkapi dengan fitur audit trail yang memungkinkan setiap aktivitas pengguna dapat dicatat dan dilacak. Hal ini bertujuan untuk meningkatkan transparansi dan akuntabilitas dalam pengelolaan aset. Selain itu, penggunaan QR Code dalam sistem juga membantu mempercepat proses identifikasi dan pencarian aset.

Dengan demikian, penerapan manajemen aset berbasis sistem informasi diharapkan mampu meningkatkan efisiensi operasional, mengurangi kesalahan pencatatan, serta menyediakan informasi yang akurat dan dapat digunakan sebagai dasar dalam pengambilan keputusan.

### 2.2.5 Laravel

Laravel merupakan framework berbasis PHP yang digunakan untuk membangun aplikasi web dengan struktur yang terorganisir dan efisien. Laravel mengadopsi arsitektur Model-View-Controller (MVC) yang memisahkan antara logika aplikasi, tampilan, dan pengelolaan data, sehingga memudahkan proses pengembangan, pemeliharaan, serta pengujian sistem.

Menurut dokumentasi resmi Laravel (2023), Laravel adalah framework aplikasi web dengan sintaks yang elegan dan ekspresif, yang dirancang untuk mempermudah tugas-tugas umum dalam pengembangan aplikasi web seperti routing, autentikasi, manajemen sesi, dan pengelolaan database. Penggunaan Laravel memungkinkan pengembang untuk fokus pada logika bisnis tanpa harus membangun komponen dasar dari awal.

Selain itu, Purbadian (2021) menyatakan bahwa Laravel merupakan salah satu framework PHP yang populer karena menyediakan berbagai fitur yang lengkap dan mendukung pengembangan aplikasi secara cepat dan terstruktur. Framework ini banyak digunakan dalam pengembangan sistem informasi berbasis web karena kemudahan dalam penggunaannya serta fleksibilitas dalam pengembangan.

Laravel memiliki beberapa fitur utama yang mendukung pengembangan sistem informasi, antara lain:

1. Model-View-Controller (MVC) — Laravel menggunakan arsitektur MVC yang memisahkan antara model (data), view (tampilan), dan controller (logika aplikasi). Hal ini membuat kode lebih terstruktur dan mudah dikelola.
2. Routing — Routing digunakan untuk mengatur alur permintaan pengguna ke dalam sistem. Laravel menyediakan sistem routing yang sederhana dan fleksibel.
3. Eloquent ORM — Eloquent ORM merupakan fitur yang digunakan untuk mempermudah interaksi dengan database menggunakan pendekatan objek.
4. Blade Template Engine — Blade merupakan template engine yang digunakan untuk membangun tampilan (view) secara dinamis.
5. Middleware — Middleware digunakan untuk mengatur akses pengguna terhadap sistem, seperti autentikasi dan otorisasi.
6. Security — Laravel menyediakan fitur keamanan seperti proteksi terhadap serangan SQL Injection, Cross-Site Request Forgery (CSRF), dan Cross-Site Scripting (XSS).

Dalam penelitian ini, Laravel digunakan sebagai framework utama dalam pengembangan sistem informasi manajemen aset berbasis web. Penggunaan Laravel mempermudah dalam membangun sistem yang terstruktur, aman, dan mudah dikembangkan.

Selain itu, Laravel juga mendukung integrasi dengan berbagai teknologi lain seperti database MySQL serta library tambahan yang digunakan dalam sistem, seperti QR Code dan pengolahan data Excel. Hal ini memungkinkan sistem yang dikembangkan memiliki fitur yang lengkap dan sesuai dengan kebutuhan pengguna.

Dengan demikian, penggunaan Laravel dalam penelitian ini diharapkan mampu meningkatkan kualitas sistem yang dikembangkan, baik dari segi struktur kode, keamanan, maupun kemudahan dalam pengembangan dan pemeliharaan sistem.

### 2.2.6 Basis Data

Basis data merupakan kumpulan data yang disimpan secara terstruktur dan saling berhubungan, sehingga dapat diakses, dikelola, dan diperbarui dengan mudah. Dalam sistem informasi, basis data berperan sebagai komponen utama yang digunakan untuk menyimpan dan mengelola data secara efisien. Dengan adanya basis data, proses pengolahan data dapat dilakukan secara terorganisir sehingga menghasilkan informasi yang akurat dan konsisten.

Menurut Connolly dan Begg (2021), basis data adalah kumpulan data yang terintegrasi dan memiliki hubungan logis yang dirancang untuk memenuhi kebutuhan informasi suatu organisasi. Definisi ini menekankan bahwa data dalam basis data tidak berdiri sendiri, melainkan saling berkaitan dan disusun sedemikian rupa sehingga dapat mendukung kebutuhan pengguna.

Sejalan dengan itu, Coronel dan Morris (2022) menyatakan bahwa basis data merupakan struktur penyimpanan data yang memungkinkan data diorganisasikan secara efisien sehingga mudah diakses dan dimodifikasi. Basis data biasanya dikelola menggunakan perangkat lunak yang disebut Database Management System (DBMS), seperti MySQL, PostgreSQL, dan Oracle.

Basis data memiliki beberapa karakteristik utama, antara lain:

1. Terstruktur (Structured) — Data disusun dalam bentuk tabel yang terdiri dari baris dan kolom sehingga mudah dipahami dan dikelola.
2. Terintegrasi (Integrated) — Data saling berhubungan satu sama lain sehingga membentuk suatu kesatuan yang utuh.
3. Dapat Diakses (Accessible) — Data dapat diakses oleh pengguna sesuai dengan hak akses yang diberikan.
4. Konsisten (Consistent) — Data dijaga agar tetap konsisten dan tidak terjadi duplikasi yang tidak diperlukan.
5. Aman (Secure) — Basis data dilengkapi dengan mekanisme keamanan untuk melindungi data dari akses yang tidak sah.

Dalam sistem informasi, basis data memiliki beberapa fungsi utama, yaitu menyimpan data secara terpusat, mempermudah pengelolaan data, mendukung proses pencarian data, menjamin integritas data, serta mendukung pengambilan keputusan.

Dalam penelitian ini, basis data digunakan untuk menyimpan berbagai data yang berkaitan dengan pengelolaan aset, seperti data pengguna, data aset, data kategori, data ruangan, data kondisi, serta data transaksi barang masuk dan keluar. Data tersebut disimpan dalam database MySQL yang dikelola menggunakan sistem manajemen basis data.

Penggunaan basis data dalam sistem ini memungkinkan pengelolaan data dilakukan secara lebih efisien dibandingkan dengan metode manual. Selain itu, basis data juga memungkinkan integrasi data sehingga setiap perubahan yang dilakukan dapat langsung tercermin dalam sistem secara keseluruhan.

Dengan adanya basis data yang terstruktur dan terintegrasi, sistem informasi manajemen aset yang dikembangkan diharapkan mampu menyediakan informasi yang akurat, konsisten, dan mudah diakses oleh pengguna. Hal ini sangat penting dalam mendukung proses pengelolaan aset serta pengambilan keputusan dalam organisasi.

### 2.2.7 Entity Relationship Diagram (ERD)

Entity Relationship Diagram (ERD) merupakan salah satu metode pemodelan data yang digunakan untuk menggambarkan struktur basis data secara konseptual. ERD digunakan untuk menunjukkan hubungan antar entitas dalam suatu sistem serta atribut yang dimiliki oleh masing-masing entitas. Dengan menggunakan ERD, perancang sistem dapat memahami bagaimana data saling berhubungan sehingga mempermudah dalam proses perancangan database.

Menurut Coronel dan Morris (2022), ERD adalah representasi grafis dari entitas, atribut, dan hubungan antar entitas dalam suatu sistem basis data. ERD membantu dalam mengidentifikasi kebutuhan data serta hubungan antar data sebelum sistem diimplementasikan ke dalam database. Dengan demikian, ERD menjadi alat penting dalam tahap perancangan sistem informasi.

Dalam ERD, terdapat beberapa komponen utama, yaitu:

1. Entitas (Entity) — Entitas merupakan objek atau sesuatu yang memiliki keberadaan dan dapat dibedakan dari objek lainnya. Dalam sistem informasi, entitas biasanya direpresentasikan dalam bentuk tabel, seperti tabel aset, kategori, atau pengguna.
2. Atribut (Attribute) — Atribut adalah karakteristik atau sifat yang dimiliki oleh suatu entitas. Setiap entitas memiliki atribut yang digunakan untuk menjelaskan informasi mengenai entitas tersebut, seperti nama aset, kode aset, dan kondisi aset.
3. Relasi (Relationship) — Relasi adalah hubungan antara satu entitas dengan entitas lainnya. Relasi menunjukkan bagaimana data dalam suatu entitas berhubungan dengan data dalam entitas lain.
4. Kunci Utama (Primary Key) — Primary key merupakan atribut yang digunakan untuk mengidentifikasi setiap record dalam suatu tabel secara unik.
5. Kunci Tamu (Foreign Key) — Foreign key adalah atribut yang digunakan untuk menghubungkan satu tabel dengan tabel lainnya.

ERD memiliki beberapa jenis hubungan (relationship) yang umum digunakan, yaitu One to One (1:1), One to Many (1:N), dan Many to Many (M:N).

Dalam penelitian ini, ERD digunakan untuk merancang struktur database sistem informasi manajemen aset. Beberapa entitas utama yang digunakan dalam sistem ini antara lain entitas barang/aset, entitas kategori, entitas ruangan, entitas kondisi, entitas barang masuk, entitas barang keluar, entitas pengguna (users), dan entitas activity log.

Hubungan antar entitas dalam sistem ini dapat dijelaskan sebagai berikut: satu kategori dapat memiliki banyak barang (one-to-many), satu ruangan dapat memiliki banyak barang, satu barang memiliki satu kondisi, dan satu barang dapat memiliki banyak transaksi barang masuk dan keluar.

Dengan adanya ERD, perancangan database menjadi lebih terstruktur dan mudah dipahami. ERD juga membantu dalam memastikan bahwa tidak terjadi redundansi data serta menjaga integritas data dalam sistem.

Selain itu, ERD juga menjadi dasar dalam pembuatan tabel-tabel dalam database MySQL yang digunakan dalam sistem ini. Dengan perancangan yang baik, sistem dapat berjalan lebih optimal dan mudah dalam pengembangan lebih lanjut.

Dengan demikian, penggunaan ERD dalam penelitian ini sangat penting untuk memastikan bahwa struktur database yang dibangun sesuai dengan kebutuhan sistem serta mampu mendukung pengelolaan data aset secara efektif dan efisien.

### 2.2.8 Normalisasi

Normalisasi merupakan proses pengorganisasian data dalam suatu basis data untuk mengurangi redundansi (duplikasi data) serta meningkatkan integritas data. Tujuan utama dari normalisasi adalah memastikan bahwa data disimpan secara efisien dan konsisten sehingga meminimalkan terjadinya anomali dalam proses pengolahan data.

Menurut Connolly dan Begg (2021), normalisasi adalah teknik dalam perancangan basis data yang digunakan untuk mengorganisasikan atribut-atribut dalam suatu relasi sehingga mengurangi redundansi data dan meningkatkan integritas data. Dengan melakukan normalisasi, struktur database menjadi lebih sistematis dan mudah dikelola.

Sejalan dengan itu, Coronel dan Morris (2022) menyatakan bahwa normalisasi merupakan proses bertahap dalam memecah tabel yang kompleks menjadi beberapa tabel yang lebih sederhana, sehingga hubungan antar data menjadi lebih jelas dan tidak terjadi pengulangan data yang tidak diperlukan.

Dalam proses normalisasi, terdapat beberapa tahapan yang dikenal dengan istilah bentuk normal (normal forms), yaitu:

1. First Normal Form (1NF) — Pada bentuk normal pertama, setiap atribut dalam tabel harus memiliki nilai yang bersifat atomik, artinya tidak boleh ada atribut yang memiliki nilai ganda atau berulang dalam satu kolom. Setiap field harus berisi satu nilai saja.
2. Second Normal Form (2NF) — Bentuk normal kedua dicapai jika tabel sudah berada dalam 1NF dan setiap atribut non-primary key bergantung sepenuhnya pada primary key. Dengan kata lain, tidak boleh ada ketergantungan parsial.
3. Third Normal Form (3NF) — Bentuk normal ketiga dicapai jika tabel sudah berada dalam 2NF dan tidak terdapat ketergantungan transitif, yaitu atribut non-primary key tidak boleh bergantung pada atribut non-primary key lainnya.

Proses normalisasi sangat penting dalam perancangan basis data karena dapat menghindari berbagai permasalahan, seperti anomali penyisipan (Insertion Anomaly), anomali penghapusan (Deletion Anomaly), dan anomali pembaruan (Update Anomaly).

Dalam penelitian ini, proses normalisasi dilakukan pada struktur database sistem informasi manajemen aset untuk memastikan bahwa data tersimpan secara efisien dan tidak terjadi duplikasi. Tabel-tabel seperti tabel barang, kategori, ruangan, kondisi, serta transaksi barang masuk dan keluar dirancang dengan memperhatikan prinsip normalisasi hingga mencapai bentuk normal ketiga (3NF).

Sebagai contoh, data kategori tidak disimpan berulang dalam tabel barang, melainkan dipisahkan ke dalam tabel kategori dan dihubungkan melalui foreign key. Hal ini bertujuan untuk menghindari redundansi data serta memudahkan dalam pengelolaan data kategori.

Dengan penerapan normalisasi yang baik, sistem yang dikembangkan memiliki struktur database yang lebih rapi, efisien, dan mudah dikembangkan. Selain itu, normalisasi juga membantu dalam menjaga konsistensi data sehingga informasi yang dihasilkan menjadi lebih akurat.

Dengan demikian, normalisasi merupakan langkah penting dalam perancangan basis data yang bertujuan untuk meningkatkan kualitas dan keandalan sistem informasi.

### 2.2.9 Structured Query Language (SQL)

Structured Query Language (SQL) merupakan bahasa standar yang digunakan untuk mengelola dan memanipulasi data dalam sistem basis data relasional. SQL digunakan untuk melakukan berbagai operasi terhadap data, seperti pengambilan data, penyimpanan data, pembaruan data, serta penghapusan data. SQL menjadi komponen penting dalam sistem informasi karena berperan sebagai penghubung antara aplikasi dengan basis data.

Menurut Coronel dan Morris (2022), SQL adalah bahasa yang digunakan untuk berinteraksi dengan basis data relasional yang memungkinkan pengguna untuk melakukan query terhadap data serta mengelola struktur database. SQL telah menjadi standar internasional yang digunakan oleh berbagai sistem manajemen basis data (DBMS) seperti MySQL, PostgreSQL, dan Oracle.

Sejalan dengan itu, Connolly dan Begg (2021) menyatakan bahwa SQL merupakan bahasa yang dirancang untuk mendefinisikan, mengelola, dan mengontrol data dalam basis data. SQL memungkinkan pengguna untuk mengakses data secara efisien serta memastikan integritas data dalam sistem.

Secara umum, SQL memiliki beberapa fungsi utama, yaitu:

1. Data Definition Language (DDL) — Digunakan untuk mendefinisikan struktur database, seperti membuat tabel, mengubah tabel, dan menghapus tabel. Contoh perintah: CREATE, ALTER, DROP.
2. Data Manipulation Language (DML) — Digunakan untuk mengelola data dalam tabel. Contoh perintah: INSERT (menambahkan data), UPDATE (mengubah data), DELETE (menghapus data).
3. Data Query Language (DQL) — Digunakan untuk mengambil data dari database. Contoh perintah: SELECT.
4. Data Control Language (DCL) — Digunakan untuk mengatur hak akses pengguna terhadap database. Contoh perintah: GRANT, REVOKE.

Dalam sistem informasi, SQL digunakan untuk mengelola seluruh data yang tersimpan dalam basis data. SQL memungkinkan sistem untuk melakukan pencarian data dengan cepat, mengolah data secara efisien, serta menjaga konsistensi data.

Dalam penelitian ini, SQL digunakan melalui integrasi dengan framework Laravel menggunakan fitur Eloquent ORM. Eloquent ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan pendekatan objek tanpa harus menuliskan query SQL secara langsung. Meskipun demikian, SQL tetap menjadi dasar dalam pengelolaan data karena setiap operasi yang dilakukan oleh ORM akan diterjemahkan menjadi query SQL.

Sebagai contoh, proses penyimpanan data aset dalam sistem dilakukan menggunakan perintah INSERT, sedangkan proses pengambilan data aset dilakukan menggunakan perintah SELECT. Selain itu, SQL juga digunakan dalam proses pembaruan data (UPDATE) dan penghapusan data (DELETE) dalam sistem.

Dengan penggunaan SQL, sistem informasi manajemen aset yang dikembangkan mampu mengelola data secara efisien dan terstruktur. SQL juga membantu dalam menjaga integritas data serta memastikan bahwa data yang disimpan dalam database dapat diakses dengan mudah oleh pengguna.

Dengan demikian, SQL merupakan komponen penting dalam sistem informasi yang berperan dalam mengelola data serta mendukung proses pengolahan informasi secara efektif dan efisien.

---

## 2.3 Metode Analisis

Metode analisis merupakan tahapan yang dilakukan untuk memahami kondisi sistem yang sedang berjalan serta mengidentifikasi permasalahan yang terjadi. Tujuan dari analisis adalah untuk memperoleh gambaran yang jelas mengenai kebutuhan sistem yang akan dikembangkan sehingga solusi yang dihasilkan dapat sesuai dengan kebutuhan pengguna.

Dalam penelitian ini, metode analisis yang digunakan adalah metode deskriptif, yaitu dengan menggambarkan kondisi sistem yang berjalan berdasarkan hasil observasi, studi pustaka, serta analisis terhadap proses bisnis yang ada. Metode ini digunakan untuk mengidentifikasi permasalahan yang terjadi dalam pengelolaan aset di RBTV Bengkulu.

Berdasarkan hasil analisis, diketahui bahwa pengelolaan aset masih dilakukan secara manual menggunakan Microsoft Excel. Sistem manual ini memiliki beberapa kelemahan, antara lain:

- Kesulitan dalam pencatatan data aset secara terstruktur
- Proses pencarian data yang lambat
- Tidak adanya pencatatan riwayat perubahan data (audit trail)
- Proses pembuatan laporan yang memerlukan waktu lama
- Risiko kesalahan dan duplikasi data

Untuk menganalisis permasalahan tersebut secara lebih sistematis, digunakan pendekatan analisis yang mengacu pada aspek-aspek utama dalam sistem informasi, yaitu:

1. **Analisis Proses** — Analisis proses dilakukan untuk memahami alur kerja pengelolaan aset yang sedang berjalan. Proses yang dianalisis meliputi pencatatan barang masuk, pencatatan barang keluar, serta pembuatan laporan. Dari hasil analisis, diketahui bahwa proses masih dilakukan secara manual sehingga kurang efisien dan rentan terhadap kesalahan.

2. **Analisis Data** — Analisis data dilakukan untuk mengidentifikasi jenis data yang digunakan dalam sistem. Data yang dianalisis meliputi data aset, data kategori, data ruangan, data kondisi, serta data transaksi. Hasil analisis menunjukkan bahwa data belum terintegrasi dengan baik sehingga sulit untuk dikelola secara efektif.

3. **Analisis Kebutuhan Sistem** — Analisis kebutuhan sistem dilakukan untuk menentukan fitur-fitur yang dibutuhkan dalam sistem yang akan dikembangkan. Berdasarkan hasil analisis, sistem yang dibutuhkan harus mampu mengelola data aset secara terstruktur, menyediakan fitur pencatatan barang masuk dan keluar, menyediakan fitur pencarian data secara cepat, menyediakan laporan secara otomatis, menyediakan fitur audit trail, dan mendukung penggunaan QR Code untuk identifikasi aset.

4. **Analisis Permasalahan** — Permasalahan utama yang dihadapi dalam sistem lama antara lain sistem belum terkomputerisasi secara optimal, data tidak terpusat, tidak adanya sistem monitoring aset secara real-time, dan kurangnya transparansi dalam pengelolaan data.

Berdasarkan hasil analisis tersebut, maka diperlukan suatu sistem informasi berbasis web yang dapat mengatasi permasalahan tersebut. Sistem yang dikembangkan diharapkan mampu meningkatkan efisiensi dalam pengelolaan aset, meminimalkan kesalahan, serta menyediakan informasi yang akurat dan mudah diakses.

Dengan demikian, metode analisis yang dilakukan dalam penelitian ini menjadi dasar dalam perancangan dan pengembangan sistem informasi manajemen aset berbasis web yang sesuai dengan kebutuhan pengguna.

---

## 2.4 Langkah-langkah Pengembangan Aplikasi

Langkah-langkah pengembangan sistem merupakan tahapan yang dilakukan dalam proses pembangunan sistem informasi, mulai dari tahap awal hingga sistem siap digunakan. Metode pengembangan sistem yang digunakan dalam penelitian ini adalah metode Waterfall, yaitu metode pengembangan sistem yang dilakukan secara berurutan dan sistematis. Metode ini dipilih karena memiliki alur yang jelas dan terstruktur sehingga memudahkan dalam proses pengembangan sistem.

Menurut Pressman (2021), model Waterfall merupakan salah satu model pengembangan perangkat lunak yang dilakukan secara berurutan melalui tahapan-tahapan yang sistematis, di mana setiap tahap harus diselesaikan terlebih dahulu sebelum melanjutkan ke tahap berikutnya. Metode ini cocok digunakan dalam pengembangan sistem yang memiliki kebutuhan yang jelas dan tidak banyak mengalami perubahan.

> **Gambar 2.1 Model Waterfall**

Tahapan dalam metode Waterfall yang digunakan dalam penelitian ini meliputi:

1. **Analisis Kebutuhan (Requirement Analysis)** — Pada tahap ini dilakukan pengumpulan dan analisis kebutuhan sistem berdasarkan permasalahan yang ditemukan. Analisis dilakukan melalui observasi terhadap sistem yang berjalan serta studi pustaka. Hasil dari tahap ini berupa spesifikasi kebutuhan sistem yang akan dikembangkan, seperti kebutuhan fitur dan fungsi sistem.

2. **Perancangan Sistem (System Design)** — Tahap perancangan sistem dilakukan untuk merancang struktur sistem yang akan dibangun. Perancangan meliputi perancangan database menggunakan ERD, perancangan alur sistem menggunakan flowchart atau diagram, serta perancangan antarmuka (user interface). Tahap ini bertujuan untuk memberikan gambaran mengenai sistem sebelum diimplementasikan.

3. **Implementasi (Implementation)** — Tahap implementasi merupakan proses pembangunan sistem berdasarkan hasil perancangan. Sistem dikembangkan menggunakan framework Laravel dan database MySQL. Pada tahap ini dilakukan pembuatan kode program, integrasi database, serta pengembangan fitur-fitur sistem seperti dashboard, CRUD data, audit trail, laporan, dan QR Code.

4. **Pengujian (Testing)** — Tahap pengujian dilakukan untuk memastikan bahwa sistem yang dikembangkan berjalan sesuai dengan kebutuhan. Pengujian dilakukan menggunakan metode black-box testing untuk menguji fungsi sistem dan white-box testing untuk menguji logika program. Hasil pengujian digunakan untuk mengetahui apakah terdapat kesalahan dalam sistem yang perlu diperbaiki.

5. **Pemeliharaan (Maintenance)** — Tahap pemeliharaan dilakukan setelah sistem diimplementasikan. Pada tahap ini dilakukan perbaikan jika terdapat kesalahan serta pengembangan sistem untuk meningkatkan kinerja dan menyesuaikan dengan kebutuhan pengguna.

Metode Waterfall dipilih dalam penelitian ini karena sesuai dengan karakteristik pengembangan sistem yang dilakukan secara terstruktur dan memiliki kebutuhan yang relatif jelas. Dengan menggunakan metode ini, setiap tahapan dapat dilakukan secara sistematis sehingga meminimalkan kesalahan dalam proses pengembangan.

Dengan demikian, langkah-langkah pengembangan sistem yang digunakan dalam penelitian ini diharapkan mampu menghasilkan sistem informasi manajemen aset yang sesuai dengan kebutuhan serta dapat digunakan secara optimal oleh pengguna.
