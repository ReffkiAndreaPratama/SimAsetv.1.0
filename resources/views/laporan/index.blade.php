@extends('layouts.app')
@section('title', 'Laporan & Export')

@push('styles')
<style>
.lap-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:16px; }
.lap-card {
    background:#fff; border-radius:16px; border:1px solid #E5E7EB;
    box-shadow:0 1px 4px rgba(0,0,0,.04); overflow:hidden;
    transition:all .2s ease; display:flex; flex-direction:column;
}
.lap-card:hover { transform:translateY(-3px); box-shadow:0 8px 24px rgba(0,0,0,.09); border-color:#BFDBFE; }
.lap-card-body { padding:22px 22px 16px; flex:1; }
.lap-card-icon { width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:22px; margin-bottom:14px; }
.lap-card-title { font-size:1rem; font-weight:700; color:#111827; margin-bottom:5px; }
.lap-card-desc  { font-size:.8rem; color:#9CA3AF; line-height:1.5; }
.lap-card-footer {
    padding:14px 22px; border-top:1px solid #F3F4F6;
    background:#FAFAFA; display:flex; gap:8px; flex-wrap:wrap;
}
.lap-btn {
    display:inline-flex; align-items:center; gap:6px;
    padding:8px 14px; border-radius:8px; border:none;
    font-size:.78rem; font-weight:600; cursor:pointer;
    text-decoration:none; transition:all .15s; flex:1; justify-content:center;
}
.lap-btn:hover { transform:translateY(-1px); filter:brightness(.92); }
.lap-btn-blue   { background:#2563EB; color:#fff; }
.lap-btn-green  { background:#059669; color:#fff; }
.lap-btn-red    { background:#DC2626; color:#fff; }
.lap-btn-orange { background:#D97706; color:#fff; }
.lap-btn-gray   { background:#F3F4F6; color:#374151; border:1px solid #E5E7EB; }
.lap-btn-gray:hover { background:#E5E7EB; filter:none; }
.section-title { font-size:.72rem; font-weight:700; color:#9CA3AF; text-transform:uppercase; letter-spacing:.08em; margin:24px 0 12px; }

/* Ruangan selector */
.ruangan-selector { background:#fff; border-radius:16px; border:1px solid #E5E7EB; box-shadow:0 1px 4px rgba(0,0,0,.04); overflow:hidden; }
.ruangan-selector-body { padding:22px; }
.ruangan-select-wrap { display:flex; gap:10px; align-items:flex-end; flex-wrap:wrap; }
.ruangan-select-wrap select { flex:1; min-width:200px; height:42px; border:1.5px solid #E5E7EB; border-radius:10px; padding:0 14px; font-size:.875rem; color:#374151; background:#F9FAFB; outline:none; transition:border-color .15s; }
.ruangan-select-wrap select:focus { border-color:#3B82F6; background:#fff; }
.ruangan-list { margin-top:16px; display:flex; flex-direction:column; gap:8px; }
.ruangan-item { display:flex; align-items:center; justify-content:space-between; padding:10px 14px; border-radius:10px; border:1px solid #F3F4F6; background:#FAFAFA; transition:all .15s; }
.ruangan-item:hover { border-color:#BFDBFE; background:#EFF6FF; }
.ruangan-item-left { display:flex; align-items:center; gap:10px; }
.ruangan-item-icon { width:34px; height:34px; border-radius:8px; background:#EFF6FF; color:#2563EB; display:flex; align-items:center; justify-content:center; font-size:14px; flex-shrink:0; }
.ruangan-item-name { font-weight:600; font-size:.875rem; color:#111827; }
.ruangan-item-meta { font-size:.72rem; color:#9CA3AF; margin-top:1px; }
.ruangan-item-badge { font-size:.7rem; font-weight:700; padding:2px 8px; border-radius:6px; background:#ECFDF5; color:#059669; }
.ruangan-item-badge.empty { background:#F3F4F6; color:#9CA3AF; }

/* Filter modal date inputs */
.filter-date-row { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px; }
.filter-date-row label { font-size:.78rem; font-weight:600; color:#374151; display:block; margin-bottom:5px; }
.filter-date-row input[type=date] { width:100%; padding:9px 12px; border:1.5px solid #E2E8F0; border-radius:9px; font-size:.875rem; color:#374151; background:#F8FAFC; font-family:inherit; }
.filter-date-row input[type=date]:focus { border-color:#3B82F6; outline:none; background:#fff; }
.filter-select-row { margin-bottom:14px; }
.filter-select-row label { font-size:.78rem; font-weight:600; color:#374151; display:block; margin-bottom:5px; }
.filter-select-row select { width:100%; padding:9px 12px; border:1.5px solid #E2E8F0; border-radius:9px; font-size:.875rem; color:#374151; background:#F8FAFC; font-family:inherit; }
.filter-select-row select:focus { border-color:#3B82F6; outline:none; background:#fff; }
.filter-hint { font-size:.72rem; color:#94A3B8; margin-top:4px; }
</style>
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="dashboard-hero mb-4" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;">
        <div style="position:relative;z-index:2;">
            <span class="hero-badge"><i class="fas fa-chart-bar"></i> &nbsp;Laporan</span>
            <h2 class="hero-title" style="font-size:1.5rem;">Laporan & Export Data</h2>
            <p class="hero-subtitle">Cetak, export, dan unduh laporan aset RBTV Bengkulu</p>
        </div>
    </div>

    {{-- ── LAPORAN ASET ── --}}
    <div class="section-title">Laporan Aset</div>
    <div class="lap-grid">

        <div class="lap-card">
            <div class="lap-card-body">
                <div class="lap-card-icon" style="background:#EFF6FF;color:#2563EB;"><i class="fas fa-file-pdf"></i></div>
                <div class="lap-card-title">Laporan Aset — PDF</div>
                <div class="lap-card-desc">Cetak laporan aset dengan filter rentang tanggal, kondisi, status, dan ruangan.</div>
            </div>
            <div class="lap-card-footer">
                <button type="button" class="lap-btn lap-btn-red"
                    onclick="openModal('modalAsetPdf')">
                    <i class="fas fa-filter"></i> Filter & Cetak PDF
                </button>
            </div>
        </div>

        <div class="lap-card">
            <div class="lap-card-body">
                <div class="lap-card-icon" style="background:#ECFDF5;color:#059669;"><i class="fas fa-file-csv"></i></div>
                <div class="lap-card-title">Laporan Aset — CSV</div>
                <div class="lap-card-desc">Export data aset ke CSV dengan filter rentang tanggal dan kondisi.</div>
            </div>
            <div class="lap-card-footer">
                <button type="button" class="lap-btn lap-btn-green"
                    onclick="openModal('modalAsetCsv')">
                    <i class="fas fa-filter"></i> Filter & Export CSV
                </button>
            </div>
        </div>

        <div class="lap-card">
            <div class="lap-card-body">
                <div class="lap-card-icon" style="background:#ECFDF5;color:#059669;"><i class="fas fa-file-excel"></i></div>
                <div class="lap-card-title">Export Aset — Excel</div>
                <div class="lap-card-desc">Download data aset ke format Excel dengan styling lengkap.</div>
            </div>
            <div class="lap-card-footer">
                <button type="button" class="lap-btn lap-btn-green"
                    onclick="openModal('modalAsetExcel')">
                    <i class="fas fa-filter"></i> Filter & Download Excel
                </button>
            </div>
        </div>

    </div>

    {{-- ── LAPORAN MASTER BARANG ── --}}
    <div class="section-title">Laporan Master Barang</div>
    <div class="lap-grid">

        <div class="lap-card">
            <div class="lap-card-body">
                <div class="lap-card-icon" style="background:#FEF3C7;color:#D97706;"><i class="fas fa-cubes"></i></div>
                <div class="lap-card-title">Export Master Barang</div>
                <div class="lap-card-desc">Download data master barang ke format Excel atau PDF dengan filter tanggal.</div>
            </div>
            <div class="lap-card-footer">
                <button type="button" class="lap-btn lap-btn-green"
                    onclick="openModal('modalBarangExcel')">
                    <i class="fas fa-filter"></i> Excel
                </button>
                <button type="button" class="lap-btn lap-btn-red"
                    onclick="openModal('modalBarangPdf')">
                    <i class="fas fa-filter"></i> PDF
                </button>
            </div>
        </div>

    </div>

    {{-- ── LAPORAN PER RUANGAN ── --}}
    <div class="section-title">Laporan Per Ruangan</div>

    <div class="ruangan-selector">
        <div class="ruangan-selector-body">
            <div style="display:flex;align-items:flex-start;gap:14px;margin-bottom:18px;">
                <div class="lap-card-icon" style="background:#EFF6FF;color:#2563EB;flex-shrink:0;margin-bottom:0;">
                    <i class="fas fa-building"></i>
                </div>
                <div>
                    <div style="font-size:1rem;font-weight:700;color:#111827;margin-bottom:4px;">Cetak PDF Per Ruangan</div>
                    <div style="font-size:.8rem;color:#9CA3AF;">Pilih ruangan untuk mengunduh laporan aset khusus ruangan tersebut.</div>
                </div>
            </div>

            <div class="ruangan-select-wrap">
                <select id="ruanganSelect" onchange="updatePdfBtn()">
                    <option value="">— Pilih Ruangan —</option>
                    @foreach($ruangans as $r)
                    <option value="{{ $r->kode_ruangan }}"
                            data-count="{{ $r->assets_count }}"
                            {{ $r->assets_count == 0 ? 'disabled' : '' }}>
                        {{ $r->nama_ruangan }}
                        @if($r->lantai) — {{ $r->lantai }}@endif
                        ({{ $r->assets_count }} aset)
                    </option>
                    @endforeach
                </select>
                <a id="pdfBtn" href="#" class="lap-btn lap-btn-red"
                   style="pointer-events:none;opacity:.45;flex:0 0 auto;height:42px;padding:0 20px;"
                   target="_blank">
                    <i class="fas fa-file-pdf"></i> Cetak PDF
                </a>
            </div>

            @if($ruangans->count() > 0)
            <div class="ruangan-list">
                @foreach($ruangans as $r)
                <div class="ruangan-item">
                    <div class="ruangan-item-left">
                        <div class="ruangan-item-icon"><i class="fas fa-door-open"></i></div>
                        <div>
                            <div class="ruangan-item-name">{{ $r->nama_ruangan }}</div>
                            <div class="ruangan-item-meta">
                                @if($r->lantai)<span style="margin-right:6px;"><i class="fas fa-layer-group" style="font-size:.6rem;"></i> {{ $r->lantai }}</span>@endif
                                <span style="font-family:monospace;font-size:.7rem;color:#9CA3AF;">{{ $r->kode_ruangan }}</span>
                            </div>
                        </div>
                    </div>
                    <div style="display:flex;align-items:center;gap:10px;">
                        <span class="ruangan-item-badge {{ $r->assets_count == 0 ? 'empty' : '' }}">
                            {{ $r->assets_count }} aset
                        </span>
                        @if($r->assets_count > 0)
                        <a href="{{ route('laporan.ruangan', $r->kode_ruangan) }}"
                           class="lap-btn lap-btn-red"
                           style="flex:0 0 auto;height:32px;padding:0 12px;font-size:.72rem;"
                           target="_blank">
                            <i class="fas fa-file-pdf"></i> PDF
                        </a>
                        @else
                        <span style="font-size:.72rem;color:#D1D5DB;padding:0 12px;">Kosong</span>
                        @endif
                    </div>
                </div>
                @endforeach
            </div>
            @endif
        </div>
    </div>

    {{-- ── LAPORAN MAINTENANCE ── --}}
    <div class="section-title">Laporan Maintenance</div>
    <div class="lap-grid">
        <div class="lap-card">
            <div class="lap-card-body">
                <div class="lap-card-icon" style="background:#FEF3C7;color:#D97706;"><i class="fas fa-tools"></i></div>
                <div class="lap-card-title">Laporan Aset Maintenance</div>
                <div class="lap-card-desc">Cetak atau export daftar aset maintenance dengan filter rentang tanggal.</div>
            </div>
            <div class="lap-card-footer">
                <button type="button" class="lap-btn lap-btn-red"
                    onclick="openModal('modalMaintPdf')">
                    <i class="fas fa-filter"></i> PDF
                </button>
                <button type="button" class="lap-btn lap-btn-green"
                    onclick="openModal('modalMaintCsv')">
                    <i class="fas fa-filter"></i> CSV
                </button>
            </div>
        </div>
    </div>

    {{-- ── IMPORT DATA ── --}}
    <div class="section-title">Import Data</div>
    <div class="lap-grid">
        <div class="lap-card">
            <div class="lap-card-body">
                <div class="lap-card-icon" style="background:#EFF6FF;color:#2563EB;"><i class="fas fa-file-import"></i></div>
                <div class="lap-card-title">Import Data Massal</div>
                <div class="lap-card-desc">Upload data aset atau master barang secara massal melalui file Excel atau CSV.</div>
            </div>
            <div class="lap-card-footer">
                <a href="{{ route('aset.index') }}" class="lap-btn lap-btn-blue">
                    <i class="fas fa-boxes"></i> Import Aset
                </a>
                <a href="{{ route('barang.index') }}" class="lap-btn lap-btn-orange">
                    <i class="fas fa-cubes"></i> Import Barang
                </a>
            </div>
        </div>
    </div>

</div>

{{-- ════════════════════════════════════════
     MODALS FILTER
════════════════════════════════════════ --}}

{{-- Modal: Aset PDF --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalAsetPdf',
    'title'    => 'Filter Laporan Aset — PDF',
    'action'   => route('laporan.aset.cetak'),
    'method'   => 'GET',
    'btnLabel' => 'Cetak PDF',
    'btnClass' => 'btn-danger',
    'showRuangan' => true,
    'showKondisi' => true,
    'showStatus'  => true,
])

{{-- Modal: Aset CSV --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalAsetCsv',
    'title'    => 'Filter Laporan Aset — CSV',
    'action'   => route('laporan.aset.export'),
    'method'   => 'GET',
    'btnLabel' => 'Export CSV',
    'btnClass' => 'btn-success',
    'showRuangan' => true,
    'showKondisi' => true,
    'showStatus'  => true,
])

{{-- Modal: Aset Excel --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalAsetExcel',
    'title'    => 'Filter Export Aset — Excel',
    'action'   => route('export.aset.excel'),
    'method'   => 'GET',
    'btnLabel' => 'Download Excel',
    'btnClass' => 'btn-success',
    'showRuangan' => true,
    'showKondisi' => true,
    'showStatus'  => true,
])

{{-- Modal: Barang Excel --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalBarangExcel',
    'title'    => 'Filter Export Barang — Excel',
    'action'   => route('export.barang.excel'),
    'method'   => 'GET',
    'btnLabel' => 'Download Excel',
    'btnClass' => 'btn-success',
    'showRuangan' => false,
    'showKondisi' => false,
    'showStatus'  => false,
])

{{-- Modal: Barang PDF --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalBarangPdf',
    'title'    => 'Filter Export Barang — PDF',
    'action'   => route('export.barang.pdf'),
    'method'   => 'GET',
    'btnLabel' => 'Cetak PDF',
    'btnClass' => 'btn-danger',
    'showRuangan' => false,
    'showKondisi' => false,
    'showStatus'  => false,
])

{{-- Modal: Maintenance PDF --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalMaintPdf',
    'title'    => 'Filter Laporan Maintenance — PDF',
    'action'   => route('laporan.maintenance.pdf'),
    'method'   => 'GET',
    'btnLabel' => 'Cetak PDF',
    'btnClass' => 'btn-danger',
    'showRuangan' => false,
    'showKondisi' => true,
    'showStatus'  => false,
])

{{-- Modal: Maintenance CSV --}}
@include('laporan.partials.modal-filter', [
    'id'       => 'modalMaintCsv',
    'title'    => 'Filter Laporan Maintenance — CSV',
    'action'   => route('laporan.maintenance.csv'),
    'method'   => 'GET',
    'btnLabel' => 'Export CSV',
    'btnClass' => 'btn-success',
    'showRuangan' => false,
    'showKondisi' => true,
    'showStatus'  => false,
])

@push('scripts')
<script>
const baseUrl = '{{ url("/laporan/ruangan") }}/';

function updatePdfBtn() {
    const sel = document.getElementById('ruanganSelect');
    const btn = document.getElementById('pdfBtn');
    const val = sel.value;
    if (val) {
        btn.href = baseUrl + encodeURIComponent(val);
        btn.style.pointerEvents = 'auto';
        btn.style.opacity = '1';
    } else {
        btn.href = '#';
        btn.style.pointerEvents = 'none';
        btn.style.opacity = '.45';
    }
}

function openModal(id) {
    const el = document.getElementById(id);
    if (el) {
        const modal = new bootstrap.Modal(el);
        modal.show();
    }
}
</script>
@endpush
@endsection
