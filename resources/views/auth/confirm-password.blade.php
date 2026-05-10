@extends('layouts.auth')

@section('title', 'Konfirmasi Password')
@section('page-title', 'Konfirmasi Password')
@section('page-subtitle', 'Masukkan kembali password Anda untuk melanjutkan')

@section('auth-content')

@if ($errors->any())
<div class="alert-err"><i class="fas fa-exclamation-circle"></i> {{ $errors->first() }}</div>
@endif

<div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:12px 14px;margin-bottom:18px;display:flex;align-items:flex-start;gap:9px;">
    <i class="fas fa-shield-alt" style="color:#2563EB;font-size:.9rem;margin-top:1px;flex-shrink:0;"></i>
    <p style="font-size:.8rem;color:#1E40AF;margin:0;line-height:1.5;">
        Untuk keamanan akun, konfirmasi password Anda sebelum melanjutkan ke area sensitif ini.
    </p>
</div>

<form method="POST" action="{{ route('password.confirm') }}">
    @csrf
    <div class="form-group">
        <label class="form-label" for="password">Password Anda</label>
        <div class="input-wrap">
            <input type="password" id="password" name="password" class="form-control"
                   placeholder="Masukkan password" required autocomplete="current-password">
            <i class="fas fa-lock input-icon"></i>
            <button type="button" class="pw-toggle" id="pwToggle">
                <i class="fas fa-eye" id="pwIcon"></i>
            </button>
        </div>
    </div>
    <button type="submit" class="btn-submit">
        <i class="fas fa-check-circle"></i> Konfirmasi & Lanjutkan
    </button>
</form>

@endsection

@push('scripts')
<script>
document.getElementById('pwToggle').addEventListener('click', function() {
    const pw = document.getElementById('password');
    const icon = document.getElementById('pwIcon');
    if (pw.type === 'password') { pw.type = 'text'; icon.classList.replace('fa-eye','fa-eye-slash'); }
    else { pw.type = 'password'; icon.classList.replace('fa-eye-slash','fa-eye'); }
});
</script>
@endpush
