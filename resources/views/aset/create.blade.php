@extends('layouts.app')
@section('title', 'Tambah Aset Baru')
@push('styles')
@include('components.form-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero-mini">
        <div class="hero-mini-left">
            <div class="hero-mini-badge"><i class="fas fa-plus-circle"></i> Tambah Aset</div>
            <h1 class="hero-mini-title">Tambah Aset Baru</h1>
            <p class="hero-mini-sub">Daftarkan unit aset baru ke dalam sistem RBTV Bengkulu</p>
        </div>
        <div class="hero-mini-right">
            <a href="{{ route('aset.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
        <div class="hero-accent-bar"></div>
    </div>

    @if($errors->any())
    <div class="alert alert-danger d-flex gap-2 mb-4">
        <i class="fas fa-exclamation-circle flex-shrink-0 mt-1"></i>
        <div>
            <strong>Terdapat kesalahan input:</strong>
            <ul class="mb-0 mt-1 ps-3">
                @foreach($errors->all() as $err)<li style="font-size:.875rem;">{{ $err }}</li>@endforeach
            </ul>
        </div>
    </div>
    @endif

    <form method="POST" action="{{ route('aset.store') }}" enctype="multipart/form-data">
        @csrf

        {{-- Informasi Barang --}}
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(79,70,229,.1);--ic-color:#4F46E5;"><i class="fas fa-box-open"></i></div>
                <h2 class="form-card-header-title">Informasi Barang</h2>
            </div>
            <div class="form-card-body">
                <div class="row g-3">
                    <div class="col-md-8">
                        <label class="field-label">Jenis Barang <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-cubes"></i></span>
                            <select name="kode_barang" class="form-select @error('kode_barang') is-invalid @enderror" required>
                                <option value="">Pilih Barang...</option>
                                @foreach($barangs as $b)
                                <option value="{{ $b->kode_barang }}" {{ old('kode_barang') == $b->kode_barang ? 'selected' : '' }}>
                                    {{ $b->kode_barang }} — {{ $b->nama_barang }}@if($b->kategori) ({{ $b->kategori }})@endif
                                </option>
                                @endforeach
                            </select>
                            @error('kode_barang')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-4">
                        <label class="field-label">Serial Number</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-hashtag"></i></span>
                            <input type="text" name="serial_number" class="form-control @error('serial_number') is-invalid @enderror"
                                value="{{ old('serial_number') }}" placeholder="Contoh: SN-123456">
                            @error('serial_number')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                </div>
            </div>
        </div>

        {{-- Lokasi & Harga --}}
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(16,185,129,.1);--ic-color:#10B981;"><i class="fas fa-map-marker-alt"></i></div>
                <h2 class="form-card-header-title">Lokasi & Harga</h2>
            </div>
            <div class="form-card-body">
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="field-label">Ruangan <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-building"></i></span>
                            <select name="kode_ruangan" class="form-select @error('kode_ruangan') is-invalid @enderror" required>
                                <option value="">Pilih Ruangan...</option>
                                @foreach($ruangans as $r)
                                <option value="{{ $r->kode_ruangan }}" {{ old('kode_ruangan') == $r->kode_ruangan ? 'selected' : '' }}>{{ $r->nama_ruangan }}</option>
                                @endforeach
                            </select>
                            @error('kode_ruangan')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="field-label">Harga</label>
                        <div class="input-group">
                            <span class="input-group-text">Rp</span>
                            <input type="number" name="harga" class="form-control @error('harga') is-invalid @enderror"
                                value="{{ old('harga') }}" placeholder="0" min="0" step="1000">
                            @error('harga')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                </div>
            </div>
        </div>

        {{-- Kondisi & Status --}}
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(245,158,11,.1);--ic-color:#F59E0B;"><i class="fas fa-star-half-alt"></i></div>
                <h2 class="form-card-header-title">Kondisi & Status</h2>
            </div>
            <div class="form-card-body">
                <div class="row g-3">
                    <div class="col-md-4">
                        <label class="field-label">Kondisi <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-star"></i></span>
                            <select name="kondisi" class="form-select @error('kondisi') is-invalid @enderror" required>
                                @foreach(['Baik','Rusak Ringan','Rusak Berat'] as $k)
                                <option value="{{ $k }}" {{ old('kondisi','Baik') == $k ? 'selected' : '' }}>{{ $k }}</option>
                                @endforeach
                            </select>
                            @error('kondisi')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-md-4">
                        <label class="field-label">Status <span class="req">*</span></label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-toggle-on"></i></span>
                            <select name="status" class="form-select @error('status') is-invalid @enderror" required>
                                @foreach(['Aktif','Maintenance','Non-Aktif'] as $s)
                                <option value="{{ $s }}" {{ old('status','Aktif') == $s ? 'selected' : '' }}>{{ $s }}</option>
                                @endforeach
                            </select>
                            @error('status')<div class="invalid-feedback">{{ $message }}</div>@enderror
                        </div>
                    </div>
                    <div class="col-12">
                        <label class="field-label">Keterangan</label>
                        <textarea name="keterangan" class="form-control @error('keterangan') is-invalid @enderror"
                            rows="3" placeholder="Catatan tambahan tentang aset ini...">{{ old('keterangan') }}</textarea>
                        @error('keterangan')<div class="invalid-feedback">{{ $message }}</div>@enderror
                    </div>
                </div>
            </div>
        </div>

        {{-- Foto --}}
        <div class="form-card">
            <div class="form-card-header">
                <div class="form-card-header-icon" style="--ic-bg:rgba(6,182,212,.1);--ic-color:#06B6D4;"><i class="fas fa-image"></i></div>
                <h2 class="form-card-header-title">Foto Aset</h2>
                <span class="form-card-header-badge">Opsional</span>
            </div>
            <div class="form-card-body">
                <div class="row g-3 align-items-start">
                    <div class="col-md-8">
                        <label class="field-label">Upload Foto</label>
                        <input type="file" name="foto" class="form-control @error('foto') is-invalid @enderror"
                            accept="image/jpeg,image/png,image/gif" id="fotoInput">
                        <div class="field-hint"><i class="fas fa-info-circle"></i> Format: JPG, PNG, GIF — Maks. 2MB</div>
                        @error('foto')<div class="text-danger small mt-1">{{ $message }}</div>@enderror
                    </div>
                    <div class="col-md-4">
                        <label class="field-label">Preview</label>
                        <div class="foto-preview-box" id="fotoPreview">
                            <span><i class="fas fa-image me-1"></i> Belum ada foto</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="form-actions">
            <a href="{{ route('aset.index') }}" class="btn btn-light border px-4"><i class="fas fa-times me-1"></i> Batal</a>
            <button type="submit" class="btn btn-primary px-5"><i class="fas fa-save me-1"></i> Simpan Aset</button>
        </div>
    </form>
</div>

@push('scripts')
<script>
document.getElementById('fotoInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    const preview = document.getElementById('fotoPreview');
    if (file) {
        const reader = new FileReader();
        reader.onload = ev => { preview.innerHTML = '<img src="' + ev.target.result + '" style="width:100%;height:100%;object-fit:cover;">'; };
        reader.readAsDataURL(file);
    } else {
        preview.innerHTML = '<span><i class="fas fa-image me-1"></i> Belum ada foto</span>';
    }
});
</script>
@endpush
@endsection
