@extends('layouts.app')
@section('title', 'Tambah Ruangan Baru')
@push('styles')
@include('components.form-styles')
@endpush

@section('content')
<div class="page-container">

    <div class="page-hero-mini">
        <div class="hero-mini-left">
            <div class="hero-mini-badge"><i class="fas fa-plus-circle"></i> Tambah Ruangan</div>
            <h1 class="hero-mini-title">Tambah Ruangan Baru</h1>
            <p class="hero-mini-sub">Daftarkan lokasi/ruangan baru ke dalam sistem</p>
        </div>
        <div class="hero-mini-right">
            <a href="{{ route('ruangan.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
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

    <form action="{{ route('ruangan.store') }}" method="POST">
        @csrf
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(59,130,246,.1);--ic-color:#2563EB;"><i class="fas fa-building"></i></div>
                <h2 class="form-card-header-title">Informasi Ruangan</h2>
            </div>
            <div class="form-card-body">
                <div class="row g-3">
                    <div class="col-md-8">
                        <label class="field-label">Nama Ruangan <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-door-open"></i></span>
                            <input type="text" name="nama_ruangan" class="form-control @error('nama') is-invalid @enderror"
                                value="{{ old('nama_ruangan') }}" required placeholder="Contoh: Studio Utama">
                            @error('nama')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-4">
                        <label class="field-label">Lantai</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-layer-group"></i></span>
                            <input type="text" name="lantai" class="form-control"
                                value="{{ old('lantai') }}" placeholder="Contoh: Lantai 1">
                        </div>
                    </div>
                    <div class="col-12">
                        <label class="field-label">Keterangan</label>
                        <div class="input-group">
                            <span class="input-group-text" style="align-items:flex-start;padding-top:12px;"><i class="fas fa-align-left"></i></span>
                            <textarea name="keterangan" class="form-control @error('keterangan') is-invalid @enderror"
                                rows="3" placeholder="Fungsi ruangan, lokasi detail, atau catatan lain (opsional)">{{ old('keterangan') }}</textarea>
                            @error('keterangan')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="form-actions">
            <a href="{{ route('ruangan.index') }}" class="btn btn-light border px-4"><i class="fas fa-times me-1"></i> Batal</a>
            <button type="submit" class="btn btn-primary px-5"><i class="fas fa-save me-1"></i> Simpan Ruangan</button>
        </div>
    </form>
</div>
@endsection

