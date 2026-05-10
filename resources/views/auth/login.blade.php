<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Login — SimAset RBTV Bengkulu</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { font-family: 'Inter', sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
        body { min-height: 100vh; display: flex; background: #060e28; }

        /* ── LEFT PANEL ── */
        .lp {
            flex: 1; position: relative; overflow: hidden;
            display: flex; flex-direction: column; justify-content: space-between;
            padding: 40px 52px;
            background: linear-gradient(150deg, #060e28 0%, #0b1a45 20%, #0f2255 45%, #1a3470 70%, #1c3d9e 88%, #1e45b8 100%);
        }
        .lp-blob { position: absolute; border-radius: 50%; pointer-events: none; }
        .lp-blob-1 { width: 600px; height: 600px; top: -200px; right: -200px; background: radial-gradient(circle, rgba(59,130,246,.12) 0%, transparent 60%); }
        .lp-blob-2 { width: 500px; height: 500px; bottom: -150px; left: -150px; background: radial-gradient(circle, rgba(185,28,28,.12) 0%, transparent 60%); }
        .lp-grid { position: absolute; inset: 0; pointer-events: none; background-image: radial-gradient(rgba(255,255,255,.06) 1px, transparent 1px); background-size: 28px 28px; }
        .lp-accent { position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #991b1b, #ef4444 50%, transparent); }

        .lp-brand { position: relative; z-index: 2; display: flex; align-items: center; gap: 12px; }
        .lp-logo { width: 52px; height: 52px; border-radius: 13px; background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.15); display: flex; align-items: center; justify-content: center; overflow: hidden; flex-shrink: 0; }
        .lp-logo img { width: 100%; height: 100%; object-fit: contain; padding: 8px; }
        .lp-sep { width: 1px; height: 34px; background: rgba(255,255,255,.15); flex-shrink: 0; }
        .lp-brand-name { font-size: 1.15rem; font-weight: 900; color: #fff; letter-spacing: .07em; text-transform: uppercase; line-height: 1; }
        .lp-brand-sub  { font-size: .6rem; color: rgba(255,255,255,.4); letter-spacing: .1em; text-transform: uppercase; font-weight: 500; margin-top: 2px; }

        .lp-hero { position: relative; z-index: 2; }
        .lp-pill { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.14); border-radius: 100px; padding: 5px 14px 5px 8px; font-size: .68rem; font-weight: 600; color: rgba(255,255,255,.75); margin-bottom: 22px; }
        .lp-pill-dot { width: 8px; height: 8px; border-radius: 50%; background: #4ade80; box-shadow: 0 0 8px #4ade80; flex-shrink: 0; }
        .lp-title { font-size: clamp(1.65rem, 2.8vw, 2.4rem); font-weight: 900; color: #fff; line-height: 1.18; margin-bottom: 14px; letter-spacing: -.03em; }
        .lp-title em { font-style: normal; color: #fca5a5; }
        .lp-desc { font-size: .85rem; color: rgba(255,255,255,.5); line-height: 1.85; max-width: 360px; }
        .lp-feats { list-style: none; padding: 0; margin: 26px 0 0; display: flex; flex-direction: column; gap: 11px; }
        .lp-feats li { display: flex; align-items: center; gap: 10px; font-size: .82rem; color: rgba(255,255,255,.65); }
        .lp-dot { width: 6px; height: 6px; border-radius: 50%; background: #93c5fd; flex-shrink: 0; opacity: .8; }
        .lp-badges { display: flex; gap: 7px; flex-wrap: wrap; margin-top: 26px; position: relative; z-index: 2; }
        .lp-badge { display: inline-flex; align-items: center; padding: 5px 11px; border-radius: 7px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.1); font-size: .67rem; font-weight: 600; color: rgba(255,255,255,.55); }
        .lp-footer { position: relative; z-index: 2; font-size: .65rem; color: rgba(255,255,255,.2); }

        /* ── RIGHT PANEL ── */
        .rp {
            width: 460px; flex-shrink: 0; background: #fff;
            display: flex; flex-direction: column; justify-content: center;
            padding: 44px 40px; position: relative; overflow-y: auto;
            animation: rpIn .4s cubic-bezier(.16,1,.3,1) both;
        }
        @keyframes rpIn { from { opacity: 0; transform: translateX(18px); } to { opacity: 1; transform: translateX(0); } }
        .rp::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #1d4ed8, #3b82f6, #93c5fd); }

        .rp-identity { display: flex; align-items: center; gap: 11px; margin-bottom: 26px; padding-bottom: 18px; border-bottom: 1px solid #F1F5F9; }
        .rp-logo { width: 40px; height: 40px; border-radius: 9px; background: #EFF6FF; border: 1.5px solid #BFDBFE; display: flex; align-items: center; justify-content: center; overflow: hidden; flex-shrink: 0; }
        .rp-logo img { width: 100%; height: 100%; object-fit: contain; padding: 6px; }
        .rp-logo-sep { width: 1px; height: 26px; background: #E2E8F0; flex-shrink: 0; }
        .rp-app-name { font-size: .95rem; font-weight: 800; color: #0F172A; letter-spacing: -.01em; line-height: 1.2; }
        .rp-app-tag  { font-size: .62rem; color: #94A3B8; font-weight: 500; line-height: 1.4; margin-top: 1px; }

        .login-head { margin-bottom: 22px; }
        .login-head h2 { font-size: 1.3rem; font-weight: 800; color: #0F172A; margin-bottom: 4px; letter-spacing: -.025em; }
        .login-head p  { font-size: .8rem; color: #64748B; line-height: 1.6; }

        .fg { margin-bottom: 15px; }
        .fl { font-size: .78rem; font-weight: 600; color: #374151; margin-bottom: 6px; display: block; }
        .iw { position: relative; }
        .fc { width: 100%; padding: 11px 14px; border-radius: 9px; border: 1.5px solid #E2E8F0; background: #F8FAFC; color: #0F172A; font-size: .875rem; transition: border-color .2s, background .2s, box-shadow .2s; font-family: 'Inter', sans-serif; }
        .fc:focus { background: #fff; border-color: #3B82F6; box-shadow: 0 0 0 3px rgba(59,130,246,.1); outline: none; }
        .fc::placeholder { color: #CBD5E1; }
        .fc-pw { padding-right: 42px; }
        .pt { position: absolute; right: 11px; top: 50%; transform: translateY(-50%); color: #CBD5E1; cursor: pointer; font-size: .82rem; background: none; border: none; padding: 4px; transition: color .2s; z-index: 1; line-height: 1; }
        .pt:hover { color: #3B82F6; }
        /* eye SVG icons */
        .eye-open::before  { content: '👁'; font-size: 14px; }
        .eye-shut::before  { content: '🙈'; font-size: 14px; }

        .action-row { display: flex; justify-content: space-between; align-items: center; margin: 4px 0 18px; }
        .chk-wrap { display: flex; align-items: center; gap: 7px; }
        .chk-wrap input[type=checkbox] { width: 15px; height: 15px; border-radius: 4px; cursor: pointer; accent-color: #3B82F6; }
        .chk-wrap label { font-size: .78rem; color: #64748B; cursor: pointer; }
        .forgot-link { font-size: .78rem; font-weight: 600; color: #3B82F6; text-decoration: none; }
        .forgot-link:hover { color: #1D4ED8; }

        .btn-go { width: 100%; padding: 12px 20px; background: linear-gradient(135deg, #1d4ed8, #3b82f6); color: #fff; border: none; border-radius: 9px; font-size: .875rem; font-weight: 700; cursor: pointer; transition: all .22s; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 14px rgba(59,130,246,.25); font-family: 'Inter', sans-serif; letter-spacing: .01em; }
        .btn-go:hover { background: linear-gradient(135deg, #1e40af, #2563eb); transform: translateY(-1px); box-shadow: 0 6px 20px rgba(59,130,246,.35); }
        .btn-go:active { transform: translateY(0); }

        .al-err { background: #FEF2F2; border: 1px solid #FECACA; color: #B91C1C; border-radius: 9px; padding: 10px 13px; margin-bottom: 16px; font-size: .8rem; line-height: 1.55; }
        .al-ok  { background: #ECFDF5; border: 1px solid #A7F3D0; color: #065F46; border-radius: 9px; padding: 10px 13px; margin-bottom: 16px; font-size: .8rem; line-height: 1.55; }

        .divider { position: relative; text-align: center; margin: 20px 0 14px; }
        .divider::before { content: ''; position: absolute; top: 50%; left: 0; right: 0; height: 1px; background: #F1F5F9; }
        .divider span { position: relative; background: #fff; padding: 0 10px; font-size: .68rem; color: #CBD5E1; font-weight: 500; }

        .sys-badges { display: flex; gap: 6px; flex-wrap: wrap; }
        .sys-badge { display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F8FAFC; border: 1px solid #F1F5F9; font-size: .67rem; font-weight: 600; color: #94A3B8; }

        .rp-footer { text-align: center; margin-top: 20px; font-size: .65rem; color: #CBD5E1; }

        @media (max-width: 900px) { .lp { display: none; } .rp { width: 100%; padding: 36px 24px; } }
    </style>
</head>
<body>

{{-- LEFT PANEL --}}
<div class="lp">
    <div class="lp-accent"></div>
    <div class="lp-grid"></div>
    <div class="lp-blob lp-blob-1"></div>
    <div class="lp-blob lp-blob-2"></div>

    <div class="lp-brand">
        <div class="lp-logo"><img src="{{ asset('logoweb.png') }}" alt="SimAset" onerror="this.style.display='none'"></div>
        <div class="lp-sep"></div>
        <div class="lp-logo"><img src="{{ asset('logo.png') }}" alt="RBTV" onerror="this.style.display='none'"></div>
        <div>
            <div class="lp-brand-name">SimAset</div>
            <div class="lp-brand-sub">Rakyat Bengkulu Televisi</div>
        </div>
    </div>

    <div class="lp-hero">
        <div class="lp-pill">
            <span class="lp-pill-dot"></span>
            Sistem Informasi Manajemen Aset
        </div>
        <h1 class="lp-title">Kelola Aset Kantor<br>dengan <em>Lebih Mudah</em></h1>
        <p class="lp-desc">Platform digital terpusat untuk pencatatan, pemantauan, dan pelaporan aset barang kantor RBTV Bengkulu secara real-time.</p>
        <ul class="lp-feats">
            <li><span class="lp-dot"></span> Manajemen aset lengkap — CRUD, kondisi, dan lokasi</li>
            <li><span class="lp-dot"></span> Generate & scan QR Code untuk identifikasi cepat</li>
            <li><span class="lp-dot"></span> Laporan PDF & Excel otomatis dengan filter lengkap</li>
            <li><span class="lp-dot"></span> Audit trail — rekam semua aktivitas pengguna</li>
        </ul>
        <div class="lp-badges">
            <span class="lp-badge">Laravel 12</span>
            <span class="lp-badge">Role-Based Access</span>
            <span class="lp-badge">Secure Login</span>
            <span class="lp-badge">Responsive</span>
        </div>
    </div>

    <div class="lp-footer">&copy; {{ date('Y') }} RBTV Bengkulu &mdash; SimAset v1.0</div>
</div>

{{-- RIGHT PANEL --}}
<div class="rp">

    <div class="rp-identity">
        <div class="rp-logo"><img src="{{ asset('logoweb.png') }}" alt="SimAset" onerror="this.style.display='none'"></div>
        <div class="rp-logo-sep"></div>
        <div class="rp-logo"><img src="{{ asset('logo.png') }}" alt="RBTV" onerror="this.style.display='none'"></div>
        <div>
            <div class="rp-app-name">SimAset</div>
            <div class="rp-app-tag">Sistem Informasi Manajemen Aset<br>Barang Kantor RBTV Bengkulu</div>
        </div>
    </div>

    <div class="login-head">
        <h2>Masuk ke Sistem</h2>
        <p>Gunakan akun yang telah diberikan oleh administrator</p>
    </div>

    @if ($errors->any())
    <div class="al-err">{{ $errors->first() }}</div>
    @endif
    @if (session('status'))
    <div class="al-ok">{{ session('status') }}</div>
    @endif

    <form method="POST" action="{{ route('login') }}">
        @csrf

        <div class="fg">
            <label class="fl" for="email">Alamat Email</label>
            <div class="iw">
                <input type="email" id="email" name="email" class="fc"
                    placeholder="email@rbtv.co.id"
                    value="{{ old('email') }}"
                    required autofocus autocomplete="email">
            </div>
        </div>

        <div class="fg">
            <label class="fl" for="password">Kata Sandi</label>
            <div class="iw">
                <input type="password" id="password" name="password" class="fc fc-pw"
                    placeholder="Masukkan kata sandi"
                    required autocomplete="current-password">
                <button type="button" class="pt" id="pwToggle" aria-label="Tampilkan password">
                    <span id="pwIcon" class="eye-open"></span>
                </button>
            </div>
        </div>

        <div class="action-row">
            <div class="chk-wrap">
                <input type="checkbox" id="remember" name="remember">
                <label for="remember">Ingat Saya</label>
            </div>
            @if (Route::has('password.request'))
                <a href="{{ route('password.request') }}" class="forgot-link">Lupa Password?</a>
            @endif
        </div>

        <button type="submit" class="btn-go">Masuk ke Sistem &rarr;</button>
    </form>

    <div class="divider"><span>Informasi Sistem</span></div>
    <div class="sys-badges">
        <span class="sys-badge">Laravel 12</span>
        <span class="sys-badge">Role-Based Access</span>
        <span class="sys-badge">Secure Login</span>
    </div>

    <div class="rp-footer">&copy; {{ date('Y') }} RBTV Bengkulu &mdash; SimAset v1.0</div>
</div>

<script>
document.getElementById('pwToggle').addEventListener('click', function() {
    const pw   = document.getElementById('password');
    const icon = document.getElementById('pwIcon');
    if (pw.type === 'password') {
        pw.type = 'text';
        icon.className = 'eye-shut';
    } else {
        pw.type = 'password';
        icon.className = 'eye-open';
    }
});
</script>
</body>
</html>
