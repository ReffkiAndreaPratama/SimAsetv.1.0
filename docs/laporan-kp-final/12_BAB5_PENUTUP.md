# BAB V PENUTUP

## 5.1 Kesimpulan

Berdasarkan hasil penelitian, perancangan, implementasi, dan pengujian yang telah dilakukan, dapat ditarik kesimpulan sebagai berikut:

1. Sistem pengelolaan aset barang yang berjalan di RBTV Bengkulu sebelumnya masih dilakukan secara manual menggunakan dokumen tertulis dan file spreadsheet yang terpisah. Kondisi tersebut menyebabkan proses pencarian data memerlukan waktu yang lama, informasi kondisi dan lokasi aset tidak selalu akurat, serta penyusunan laporan inventaris tidak dapat dilakukan secara cepat dan efisien.

2. Sistem Informasi Manajemen Aset Barang berbasis web berhasil dirancang dan dibangun menggunakan framework Laravel dengan basis data MySQL. Sistem yang dikembangkan mencakup fitur pengelolaan data aset, manajemen kategori barang, manajemen ruangan, pembuatan dan pemindaian QR Code, pencatatan pemeliharaan, impor dan ekspor data, pembuatan laporan otomatis, manajemen pengguna, serta audit log aktivitas.

3. Berdasarkan hasil white-box testing, seluruh jalur logika pada fungsi-fungsi kritis sistem berjalan sesuai dengan algoritma yang telah dirancang tanpa ditemukan kesalahan logika. Berdasarkan hasil black-box testing terhadap 20 skenario pengujian, seluruh fitur sistem menghasilkan output yang sesuai dengan yang diharapkan dan memenuhi seluruh kebutuhan fungsional yang telah ditetapkan.

4. Sistem yang dibangun terbukti mampu mengatasi permasalahan yang sebelumnya dihadapi dalam pengelolaan aset di RBTV Bengkulu. Data aset kini tersimpan secara terpusat dalam basis data yang terstruktur, proses pencarian dan pembaruan data dapat dilakukan dengan cepat, laporan inventaris dapat dihasilkan secara otomatis, dan seluruh aktivitas pengguna tercatat dalam audit log untuk mendukung akuntabilitas pengelolaan aset.

---

## 5.2 Saran

Berdasarkan hasil penelitian yang telah dilakukan, terdapat beberapa saran yang dapat dijadikan bahan pertimbangan untuk pengembangan sistem lebih lanjut:

1. Sistem yang telah dibangun dapat dikembangkan dengan menambahkan fitur notifikasi otomatis melalui email atau pesan singkat untuk mengingatkan staf mengenai jadwal pemeliharaan aset yang akan jatuh tempo, sehingga pemeliharaan dapat dilakukan secara lebih terencana dan tepat waktu.

2. Fitur perhitungan penyusutan nilai aset secara otomatis dapat ditambahkan pada pengembangan berikutnya untuk mendukung pengelolaan aset dari aspek keuangan dan membantu pihak manajemen dalam perencanaan anggaran pengadaan aset baru.

3. Sistem dapat dikembangkan dengan menambahkan fitur manajemen pengadaan aset yang terintegrasi dengan sistem pengelolaan aset yang sudah ada, sehingga seluruh siklus hidup aset mulai dari pengadaan hingga penghapusan dapat dikelola dalam satu platform yang terpadu.

4. Untuk meningkatkan keamanan sistem, disarankan agar ditambahkan fitur autentikasi dua faktor (two-factor authentication) dan pembatasan percobaan login untuk mencegah akses tidak sah ke dalam sistem.

5. Pengembangan aplikasi mobile berbasis Android atau iOS dapat dipertimbangkan untuk memudahkan staf dalam melakukan pemindaian QR Code dan pembaruan kondisi aset secara langsung di lapangan tanpa harus menggunakan komputer.
