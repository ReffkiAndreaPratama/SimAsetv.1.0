@extends('layouts.app')
@section('title', 'Edit Pengguna — ' . $user->nama)
@push('styles')
@include('components.form-styles')
@endpush

@section('content')
<div class="page-container">

    <div class="page-hero-mini">
        <div class="hero-mini-left">
            <div class="hero-mini-badge"><i class="fas fa-user-edit"></i> Edit Pengguna</div>
            <h1 class="hero-mini-title">
                Edit Pengguna &nbsp;<span class="kode-chip-white">{{ $user->nama }}</span>
            </h1>
            <p class="hero-mini-sub">{{ $user->email }} &nbsp;·&nbsp; {{ ucfirst($user->role) }}</p>
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

    <form method="POST" action="{{ route('users.update', $user->id_user) }}">
        @csrf @method('PUT')

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
                                value="{{ old('nama', $user->nama) }}" required>
                            @error('nama')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Email <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            <input type="email" name="email" class="form-control @error('email') is-invalid @enderror"
                                value="{{ old('email', $user->email) }}" required>
                            @error('email')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Password Baru</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            <input type="password" id="pwEdit" name="password"
                                class="form-control @error('password') is-invalid @enderror"
                                placeholder="Kosongkan jika tidak diubah">
                            <button type="button" class="input-group-text" style="cursor:pointer;border-left:0;"
                                onclick="togglePwField('pwEdit', this)" title="Tampilkan/sembunyikan password">
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
                                <option value="admin" {{ old('role', $user->role) == 'admin' ? 'selected' : '' }}>Admin</option>
                                <option value="staff" {{ old('role', $user->role) == 'staff' ? 'selected' : '' }}>Staff</option>
                            </select>
                            @error('role')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-3">
                        <label class="field-label">Status Akun</label>
                        <input type="text" class="form-control" value="Aktif" readonly style="background:#F8FAFC;color:#6B7280;">
                    </div>
                </div>
            </div>
        </div>

        <div class="form-actions">
            <a href="{{ route('users.index') }}" class="btn btn-light border px-4"><i class="fas fa-times me-1"></i> Batal</a>
            <button type="submit" class="btn btn-primary px-5"><i class="fas fa-save me-1"></i> Perbarui Pengguna</button>
        </div>
    </form>

    {{-- Info tambahan (read-only) --}}
    <div class="form-card" style="margin-top:0;">
        <div class="form-card-header">
            <div class="form-card-header-icon" style="--ic-bg:rgba(107,114,128,.1);--ic-color:#6B7280;"><i class="fas fa-info-circle"></i></div>
            <h2 class="form-card-header-title">Informasi Sistem</h2>
        </div>
        <div class="form-card-body">
            <div class="row g-3">
                <div class="col-md-4">
                    <label class="field-label">Terdaftar Sejak</label>
                    <div class="input-group">
                        <span class="input-group-text"><i class="fas fa-calendar-plus"></i></span>
                        <input type="text" class="form-control" value="{{ $user->created_at?->format('d M Y H:i') ?? '—' }}" readonly style="background:#F8FAFC;color:#6B7280;">
                    </div>
                </div>
                <div class="col-md-4">
                    <label class="field-label">Login Terakhir</label>
                    <div class="input-group">
                        <span class="input-group-text"><i class="fas fa-sign-in-alt"></i></span>
                        <input type="text" class="form-control" readonly style="background:#F8FAFC;color:#6B7280;"
                            value="Belum pernah login">
                    </div>
                </div>
                <div class="col-md-4">
                    <label class="field-label">Diperbarui</label>
                    <div class="input-group">
                        <span class="input-group-text"><i class="fas fa-edit"></i></span>
                        <input type="text" class="form-control" value="{{ $user->updated_at?->format('d M Y H:i') ?? '—' }}" readonly style="background:#F8FAFC;color:#6B7280;">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


