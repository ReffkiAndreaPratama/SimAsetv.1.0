@extends('layouts.app')
@section('title', 'Kelola Ruangan')
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-building"></i> Master Data</div>
            <h1 class="page-hero-title">Ruangan & Lokasi</h1>
            <p class="page-hero-sub">Pantau distribusi aset di setiap ruangan RBTV Bengkulu</p>
        </div>
        <div class="page-hero-right">
            <button type="button" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;"
                data-bs-toggle="modal" data-bs-target="#modalPdfRuangan">
                <i class="fas fa-file-pdf text-danger"></i> Cetak PDF
            </button>
            <a href="{{ route('ruangan.create') }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-plus"></i> Tambah Ruangan
            </a>
        </div>
    </div>

    {{-- Stats --}}
    <div class="stats-grid" style="grid-template-columns:repeat(4,1fr);">
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(59,130,246,.1);color:#3B82F6;"><i class="fas fa-building"></i></div>
            <div>
                <div class="stat-label">Total Ruangan</div>
                <div class="stat-val">{{ number_format($totalRuangan) }}</div>
                <div class="stat-sub">Semua lokasi</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(59,130,246,.1);color:#3B82F6;"><i class="fas fa-boxes"></i></div>
            <div>
                <div class="stat-label">Total Aset</div>
                <div class="stat-val" style="color:#2563EB;">{{ number_format($totalAset) }}</div>
                <div class="stat-sub">Tersebar di semua ruangan</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(16,185,129,.1);color:#10B981;"><i class="fas fa-door-open"></i></div>
            <div>
                <div class="stat-label">Terisi Aset</div>
                <div class="stat-val" style="color:#059669;">{{ number_format($ruanganTerisi) }}</div>
                <div class="stat-sub">Ada aset di dalamnya</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(245,158,11,.1);color:#F59E0B;"><i class="fas fa-inbox"></i></div>
            <div>
                <div class="stat-label">Kosong</div>
                <div class="stat-val" style="color:#D97706;">{{ number_format($ruanganKosong) }}</div>
                <div class="stat-sub">Belum ada aset</div>
            </div>
        </div>
    </div>

    {{-- Filter --}}
    <div class="filter-bar">
        <form method="GET" action="{{ route('ruangan.index') }}">
            <div class="filter-group wide">
                <label class="filter-label">Pencarian</label>
                <input type="text" name="search" class="filter-input" placeholder="Cari nama ruangan..." value="{{ request('search') }}">
            </div>
            <div class="filter-group">
                <label class="filter-label">Status</label>
                <select name="status" class="filter-select">
                    <option value="">Semua</option>
                    <option value="terisi" {{ request('status') == 'terisi' ? 'selected' : '' }}>Terisi Aset</option>
                    <option value="kosong" {{ request('status') == 'kosong' ? 'selected' : '' }}>Kosong</option>
                </select>
            </div>
            <div class="filter-actions">
                <button type="submit" class="btn btn-primary d-flex align-items-center gap-1" style="height:38px;font-size:.85rem;padding:0 16px;">
                    <i class="fas fa-search"></i> Cari
                </button>
                <a href="{{ route('ruangan.index') }}" class="btn btn-light border" style="height:38px;" title="Reset">
                    <i class="fas fa-undo-alt"></i>
                </a>
            </div>
        </form>
    </div>

    {{-- Table --}}
    <div class="table-card">
        <div class="table-card-header">
            <h2 class="table-card-title"><i class="fas fa-building"></i> Daftar Ruangan</h2>
            <span class="table-card-meta">{{ $ruangans->total() }} ruangan</span>
        </div>

        <div style="overflow-x:auto;">
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width:40px;padding-left:20px;">#</th>
                        <th>Nama Ruangan</th>
                        <th style="width:130px;">Lantai</th>
                        <th>Keterangan</th>
                        <th style="width:140px;text-align:center;">Jumlah Aset</th>
                        <th style="width:100px;text-align:right;padding-right:20px;">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse($ruangans as $r)
                    <tr>
                        <td style="padding-left:20px;color:#9CA3AF;font-size:.75rem;">
                            {{ $loop->iteration + ($ruangans->currentPage()-1) * $ruangans->perPage() }}
                        </td>
                        <td>
                            <div style="display:flex;align-items:center;gap:12px;">
                                <div style="width:38px;height:38px;border-radius:10px;background:#EFF6FF;color:#2563EB;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0;">
                                    <i class="fas fa-door-open"></i>
                                </div>
                                <div style="font-weight:600;color:#111827;">{{ $r->nama_ruangan }}</div>
                            </div>
                        </td>
                        <td>
                            @if($r->lantai)
                                <span class="cat-chip"><i class="fas fa-layer-group" style="font-size:.6rem;"></i> {{ $r->lantai }}</span>
                            @else
                                <span style="color:#D1D5DB;">—</span>
                            @endif
                        </td>
                        <td>
                            @if($r->keterangan)
                                <span style="font-size:.8rem;color:#6B7280;" title="{{ $r->keterangan }}">
                                    {{ Str::limit($r->keterangan, 50) }}
                                </span>
                            @else
                                <span style="color:#D1D5DB;">—</span>
                            @endif
                        </td>
                        <td style="text-align:center;">
                            @if($r->assets_count > 0)
                                <span class="status-pill pill-aktif"><i class="fas fa-boxes" style="font-size:.65rem;"></i> {{ $r->assets_count }} aset</span>
                            @else
                                <span class="status-pill pill-nonaktif"><i class="fas fa-inbox" style="font-size:.65rem;"></i> Kosong</span>
                            @endif
                        </td>
                        <td style="padding-right:20px;">
                            <div class="act-group">
                                <a href="{{ route('ruangan.show', $r->kode_ruangan) }}" class="act-btn act-view" title="Detail"><i class="fas fa-eye"></i></a>
                                <a href="{{ route('ruangan.edit', $r->kode_ruangan) }}" class="act-btn act-edit" title="Edit"><i class="fas fa-pencil-alt"></i></a>
                                @if($r->assets_count > 0)
                                <a href="{{ route('laporan.ruangan', $r->kode_ruangan) }}" class="act-btn" title="Cetak PDF" target="_blank"
                                   style="background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;">
                                    <i class="fas fa-file-pdf"></i>
                                </a>
                                @endif
                                <form action="{{ route('ruangan.destroy', $r->kode_ruangan) }}" method="POST" style="display:inline;margin:0;"
                                    data-confirm data-confirm-name="{{ $r->nama_ruangan }}">
                                    @csrf @method('DELETE')
                                    <button type="submit" class="act-btn act-del" title="Hapus"><i class="fas fa-trash-alt"></i></button>
                                </form>
                            </div>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="6">
                            <div class="empty-state">
                                <i class="fas fa-building empty-icon"></i>
                                <h4>Belum Ada Ruangan</h4>
                                <p>Mulai dengan menambahkan ruangan pertama.</p>
                                <a href="{{ route('ruangan.create') }}" class="btn btn-primary btn-sm"><i class="fas fa-plus me-1"></i> Tambah Ruangan</a>
                            </div>
                        </td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
        </div>

        <div class="pagi-bar">
            <span class="pagi-info">
                @if($ruangans->total() > 0)
                    Menampilkan <strong>{{ $ruangans->firstItem() }}</strong>–<strong>{{ $ruangans->lastItem() }}</strong>
                    dari <strong>{{ number_format($ruangans->total()) }}</strong> data
                @else
                    Menampilkan 0 data
                @endif
            </span>
            @if($ruangans->hasPages())
                {{ $ruangans->withQueryString()->links() }}
            @endif
        </div>
    </div>

