# MODUL 6 — AUTENTIKASI DAN HAK AKSES
## SimAset — Sistem Informasi Manajemen Aset RBTV Bengkulu

---

## 6.1 Pendahuluan

Autentikasi dan pengelolaan hak akses adalah fondasi keamanan SimAset. Sistem yang tidak memiliki mekanisme autentikasi yang baik berpotensi mengalami penyalahgunaan data, perubahan data tanpa izin, atau akses ilegal ke fitur administratif yang dapat merusak integritas seluruh sistem.

SimAset menggunakan **Laravel Breeze** sebagai scaffolding autentikasi yang menyediakan implementasi login, logout, reset password, dan verifikasi email yang sudah teruji dan aman. Di atas itu, sistem menambahkan **role-based access control (RBAC)** melalui `RoleMiddleware` untuk membedakan hak akses Admin dan Staff, serta **SecurityHeaders middleware** untuk menambahkan lapisan keamanan HTTP.

Berdasarkan data aktual dari database, sistem saat ini memiliki tiga pengguna aktif: Admin Magang (admin), Staff RBTV (staff), dan reffki (staff). Seluruh aktivitas login mereka tercatat di tabel `log_aktivitas` — dari 39 record yang ada, sebagian besar adalah record Login.

---

## 6.2 Implementasi Login

### 6.2.1 Route Login

```php
// routes/auth.php (dikelola Laravel Breeze)
Route::middleware('guest')->group(function () {
    Route::get('login', [AuthenticatedSessionController::class, 'create'])
        ->name('login');
    Route::post('login', [AuthenticatedSessionController::class, 'store']);
});
```

Middleware `guest` memastikan pengguna yang sudah login tidak dapat mengakses halaman login lagi — mereka akan di-redirect ke dashboard.

### 6.2.2 Form Request: LoginRequest

`LoginRequest` menangani validasi dan autentikasi login dengan fitur rate limiting bawaan:

```php
class LoginRequest extends FormRequest
{
    public function rules(): array
    {
        return [
            'email'    => ['required', 'string', 'email'],
            'password' => ['required', 'string'],
        ];
    }

    public function authenticate(): void
    {
        // Cek rate limit — mencegah brute force attack
        $this->ensureIsNotRateLimited();

        // Coba autentikasi
        if (!Auth::attempt($this->only('email', 'password'), $this->boolean('remember'))) {
            // Tambah hitungan percobaan gagal
            RateLimiter::hit($this->throttleKey());

            throw ValidationException::withMessages([
                'email' => trans('auth.failed'),
            ]);
        }

        // Reset hitungan jika berhasil
        RateLimiter::clear($this->throttleKey());
    }

    public function ensureIsNotRateLimited(): void
    {
        // Batasi 5 percobaan per menit per email+IP
        if (!RateLimiter::tooManyAttempts($this->throttleKey(), 5)) {
            return;
        }

        event(new Lockout($this));

        $seconds = RateLimiter::availableIn($this->throttleKey());
        throw ValidationException::withMessages([
            'email' => trans('auth.throttle', [
                'seconds' => $seconds,
                'minutes' => ceil($seconds / 60),
            ]),
        ]);
    }
}
```

### 6.2.3 Controller Login

```php
class AuthenticatedSessionController extends Controller
{
    // Tampilkan form login
    public function create(): View
    {
        return view('auth.login');
    }

    // Proses login
    public function store(LoginRequest $request): RedirectResponse
    {
        $request->authenticate();

        // Regenerate session ID untuk mencegah session fixation attack
        $request->session()->regenerate();

        return redirect()->intended(route('dashboard', absolute: false));
    }

    // Proses logout
    public function destroy(Request $request): RedirectResponse
    {
        Auth::guard('web')->logout();
        $request->session()->invalidate();
        $request->session()->regenerateToken();
        return redirect('/');
    }
}
```

> **[GAMBAR 6.1: Tampilan halaman login SimAset dengan form email dan password, tombol Masuk, dan link Lupa Password]**

### 6.2.4 Fitur Keamanan Login

| Fitur | Implementasi | Tujuan |
|-------|-------------|--------|
| Rate Limiting | RateLimiter (5 percobaan/menit) | Mencegah brute force attack |
| Session Regeneration | `session()->regenerate()` | Mencegah session fixation attack |
| CSRF Protection | Token CSRF di setiap form | Mencegah Cross-Site Request Forgery |
| Password Hashing | bcrypt via `Hash::make()` | Password tidak tersimpan plain text |
| Session Invalidation | `session()->invalidate()` saat logout | Mencegah session hijacking |

