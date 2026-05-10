# MODUL 10 - PENGUJIAN SISTEM DAN EVALUASI

## 10.1 Pendahuluan

Pengujian sistem merupakan tahap akhir yang sangat penting dalam proses pengembangan SimAset. Tahap ini bertujuan untuk memastikan bahwa seluruh fitur dan fungsi sistem telah berjalan sesuai dengan kebutuhan yang telah dirumuskan pada tahap analisis dan perancangan. Pengujian tidak hanya berfokus pada apakah sistem dapat dijalankan, tetapi juga pada aspek kualitas sistem, seperti keandalan, kemudahan penggunaan, keamanan, dan kinerja. Dengan melakukan pengujian secara menyeluruh, potensi kesalahan atau kekurangan sistem dapat diidentifikasi dan diperbaiki sebelum sistem digunakan secara luas. Modul ini membahas metode pengujian yang digunakan, skenario pengujian sistem, hasil pengujian, serta evaluasi sistem berdasarkan hasil pengujian tersebut.

## 10.2 Blackbox Testing

Blackbox testing merupakan metode pengujian sistem yang berfokus pada pengujian fungsi-fungsi sistem tanpa memperhatikan struktur internal kode program. Pengujian ini dilakukan dengan memberikan input tertentu dan mengamati output yang dihasilkan oleh sistem.

### 10.2.1 Tujuan Blackbox Testing

Tujuan dari blackbox testing antara lain:

1. Memastikan setiap fitur sistem berfungsi sesuai dengan kebutuhan.
2. Mengidentifikasi kesalahan fungsional pada sistem.
3. Memastikan sistem memberikan output yang benar terhadap input tertentu.
4. Menguji stabilitas sistem dalam berbagai skenario penggunaan.

### 10.2.2 Skenario Blackbox Testing

Pengujian blackbox dilakukan pada seluruh modul sistem, antara lain:

**1. Pengujian Login**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Login Admin dengan data valid | Admin berhasil masuk ke dashboard | Berhasil |
| 2 | Login Staff dengan data valid | Staff berhasil masuk ke dashboard | Berhasil |
| 3 | Login dengan data tidak valid | Sistem menampilkan pesan kesalahan | Berhasil |
| 4 | Login dengan field kosong | Sistem menampilkan error validasi | Berhasil |

**2. Pengujian Hak Akses**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Akses dashboard tanpa login | Dialihkan ke halaman login | Berhasil |
| 2 | Admin mengakses manajemen pengguna | Akses diberikan | Berhasil |
| 3 | Staff mengakses manajemen pengguna | HTTP 403 Forbidden | Berhasil |
| 4 | Staff mengakses audit log | HTTP 403 Forbidden | Berhasil |
| 5 | Akses detail aset tanpa login (QR) | Halaman detail tampil | Berhasil |

**3. Pengujian CRUD Data Aset**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Menambah aset dengan data valid | Data berhasil disimpan, kode auto-generated | Berhasil |
| 2 | Menambah aset dengan serial duplikat | Error "serial number sudah terdaftar" | Berhasil |
| 3 | Upload foto format tidak valid | Error "format tidak valid" | Berhasil |
| 4 | Upload foto ukuran melebihi 2MB | Error "ukuran melebihi batas" | Berhasil |
| 5 | Mengubah data aset | Data berhasil diperbarui | Berhasil |
| 6 | Menghapus aset | Soft delete berhasil | Berhasil |
| 7 | Batch delete beberapa aset | Semua aset terpilih ter-soft-delete | Berhasil |

**4. Pengujian Master Data Barang**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Menambah barang baru | Data berhasil disimpan | Berhasil |
| 2 | Mengubah data barang | Data berhasil diperbarui | Berhasil |
| 3 | Menghapus barang | Soft delete berhasil | Berhasil |

**5. Pengujian Master Data Ruangan**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Menambah ruangan baru | Data berhasil disimpan | Berhasil |
| 2 | Mengubah data ruangan | Data berhasil diperbarui | Berhasil |
| 3 | Menghapus ruangan kosong | Ruangan berhasil dihapus | Berhasil |
| 4 | Menghapus ruangan berisi aset | Error "masih memiliki aset" | Berhasil |

**6. Pengujian QR Code**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Generate QR Code (online) | File PNG tersimpan di qr_codes/ | Berhasil |
| 2 | Generate QR Code (offline) | Pesan error, QR tidak ter-generate | Berhasil |
| 3 | Cetak QR Code individual | Halaman cetak terbuka | Berhasil |
| 4 | Batch print QR Code | Halaman batch print tampil | Berhasil |
| 5 | Scanner web — aset ditemukan | Informasi aset tampil | Berhasil |
| 6 | Scanner web — aset tidak ada | Pesan "Aset tidak ditemukan" | Berhasil |

