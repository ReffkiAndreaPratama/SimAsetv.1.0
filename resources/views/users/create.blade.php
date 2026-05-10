@extends('layouts.app')
@section('title', 'Tambah Pengguna Baru')
@push('styles')
@include('components.form-styles')
@endpush

@section('content')
<div class="page-container">

    <div class="page-hero-mini">
        <div class="hero-mini-left">
            <div class="hero-mini-badge"><i class="fas fa-user-plus"></i> Tambah Pengguna</div>
            <h1 class="hero-mini-title">Tambah Pengguna Baru</h1>
            <p class="hero-mini-sub">Daftarkan akun pengguna baru ke dalam sistem</p>
        </div>
        <div class="hero-mini-right">
            <a href="{{ route('users.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
        <div class="hero-accent-bar"></div>
    </div>

    @if($errors->any())
    <div class="alert alert-danger d-flex gap-2 mb-4">
        <i class="fas fa-exclamation-circle flex-shrink-0 mt-1"></i>
        <div><strong>Terdapat kesalahan:</strong>
            <ul class="mb-0 mt-1 ps-3">@foreach($errors->all() as $err)<li style="font-size:.875rem;">{{ $err }}</li>@endforeach</ul>
        </div>
    </div>
    @endif

    <form method="POST" action="{{ route('users.store') }}">
        @csrf

        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(59,130,246,.1);--ic-color:#2563EB;"><i class="fas fa-id-card"></i></div>
                <h2 class="form-card-header-title">Informasi Akun</h2>
            </div>
            <div class="form-card-body">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="field-label">Nama Lengkap <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-user"></i></span>
                            <input type="text" name="nama" class="form-control @error('nama') is-invalid @enderror"
                                value="{{ old('nama') }}" required placeholder="Nama lengkap">
                            @error('nama')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Email <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            <input type="email" name="email" class="form-control @error('email') is-invalid @enderror"
                                value="{{ old('email') }}" required placeholder="email@rbtv.co.id">
                            @error('email')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Password <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            <input type="password" id="pwCreate" name="password"
                                class="form-control @error('password') is-invalid @enderror"
                                required placeholder="Minimal 8 karakter">
                            <button type="button" class="input-group-text" style="cursor:pointer;border-left:0;"
                                onclick="togglePwField('pwCreate', this)" title="Tampilkan/sembunyikan password">
                                <i class="fas fa-eye" style="color:#94A3B8;font-size:.85rem;"></i>
                            </button>
                            @error('password')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                        <div class="field-hint"><i class="fas fa-info-circle"></i> Harus mengandung huruf besar, huruf kecil, dan angka.</div>
                    </div>
                    <div class="col-md-3">
                        <label class="field-label">Role <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-shield-alt"></i></span>
                            <select name="role" class="form-select @error('role') is-invalid @enderror" required>
                                <option value="">Pilih Role...</option>
                                <option value="admin" {{ old('role') == 'admin' ? 'selected' : '' }}>Admin</option>
                                <option value="staff" {{ old('role') == 'staff' ? 'selected' : '' }}>Staff</option>
                            </select>
                            @error('role')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-3">
                        <label class="field-label">Status Akun</label>
                        <select name="is_active" class="form-select">
                            <option value="1" selected>Aktif</option>
                            <option value="0">Nonaktif</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>

        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(16,185,129,.1);--ic-color:#10B981;"><i class="fas fa-envelope"></i></div>
                <h2 class="form-card-header-title">Notifikasi Email</h2>
                <span class="form-card-header-badge">Opsional</span>
            </div>
            <div class="form-card-body">
                <div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
                    <input type="checkbox" name="kirim_email" id="kirimEmail" value="1"
                        {{ old('kirim_email') ? 'checked' : '' }}
                        style="width:16px;height:16px;margin-top:2px;flex-shrink:0;cursor:pointer;">
                    <div>
                        <label for="kirimEmail" style="font-size:.875rem;font-weight:600;color:#1E40AF;cursor:pointer;display:block;margin-bottom:3px;">
                            <i class="fas fa-paper-plane me-1"></i> Kirim email notifikasi ke pengguna
                        </label>
                        <p style="font-size:.78rem;color:#3B82F6;margin:0;">
                            Sistem akan mengirimkan email berisi kredensial (email & password) agar pengguna bisa langsung login.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="form-actions">
            <a href="{{ route('users.index') }}" class="btn btn-light border px-4"><i class="fas fa-times me-1"></i> Batal</a>
            <button type="submit" class="btn btn-primary px-5"><i class="fas fa-save me-1"></i> Simpan Pengguna</button>
        </div>
    </form>
</div>
@endsection