> **[GAMBAR 6.2: Tampilan pesan error "Kredensial yang diberikan tidak cocok dengan catatan kami" saat login dengan password salah]**

---

## 6.3 Role-Based Access Control

### 6.3.1 RoleMiddleware

```php
// app/Http/Middleware/RoleMiddleware.php
class RoleMiddleware
{
    public function handle(Request $request, Closure $next, ...$roles)
    {
        if (!Auth::check()) {
            abort(403);
        }

        if (!in_array(Auth::user()->role, $roles)) {
            abort(403, 'Akses ditolak. Fitur ini hanya untuk: ' . implode(', ', $roles));
        }

        return $next($request);
    }
}
```

### 6.3.2 Registrasi Middleware

```php
// bootstrap/app.php
->withMiddleware(function (Middleware $middleware) {
    $middleware->alias([
        'role'     => RoleMiddleware::class,
        'security' => SecurityHeaders::class,
    ]);
    // SecurityHeaders ditambahkan ke SEMUA request
    $middleware->append(SecurityHeaders::class);
})
```

### 6.3.3 Penggunaan di Routes

```php
// routes/web.php
Route::middleware(['auth'])->group(function () {
    // Semua route ini memerlukan login
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::resource('aset', AssetController::class);
    Route::resource('barang', BarangController::class);
    // ... semua route operasional

    // Route khusus Admin
    Route::middleware('role:admin')->group(function () {
        Route::resource('users', UserController::class);
        Route::get('/audit-log', [AuditLogController::class, 'index'])->name('audit-log.index');
    });
});
```

### 6.3.4 Matriks Hak Akses Lengkap

| Fitur | Admin | Staff | Keterangan |
|-------|-------|-------|------------|
| Dashboard | ✅ | ✅ | Semua pengguna |
| Lihat daftar aset | ✅ | ✅ | |
| Tambah aset | ✅ | ✅ | |
| Edit aset | ✅ | ✅ | |
| Hapus aset | ✅ | ✅ | Soft delete |
| Batch delete aset | ✅ | ✅ | |
| Kelola barang (CRUD) | ✅ | ✅ | |
| Kelola ruangan (CRUD) | ✅ | ✅ | |
| Generate & cetak QR | ✅ | ✅ | |
| Scanner QR | ✅ | ✅ | |
| Set/selesai maintenance | ✅ | ✅ | |
| Import aset/barang | ✅ | ✅ | |
| Export & laporan | ✅ | ✅ | |
| Edit profil sendiri | ✅ | ✅ | |
| **Kelola pengguna** | ✅ | ❌ | Admin only |
| **Audit log** | ✅ | ❌ | Admin only |

---

## 6.4 Security Headers Middleware

```php
// app/Http/Middleware/SecurityHeaders.php
class SecurityHeaders
{
    public function handle(Request $request, Closure $next)
    {
        $response = $next($request);

        // Mencegah browser menebak tipe konten (MIME sniffing)
        $response->headers->set('X-Content-Type-Options', 'nosniff');

        // Mencegah halaman dimuat dalam iframe (clickjacking protection)
        $response->headers->set('X-Frame-Options', 'DENY');

        // Mengaktifkan filter XSS bawaan browser
        $response->headers->set('X-XSS-Protection', '1; mode=block');

        // Mengontrol informasi referrer yang dikirim ke server lain
        $response->headers->set('Referrer-Policy', 'strict-origin-when-cross-origin');

        // Membatasi sumber yang dapat memuat halaman dalam frame
        $response->headers->set('Content-Security-Policy', "frame-ancestors 'self';");

        return $response;
    }
}
```

Middleware ini ditambahkan ke **semua request** melalui `$middleware->append(SecurityHeaders::class)`, sehingga setiap response dari SimAset selalu menyertakan header-header keamanan ini.

---

## 6.5 Activity Logging

