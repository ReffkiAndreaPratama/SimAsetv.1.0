@extends('layouts.app')
@section('title', 'QR Code — ' . $asset->kode_aset)

@push('styles')
<style>
.qr-page-wrap { max-width: 520px; margin: 0 auto; }
.qr-hero {
    background: linear-gradient(135deg, #0d1f4e 0%, #1a3470 40%, #1c3d9e 75%, #1e45b8 100%);
    border-radius: 16px; padding: 22px 28px; color: #fff;
    margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between;
    gap: 16px; flex-wrap: wrap; position: relative; overflow: hidden;
    box-shadow: 0 6px 24px rgba(13,31,78,.28);
}
.qr-hero::after {
    content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #dc2626, #ef4444, rgba(255,255,255,.1));
}
.qr-hero-left { position: relative; z-index: 2; }
.qr-hero-badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 3px 10px; background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25); border-radius: 20px;
    font-size: .68rem; font-weight: 600; color: #fff; margin-bottom: 8px;
}
.qr-hero-title { font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0 0 3px; }
.qr-hero-sub   { font-size: .8rem; color: rgba(255,255,255,.75); margin: 0; }
.kode-chip-w {
    display: inline-flex; align-items: center; padding: 2px 9px;
    background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3);
    border-radius: 5px; font-family: monospace; font-size: .78rem; font-weight: 700; color: #fff;
}

.qr-card {
    background: #fff; border: 1px solid #E5E7EB; border-radius: 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,.06); overflow: hidden;
}
.qr-card-body { padding: 32px; text-align: center; }
.qr-img-wrap {
    display: inline-block; padding: 16px;
    background: #fff; border: 2px solid #E5E7EB; border-radius: 14px;
    margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,.06);
}
.qr-img-wrap img { width: 220px; height: 220px; display: block; }
.qr-scan-hint { font-size: .78rem; color: #9CA3AF; margin-bottom: 24px; }
.qr-actions { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }

.qr-placeholder {
    padding: 40px 20px; background: #F9FAFB;
    border-radius: 12px; border: 2px dashed #E5E7EB;
    color: #9CA3AF; margin-bottom: 20px;
}
.qr-placeholder i { font-size: 3rem; opacity: .25; display: block; margin-bottom: 10px; }

.qr-card-footer {
    padding: 14px 24px; background: #FAFAFA; border-top: 1px solid #F3F4F6;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;
}
.qr-meta { font-size: .78rem; color: #6B7280; display: flex; align-items: center; gap: 5px; }

@media print {
    .qr-hero, .qr-actions, nav, .sidebar, .header, .footer, .no-print { display: none !important; }
    body { background: white !important; }
    .qr-card { box-shadow: none; border: none; }
}
</style>
@endpush

@section('content')
<div class="page-container qr-page-wrap">

    {{-- Hero --}}
    <div class="qr-hero">
        <div class="qr-hero-left">
            <div class="qr-hero-badge"><i class="fas fa-qrcode"></i> QR Code Aset</div>
            <h1 class="qr-hero-title">
                {{ $asset->barang?->nama_barang ?? 'Aset' }}
                &nbsp;<span class="kode-chip-w">{{ $asset->kode_aset }}</span>
            </h1>
            <p class="qr-hero-sub">
                {{ $asset->barang?->kategori ?? '—' }}
                @if($asset->ruangan?->nama_ruangan) &nbsp;·&nbsp; <i class="fas fa-map-marker-alt me-1"></i>{{ $asset->ruangan->nama_ruangan }} @endif
            </p>
        </div>
        <div style="position:relative;z-index:2;">
            <a href="{{ route('aset.show', $asset->kode_aset) }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali
            </a>
        </div>
    </div>

    {{-- QR Card --}}
    <div class="qr-card">
        <div class="qr-card-body">

            @php
                $qrDir   = public_path('qr_codes');
                $qrPath  = null;
                $qrFile  = null;
                if (file_exists($qrDir)) {
                    $files = glob($qrDir . '/qr_' . $asset->kode_aset . '*.png');
                    if (!empty($files)) {
                        $qrPath = $files[0];
                        $qrFile = basename($qrPath);
                    }
                }
            @endphp

            @if($qrPath && file_exists($qrPath))
                <div class="qr-img-wrap">
                    <img src="{{ asset('qr_codes/' . $qrFile) }}" alt="QR Code {{ $asset->kode_aset }}">
                </div>
                <p class="qr-scan-hint">
                    <i class="fas fa-mobile-alt me-1"></i>
                    Scan dengan kamera untuk melihat detail aset ini
                </p>
                <div class="qr-actions">
                    <a href="{{ asset('qr_codes/' . $qrFile) }}"
                       class="btn btn-primary d-flex align-items-center gap-2"
                       download="{{ $asset->kode_aset }}.png">
                        <i class="fas fa-download"></i> Download PNG
                    </a>
                    <button onclick="window.print()" class="btn btn-light border d-flex align-items-center gap-2">
                        <i class="fas fa-print"></i> Cetak
                    </button>
                    <a href="{{ route('qrcode.download', $asset->kode_aset) }}" target="_blank"
                       class="btn btn-outline-primary d-flex align-items-center gap-2">
                        <i class="fas fa-expand"></i> Lihat Label
                    </a>
                </div>
            @else
                <div class="qr-placeholder">
                    <i class="fas fa-qrcode"></i>
                    <span style="font-size:.85rem;">QR Code belum di-generate</span>
                </div>
                <form action="{{ route('aset.generateQr', $asset->kode_aset) }}" method="POST">
                    @csrf
                    <button type="submit" class="btn btn-primary d-inline-flex align-items-center gap-2">
                        <i class="fas fa-magic"></i> Generate QR Code
                    </button>
                </form>
            @endif

        </div>
        <div class="qr-card-footer">
            <span class="qr-meta"><i class="fas fa-building"></i> {{ $asset->ruangan?->nama_ruangan ?? '—' }}</span>
            <span class="qr-meta"><i class="fas fa-tags"></i> {{ $asset->barang?->kategori ?? '—' }}</span>
            <span class="qr-meta"><i class="fas fa-circle" style="font-size:.45rem;color:{{ $asset->status == 'Aktif' ? '#10B981' : '#F59E0B' }};"></i> {{ $asset->status ?? '—' }}</span>
        </div>
    </div>

</div>
@endsection


