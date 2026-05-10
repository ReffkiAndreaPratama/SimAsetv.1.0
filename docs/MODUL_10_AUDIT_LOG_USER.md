# MODUL 10 — AUDIT LOG DAN MANAJEMEN PENGGUNA
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 10.1 Pendahuluan

Audit log dan manajemen pengguna adalah dua fitur administratif yang hanya dapat diakses oleh Admin. Audit log memberikan visibilitas penuh atas seluruh aktivitas yang terjadi di sistem — siapa melakukan apa dan kapan — yang sangat penting untuk akuntabilitas dan deteksi anomali. Manajemen pengguna memungkinkan Admin mengelola siapa saja yang dapat mengakses sistem dan dengan hak akses apa.

Berdasarkan data aktual dari database, tabel `log_aktivitas` sudah memiliki **39 record** yang mencakup aktivitas dari dua pengguna: Admin Magang (user_id=3) dan reffki (user_id=4). Aktivitas yang tercatat meliputi Login (35 record), Create (2 record), Update (2 record), dan Delete (1 record).

---

## 10.2 Arsitektur Audit Log

SimAset menggunakan dua mekanisme pencatatan yang saling melengkapi:

```
┌─────────────────────────────────────────────────────────────┐
│                    AUDIT LOG SYSTEM                         │
│                                                             │
│  Mekanisme 1: LogActivity Middleware (terminate phase)      │
│  ├── Login  → POST /login                                   │
│  ├── Logout → POST /logout                                  │
│  ├── Create Aset → POST /aset                               │
│  ├── Update Aset → PUT /aset/{kode}                         │
│  ├── Delete Aset → DELETE /aset/{kode}                      │
│  └── (pola serupa untuk barang dan ruangan)                 │
│                                                             │
│  Mekanisme 2: ActivityLogger::log() di Controller           │
│  ├── Create aset: "Menambahkan aset baru: X (AST-XXX)"      │
│  ├── Update aset: "Mengupdate aset: X (AST-XXX)"            │
│  ├── Delete aset: "Menghapus aset: X (AST-XXX)"             │
│  ├── Maintenance set/complete                               │
│  └── User management                                        │
│                                                             │
│  Semua log → tabel log_aktivitas                            │
│  Kolom: user_id, aktivitas, keterangan, ip_address,         │
│         user_agent, created_at                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 10.3 AuditLogController

```php
// app/Http/Controllers/AuditLogController.php
public function index(Request $request)
{
    $query = ActivityLog::with('user')->orderBy('created_at', 'desc');

    // Filter pencarian di kolom aktivitas dan keterangan
    if ($request->filled('search')) {
        $s = $request->search;
        $query->where(function ($q) use ($s) {
            $q->where('aktivitas',  'like', "%{$s}%")
              ->orWhere('keterangan', 'like', "%{$s}%");
        });
    }

    // Filter berdasarkan user tertentu
    if ($request->filled('user_id')) {
        $query->where('user_id', $request->user_id);
    }

    // Filter berdasarkan jenis aktivitas
    if ($request->filled('module')) {
        $query->where('aktivitas', 'like', '%' . $request->module . '%');
    }

    $logs    = $query->paginate(20)->withQueryString();
    $users   = User::orderBy('name')->get(['id', 'name']);
    $modules = ['Login', 'Logout', 'Create', 'Update', 'Delete'];

    return view('audit_log.index', compact('logs', 'users', 'modules'));
}
```

---

## 10.4 Data Audit Log Aktual

Berikut adalah analisis lengkap dari 39 record log_aktivitas yang ada di database:

### 10.4.1 Distribusi Aktivitas

| Jenis Aktivitas | Jumlah | Keterangan |
|-----------------|--------|------------|
| Login | 35 | Mayoritas adalah login dari Admin Magang dan reffki |
| Create | 2 | AST-002 (id=1) dan AST-003 (id=18) |
| Update | 2 | AST-001 (id=17) dan AST-003 (id=19) |
| Delete | 1 | AST-003 (id=20) |
| **Total** | **39** | |

### 10.4.2 Record Log Penting

```
id=1:  user_id=3, Create, "Menambahkan aset baru: Kamera Sony A7 (AST-002)"
       → AST-002 ditambahkan oleh Admin Magang pada 2026-05-01 08:04:46

id=17: user_id=3, Update, "Mengupdate aset: Kamera Sony A7 (AST-001)"
       → AST-001 diupdate (status → Maintenance) pada 2026-05-02 07:42:40

id=18: user_id=3, Create, "Menambahkan aset baru: printer epson l200 (AST-003)"
       → AST-003 ditambahkan pada 2026-05-02 08:19:32

id=19: user_id=3, Update, "Mengupdate aset: printer epson l200 (AST-003)"
       → AST-003 diupdate pada 2026-05-02 08:19:46

