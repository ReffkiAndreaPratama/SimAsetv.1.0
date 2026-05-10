@extends('layouts.app')
@section('title', 'Kelola Aset')
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-boxes"></i> Manajemen Aset</div>
            <h1 class="page-hero-title">Kelola Aset</h1>
            <p class="page-hero-sub">Pantau kondisi, lokasi, dan status seluruh aset kantor RBTV Bengkulu</p>
        </div>
        <div class="page-hero-right">
            <a href="{{ route('export.aset.excel') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-file-excel text-success"></i> Export Excel
            </a>
            <a href="{{ route('export.aset.pdf') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-file-pdf text-danger"></i> Export PDF
            </a>
            <button type="button" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;"
                data-bs-toggle="modal" data-bs-target="#modalImportAset">
                <i class="fas fa-file-import" style="color:#7C3AED;"></i> Import
            </button>
            <a href="{{ route('aset.create') }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-plus"></i> Tambah Aset
            </a>
        </div>
    </div>

    {{-- Stats --}}
    <div class="stats-grid" style="grid-template-columns:repeat(4,1fr);">
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(59,130,246,.1);color:#3B82F6;"><i class="fas fa-boxes"></i></div>
            <div>
                <div class="stat-label">Total Aset</div>
                <div class="stat-val">{{ number_format($stats['total']) }}</div>
                <div class="stat-sub">Semua aset terdaftar</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(16,185,129,.1);color:#10B981;"><i class="fas fa-check-circle"></i></div>
            <div>
                <div class="stat-label">Aktif</div>
                <div class="stat-val" style="color:#059669;">{{ number_format($stats['aktif']) }}</div>
                <div class="stat-sub">Kondisi baik</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(6,182,212,.1);color:#0E7490;"><i class="fas fa-tools"></i></div>
            <div>
                <div class="stat-label">Maintenance</div>
                <div class="stat-val" style="color:#0E7490;">{{ number_format($stats['maintenance']) }}</div>
                <div class="stat-sub">Sedang diperbaiki</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(107,114,128,.1);color:#6B7280;"><i class="fas fa-ban"></i></div>
            <div>
                <div class="stat-label">Non-Aktif</div>
                <div class="stat-val" style="color:#6B7280;">{{ number_format($stats['non_aktif']) }}</div>
                <div class="stat-sub">Tidak aktif</div>
            </div>
        </div>
    </div>

    {{-- Filter --}}
    <div class="filter-bar">
        <form method="GET" action="{{ route('aset.index') }}">
            <div class="filter-group wide">
                <label class="filter-label">Pencarian</label>
                <input type="text" name="search" class="filter-input"
                    placeholder="Kode aset, nama barang, serial number..."
                    value="{{ request('search') }}">
            </div>
            <div class="filter-group">
                <label class="filter-label">Status</label>
                <select name="status" class="filter-select">
                    <option value="">Semua Status</option>
                    @foreach(['Aktif','Maintenance','Non-Aktif'] as $s)
                    <option value="{{ $s }}" {{ request('status') == $s ? 'selected' : '' }}>{{ $s }}</option>
                    @endforeach
                </select>
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
            <div class="filter-group">
                <label class="filter-label">Kategori</label>
                <select name="kategori" class="filter-select">
                    <option value="">Semua Kategori</option>
                    @foreach($kategoriList as $kat)
                    <option value="{{ $kat }}" {{ request('kategori') == $kat ? 'selected' : '' }}>{{ $kat }}</option>
                    @endforeach
                </select>
            </div>
            <div class="filter-actions">
                <button type="submit" class="btn btn-primary d-flex align-items-center gap-1" style="height:38px;font-size:.85rem;padding:0 16px;">
                    <i class="fas fa-search"></i> Cari
                </button>
                <a href="{{ route('aset.index') }}" class="btn btn-light border" style="height:38px;" title="Reset">
                    <i class="fas fa-undo-alt"></i>
                </a>
            </div>
        </form>
    </div>

    {{-- Table --}}
    <div class="table-card">
        <div class="table-card-header">
            <h2 class="table-card-title"><i class="fas fa-list"></i> Daftar Aset</h2>
            <span class="table-card-meta">
                {{ $assets->total() }} data
                @if(request()->hasAny(['search','status','kondisi','kategori']))
                &nbsp;·&nbsp;
                <a href="{{ route('aset.index') }}" style="color:#DC2626;font-size:.75rem;">
                    <i class="fas fa-times"></i> Hapus Filter
                </a>
                @endif
            </span>
        </div>

        {{-- Bulk action bar --}}
        <div class="bulk-bar" id="bulkBar">
            <span class="bulk-bar-info"><span id="bulkCount">0</span> aset dipilih</span>
            <div class="bulk-bar-actions">
                <a href="#" class="bulk-btn bulk-btn-qr" onclick="bulkQr(event)">
                    <i class="fas fa-qrcode"></i> Cetak QR
                </a>
                <button type="button" class="bulk-btn bulk-btn-danger" onclick="bulkDelete()">
                    <i class="fas fa-trash-alt"></i> Hapus Terpilih
                </button>
            </div>
        </div>

        <div style="overflow-x:auto;">
            <form id="bulkForm" method="POST" action="{{ route('aset.batch-destroy') }}">
                @csrf
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width:40px;padding-left:16px;text-align:center;">
                                <input type="checkbox" class="bulk-checkbox" id="checkAll" title="Pilih semua">
                            </th>
                            <th style="width:44px;">Foto</th>
                            <th style="width:110px;">Kode Aset</th>
                            <th>Nama Barang</th>
                            <th style="width:110px;">Kategori</th>
                            <th style="width:130px;">Ruangan</th>
                            <th style="width:90px;">Keterangan</th>
                            
                            <th style="width:110px;text-align:center;">Kondisi</th>
                            <th style="width:95px;text-align:center;">Status</th>
                            <th style="width:110px;text-align:right;padding-right:20px;">Aksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        @forelse($assets as $a)
                        <tr>
                            <td style="padding-left:16px;text-align:center;">
                                <input type="checkbox" class="bulk-checkbox row-check" name="kodes[]" value="{{ $a->kode_aset }}">
                            </td>
                            <td>
                                @if($a->foto && file_exists(public_path('foto_aset/'.$a->foto)))
                                    <img src="{{ asset('foto_aset/'.$a->foto) }}"
                                         style="width:36px;height:36px;border-radius:8px;object-fit:cover;border:1px solid #E5E7EB;display:block;" alt="">
                                @else
                                    <div style="width:36px;height:36px;border-radius:8px;background:#F3F4F6;border:1px solid #E5E7EB;display:flex;align-items:center;justify-content:center;color:#D1D5DB;font-size:14px;">
                                        <i class="fas fa-image"></i>
                                    </div>
                                @endif
                            </td>
                            <td><span class="kode-chip">{{ $a->kode_aset }}</span></td>
                            <td>
                                <div style="font-weight:600;color:#111827;">
                                    <a href="{{ route('aset.show', $a->kode_aset) }}"
                                       style="color:#111827;text-decoration:none;"
                                       onmouseover="this.style.color='#2563EB'"
                                       onmouseout="this.style.color='#111827'">
                                        {{ $a->barang?->nama_barang ?? '—' }}
                                    </a>
                                </div>
                                @if($a->serial_number)
                                <div style="font-size:.7rem;color:#9CA3AF;margin-top:2px;">
                                    <i class="fas fa-hashtag" style="font-size:.6rem;"></i> {{ $a->serial_number }}
                                </div>
                                @endif
                            </td>
                            <td>
                                @if($a->barang?->kategori)
                                    <span class="cat-chip"><i class="fas fa-tag" style="font-size:.6rem;"></i> {{ $a->barang->kategori }}</span>
                                @else
                                    <span style="color:#D1D5DB;">—</span>
                                @endif
                            </td>
                            <td>
                                <span style="font-size:.82rem;color:#6B7280;">
                                    <i class="fas fa-map-marker-alt" style="color:#93C5FD;font-size:.65rem;margin-right:3px;"></i>
                                    {{ $a->ruangan?->nama_ruangan ?? '—' }}
                                </span>
                            </td>
                            <td style="font-size:.8rem;color:#6B7280;">
                                {{ $a->keterangan ? \Illuminate\Support\Str::limit($a->keterangan, 30) : '—' }}
                            </td>
                            
                            <td style="text-align:center;">
                                @switch($a->kondisi)
                                    @case('Baik')         <span class="status-pill pill-baik"><span class="pill-dot"></span> Baik</span> @break
                                    @case('Rusak Ringan') <span class="status-pill pill-rusak-r"><span class="pill-dot"></span> Rusak Ringan</span> @break
                                    @case('Rusak Berat')  <span class="status-pill pill-rusak-b"><span class="pill-dot"></span> Rusak Berat</span> @break
                                    @default <span style="color:#D1D5DB;">—</span>
                                @endswitch
                            </td>
                            <td style="text-align:center;">
                                @switch($a->status)
                                    @case('Aktif')       <span class="status-pill pill-aktif"><span class="pill-dot"></span> Aktif</span> @break
                                    @case('Maintenance') <span class="status-pill pill-maintenance"><span class="pill-dot"></span> Maintenance</span> @break
                                    @default             <span class="status-pill pill-nonaktif"><span class="pill-dot"></span> Non-Aktif</span>
                                @endswitch
                            </td>
                            <td style="padding-right:20px;">
                                <div class="act-group">
                                    <a href="{{ route('aset.show', $a->kode_aset) }}" class="act-btn act-view" title="Detail"><i class="fas fa-eye"></i></a>
                                    <a href="{{ route('aset.edit', $a->kode_aset) }}" class="act-btn act-edit" title="Edit"><i class="fas fa-pencil-alt"></i></a>
                                    <a href="{{ route('aset.showQr', $a->kode_aset) }}" class="act-btn act-qr" title="QR Code" target="_blank"><i class="fas fa-qrcode"></i></a>
                                    <form action="{{ route('aset.destroy', $a->kode_aset) }}" method="POST" style="display:inline;margin:0;"
                                        data-confirm data-confirm-name="{{ $a->kode_aset }}">
                                        @csrf @method('DELETE')
                                        <button type="submit" class="act-btn act-del" title="Hapus"><i class="fas fa-trash-alt"></i></button>
                                    </form>
                                </div>
                            </td>
                        </tr>
                        @empty
                        <tr>
                            <td colspan="11">
                                <div class="empty-state">
                                    <i class="fas fa-box-open empty-icon"></i>
                                    <h4>{{ request()->hasAny(['search','status','kondisi','kategori']) ? 'Tidak Ada Hasil' : 'Belum Ada Data Aset' }}</h4>
                                    <p>{{ request()->hasAny(['search','status','kondisi','kategori']) ? 'Tidak ada aset yang cocok dengan filter.' : 'Mulai dengan menambahkan aset pertama.' }}</p>
                                    @if(request()->hasAny(['search','status','kondisi','kategori']))
                                        <a href="{{ route('aset.index') }}" class="btn btn-light border btn-sm"><i class="fas fa-undo-alt me-1"></i> Reset Filter</a>
                                    @else
                                        <a href="{{ route('aset.create') }}" class="btn btn-primary btn-sm"><i class="fas fa-plus me-1"></i> Tambah Aset</a>
                                    @endif
                                </div>
                            </td>
                        </tr>
                        @endforelse
                    </tbody>
                </table>
            </form>
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

