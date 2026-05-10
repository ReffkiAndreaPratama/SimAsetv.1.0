@extends('layouts.auth')

@section('title', 'Reset Password')
@section('page-title', 'Buat Password Baru')
@section('page-subtitle', 'Masukkan password baru yang kuat untuk akun Anda')

@section('auth-content')

@if ($errors->any())
<div class="al-err">{{ $errors->first() }}</div>
@endif

{{-- Step indicator --}}
<div class="steps">
    <div class="step-item">
        <div class="step-num done">&#10003;</div>
        <span class="step-label done">Email Terkirim</span>
    </div>
    <div class="step-line done"></div>
    <div class="step-item">
        <div class="step-num done">&#10003;</div>
        <span class="step-label done">Link Dibuka</span>
    </div>
    <div class="step-line idle"></div>
    <div class="step-item">
        <div class="step-num active">3</div>
        <span class="step-label active">Reset Password</span>
    </div>
</div>

<form method="POST" action="{{ route('password.store') }}">
    @csrf
    <input type="hidden" name="token" value="{{ $request->route('token') }}">

    {{-- Email readonly --}}
    <div class="fg">
        <label class="fl" for="email">Alamat Email</label>
        <div class="iw">
            <input id="email" type="email" name="email" class="fc fc-ro"
                value="{{ old('email', $request->email) }}"
                required autocomplete="username" readonly>
        </div>
    </div>

    {{-- Password baru --}}
    <div class="fg">
        <label class="fl" for="password">Password Baru</label>
        <div class="iw">
            <input id="password" type="password" name="password" class="fc fc-pw"
                placeholder="Minimal 8 karakter"
                required autocomplete="new-password"
                oninput="checkStrength(this.value)">
            <button type="button" class="pt" onclick="togglePw('password',this)">&#128065;</button>
        </div>
        <div class="str-bar-wrap"><div id="sBar" class="str-bar"></div></div>
        <div class="str-meta">
            <span id="sText" class="str-text"></span>
            <span class="str-hint">Min. 8 karakter</span>
        </div>
    </div>

    {{-- Konfirmasi --}}
    <div class="fg">
        <label class="fl" for="password_confirmation">Konfirmasi Password</label>
        <div class="iw">
            <input id="password_confirmation" type="password" name="password_confirmation" class="fc fc-pw"
                placeholder="Ulangi password baru"
                required autocomplete="new-password"
                oninput="checkMatch()">
            <button type="button" class="pt" onclick="togglePw('password_confirmation',this)">&#128065;</button>
        </div>
        <div id="matchMsg" class="match-msg"></div>
    </div>

    {{-- Rules --}}
    <div class="pw-rules">
        <div class="pw-rules-title">Syarat Password</div>
        <div class="pw-rules-grid">
            <div id="r-len" class="pw-rule">Min. 8 karakter</div>
            <div id="r-up"  class="pw-rule">Huruf kapital (A-Z)</div>
            <div id="r-low" class="pw-rule">Huruf kecil (a-z)</div>
            <div id="r-num" class="pw-rule">Angka (0-9)</div>
        </div>
    </div>

    <button type="submit" class="btn-go">Simpan Password Baru</button>
</form>

<a href="{{ route('login') }}" class="back-link">&larr; Kembali ke halaman login</a>

@push('scripts')
<script>
function togglePw(id, btn) {
    const el = document.getElementById(id);
    el.type = el.type === 'password' ? 'text' : 'password';
    btn.textContent = el.type === 'password' ? '\u{1F441}' : '\u{1F648}';
}

function checkStrength(val) {
    const hasLen = val.length >= 8;
    const hasUp  = /[A-Z]/.test(val);
    const hasLow = /[a-z]/.test(val);
    const hasNum = /[0-9]/.test(val);

    document.getElementById('r-len').classList.toggle('ok', hasLen);
    document.getElementById('r-up').classList.toggle('ok',  hasUp);
    document.getElementById('r-low').classList.toggle('ok', hasLow);
    document.getElementById('r-num').classList.toggle('ok', hasNum);

    const score = [hasLen, hasUp, hasLow, hasNum].filter(Boolean).length;
    const cfg = [null,
        { w:'25%', c:'#EF4444', t:'Sangat Lemah' },
        { w:'50%', c:'#F97316', t:'Lemah' },
        { w:'75%', c:'#EAB308', t:'Cukup' },
        { w:'100%',c:'#22C55E', t:'Kuat' },
    ];
    const bar  = document.getElementById('sBar');
    const text = document.getElementById('sText');
    if (!score) { bar.style.width = '0'; text.textContent = ''; return; }
    bar.style.width      = cfg[score].w;
    bar.style.background = cfg[score].c;
    text.textContent     = cfg[score].t;
    text.style.color     = cfg[score].c;
}

function checkMatch() {
    const pw   = document.getElementById('password').value;
    const conf = document.getElementById('password_confirmation').value;
    const msg  = document.getElementById('matchMsg');
    if (!conf) { msg.innerHTML = ''; return; }
    msg.innerHTML = pw === conf
        ? '<span style="color:#059669;">&#10003; Password cocok</span>'
        : '<span style="color:#EF4444;">&#10007; Password tidak cocok</span>';
}
</script>
@endpush

@endsection
