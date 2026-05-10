# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Pengelolaan aset merupakan salah satu aspek penting dalam operasional suatu organisasi atau perusahaan. Aset barang kantor seperti peralatan elektronik, furnitur, dan perlengkapan teknis merupakan sumber daya yang memiliki nilai ekonomis dan perlu dikelola secara efektif agar dapat mendukung produktivitas kerja secara optimal. Tanpa sistem pengelolaan yang baik, organisasi berisiko mengalami kehilangan aset, ketidakakuratan data inventaris, serta kesulitan dalam melacak kondisi dan lokasi aset secara real-time.

Rakyat Bengkulu Televisi (RBTV) merupakan salah satu stasiun televisi lokal yang beroperasi di Kota Bengkulu. Sebagai perusahaan media yang bergerak di bidang penyiaran, RBTV memiliki berbagai jenis aset barang kantor yang tersebar di berbagai ruangan, mulai dari peralatan kamera, audio, komputer, lighting, hingga furnitur dan peralatan kantor lainnya. Pengelolaan aset yang baik sangat penting bagi RBTV untuk memastikan keberlangsungan operasional siaran yang berkualitas.

Berdasarkan hasil observasi dan wawancara yang dilakukan selama pelaksanaan Kerja Praktik, diketahui bahwa RBTV masih mengelola data aset barang kantor secara manual menggunakan dokumen fisik dan spreadsheet sederhana. Kondisi ini menimbulkan beberapa permasalahan, antara lain: data aset yang tidak terupdate secara real-time, kesulitan dalam melacak lokasi dan kondisi aset, tidak adanya sistem notifikasi untuk aset yang memerlukan perawatan, serta proses pencarian dan pelaporan data aset yang memakan waktu lama.

Perkembangan teknologi informasi, khususnya teknologi web, membuka peluang besar untuk mengatasi permasalahan tersebut. Pengembangan sistem informasi manajemen aset berbasis web dapat menjadi solusi yang efektif dan efisien. Sistem berbasis web memiliki keunggulan dapat diakses dari berbagai perangkat tanpa perlu instalasi khusus, memungkinkan pengelolaan data secara terpusat, serta mendukung kolaborasi antar pengguna secara bersamaan.

Salah satu teknologi yang relevan untuk mendukung pengelolaan aset adalah QR Code. Dengan mengintegrasikan QR Code pada setiap aset, proses identifikasi dan pelacakan aset dapat dilakukan dengan cepat hanya dengan memindai kode menggunakan kamera perangkat. Teknologi ini telah terbukti efektif dalam berbagai sistem manajemen aset di berbagai organisasi.

Berdasarkan latar belakang tersebut, penulis mengembangkan **SimAset** — Sistem Informasi Manajemen Aset Barang Kantor Berbasis Web pada Rakyat Bengkulu Televisi (RBTV). Sistem ini dibangun menggunakan framework Laravel 12 dengan fitur-fitur utama meliputi manajemen aset, manajemen master data (barang dan ruangan), QR Code per aset, pelacakan maintenance, import/export data, laporan, audit log, dan manajemen pengguna berbasis role. Pengembangan sistem ini diharapkan dapat meningkatkan efisiensi dan akurasi pengelolaan aset barang kantor di RBTV Bengkulu.

---

## 1.2 Rumusan Masalah

1. Bagaimana merancang dan membangun sistem informasi manajemen aset barang kantor berbasis web yang dapat mengelola data aset secara terpusat dan real-time di RBTV Bengkulu?
2. Bagaimana mengintegrasikan teknologi QR Code ke dalam sistem untuk mempermudah identifikasi dan pelacakan aset secara cepat?
3. Bagaimana sistem dapat menyediakan fitur pelaporan, import/export data, dan audit log untuk mendukung pengambilan keputusan manajemen?

---

## 1.3 Batasan Masalah

1. Sistem dikembangkan khusus untuk pengelolaan aset barang kantor di lingkungan RBTV Bengkulu.
2. Sistem dibangun berbasis web menggunakan framework Laravel 12 dan database MySQL/SQLite.
3. Fitur QR Code hanya mencakup generate, download, batch print, dan scanner — tidak mencakup integrasi dengan sistem eksternal.
4. Sistem memiliki dua level hak akses: Admin dan Staff.
5. Fitur laporan mencakup laporan aset, laporan per ruangan, dan laporan maintenance dalam format PDF dan CSV.
6. Sistem tidak mencakup pengelolaan aset tidak berwujud (intangible assets) seperti lisensi perangkat lunak atau hak paten.
7. Notifikasi email hanya dikirimkan untuk event maintenance selesai dan pembuatan akun pengguna baru.

---

## 1.4 Tujuan Kerja Praktik

1. Merancang dan membangun sistem informasi manajemen aset barang kantor berbasis web yang dapat digunakan oleh RBTV Bengkulu secara efektif.
2. Mengintegrasikan teknologi QR Code untuk mempermudah identifikasi, pelacakan, dan pengelolaan aset secara digital.
3. Menyediakan fitur import/export data dan laporan yang memudahkan proses administrasi dan pengambilan keputusan manajemen.
4. Mengimplementasikan sistem audit log untuk meningkatkan akuntabilitas dan keamanan pengelolaan data aset.
5. Menerapkan ilmu dan keterampilan yang diperoleh selama perkuliahan dalam pengembangan sistem informasi nyata di lingkungan kerja profesional.

---

## 1.5 Manfaat Kerja Praktik

### Bagi RBTV Bengkulu:
1. Memiliki sistem pengelolaan aset yang terpusat, akurat, dan dapat diakses secara real-time.
2. Mempermudah proses identifikasi dan pelacakan aset melalui teknologi QR Code.
3. Meningkatkan efisiensi proses administrasi aset, termasuk pencatatan, pelaporan, dan pemantauan kondisi aset.
4. Memiliki sistem notifikasi maintenance yang membantu dalam perencanaan perawatan aset secara proaktif.
5. Meningkatkan akuntabilitas pengelolaan aset melalui fitur audit log yang mencatat seluruh aktivitas pengguna.

### Bagi Penulis:
1. Mendapatkan pengalaman nyata dalam pengembangan sistem informasi berbasis web di lingkungan kerja profesional.
2. Menerapkan dan mengembangkan kemampuan dalam penggunaan framework Laravel, database MySQL, dan teknologi pendukung lainnya.
3. Meningkatkan kemampuan analisis kebutuhan, perancangan sistem, dan implementasi perangkat lunak.
4. Memenuhi persyaratan akademik mata kuliah Kerja Praktik Program Studi Informatika Universitas Bengkulu.

### Bagi Universitas Bengkulu:
1. Memperkuat hubungan kerjasama antara Universitas Bengkulu dengan industri media di Kota Bengkulu.
2. Menjadi referensi dan bahan pembelajaran bagi mahasiswa lain dalam pengembangan sistem informasi manajemen aset.

---

## 1.6 Waktu dan Tempat Pelaksanaan

**Tempat Pelaksanaan:**
Rakyat Bengkulu Televisi (RBTV)
Jl. [Alamat RBTV], Kota Bengkulu

**Waktu Pelaksanaan:**
[Bulan Mulai] – [Bulan Selesai] 2025/2026

**Bidang Kerja:**
Divisi Teknologi Informasi / Bagian Umum dan Administrasi