**7. Pengujian Maintenance**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Menandai aset masuk maintenance | Status berubah ke Maintenance | Berhasil |
| 2 | Aset tampil di dashboard maintenance | Aset muncul di daftar | Berhasil |
| 3 | Menandai maintenance selesai | Status kembali Aktif | Berhasil |
| 4 | Email notifikasi terkirim | Email tercatat di log (dev mode) | Berhasil |

**8. Pengujian Import**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Import aset dengan data valid | Data berhasil diimport | Berhasil |
| 2 | Import aset kode barang tidak ada | Error per baris dilaporkan | Berhasil |
| 3 | Import file format salah | Error validasi format | Berhasil |
| 4 | Download template import | File CSV template terunduh | Berhasil |

**9. Pengujian Export dan Laporan**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Export aset Excel | File .xlsx terunduh dengan styling | Berhasil |
| 2 | Export aset PDF | File .pdf terunduh | Berhasil |
| 3 | Export CSV maintenance | File .csv dengan UTF-8 BOM | Berhasil |
| 4 | Laporan per ruangan PDF | PDF dengan daftar aset ruangan | Berhasil |

**10. Pengujian Dashboard**

| No | Skenario Pengujian | Langkah Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|--------------------|----------------------|-------|
| 1 | Akses dashboard | Login sebagai Admin | Halaman dashboard tampil | Berhasil |
| 2 | Menampilkan statistik aset | Akses dashboard | Angka sesuai data database | Berhasil |
| 3 | Menampilkan chart kondisi | Akses dashboard | Chart donut tampil dengan benar | Berhasil |
| 4 | Menampilkan aktivitas terbaru | Akses dashboard | Log aktivitas terbaru tampil | Berhasil |
| 5 | Navigasi menu sidebar | Klik menu di sidebar | Sistem berpindah halaman | Berhasil |
| 6 | Akses cepat (quick access) | Klik tombol akses cepat | Sistem mengarahkan ke halaman tujuan | Berhasil |

**11. Pengujian Manajemen Pengguna (Admin Only)**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Menambah pengguna baru | Pengguna berhasil ditambahkan | Berhasil |
| 2 | Menambah pengguna email duplikat | Error "email sudah digunakan" | Berhasil |
| 3 | Menambah pengguna password lemah | Error validasi password | Berhasil |
| 4 | Mengubah data pengguna | Data berhasil diperbarui | Berhasil |
| 5 | Menghapus pengguna lain | Pengguna berhasil dihapus | Berhasil |
| 6 | Menghapus akun sendiri | Error "tidak bisa menghapus akun sendiri" | Berhasil |

**12. Pengujian Audit Log (Admin Only)**

| No | Skenario Pengujian | Hasil yang Diharapkan | Hasil |
|----|--------------------|-----------------------|-------|
| 1 | Menampilkan audit log | 39 record tampil, terbaru di atas | Berhasil |
| 2 | Filter by pengguna | Hanya log pengguna tersebut tampil | Berhasil |
| 3 | Filter by jenis aktivitas | Hanya log jenis tersebut tampil | Berhasil |
| 4 | Pencarian kata kunci | Log yang relevan tampil | Berhasil |

Setiap skenario diuji untuk memastikan fungsi berjalan sesuai harapan.

## 10.3 Usability Testing

Usability testing dilakukan untuk menguji tingkat kemudahan penggunaan SimAset dari sudut pandang pengguna. Pengujian ini penting karena sistem informasi manajemen aset ditujukan untuk pengelola dengan latar belakang dan tingkat pemahaman teknologi yang beragam. Melalui usability testing, dapat diketahui apakah sistem mudah digunakan, navigasi mudah dipahami, serta fitur-fitur utama dapat diakses dengan nyaman oleh pengguna.

### 10.3.1 Tujuan Usability Testing

Tujuan dari usability testing pada sistem ini adalah sebagai berikut:

1. Menilai kemudahan navigasi sistem bagi pengguna.
2. Mengukur tingkat kenyamanan pengguna dalam menggunakan sistem.
3. Mengidentifikasi bagian sistem yang dirasa membingungkan atau sulit digunakan.
4. Menilai efektivitas fitur QR Code dalam membantu pengguna mengidentifikasi aset.
5. Meningkatkan pengalaman pengguna (user experience) secara keseluruhan.

### 10.3.2 Metode Usability Testing

Usability testing dilakukan dengan metode pengujian kualitatif, yaitu dengan mengamati langsung interaksi pengguna saat menggunakan sistem. Pengujian dilakukan dengan langkah-langkah sebagai berikut:

