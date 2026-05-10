@extends('layouts.app')
@section('title', 'Detail Aset — ' . $asset->kode_aset)
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="detail-hero">
        <div class="detail-hero-left">
            <div class="detail-hero-badge"><i class="fas fa-eye"></i> Detail Aset</div>
            <h1 class="detail-hero-title">
                {{ $asset->barang?->nama_barang ?? 'Detail Aset' }}
                <span class="kode-chip-white ms-2">{{ $asset->kode_aset }}</span>
            </h1>
            <p class="detail-hero-sub">
                {{ $asset->barang?->kategori ?? '—' }}
                @if($asset->ruangan?->nama_ruangan)
                    &nbsp;·&nbsp; <i class="fas fa-map-marker-alt me-1"></i>{{ $asset->ruangan->nama_ruangan }}
                @endif
            </p>
        </div>
        <div class="detail-hero-right">
            <a href="{{ route('aset.edit', $asset->kode_aset) }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-pencil-alt"></i> Edit
            </a>
            <a href="{{ route('aset.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
    </div>

    <div class="row g-3">

        {{-- Kolom Kiri --}}
        <div class="col-lg-8">
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(29,78,216,.1);--ic-color:#1d4ed8;"><i class="fas fa-info-circle"></i></div>
                    <h2 class="detail-card-title">Informasi Aset</h2>
                </div>
                <div class="info-row">
                    <span class="info-label">Kode Aset</span>
                    <span class="info-value"><span class="kode-chip">{{ $asset->kode_aset }}</span></span>
                </div>
                <div class="info-row">
                    <span class="info-label">Kode Barang</span>
                    <span class="info-value">
                        <a href="{{ route('barang.show', $asset->kode_barang) }}" style="font-family:monospace;font-size:.82rem;font-weight:600;color:#1d4ed8;text-decoration:none;">
                            {{ $asset->kode_barang }}
                        </a>
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Nama Barang</span>
                    <span class="info-value fw-semibold">{{ $asset->barang?->nama_barang ?? '—' }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Kategori</span>
                    <span class="info-value">
                        @if($asset->barang?->kategori)
                            <span class="cat-chip"><i class="fas fa-tag" style="font-size:.6rem;"></i> {{ $asset->barang->kategori }}</span>
                        @else
                            <span class="text-muted">—</span>
                        @endif
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Serial Number</span>
                    <span class="info-value" style="font-family:monospace;font-size:.85rem;">{{ $asset->serial_number ?? '—' }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Ruangan</span>
                    <span class="info-value">
                        <i class="fas fa-map-marker-alt text-primary me-1" style="font-size:.75rem;"></i>
                        {{ $asset->ruangan?->nama_ruangan ?? '—' }}
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Harga Perolehan</span>
                    <span class="info-value">
                        @if($asset->harga)
                            <span style="font-weight:600;">Rp {{ number_format($asset->harga, 0, ',', '.') }}</span>
                        @else
                            <span class="text-muted">—</span>
                        @endif
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Keterangan</span>
                    <span class="info-value">{{ $asset->keterangan ?? '—' }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Kondisi</span>
                    <span class="info-value">
                        @switch($asset->kondisi)
                            @case('Baik')         <span class="status-pill pill-baik"><span class="pill-dot"></span> Baik</span> @break
                            @case('Rusak Ringan') <span class="status-pill pill-rusak-r"><span class="pill-dot"></span> Rusak Ringan</span> @break
                            @case('Rusak Berat')  <span class="status-pill pill-rusak-b"><span class="pill-dot"></span> Rusak Berat</span> @break
                            @default              <span class="text-muted">—</span>
                        @endswitch
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Status</span>
                    <span class="info-value">
                        @switch($asset->status)
                            @case('Aktif')       <span class="status-pill pill-aktif"><span class="pill-dot"></span> Aktif</span> @break
                            @case('Maintenance') <span class="status-pill pill-maintenance"><span class="pill-dot"></span> Maintenance</span> @break
                            @default             <span class="status-pill pill-nonaktif"><span class="pill-dot"></span> Non-Aktif</span>
                        @endswitch
                    </span>
                </div>
            </div>
        </div>

        {{-- Kolom Kanan --}}
        <div class="col-lg-4">

            {{-- Foto --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(6,182,212,.1);--ic-color:#06B6D4;"><i class="fas fa-image"></i></div>
                    <h2 class="detail-card-title">Foto Aset</h2>
                </div>
                <div style="padding:16px;">
                    @if($asset->foto && file_exists(public_path('foto_aset/'.$asset->foto)))
                        <img src="{{ asset('foto_aset/'.$asset->foto) }}" alt="Foto Aset"
                             class="img-fluid rounded-3 w-100" style="object-fit:cover;max-height:220px;border:1px solid #E5E7EB;">
                    @else
                        <div class="foto-placeholder">
                            <i class="fas fa-camera-retro" style="font-size:2rem;opacity:.25;"></i>
                            <span style="font-size:.82rem;">Tidak ada foto</span>
                        </div>
                    @endif
                </div>
            </div>

            {{-- QR Code --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(79,70,229,.1);--ic-color:#4F46E5;"><i class="fas fa-qrcode"></i></div>
                    <h2 class="detail-card-title">QR Code</h2>
                </div>
                <div style="padding:16px;text-align:center;">
                    @php
                        $qrDir  = public_path('qr_codes');
                        $qrPath = null; $qrFile = null;
                        if (file_exists($qrDir)) {
                            $files = glob($qrDir . '/qr_' . $asset->kode_aset . '*.png');
                            if (!empty($files)) { $qrPath = $files[0]; $qrFile = basename($qrPath); }
                        }
                    @endphp
                    @if($qrPath && file_exists($qrPath))
                        <img src="{{ asset('qr_codes/' . $qrFile) }}" alt="QR Code"
                             class="img-fluid rounded border p-2 bg-white mb-3" style="max-width:150px;">
                        <div>
                            <a href="{{ route('aset.showQr', $asset->kode_aset) }}" target="_blank"
                               class="btn btn-outline-primary btn-sm d-inline-flex align-items-center gap-1">
                                <i class="fas fa-print"></i> Cetak QR
                            </a>
                        </div>
                    @else
                        <div class="foto-placeholder mb-3">
                            <i class="fas fa-qrcode" style="font-size:2rem;opacity:.25;"></i>
                            <span style="font-size:.82rem;">QR belum digenerate</span>
                        </div>
                        <form action="{{ route('aset.generateQr', $asset->kode_aset) }}" method="POST">
                            @csrf
                            <button type="submit" class="btn btn-primary btn-sm d-inline-flex align-items-center gap-1">
                                <i class="fas fa-magic"></i> Generate QR
                            </button>
                        </form>
                    @endif
                </div>
            </div>

            {{-- Sistem --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(107,114,128,.1);--ic-color:#6B7280;"><i class="fas fa-server"></i></div>
                    <h2 class="detail-card-title">Informasi Sistem</h2>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-plus-circle me-1 text-success"></i> Dibuat</span>
                    <span class="sys-value">{{ $asset->created_at?->format('d M Y H:i') ?? '—' }}</span>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-edit me-1 text-warning"></i> Diperbarui</span>
                    <span class="sys-value">{{ $asset->updated_at?->format('d M Y H:i') ?? '—' }}</span>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-user me-1 text-primary"></i> Dibuat Oleh</span>
                    <span class="sys-value">{{ $asset->user?->nama ?? 'System' }}</span>
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
                        <a href="{{ route('aset.edit', $asset->kode_aset) }}" class="btn btn-warning d-flex align-items-center justify-content-center gap-2" style="color:#fff;">
                            <i class="fas fa-pencil-alt"></i> Edit Aset Ini
                        </a>
                        <form action="{{ route('aset.destroy', $asset->kode_aset) }}" method="POST"
                            data-confirm data-confirm-name="{{ $asset->kode_aset }}">
                            @csrf @method('DELETE')
                            <button type="submit" class="btn btn-danger w-100 d-flex align-items-center justify-content-center gap-2">
                                <i class="fas fa-trash-alt"></i> Hapus Aset
                            </button>
                        </form>
                        <a href="{{ route('aset.index') }}" class="btn btn-light border d-flex align-items-center justify-content-center gap-2">
                            <i class="fas fa-list-ul"></i> Kembali ke Daftar
                        </a>
                    </div>
                </div>
            </div>

        </div>
    </div>

</div>
@endsection