</div>

{{-- Modal Pilih Ruangan untuk PDF --}}
<div class="modal fade" id="modalPdfRuangan" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content" style="border-radius:16px;border:1px solid #E5E7EB;">
            <div class="modal-header" style="border-bottom:1px solid #F3F4F6;padding:18px 24px 14px;">
                <h5 class="modal-title fw-bold">
                    <i class="fas fa-file-pdf text-danger me-2"></i> Cetak PDF Per Ruangan
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body" style="padding:20px 24px;">
                <p class="text-muted mb-3" style="font-size:.875rem;">
                    Pilih ruangan untuk mengunduh laporan aset khusus ruangan tersebut.
                </p>
                <label class="form-label fw-semibold" style="font-size:.82rem;">Pilih Ruangan</label>
                <select id="modalRuanganSelect" class="form-select" style="font-size:.875rem;">
                    <option value="">— Pilih Ruangan —</option>
                    @foreach($allRuangans as $r)
                    <option value="{{ route('laporan.ruangan', $r->kode_ruangan) }}"
                        {{ $r->assets_count == 0 ? 'disabled' : '' }}>
                        {{ $r->nama_ruangan }}
                        @if($r->lantai) — {{ $r->lantai }}@endif
                        ({{ $r->assets_count }} aset)
                    </option>
                    @endforeach
                </select>
                @if($allRuangans->where('assets_count', 0)->count() > 0)
                <div class="form-text mt-1" style="font-size:.75rem;">
                    <i class="fas fa-info-circle me-1"></i> Ruangan kosong tidak dapat dicetak.
                </div>
                @endif
            </div>
            <div class="modal-footer" style="border-top:1px solid #F3F4F6;padding:14px 24px 18px;">
                <button type="button" class="btn btn-light border" data-bs-dismiss="modal">Batal</button>
                <a id="modalPdfLink" href="#" target="_blank"
                   class="btn btn-danger d-flex align-items-center gap-2"
                   style="pointer-events:none;opacity:.45;"
                   onclick="if(this.style.pointerEvents==='none')return false;">
                    <i class="fas fa-file-pdf"></i> Unduh PDF
                </a>
            </div>
        </div>
    </div>
</div>

@push('scripts')
<script>
document.getElementById('modalRuanganSelect').addEventListener('change', function() {
    const link = document.getElementById('modalPdfLink');
    if (this.value) {
        link.href = this.value;
        link.style.pointerEvents = 'auto';
        link.style.opacity = '1';
    } else {
        link.href = '#';
        link.style.pointerEvents = 'none';
        link.style.opacity = '.45';
    }
});
</script>
@endpush
@endsection

