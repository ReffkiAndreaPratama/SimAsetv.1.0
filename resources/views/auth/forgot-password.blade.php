@extends('layouts.auth')

@section('title', 'Lupa Password')
@section('page-title', 'Lupa Password?')
@section('page-subtitle', 'Masukkan email Anda dan kami akan kirimkan link reset password')

@section('auth-content')

@if (session('status'))
<div class="al-ok">
    <strong>Link terkirim!</strong> {{ session('status') }}
</div>
@endif

@if ($errors->any())
<div class="al-err">{{ $errors->first() }}</div>
@endif

{{-- Step indicator --}}
<div class="steps">
    <div class="step-item">
        <div class="step-num active">1</div>
        <span class="step-label active">Masukkan Email</span>
    </div>
    <div class="step-line idle"></div>
    <div class="step-item">
        <div class="step-num idle">2</div>
        <span class="step-label idle">Cek Email</span>
    </div>
    <div class="step-line idle"></div>
    <div class="step-item">
        <div class="step-num idle">3</div>
        <span class="step-label idle">Reset Password</span>
    </div>
</div>

<form method="POST" action="{{ route('password.email') }}">
    @csrf

    <div class="fg">
        <label class="fl" for="email">Alamat Email Terdaftar</label>
        <div class="iw">
            <input id="email" type="email" name="email" class="fc"
                value="{{ old('email') }}"
                placeholder="email@rbtv.co.id"
                required autofocus autocomplete="email">
        </div>
    </div>

    <div class="info-box">
        Link reset akan dikirim ke email yang terdaftar di sistem. Periksa folder <strong>Spam</strong> jika tidak muncul dalam beberapa menit.
    </div>

    <button type="submit" class="btn-go">Kirim Link Reset Password &rarr;</button>
</form>

<a href="{{ route('login') }}" class="back-link">&larr; Kembali ke halaman login</a>

@endsection
