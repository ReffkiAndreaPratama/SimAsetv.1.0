@extends('layouts.app')
@section('title', 'Detail Ruangan — ' . $ruangan->nama_ruangan)
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="detail-hero">
        <div class="detail-hero-left">
            <div class="detail-hero-badge"><i class="fas fa-building"></i> Detail Ruangan</div>
            <h1 class="detail-hero-title">{{ $ruangan->nama_ruangan }}</h1>
            <p class="detail-hero-sub">
                @if($ruangan->lantai) {{ $ruangan->lantai }} &nbsp;·&nbsp; @endif
                {{ $ruangan->assets->count() }} aset terdaftar
            </p>
        </div>
        <div class="detail-hero-right">
            <a href="{{ route('ruangan.edit', $ruangan->kode_ruangan) }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-pencil-alt"></i> Edit
            </a>
            <a href="{{ route('ruangan.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
    </div>

    <div class="row g-3">

        {{-- Kolom Kiri --}}
        <div class="col-lg-8">

            {{-- Info --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(59,130,246,.1);--ic-color:#2563EB;"><i class="fas fa-info-circle"></i></div>
                    <h2 class="detail-card-title">Informasi Ruangan</h2>
                </div>
                <div class="info-row">
                    <span class="info-label">Nama Ruangan</span>
                    <span class="info-value fw-semibold">{{ $ruangan->nama_ruangan }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Lantai</span>
                    <span class="info-value">
                        @if($ruangan->lantai)
                            <span class="cat-chip"><i class="fas fa-layer-group" style="font-size:.6rem;"></i> {{ $ruangan->lantai }}</span>
                        @else
                            <span style="color:#D1D5DB;">—</span>
                        @endif
                    </span>
                </div>
                <div class="info-row">
                    <span class="info-label">Jumlah Aset</span>
                    <span class="info-value">
                        <span class="fw-bold" style="font-size:1.05rem;color:{{ $ruangan->assets->count() > 0 ? '#059669' : '#6B7280' }};">
                            {{ $ruangan->assets->count() }}
                        </span>
                        <span class="text-muted ms-1" style="font-size:.8rem;">unit aset</span>
                    </span>
                </div>
                @if($ruangan->keterangan)
                <div class="info-row">
                    <span class="info-label">Keterangan</span>
                    <span class="info-value" style="white-space:pre-line;color:#374151;">{{ $ruangan->keterangan }}</span>
                </div>
                @endif
            </div>

            {{-- Daftar Aset --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(16,185,129,.1);--ic-color:#10B981;"><i class="fas fa-boxes"></i></div>
                    <h2 class="detail-card-title">Aset di Ruangan Ini</h2>
                    <span class="detail-card-badge">{{ $ruangan->assets->count() }} aset</span>
                </div>
                @if($ruangan->assets->count() > 0)
                <div style="overflow-x:auto;">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Kode Aset</th>
                                <th>Nama Barang</th>
                                <th>Kondisi</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach($ruangan->assets as $asset)
                            <tr>
                                <td>
                                    <a href="{{ route('aset.show', $asset->kode_aset) }}" style="font-family:monospace;font-size:.8rem;font-weight:600;color:#1d4ed8;text-decoration:none;">
                                        {{ $asset->kode_aset }}
                                    </a>
                                </td>
                                <td style="font-weight:500;font-size:.85rem;">{{ $asset->barang?->nama_barang ?? '—' }}</td>
                                <td>
                                    @switch($asset->kondisi)
                                        @case('Baik')         <span class="status-pill pill-baik" style="font-size:.68rem;padding:2px 8px;"><span class="pill-dot"></span> Baik</span> @break
                                        @case('Rusak Ringan') <span class="status-pill pill-rusak-r" style="font-size:.68rem;padding:2px 8px;"><span class="pill-dot"></span> Rusak Ringan</span> @break
                                        @case('Rusak Berat')  <span class="status-pill pill-rusak-b" style="font-size:.68rem;padding:2px 8px;"><span class="pill-dot"></span> Rusak Berat</span> @break
                                        @default <span style="color:#D1D5DB;">—</span>
                                    @endswitch
                                </td>
                                <td>
                                    @switch($asset->status)
                                        @case('Aktif')       <span class="status-pill pill-aktif" style="font-size:.68rem;padding:2px 8px;"><span class="pill-dot"></span> Aktif</span> @break
                                        @case('Maintenance') <span class="status-pill pill-maintenance" style="font-size:.68rem;padding:2px 8px;"><span class="pill-dot"></span> Maintenance</span> @break
                                        @default             <span class="status-pill pill-nonaktif" style="font-size:.68rem;padding:2px 8px;"><span class="pill-dot"></span> Non-Aktif</span>
                                    @endswitch
                                </td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
                @else
                <div class="empty-state" style="padding:36px 20px;">
                    <i class="fas fa-box-open empty-icon"></i>
                    <p style="font-size:.85rem;color:#9CA3AF;margin:0;">Belum ada aset di ruangan ini</p>
                </div>
                @endif
            </div>

        </div>

        {{-- Kolom Kanan --}}
        <div class="col-lg-4">

            {{-- Statistik --}}
            <div class="detail-card">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(59,130,246,.1);--ic-color:#2563EB;"><i class="fas fa-chart-pie"></i></div>
                    <h2 class="detail-card-title">Statistik</h2>
                </div>
                <div style="padding:16px;">
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                        <div style="text-align:center;padding:14px;background:#F9FAFB;border-radius:10px;border:1px solid #F3F4F6;">
                            <div style="font-size:22px;font-weight:800;color:#2563EB;">{{ $ruangan->assets->count() }}</div>
                            <div style="font-size:.72rem;color:#6B7280;margin-top:2px;">Total Aset</div>
                        </div>
                        <div style="text-align:center;padding:14px;background:#F9FAFB;border-radius:10px;border:1px solid #F3F4F6;">
                            <div style="font-size:22px;font-weight:800;color:#059669;">{{ $ruangan->assets->where('kondisi','Baik')->count() }}</div>
                            <div style="font-size:.72rem;color:#6B7280;margin-top:2px;">Kondisi Baik</div>
                        </div>
                    </div>
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
                    <span class="sys-value">{{ $ruangan->created_at?->format('d M Y H:i') ?? '—' }}</span>
                </div>
                <div class="sys-row">
                    <span class="sys-label"><i class="fas fa-fingerprint me-1 text-primary"></i> ID</span>
                    <span class="sys-value" style="color:#2563EB;">{{ $ruangan->kode_ruangan }}</span>
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
                        <a href="{{ route('ruangan.edit', $ruangan->kode_ruangan) }}" class="btn btn-warning d-flex align-items-center justify-content-center gap-2" style="color:#fff;">
                            <i class="fas fa-pencil-alt"></i> Edit Ruangan Ini
                        </a>
                        <form action="{{ route('ruangan.destroy', $ruangan->kode_ruangan) }}" method="POST"
                            data-confirm data-confirm-name="{{ $ruangan->nama_ruangan }}"
                            data-confirm-extra="{{ $ruangan->assets->count() > 0 ? 'Ruangan ini masih memiliki ' . $ruangan->assets->count() . ' aset.' : '' }}">
                            @csrf @method('DELETE')
                            <button type="submit" class="btn btn-danger w-100 d-flex align-items-center justify-content-center gap-2">
                                <i class="fas fa-trash-alt"></i> Hapus Ruangan
                            </button>
                        </form>
                        <a href="{{ route('ruangan.index') }}" class="btn btn-light border d-flex align-items-center justify-content-center gap-2">
                            <i class="fas fa-list-ul"></i> Kembali ke Daftar
                        </a>
                    </div>
                </div>
            </div>

        </div>
    </div>

</div>
@endsection


