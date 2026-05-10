@extends('layouts.app')
@section('title', 'Detail Barang — ' . $barang->kode_barang)
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="detail-hero">
        <div class="detail-hero-left">
            <div class="detail-hero-badge"><i class="fas fa-cubes"></i> Detail Barang</div>
            <h1 class="detail-hero-title">
                {{ $barang->nama_barang }}
                <span class="kode-chip-white ms-2">{{ $barang->kode_barang }}</span>
            </h1>
            <p class="detail-hero-sub">
                {{ $barang->kategori ?? 'Tanpa Kategori' }}
                &nbsp;·&nbsp;
                Aktif
            </p>
        </div>
        <div class="detail-hero-right">
            <a href="{{ route('barang.edit', $barang->kode_barang) }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-pencil-alt"></i> Edit
            </a>
            <a href="{{ route('barang.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
    </div>

    <div class="row g-3">

        {{-- Kolom Kiri --}}
        <div class="col-lg-8">

            {{-- Informasi Barang --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(29,78,216,.1);--ic-color:#1d4ed8;"><i class="fas fa-info-circle"></i></div>
                    <h2 class="detail-card-title">Informasi Barang</h2>
                </div>
                <div class="info-row">
                    <span class="info-label">Kode Barang</span>
                    <span class="info-value"><span class="kode-chip">{{ $barang->kode_barang }}</span></span>
                </div>
                <div class="info-row">
                    <span class="info-label">Nama Barang</span>
                    <span class="info-value fw-semibold">{{ $barang->nama_barang }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Kategori</span>
                    <span class="info-value">
                        @if($barang->kategori)
                            <span class="cat-chip"><i class="fas fa-tag" style="font-size:.6rem;"></i> {{ $barang->kategori }}</span>
                        @else
                            <span class="text-muted">—</span>
                        @endif
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Jumlah</span>
                    <span class="info-value">
                        <span class="fw-bold" style="font-size:1.05rem;">{{ $barang->jumlah ?? 0 }}</span>
                        <span class="text-muted ms-1" style="font-size:.8rem;">unit</span>
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Keterangan</span>
                    <span class="info-value">{{ $barang->keterangan ?? '—' }}</span>
                </div>
            </div>
        </div>

        {{-- Kolom Kanan --}}
        <div class="col-lg-4">

            {{-- Sistem --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(107,114,128,.1);--ic-color:#6B7280;"><i class="fas fa-server"></i></div>
                    <h2 class="detail-card-title">Informasi Sistem</h2>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-plus-circle me-1 text-success"></i> Dibuat</span>
                    <span class="sys-value">{{ $barang->created_at?->format('d M Y H:i') ?? '—' }}</span>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-edit me-1 text-warning"></i> Diperbarui</span>
                    <span class="sys-value">{{ $barang->updated_at?->format('d M Y H:i') ?? '—' }}</span>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-fingerprint me-1 text-primary"></i> Primary Key</span>
                    <span class="sys-value" style="color:#1d4ed8;font-family:monospace;">{{ $barang->kode_barang }}</span>
                </div>
            </div>

            {{-- Quick Actions --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(245,158,11,.1);--ic-color:#F59E0B;"><i class="fas fa-bolt"></i></div>
                    <h2 class="detail-card-title">Aksi Cepat</h2>
                </div>
                <div style="padding:14px;">
                    <div class="d-grid gap-2">
                        <a href="{{ route('barang.edit', $barang->kode_barang) }}" class="btn btn-warning d-flex align-items-center justify-content-center gap-2" style="color:#fff;">
                            <i class="fas fa-pencil-alt"></i> Edit Barang Ini
                        </a>
                        <form action="{{ route('barang.destroy', $barang->kode_barang) }}" method="POST"
                            data-confirm data-confirm-name="{{ $barang->nama_barang }}">
                            @csrf @method('DELETE')
                            <button type="submit" class="btn btn-danger w-100 d-flex align-items-center justify-content-center gap-2">
                                <i class="fas fa-trash-alt"></i> Hapus Barang
                            </button>
                        </form>
                        <a href="{{ route('barang.index') }}" class="btn btn-light border d-flex align-items-center justify-content-center gap-2">
                            <i class="fas fa-list-ul"></i> Kembali ke Daftar
                        </a>
                    </div>
                </div>
            </div>

        </div>
    </div>

</div>
@endsection