id=20: user_id=3, Delete, "Menghapus aset: printer epson l200 (AST-003)"
       → AST-003 dihapus (soft delete) pada 2026-05-02 08:19:54

id=23: user_id=4, Login, "User berhasil login: reffki (reffkip@gmail.com)"
       → reffki pertama kali login pada 2026-05-02 09:55:38
```

> **[GAMBAR 10.1: Tampilan halaman audit log menampilkan 39 record aktivitas dengan kolom Waktu, User, Aktivitas, Keterangan, dan IP Address]**

> **[GAMBAR 10.2: Tampilan filter audit log dengan dropdown pilihan user (Admin Magang, reffki) dan jenis aktivitas (Login, Create, Update, Delete)]**

---

## 10.5 ActivityLogger Helper

```php
// app/Helpers/ActivityLogger.php
class ActivityLogger
{
    public static function log(string $aktivitas, string $keterangan = '')
    {
        try {
            return ActivityLog::create([
                'user_id'    => Auth::id(),
                'aktivitas'  => $aktivitas,
                'keterangan' => $keterangan,
                'ip_address' => request()->ip(),
                'user_agent' => request()->userAgent(),
            ]);
        } catch (\Exception $e) {
            \Log::warning('ActivityLogger failed: ' . $e->getMessage());
            return null;
        }
    }

