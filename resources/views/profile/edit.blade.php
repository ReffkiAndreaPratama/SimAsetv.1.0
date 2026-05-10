@extends('layouts.app')
@section('title', 'Profil Saya')

@push('styles')
@include('components.form-styles')
<style>
.profile-hero {
    background: linear-gradient(135deg, #0d1f4e 0%, #1a3470 40%, #1c3d9e 75%, #1e45b8 100%);
    border-radius: 16px; padding: 26px 32px; color: #fff;
    margin-bottom: 22px; display: flex; align-items: center; gap: 20px;
    position: relative; overflow: hidden;
    box-shadow: 0 6px 24px rgba(13,31,78,.28);
}
.profile-hero::after {
    content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #dc2626, #ef4444, rgba(255,255,255,.1));
}
.profile-avatar {
    width: 72px; height: 72px; border-radius: 50%;
    background: rgba(255,255,255,.15); border: 2.5px solid rgba(255,255,255,.35);
    display: flex; align-items: center; justify-content: center;
    font-size: 28px; color: #fff; flex-shrink: 0;
    font-weight: 800;
}
.profile-info h4 { margin: 0 0 5px; font-weight: 800; font-size: 1.2rem; }
.profile-info p  { margin: 0; opacity: .8; font-size: .85rem; display: flex; align-items: center; gap: 8px; }
.role-badge {
    display: inline-flex; align-items: center; gap: 4px;
    background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3);
    border-radius: 20px; padding: 2px 10px; font-size: .72rem; font-weight: 700;
    color: #fff; text-transform: capitalize;
}
</style>
@endpush

@section('content')
<div class="page-container" style="max-width:860px;">

    {{-- Hero --}}
    <div class="profile-hero">
        <div class="profile-avatar">
            {{ strtoupper(substr(auth()->user()->nama, 0, 1)) }}
        </div>
        <div class="profile-info">
            <h4>{{ auth()->user()->nama }}</h4>
            <p>
                <span class="role-badge">
                    <i class="fas fa-{{ auth()->user()->isAdmin() ? 'shield-alt' : 'user-tie' }}" style="font-size:.6rem;"></i>
                    {{ ucfirst(auth()->user()->role) }}
                </span>
                {{ auth()->user()->email }}
            </p>
        </div>
    </div>

    @if(session('status') === 'profile-updated')
    <div class="alert alert-success alert-dismissible fade show mb-4">
        <i class="fas fa-check-circle me-2"></i> Profil berhasil diperbarui.
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    @endif
    @if(session('status') === 'password-updated')
    <div class="alert alert-success alert-dismissible fade show mb-4">
        <i class="fas fa-check-circle me-2"></i> Kata sandi berhasil diperbarui.
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    @endif
    @if(session('success'))
    <div class="alert alert-success alert-dismissible fade show mb-4">
        <i class="fas fa-check-circle me-2"></i> {{ session('success') }}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    @endif

    {{-- Informasi Dasar --}}
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-header-icon" style="--ic-bg:rgba(59,130,246,.1);--ic-color:#2563EB;"><i class="fas fa-id-card"></i></div>
            <h2 class="form-card-header-title">Informasi Dasar</h2>
        </div>
        <div class="form-card-body">
            <form method="POST" action="{{ route('profile.update') }}">
                @csrf @method('PATCH')
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="field-label">Nama Lengkap</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-user"></i></span>
                            <input type="text" name="nama" class="form-control @error('name') is-invalid @enderror"
                                value="{{ old('name', auth()->user()->nama) }}" required>
                            @error('name')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Alamat Email</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            <input type="email" name="email" class="form-control @error('email') is-invalid @enderror"
                                value="{{ old('email', auth()->user()->email) }}" required>
                            @error('email')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                </div>
                <div class="form-actions mt-3">
                    <button type="submit" class="btn btn-primary px-5"><i class="fas fa-save me-1"></i> Simpan Perubahan</button>
                </div>
            </form>
        </div>
    </div>

    {{-- Ubah Kata Sandi --}}
    <div class="form-card">
        <div class="form-card-header">
            <div class="form-card-header-icon" style="--ic-bg:rgba(239,68,68,.1);--ic-color:#DC2626;"><i class="fas fa-lock"></i></div>
            <h2 class="form-card-header-title">Ubah Kata Sandi</h2>
        </div>
        <div class="form-card-body">
            <form method="POST" action="{{ route('password.update') }}">
                @csrf @method('PUT')
                <div class="row g-3">
                    <div class="col-md-12">
                        <label class="field-label">Kata Sandi Saat Ini</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-key"></i></span>
                            <input type="password" name="current_password"
                                class="form-control @error('current_password','updatePassword') is-invalid @enderror"
                                placeholder="Password saat ini" required>
                            @error('current_password','updatePassword')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Kata Sandi Baru</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            <input type="password" name="password"
                                class="form-control @error('password','updatePassword') is-invalid @enderror"
                                placeholder="Minimal 8 karakter" required>
                            @error('password','updatePassword')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Konfirmasi Kata Sandi</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            <input type="password" name="password_confirmation"
                                class="form-control" placeholder="Ulangi password baru" required>
                        </div>
                    </div>
                </div>
                <div class="form-actions mt-3">
                    <button type="submit" class="btn btn-warning px-5" style="color:#fff;"><i class="fas fa-key me-1"></i> Perbarui Kata Sandi</button>
                </div>
            </form>
        </div>
    </div>

</div>
@endsection

