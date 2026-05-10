# MODUL 11 - PENUTUP DAN PENGEMBANGAN LANJUTAN

## 11.1 Ringkasan Pengembangan Sistem

SimAset merupakan hasil pengembangan sistem informasi manajemen aset barang kantor yang dirancang untuk mendukung pengelolaan aset secara digital, terstruktur, dan mudah diakses di lingkungan RBTV Bengkulu. Sistem ini menggantikan proses pencatatan manual berbasis spreadsheet yang tidak terintegrasi dan rawan kesalahan.

Sistem ini mengintegrasikan data aset dengan teknologi QR Code sehingga mampu menyajikan informasi aset tidak hanya dalam bentuk teks dan tabel, tetapi juga melalui identifikasi fisik yang cepat menggunakan kamera smartphone. Pengembangan sistem ini dilakukan secara bertahap dan sistematis, dimulai dari analisis kebutuhan, perancangan sistem, persiapan lingkungan pengembangan, implementasi database, penerapan autentikasi dan hak akses, manajemen data aset, integrasi QR Code dan maintenance tracking, penyajian dashboard dan fitur import/export/laporan, hingga pengujian dan evaluasi sistem. Setiap modul yang dibahas sebelumnya saling berkaitan dan membentuk satu kesatuan sistem yang utuh. Sistem yang dikembangkan mampu memenuhi kebutuhan dasar pengelolaan aset barang kantor RBTV Bengkulu, baik bagi Admin sebagai pengelola sistem maupun Staff sebagai pengguna operasional.

## 11.2 Kesimpulan

Berdasarkan hasil pengembangan dan pengujian yang telah dilakukan, dapat disimpulkan beberapa hal sebagai berikut:

1. SimAset berhasil dikembangkan sebagai aplikasi berbasis web yang mengintegrasikan pengelolaan data aset dengan fitur QR Code untuk identifikasi cepat.
2. Sistem mampu menyajikan informasi aset secara lengkap, akurat, dan mudah dipahami oleh pengguna melalui dashboard yang informatif.
3. Implementasi QR Code menggunakan SimpleSoftwareIO dan qrserver.com API memberikan nilai tambah dalam identifikasi aset di lapangan.
4. Fitur maintenance tracking dengan notifikasi email otomatis memastikan setiap proses perbaikan aset terdokumentasi dan pihak terkait selalu mendapat informasi terkini.
5. Penerapan autentikasi berbasis role (Admin/Staff) dan audit log mampu menjaga keamanan data dan akuntabilitas pengelolaan aset.
6. Hasil pengujian blackbox testing dengan 85 skenario menunjukkan bahwa sistem berfungsi dengan baik dan dapat digunakan sebagai sistem informasi manajemen aset barang kantor.

Dengan demikian, sistem ini dapat dijadikan sebagai salah satu solusi digital dalam mendukung pengelolaan aset barang kantor RBTV Bengkulu secara efisien dan akuntabel.

## 11.3 Keterbatasan Sistem

Meskipun sistem telah dikembangkan dan diuji dengan baik, terdapat beberapa keterbatasan yang perlu diperhatikan, antara lain:

1. Sistem masih berbasis web dan belum dikembangkan dalam bentuk aplikasi mobile native.
2. Generate QR Code memerlukan koneksi internet karena menggunakan API eksternal (qrserver.com).
3. Sistem belum menyediakan fitur perhitungan depresiasi atau nilai buku aset secara otomatis.
4. Sistem belum terintegrasi dengan sistem keuangan atau akuntansi.
5. Fitur mutasi aset (perpindahan antar ruangan dengan riwayat lengkap) belum diimplementasikan secara penuh.

Keterbatasan ini menjadi catatan penting sebagai bahan evaluasi dan pengembangan sistem di masa mendatang.

## 11.4 Rekomendasi Pengembangan Lanjutan

Berdasarkan keterbatasan yang telah diidentifikasi, beberapa rekomendasi pengembangan lanjutan yang dapat dilakukan antara lain:

1. **Pengembangan Aplikasi Mobile**
   Mengembangkan versi aplikasi mobile berbasis Android atau iOS agar sistem lebih mudah diakses oleh pengelola di lapangan, terutama untuk fitur pemindaian QR Code.

2. **QR Code Offline**
   Mengganti API eksternal dengan generate QR Code sepenuhnya di server menggunakan SimpleSoftwareIO yang sudah terinstal, sehingga tidak bergantung pada koneksi internet.

3. **Fitur Mutasi Aset**
   Mengaktifkan tabel riwayat_mutasi yang sudah ada di database untuk mencatat perpindahan aset antar ruangan dengan riwayat lengkap.

4. **Depresiasi Aset**
   Menambahkan fitur perhitungan depresiasi aset berdasarkan umur ekonomis dan metode yang dipilih (garis lurus atau saldo menurun).

5. **Integrasi Sistem Keuangan**
   Mengintegrasikan data nilai aset dengan sistem keuangan atau akuntansi untuk pencatatan yang lebih komprehensif.

6. **Notifikasi Real-Time**
   Implementasi WebSocket menggunakan Laravel Echo untuk notifikasi real-time saat ada aset baru masuk maintenance, tanpa perlu refresh halaman.

7. **Pengembangan Dashboard Analitik**
   Menambahkan fitur analitik lanjutan seperti tren penambahan aset per bulan, analisis umur aset, dan prediksi kebutuhan maintenance.

8. **Peningkatan Keamanan Sistem**
   Mengimplementasikan Two-Factor Authentication (2FA) untuk akun Admin dan mekanisme keamanan lanjutan lainnya.

Rekomendasi ini diharapkan dapat meningkatkan kualitas dan manfaat sistem di masa depan.

## 11.5 Penutup

Modul 11 menutup seluruh rangkaian modul pengembangan SimAset. Melalui modul ini, dapat disimpulkan bahwa sistem yang dikembangkan telah memenuhi tujuan utama sebagai sistem informasi manajemen aset barang kantor berbasis web yang terintegrasi dengan fitur QR Code dan audit log. Dengan dokumentasi modul yang lengkap dan terstruktur, sistem ini tidak hanya dapat digunakan sebagai aplikasi siap pakai, tetapi juga sebagai referensi pembelajaran dalam pengembangan sistem informasi manajemen aset berbasis web menggunakan Laravel. Diharapkan sistem ini dapat memberikan manfaat nyata bagi pengelola aset RBTV, meningkatkan efisiensi operasional, serta mendukung akuntabilitas pengelolaan aset barang kantor secara digital.
