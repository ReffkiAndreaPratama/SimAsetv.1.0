@extends('layouts.auth')

@section('title', 'Verifikasi Email')
@section('page-title', 'Verifikasi Email Anda')
@section('page-subtitle', 'Cek inbox atau folder spam untuk link verifikasi')

@section('auth-content')

@if (session('status') == 'verification-link-sent')
<div class="alert-ok"><i class="fas fa-check-circle"></i> Link verifikasi baru telah dikirim ke email Anda.</div>
@endif

<div style="text-align:center;padding:20px 0 24px;">
    <div style="width:72px;height:72px;border-radius:50%;background:#EFF6FF;border:2px solid #BFDBFE;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:28px;color:#2563EB;">
        <i class="fas fa-envelope-open-text"></i>
    </div>
    <p style="font-size:.875rem;color:#374151;line-height:1.6;margin:0;">
        Kami telah mengirimkan link verifikasi ke email Anda.<br>
        Klik link tersebut untuk mengaktifkan akun.
    </p>
</div>

<form method="POST" action="{{ route('verification.send') }}">
    @csrf
    <button type="submit" class="btn-submit" style="margin-bottom:10px;">
        <i class="fas fa-paper-plane"></i> Kirim Ulang Email Verifikasi
    </button>
</form>

<form method="POST" action="{{ route('logout') }}">
    @csrf
    <button type="submit" style="width:100%;padding:12px;background:#fff;color:#6B7280;border:1.5px solid #E2E8F0;border-radius:10px;font-size:.9rem;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;transition:all .2s;">
        <i class="fas fa-sign-out-alt"></i> Logout
    </button>
</form>

@endsection