### 6.5.1 ActivityLogger Helper

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
            // Log gagal tidak boleh menghentikan operasi utama
            \Log::warning('ActivityLogger failed: ' . $e->getMessage());
            return null;
        }
    }

    // Shortcut methods
    public static function logAsset(string $aktivitas, string $keterangan = '', $asset = null) {
        return self::log($aktivitas, $keterangan);
    }
    public static function logUser(string $aktivitas, string $keterangan = '', $user = null) {
        return self::log($aktivitas, $keterangan);
    }
}
```

### 6.5.2 Contoh Pemanggilan di Controller

```php
// Di AssetController::store() setelah aset berhasil dibuat
try {
    ActivityLogger::logAsset(
        'Create',
        "Menambahkan aset baru: {$asset->nama_barang} ({$kode_aset})",
        $asset
    );
} catch (\Exception $e) {
    // Log gagal tidak menghentikan proses
}
```

Berdasarkan data aktual, log id=1 adalah hasil dari pemanggilan ini:
```
id=1, user_id=3, aktivitas='Create',
keterangan='Menambahkan aset baru: Kamera Sony A7 (AST-002)',
ip_address='127.0.0.1', created_at='2026-05-01 08:04:46'
```

---

## 6.6 Manajemen Pengguna (Admin Only)

### 6.6.1 Tambah Pengguna Baru

```php
public function store(Request $request)
{
    $request->validate([
        'name'     => 'required|string',
        'email'    => 'required|email|unique:users,email',
        // Regex: minimal 8 char, ada huruf kecil, huruf besar, dan angka
        'password' => 'required|min:8|regex:/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/',
        'role'     => 'required|in:admin,staff',
    ], [
        'password.regex' => 'Password minimal 8 karakter, mengandung huruf besar, huruf kecil, dan angka.',
    ]);

    $plainPassword = $request->password;

    $user = User::create([
        'name'      => $request->name,
        'email'     => $request->email,
        'password'  => Hash::make($plainPassword),
        'role'      => $request->role,
        'is_active' => $request->boolean('is_active', true),
    ]);

    // Kirim email notifikasi (opsional, jika checkbox dicentang)
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
        ->with('success', 'User berhasil ditambahkan');
}
```

### 6.6.2 Proteksi Hapus Akun Sendiri

```php
public function destroy(User $user)
{
    // Admin tidak bisa menghapus akunnya sendiri
    if (auth()->id() === $user->id) {
        return back()->with('error', 'Tidak bisa menghapus akun sendiri');
    }
    $user->delete();
    return redirect()->route('users.index')->with('success', 'User berhasil dihapus');
}
```

> **[GAMBAR 6.3: Tampilan halaman daftar pengguna menampilkan 3 user aktual: Staff RBTV, Admin Magang, dan reffki]**

> **[GAMBAR 6.4: Tampilan form tambah pengguna baru dengan field nama, email, password, role, dan checkbox kirim email]**

---

## 6.7 Pengujian Autentikasi dan Hak Akses

### 6.7.1 Skenario Pengujian Login

| No | Skenario | Input | Hasil yang Diharapkan | Status |
|----|----------|-------|----------------------|--------|
| 1 | Login Admin valid | magangrbtv@gmail.com / Magang123 | Redirect ke dashboard | ✅ |
| 2 | Login Staff valid | reffkip@gmail.com / (password) | Redirect ke dashboard | ✅ |
| 3 | Email tidak terdaftar | unknown@test.com / apapun | "Kredensial tidak cocok" | ✅ |
| 4 | Password salah | magangrbtv@gmail.com / salah | "Kredensial tidak cocok" | ✅ |
| 5 | Field email kosong | (kosong) / Magang123 | Error validasi email wajib | ✅ |
| 6 | Field password kosong | magangrbtv@gmail.com / (kosong) | Error validasi password wajib | ✅ |
| 7 | Akses /dashboard tanpa login | - | Redirect ke /login | ✅ |
| 8 | Akses /users sebagai Staff | Login reffki, akses /users | HTTP 403 Forbidden | ✅ |
| 9 | Akses /audit-log sebagai Staff | Login reffki, akses /audit-log | HTTP 403 Forbidden | ✅ |
| 10 | Logout | Klik Logout | Session dihapus, redirect /login | ✅ |
| 11 | Akses /dashboard setelah logout | GET /dashboard | Redirect ke /login | ✅ |

---

## 6.8 Kesimpulan Modul

Modul 6 ini telah membahas implementasi autentikasi dan hak akses SimAset secara menyeluruh. Laravel Breeze menyediakan fondasi autentikasi yang aman dengan rate limiting, session regeneration, dan CSRF protection. RoleMiddleware memastikan fitur administratif (kelola user, audit log) hanya dapat diakses oleh Admin. SecurityHeaders middleware menambahkan lapisan keamanan HTTP ke semua response. ActivityLogger mencatat seluruh aktivitas pengguna secara otomatis.

Berdasarkan data aktual, sistem telah berhasil mencatat 39 aktivitas dari tiga pengguna (Admin Magang id=3, reffki id=4, Staff RBTV id=2), membuktikan bahwa mekanisme logging berjalan dengan baik.

---

*Kembali ke: [Modul 5 — Implementasi Database](MODUL_05_IMPLEMENTASI_DATABASE.md)*
*Lanjut ke: [Modul 7 — Manajemen Data Aset](MODUL_07_MANAJEMEN_ASET.md)*
