# BAB V KESIMPULAN DAN SARAN

## 5.1 Kesimpulan

Berdasarkan hasil pelaksanaan Kerja Praktik yang telah dilakukan di Rakyat Bengkulu Televisi (RBTV), dapat ditarik kesimpulan sebagai berikut:

1. **Sistem berhasil dirancang dan dibangun** sesuai dengan kebutuhan yang diidentifikasi. SimAset — Sistem Informasi Manajemen Aset Barang Kantor Berbasis Web berhasil dikembangkan menggunakan framework Laravel 12 dengan fitur-fitur lengkap yang mencakup manajemen aset, master data barang dan ruangan, QR Code, maintenance tracking, import/export data, laporan, manajemen pengguna, dan audit log.

2. **Teknologi QR Code berhasil diintegrasikan** ke dalam sistem untuk mempermudah identifikasi dan pelacakan aset. Setiap aset memiliki QR Code unik yang berisi URL menuju halaman detail aset, sehingga proses identifikasi aset dapat dilakukan dengan cepat hanya dengan memindai kode menggunakan kamera perangkat.

3. **Fitur import/export dan laporan** berhasil diimplementasikan dengan baik. Sistem mendukung import data massal dari Excel/CSV dengan validasi per baris, export ke format Excel dan PDF dengan filter yang fleksibel, serta pembuatan laporan aset, laporan per ruangan, dan laporan maintenance.

4. **Sistem audit log** berhasil diimplementasikan untuk meningkatkan akuntabilitas pengelolaan data. Seluruh aktivitas pengguna (login, logout, create, update, delete) dicatat secara otomatis beserta informasi pengguna, waktu, IP address, dan detail aktivitas.

5. **Hasil pengujian menunjukkan tingkat kelayakan yang sangat tinggi.** Berdasarkan pengujian dengan kuesioner skala Likert kepada dua kelompok responden:
   - Pengguna/Staff (12 responden): rata-rata skor **4.61** — Sangat Layak
   - Admin (1 responden): rata-rata skor **4.65** — Sangat Layak

6. **Sistem berhasil mengatasi permasalahan** yang diidentifikasi pada sistem pengelolaan aset manual yang sebelumnya digunakan di RBTV Bengkulu, yaitu ketidakakuratan data, kesulitan pelacakan aset, tidak adanya sistem maintenance, dan tidak adanya audit trail.

---

## 5.2 Saran

Berdasarkan hasil pelaksanaan Kerja Praktik dan evaluasi sistem yang telah dikembangkan, beberapa saran untuk pengembangan lebih lanjut adalah sebagai berikut:

### Saran untuk Pengembangan Sistem:

1. **Pengembangan Aplikasi Mobile:** Mengembangkan aplikasi mobile (Android/iOS) yang terintegrasi dengan sistem web untuk memudahkan pengelolaan aset di lapangan, terutama untuk fitur QR Code scanner dan update kondisi aset.

2. **Fitur Notifikasi In-App:** Menambahkan sistem notifikasi real-time di dalam aplikasi (in-app notification) untuk menginformasikan pengguna tentang aset yang memerlukan perhatian, seperti aset yang sudah lama dalam status maintenance.

3. **Jadwal Maintenance Berkala:** Menambahkan fitur penjadwalan maintenance berkala untuk aset-aset tertentu, dilengkapi dengan pengingat otomatis sebelum jadwal maintenance tiba.

4. **Riwayat Mutasi Aset:** Mengaktifkan dan mengembangkan fitur riwayat mutasi aset yang sudah tersedia dalam skema database, untuk mencatat perpindahan aset antar ruangan secara lengkap.

5. **Integrasi dengan Sistem Keuangan:** Mengintegrasikan sistem dengan modul keuangan untuk mendukung perhitungan depresiasi aset dan pelaporan nilai aset secara otomatis.

6. **Peningkatan Visualisasi Dashboard:** Menambahkan lebih banyak grafik dan visualisasi data pada dashboard, seperti tren penambahan aset per bulan, grafik nilai aset per kategori, dan peta lokasi aset per ruangan.

7. **Fitur Backup dan Restore:** Menambahkan fitur backup database otomatis dan restore untuk meningkatkan keamanan data.

### Saran untuk RBTV Bengkulu:

1. Melakukan pelatihan kepada seluruh staf yang akan menggunakan sistem SimAset agar dapat memanfaatkan seluruh fitur yang tersedia secara optimal.
2. Melakukan migrasi data aset yang sudah ada dari spreadsheet ke sistem SimAset secara bertahap menggunakan fitur import.
3. Menetapkan prosedur operasional standar (SOP) untuk pengelolaan aset menggunakan sistem SimAset.
4. Melakukan backup database secara berkala untuk mencegah kehilangan data.

### Saran untuk Penelitian Selanjutnya:

1. Mengembangkan penelitian lebih lanjut mengenai integrasi sistem manajemen aset dengan teknologi IoT (Internet of Things) untuk pemantauan kondisi aset secara real-time.
2. Mengkaji penerapan machine learning untuk prediksi kebutuhan maintenance aset berdasarkan pola historis kondisi aset.