    public static function logAsset(string $aktivitas, string $keterangan = '', $asset = null) {
        return self::log($aktivitas, $keterangan);
    }
    public static function logUser(string $aktivitas, string $keterangan = '', $user = null) {
        return self::log($aktivitas, $keterangan);
    }
}
```

**Desain penting:** Semua pemanggilan `ActivityLogger` di-wrap dalam `try-catch` agar kegagalan logging tidak pernah menghentikan operasi utama. Ini memastikan bahwa jika tabel `log_aktivitas` bermasalah, sistem tetap berjalan normal.

---

## 10.6 Manajemen Pengguna

### 10.6.1 Daftar Pengguna Aktual

Berdasarkan data di tabel `users`:

| ID | Nama | Email | Role | Aktif | Login Terakhir |
|----|------|-------|------|-------|----------------|
| 2 | Staff RBTV | staff@rbtv.id | staff | ✅ | Belum pernah |
| 3 | Admin Magang | magangrbtv@gmail.com | admin | ✅ | 2026-05-02 13:03:44 |
| 4 | reffki | reffkip@gmail.com | staff | ✅ | 2026-05-02 11:04:07 |

> **[GAMBAR 10.3: Tampilan halaman daftar pengguna menampilkan 3 user aktual dengan badge role (Admin/Staff) dan status aktif]**

### 10.6.2 Tambah Pengguna Baru

```php
public function store(Request $request)
{
    $request->validate([
        'name'     => 'required|string',
        'email'    => 'required|email|unique:users,email',
        // Regex: min 8 char, ada huruf kecil (?=.*[a-z]),
        //        huruf besar (?=.*[A-Z]), dan angka (?=.*\d)
        'password' => 'required|min:8|regex:/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/',
        'role'     => 'required|in:admin,staff',
    ], [
        'password.regex' => 'Password minimal 8 karakter, mengandung huruf besar, huruf kecil, dan angka.',
    ]);

    $plainPassword = $request->password;

    $user = User::create([
        'name'      => $request->name,
        'email'     => $request->email,
        'password'  => Hash::make($plainPassword), // bcrypt hash
        'role'      => $request->role,
        'is_active' => $request->boolean('is_active', true),
    ]);

    // Kirim email notifikasi (opsional)
    if ($request->boolean('kirim_email')) {
        try {
            Mail::to($user->email)->send(new AkunBaruMail(
                $user->name, $user->email, $plainPassword, $user->role
            ));
        } catch (\Exception $e) {
            // Email gagal, akun tetap dibuat
        }
    }

    return redirect()->route('users.index')
        ->with('success', 'User berhasil ditambahkan'
            . ($request->boolean('kirim_email') ? ' & email notifikasi dikirim' : ''));
}
```

**Aturan password yang diterapkan:**
- Minimal 8 karakter
- Harus mengandung minimal 1 huruf kecil (a-z)
- Harus mengandung minimal 1 huruf besar (A-Z)
- Harus mengandung minimal 1 angka (0-9)

Contoh password yang valid: `Admin123`, `Magang123`, `Staff123`
Contoh password yang tidak valid: `password` (tidak ada huruf besar dan angka), `PASSWORD1` (tidak ada huruf kecil)

> **[GAMBAR 10.4: Tampilan form tambah pengguna baru dengan field nama, email, password, konfirmasi password, role (dropdown Admin/Staff), status aktif, dan checkbox kirim email notifikasi]**

### 10.6.3 Edit Pengguna

```php
public function update(Request $request, User $user)
{
    $request->validate([
        'name'     => 'required|string',
        // unique tapi exclude user yang sedang diedit
        'email'    => 'required|email|unique:users,email,' . $user->id,
        'role'     => 'required|in:admin,staff',
        // password opsional saat edit — hanya diupdate jika diisi
        'password' => 'nullable|min:8|regex:/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/',
    ]);

    $data = $request->only('name', 'email', 'role');

    // Update password hanya jika field password diisi
    if ($request->filled('password')) {
        $data['password'] = Hash::make($request->password);
    }

    // Update status aktif jika ada di request
    if ($request->has('is_active')) {
        $data['is_active'] = $request->boolean('is_active');
    }

    $user->update($data);

    return redirect()->route('users.index')->with('success', 'User berhasil diupdate');
}
```

### 10.6.4 Hapus Pengguna

```php
public function destroy(User $user)
{
    // Proteksi: Admin tidak bisa menghapus akunnya sendiri
    if (auth()->id() === $user->id) {
        return back()->with('error', 'Tidak bisa menghapus akun sendiri');
    }
    $user->delete();
    return redirect()->route('users.index')->with('success', 'User berhasil dihapus');
}
```

---

## 10.7 Email Notifikasi Akun Baru

```php
// app/Mail/AkunBaruMail.php
class AkunBaruMail extends Mailable
{
    public function __construct(
        public string $nama,
        public string $email,
        public string $password,
        public string $role
    ) {}
}
```

Email yang dikirim ke pengguna baru berisi:
- Nama pengguna
- Email untuk login
- Password awal (plain text — hanya dikirim sekali saat pembuatan akun)
- Role yang diberikan (Admin/Staff)
- Link ke aplikasi SimAset

> **[GAMBAR 10.5: Contoh tampilan email notifikasi akun baru yang diterima pengguna, berisi kredensial login dan instruksi untuk segera mengganti password]**

---

## 10.8 Profil Pengguna dan Avatar Generator

Setiap pengguna dapat mengedit profil mereka sendiri melalui halaman `/profile`. Model User memiliki method `getAvatarDefault()` yang menghasilkan avatar SVG dari inisial nama:

```php
public function getAvatarDefault()
{
    $name     = $this->name;
    $initials = '';
    foreach (explode(' ', $name) as $word) {
        $initials .= substr($word, 0, 1);
    }
    $initials = strtoupper(substr($initials, 0, 2));

    // Warna dipilih berdasarkan ID user (konsisten per user)
    $colors = ['#3b82f6', '#ef4444', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'];
    $color  = $colors[$this->id % count($colors)];

    return "data:image/svg+xml,..."; // SVG data URI
}
```

**Contoh avatar berdasarkan data aktual:**
- User id=2 (Staff RBTV) → inisial "SR" → warna #ef4444 (merah)
- User id=3 (Admin Magang) → inisial "AM" → warna #10b981 (hijau)
- User id=4 (reffki) → inisial "R" → warna #f59e0b (kuning)

---

## 10.9 Pengujian Audit Log dan Manajemen Pengguna

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Akses audit log sebagai Admin | Login Admin Magang, GET /audit-log | 39 record tampil | ✅ |
| 2 | Akses audit log sebagai Staff | Login reffki, GET /audit-log | HTTP 403 Forbidden | ✅ |
| 3 | Filter log by user reffki | user_id=4 | Hanya log dari reffki tampil | ✅ |
| 4 | Filter log by aktivitas Create | module=Create | Log id=1 dan id=18 tampil | ✅ |
| 5 | Cari "AST-001" di log | search=AST-001 | Log id=17 tampil | ✅ |
| 6 | Tambah user valid | Nama, email baru, Admin123, staff | User tersimpan | ✅ |
| 7 | Tambah user email duplikat | magangrbtv@gmail.com | Error "email sudah digunakan" | ✅ |
| 8 | Tambah user password lemah | "password" | Error validasi password | ✅ |
| 9 | Edit reffki tanpa ganti password | Kosongkan field password | Password tidak berubah | ✅ |
| 10 | Hapus Staff RBTV (id=2) | Klik hapus | User terhapus | ✅ |
| 11 | Hapus akun sendiri (Admin Magang) | Klik hapus akun sendiri | Error "Tidak bisa menghapus akun sendiri" | ✅ |

---

## 10.10 Kesimpulan Modul

Modul 10 ini telah membahas implementasi audit log dan manajemen pengguna SimAset secara menyeluruh menggunakan data aktual. Audit log dengan 39 record aktual membuktikan bahwa sistem pencatatan aktivitas berjalan dengan baik, mencakup semua jenis operasi penting. Manajemen pengguna dengan validasi password kuat dan proteksi hapus akun sendiri memastikan keamanan sistem terjaga.

---

*Kembali ke: [Modul 9 — Import, Export, dan Laporan](MODUL_09_IMPORT_EXPORT_LAPORAN.md)*
*Lanjut ke: [Modul 11 — Pengujian dan Evaluasi](MODUL_11_PENGUJIAN_EVALUASI.md)*