{{-- Modal Import Aset --}}
<div class="modal fade" id="modalImportAset" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title"><i class="fas fa-file-import me-2" style="color:#7C3AED;"></i>Import Aset</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form action="{{ route('import.store') }}" method="POST" enctype="multipart/form-data">
                @csrf
                <input type="hidden" name="type" value="aset">
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label fw-semibold">File Excel / CSV</label>
                        <input type="file" name="file" class="form-control" accept=".xlsx,.xls,.csv" required>
                        <div class="form-text">Format: .xlsx, .xls, atau .csv</div>
                    </div>
                    <div class="alert alert-info py-2 px-3" style="font-size:.82rem;">
                        <i class="fas fa-info-circle me-1"></i>
                        Belum punya template?
                        <a href="{{ route('import.template') }}?type=aset" class="fw-semibold">Download template aset</a>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-light" data-bs-dismiss="modal">Batal</button>
                    <button type="submit" class="btn btn-warning" style="color:#fff;">
                        <i class="fas fa-upload me-1"></i> Import
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>

@push('scripts')
<script>
const checkAll  = document.getElementById('checkAll');
const bulkBar   = document.getElementById('bulkBar');
const bulkCount = document.getElementById('bulkCount');

function updateBulkBar() {
    const checked = document.querySelectorAll('.row-check:checked');
    const total   = document.querySelectorAll('.row-check').length;
    const n = checked.length;
    bulkCount.textContent = n;
    bulkBar.classList.toggle('show', n > 0);
    checkAll.indeterminate = n > 0 && n < total;
    checkAll.checked = total > 0 && n === total;
}

checkAll.addEventListener('change', function() {
    document.querySelectorAll('.row-check').forEach(cb => cb.checked = this.checked);
    updateBulkBar();
});
document.querySelectorAll('.row-check').forEach(cb => cb.addEventListener('change', updateBulkBar));

function bulkDelete() {
    const checked = document.querySelectorAll('.row-check:checked');
    if (checked.length === 0) return;
    deleteConfirm(
        checked.length + ' aset terpilih',
        'Semua aset yang dipilih akan dihapus permanen.'
    ).then(ok => { if (ok) document.getElementById('bulkForm').submit(); });
}

function bulkQr(e) {
    e.preventDefault();
    const checked = document.querySelectorAll('.row-check:checked');
    if (checked.length === 0) { alert('Pilih minimal 1 aset terlebih dahulu.'); return; }
    const kodes = Array.from(checked).map(cb => cb.value).join(',');
    window.open('{{ route("qrcode.batch-print") }}?asset_ids=' + encodeURIComponent(kodes), '_blank');
}
</script>
@endpush
@endsection
