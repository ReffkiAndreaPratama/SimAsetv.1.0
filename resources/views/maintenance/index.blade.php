@extends('layouts.app')
@section('title', 'Manajemen Maintenance')
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero" style="background:linear-gradient(135deg,#78350f 0%,#92400e 40%,#b45309 75%,#d97706 100%);">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-tools"></i> Maintenance</div>
            <h1 class="page-hero-title">Manajemen Maintenance</h1>
            <p class="page-hero-sub">Pantau dan kelola aset yang sedang dalam proses perbaikan</p>
        </div>
        <div class="page-hero-right">
            <a href="{{ route('laporan.maintenance.pdf') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-file-pdf text-danger"></i> Export PDF
            </a>
            <a href="{{ route('laporan.maintenance.csv') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-file-csv text-success"></i> Export CSV
            </a>
            <a href="{{ route('aset.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-boxes"></i> Lihat Semua Aset
            </a>
        </div>
    </div>

    {{-- Stats --}}
    <div class="stats-grid" style="grid-template-columns:repeat(4,1fr);">
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(245,158,11,.1);color:#D97706;"><i class="fas fa-tools"></i></div>
            <div>
                <div class="stat-label">Total Maintenance</div>
                <div class="stat-val" style="color:#D97706;">{{ number_format($totalMaintenance) }}</div>
                <div class="stat-sub">Sedang diperbaiki</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(220,38,38,.1);color:#DC2626;"><i class="fas fa-times-circle"></i></div>
            <div>
                <div class="stat-label">Rusak Berat</div>
                <div class="stat-val" style="color:#DC2626;">{{ number_format($rusakBerat) }}</div>
                <div class="stat-sub">Penanganan segera</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(245,158,11,.1);color:#F59E0B;"><i class="fas fa-exclamation-triangle"></i></div>
            <div>
                <div class="stat-label">Rusak Ringan</div>
                <div class="stat-val" style="color:#F59E0B;">{{ number_format($rusakRingan) }}</div>
                <div class="stat-sub">Perbaikan minor</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(107,114,128,.1);color:#6B7280;"><i class="fas fa-list-alt"></i></div>
            <div>
                <div class="stat-label">Total Bermasalah</div>
                <div class="stat-val" style="color:#6B7280;">{{ number_format($totalRusak) }}</div>
                <div class="stat-sub">Rusak ringan + berat</div>
            </div>
        </div>
    </div>

    {{-- Filter --}}
    <div class="filter-bar">
        <form method="GET" action="{{ route('maintenance.index') }}">
            <div class="filter-group wide">
                <label class="filter-label">Pencarian</label>
                <input type="text" name="search" class="filter-input" placeholder="Kode aset atau nama barang..." value="{{ request('search') }}">
            </div>
            <div class="filter-group">
                <label class="filter-label">Kondisi</label>
                <select name="kondisi" class="filter-select">
                    <option value="">Semua Kondisi</option>
                    @foreach(['Baik','Rusak Ringan','Rusak Berat'] as $k)
                    <option value="{{ $k }}" {{ request('kondisi') == $k ? 'selected' : '' }}>{{ $k }}</option>
                    @endforeach
                </select>
            </div>
            <div class="filter-actions">
                <button type="submit" class="btn btn-warning d-flex align-items-center gap-1" style="color:#fff;height:38px;font-size:.85rem;padding:0 16px;">
                    <i class="fas fa-search"></i> Cari
                </button>
                <a href="{{ route('maintenance.index') }}" class="btn btn-light border" style="height:38px;" title="Reset">
                    <i class="fas fa-undo-alt"></i>
                </a>
            </div>
        </form>
    </div>

    {{-- Table --}}
    <div class="table-card">
        <div class="table-card-header">
            <h2 class="table-card-title"><i class="fas fa-tools" style="color:#D97706;"></i> Daftar Aset Maintenance</h2>
            <span class="table-card-meta">{{ $assets->total() }} aset</span>
        </div>

        <div style="overflow-x:auto;">
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width:40px;padding-left:20px;">#</th>
                        <th style="width:110px;">Kode Aset</th>
                        <th>Nama Barang</th>
                        <th style="width:130px;">Ruangan</th>
                        <th style="width:115px;text-align:center;">Kondisi</th>
                        <th>Keterangan</th>
                        <th style="width:130px;">Diperbarui</th>
                        <th style="width:160px;text-align:right;padding-right:20px;">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse($assets as $a)
                    <tr>
                        <td style="padding-left:20px;color:#9CA3AF;font-size:.75rem;">
                            {{ $loop->iteration + ($assets->currentPage()-1) * $assets->perPage() }}
                        </td>
                        <td>
                            <span class="kode-chip" style="background:#FFFBEB;border-color:#FDE68A;color:#92400E;">{{ $a->kode_aset }}</span>
                        </td>
                        <td>
                            <div style="font-weight:600;color:#111827;">{{ $a->barang?->nama_barang ?? '—' }}</div>
                            <div style="font-size:.7rem;color:#9CA3AF;margin-top:2px;">{{ $a->barang?->kategori ?? '' }}</div>
                        </td>
                        <td>
                            <span style="font-size:.82rem;color:#6B7280;">
                                <i class="fas fa-map-marker-alt" style="color:#FCD34D;font-size:.65rem;margin-right:3px;"></i>
                                {{ $a->ruangan?->nama_ruangan ?? '—' }}
                            </span>
                        </td>
                        <td style="text-align:center;">
                            @switch($a->kondisi)
                                @case('Baik')
                                    <span class="status-pill pill-baik"><span class="pill-dot"></span> Baik</span>
                                    @break
                                @case('Rusak Ringan')
                                    <span class="status-pill pill-rusak-r"><span class="pill-dot"></span> Rusak Ringan</span>
                                    @break
                                @case('Rusak Berat')
                                    <span class="status-pill pill-rusak-b"><span class="pill-dot"></span> Rusak Berat</span>
                                    @break
                                @default
                                    <span style="color:#D1D5DB;">—</span>
                            @endswitch
                        </td>
                        <td style="font-size:.8rem;color:#6B7280;max-width:180px;">
                            @if($a->keterangan)
                                <span title="{{ $a->keterangan }}">{{ Str::limit($a->keterangan, 55) }}</span>
                            @else
                                <span style="color:#D1D5DB;">—</span>
                            @endif
                        </td>
                        <td style="font-size:.78rem;color:#6B7280;">
                            {{ $a->updated_at?->format('d M Y H:i') ?? '—' }}
                        </td>
                        <td style="padding-right:20px;">
                            <div class="act-group">
                                <a href="{{ route('aset.show', $a->kode_aset) }}" class="act-btn act-view" title="Detail">
                                    <i class="fas fa-eye"></i>
                                </a>
                                <button type="button" class="act-btn"
                                    style="background:#ECFDF5;color:#059669;width:auto;padding:0 10px;font-size:.72rem;font-weight:600;"
                                    data-bs-toggle="modal"
                                    data-bs-target="#modalSelesai"
                                    data-kode="{{ $a->kode_aset }}"
                                    data-nama="{{ $a->barang?->nama_barang ?? $a->kode_aset }}"
                                    title="Tandai Selesai">
                                    <i class="fas fa-check me-1"></i> Selesai
                                </button>
                            </div>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="8">
                            <div class="empty-state">
                                <i class="fas fa-check-double empty-icon" style="color:#FDE68A;"></i>
                                <h4>Tidak Ada Aset Maintenance</h4>
                                <p>
                                    @if(request()->hasAny(['search','kondisi']))
                                        Tidak ada aset yang cocok dengan filter.
                                    @else
                                        Semua aset dalam kondisi baik saat ini.
                                    @endif
                                </p>
                                @if(request()->hasAny(['search','kondisi']))
                                    <a href="{{ route('maintenance.index') }}" class="btn btn-light border btn-sm"><i class="fas fa-undo-alt me-1"></i> Reset Filter</a>
                                @endif
                            </div>
                        </td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
        </div>

        <div class="pagi-bar">
            <span class="pagi-info">
                @if($assets->total() > 0)
                    Menampilkan <strong>{{ $assets->firstItem() }}</strong>–<strong>{{ $assets->lastItem() }}</strong>
                    dari <strong>{{ number_format($assets->total()) }}</strong> data
                @else
                    Menampilkan 0 data
                @endif
            </span>
            @if($assets->hasPages())
                {{ $assets->withQueryString()->links() }}
            @endif
        </div>
    </div>

</div>

{{-- Modal Selesai --}}
<div class="modal fade" id="modalSelesai" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content" style="border-radius:16px;border:1px solid #E5E7EB;">
            <div class="modal-header" style="border-bottom:1px solid #F3F4F6;padding:18px 24px 14px;">
                <h5 class="modal-title fw-bold">
                    <i class="fas fa-check-circle text-success me-2"></i> Selesaikan Maintenance
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form id="formSelesai" method="POST" action="">
                @csrf @method('PATCH')
                <div class="modal-body" style="padding:20px 24px;">
                    <p class="text-muted mb-3" style="font-size:.875rem;">
                        Tandai maintenance aset <strong id="namaAsetModal">—</strong> sebagai selesai.
                        Aset akan kembali ke status <span class="badge bg-success">Aktif</span>.
                    </p>
                    <div class="mb-3">
                        <label class="form-label fw-semibold" style="font-size:.82rem;">Kondisi Setelah Maintenance <span class="text-danger">*</span></label>
                        <select name="kondisi" class="form-select" style="font-size:.875rem;" required>
                            <option value="Baik" selected>Baik</option>
                            <option value="Rusak Ringan">Rusak Ringan</option>
                            <option value="Rusak Berat">Rusak Berat</option>
                        </select>
                    </div>
                    <div>
                        <label class="form-label fw-semibold" style="font-size:.82rem;">Catatan (opsional)</label>
                        <textarea name="keterangan" class="form-control" rows="3"
                            placeholder="Catatan hasil maintenance..." style="font-size:.875rem;"></textarea>
                    </div>
                </div>
                <div class="modal-footer" style="border-top:1px solid #F3F4F6;padding:14px 24px 18px;">
                    <button type="button" class="btn btn-light border" data-bs-dismiss="modal">Batal</button>
                    <button type="submit" class="btn btn-success d-flex align-items-center gap-2">
                        <i class="fas fa-check"></i> Konfirmasi Selesai
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>

@push('scripts')
<script>
document.getElementById('modalSelesai').addEventListener('show.bs.modal', function(e) {
    const btn  = e.relatedTarget;
    const kode = btn.dataset.kode;
    const nama = btn.dataset.nama;
    document.getElementById('namaAsetModal').textContent = nama + ' (' + kode + ')';
    document.getElementById('formSelesai').action = '/maintenance/' + kode + '/complete';
});
</script>
@endpush
@endsection