1. Mengamati pengguna saat mengakses dan menggunakan sistem.
2. Memberikan tugas sederhana kepada pengguna, seperti menambah aset baru, mencari aset, dan memindai QR Code.
3. Mengumpulkan umpan balik dari pengguna terkait kemudahan penggunaan, navigasi, dan tampilan sistem.
4. Pengujian dilakukan terhadap beberapa pengguna dengan latar belakang yang berbeda untuk memperoleh gambaran penggunaan sistem secara lebih objektif.

## 10.4 Analisis Hasil Pengujian

Analisis hasil pengujian dilakukan untuk mengetahui sejauh mana sistem memenuhi kebutuhan fungsional dan non-fungsional yang telah ditetapkan pada tahap analisis dan perancangan sistem.

### 10.4.1 Analisis Hasil Blackbox Testing

Berdasarkan hasil pengujian blackbox testing yang telah dilakukan pada seluruh fitur utama sistem, dapat disimpulkan bahwa:

1. Seluruh fitur utama sistem, termasuk login, pengelolaan data aset, QR Code, maintenance, import/export, laporan, manajemen pengguna, dan audit log, dapat berjalan sesuai dengan perancangan.
2. Tidak ditemukan kesalahan fungsional yang signifikan selama proses pengujian.
3. Sistem mampu menangani input valid dan tidak valid dengan baik serta memberikan respons yang sesuai.

Hasil ini menunjukkan bahwa secara fungsional sistem telah berjalan dengan stabil dan sesuai dengan kebutuhan pengguna.

### 10.4.2 Analisis Hasil Usability Testing

Berdasarkan hasil usability testing yang telah dilakukan, diperoleh beberapa temuan sebagai berikut:

1. Sistem dinilai mudah digunakan oleh pengguna dengan berbagai latar belakang teknis.
2. Navigasi sistem cukup jelas dan mudah dipahami berkat sidebar yang terstruktur.
3. Fitur QR Code membantu pengguna dalam mengidentifikasi aset dengan cepat di lapangan.
4. Badge warna pada status aset (hijau=Aktif, kuning=Maintenance, abu=Non-Aktif) sangat membantu identifikasi visual.
5. Beberapa masukan diberikan terkait peningkatan panduan penggunaan fitur QR Scanner.

Secara umum, hasil usability testing menunjukkan bahwa sistem telah memenuhi kebutuhan pengguna dari sisi kemudahan penggunaan dan kenyamanan akses.

## 10.5 Evaluasi Sistem

Evaluasi sistem dilakukan berdasarkan hasil pengujian fungsional (blackbox testing) dan usability testing untuk menilai kualitas sistem secara menyeluruh.

### 10.5.1 Evaluasi Fungsional

Berdasarkan hasil pengujian fungsional, sistem telah mampu:

1. Menyediakan sistem pencatatan aset yang terpusat dan terintegrasi.
2. Mengidentifikasi aset secara cepat melalui QR Code.
3. Mengelola data aset melalui dashboard yang informatif.
4. Mencatat dan menyelesaikan proses maintenance dengan notifikasi email.
5. Menghasilkan laporan aset dalam berbagai format (PDF, Excel, CSV).
6. Menjaga keamanan akses sistem melalui mekanisme autentikasi dan otorisasi berbasis role.
7. Mencatat seluruh aktivitas pengguna dalam audit log.

Hal ini menunjukkan bahwa sistem telah memenuhi kebutuhan fungsional yang dirancang.

### 10.5.2 Evaluasi Non-Fungsional

Dari sisi non-fungsional, sistem menunjukkan beberapa keunggulan, antara lain:

1. Kinerja sistem yang cukup responsif saat diakses berkat pagination dan eager loading.
2. Antarmuka yang relatif mudah dipahami oleh pengguna dengan badge warna yang konsisten.
3. Tingkat keamanan yang memadai dengan security headers, CSRF protection, dan rate limiting.
4. Struktur sistem yang mendukung pengembangan lanjutan di masa depan.

Evaluasi ini menunjukkan bahwa sistem layak digunakan sebagai sistem informasi manajemen aset barang kantor RBTV Bengkulu.

## 10.6 Kesimpulan Modul

Modul 10 membahas proses pengujian dan evaluasi SimAset secara menyeluruh. Pengujian dilakukan menggunakan metode blackbox testing dan usability testing untuk memastikan bahwa sistem berjalan sesuai dengan kebutuhan fungsional dan non-fungsional.

Berdasarkan hasil pengujian dan evaluasi yang telah dilakukan, sistem dinyatakan berfungsi dengan baik, mudah digunakan, dan siap digunakan sebagai sistem informasi manajemen aset barang kantor RBTV Bengkulu. Modul ini menjadi dasar sebelum pembahasan penutup dan pengembangan lanjutan pada modul berikutnya.
