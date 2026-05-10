@extends('layouts.app')
@section('title', 'Tambah Barang Baru')
@push('styles')
@include('components.form-styles')
@endpush

@section('content')
<div class="page-container">

    <div class="page-hero-mini">
        <div class="hero-mini-left">
            <div class="hero-mini-badge"><i class="fas fa-plus-circle"></i> Tambah Barang</div>
            <h1 class="hero-mini-title">Tambah Master Barang Baru</h1>
            <p class="hero-mini-sub">Daftarkan jenis barang baru ke dalam katalog master data</p>
        </div>
        <div class="hero-mini-right">
            <a href="{{ route('barang.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
        <div class="hero-accent-bar"></div>
    </div>

    @if($errors->any())
    <div class="alert alert-danger d-flex gap-2 mb-4">
        <i class="fas fa-exclamation-circle flex-shrink-0 mt-1"></i>
        <div><strong>Terdapat kesalahan input:</strong>
            <ul class="mb-0 mt-1 ps-3">@foreach($errors->all() as $err)<li style="font-size:.875rem;">{{ $err }}</li>@endforeach</ul>
        </div>
    </div>
    @endif

    <form method="POST" action="{{ route('barang.store') }}">
        @csrf
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(79,70,229,.1);--ic-color:#4F46E5;"><i class="fas fa-cubes"></i></div>
                <h2 class="form-card-header-title">Informasi Barang</h2>
            </div>
            <div class="form-card-body">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="field-label">Nama Barang <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-cube"></i></span>
                            <input type="text" name="nama_barang" class="form-control @error('nama_barang') is-invalid @enderror"
                                value="{{ old('nama_barang') }}" required placeholder="Masukkan nama barang">
                            @error('nama_barang')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-4">
                        <label class="field-label">Kategori <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-tags"></i></span>
                            <select name="kategori" class="form-select @error('kategori') is-invalid @enderror" required>
                                <option value="">Pilih Kategori...</option>
                                @foreach(['Kamera','Audio','Komputer','Lighting','Furniture','Peralatan Kantor','Lainnya'] as $kat)
                                <option value="{{ $kat }}" {{ old('kategori') == $kat ? 'selected' : '' }}>{{ $kat }}</option>
                                @endforeach
                            </select>
                            @error('kategori')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-2">
                        <label class="field-label">Jumlah</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-sort-numeric-up"></i></span>
                            <input type="number" name="jumlah" class="form-control @error('jumlah') is-invalid @enderror"
                                value="{{ old('jumlah', 0) }}" min="0" placeholder="0">
                            @error('jumlah')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-12">
                        <label class="field-label">Keterangan</label>
                        <textarea name="keterangan" class="form-control @error('keterangan') is-invalid @enderror"
                            rows="3" placeholder="Deskripsi atau catatan tambahan tentang barang ini...">{{ old('keterangan') }}</textarea>
                        @error('keterangan')<div class="invalid-feedback">{{ $message }}</div>@enderror
                    </div>
                </div>
            </div>
        </div>
        <div class="form-actions">
            <a href="{{ route('barang.index') }}" class="btn btn-light border px-4"><i class="fas fa-times me-1"></i> Batal</a>
            <button type="submit" class="btn btn-primary px-5"><i class="fas fa-save me-1"></i> Simpan Barang</button>
        </div>
    </form>
</div>
@endsection
