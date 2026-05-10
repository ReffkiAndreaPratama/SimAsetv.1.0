@extends('layouts.app')
@section('title', 'Master Barang')
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-cubes"></i> Master Data</div>
            <h1 class="page-hero-title">Master Barang</h1>
            <p class="page-hero-sub">Kelola katalog jenis barang kantor RBTV Bengkulu</p>
        </div>
        <div class="page-hero-right">
            <a href="{{ route('export.barang.excel') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-file-excel text-success"></i> Export Excel
            </a>
            <a href="{{ route('export.barang.pdf') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-file-pdf text-danger"></i> Export PDF
            </a>
            <button type="button" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;"
                data-bs-toggle="modal" data-bs-target="#modalImportBarang">
                <i class="fas fa-file-import" style="color:#7C3AED;"></i> Import
            </button>
            <a href="{{ route('barang.create') }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-plus"></i> Tambah Barang
            </a>
        </div>
    </div>

    {{-- Stats --}}
    @php
        $totalAll      = \App\Models\Barang::count();
    @endphp
    <div class="stats-grid" style="grid-template-columns:repeat(1,1fr);">
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(59,130,246,.1);color:#3B82F6;"><i class="fas fa-cubes"></i></div>
            <div>
                <div class="stat-label">Total Jenis Barang</div>
                <div class="stat-val">{{ number_format($totalAll) }}</div>
                <div class="stat-sub">Semua barang terdaftar</div>
            </div>
        </div>
    </div>

    {{-- Filter --}}
    <div class="filter-bar">
        <form action="{{ route('barang.index') }}" method="GET">
            <div class="filter-group wide">
                <label class="filter-label">Pencarian</label>
                <input type="text" name="search" class="filter-input" placeholder="Kode atau nama barang..." value="{{ request('search') }}">
            </div>
            <div class="filter-group">
                <label class="filter-label">Kategori</label>
                <select name="kategori" class="filter-select">
                    <option value="">Semua Kategori</option>
                    @foreach(['Kamera','Audio','Komputer','Lighting','Furniture','Peralatan Kantor','Lainnya'] as $kat)
                    <option value="{{ $kat }}" {{ request('kategori') == $kat ? 'selected' : '' }}>{{ $kat }}</option>
                    @endforeach
                </select>
            </div>
            
            <div class="filter-actions">
                <button type="submit" class="btn btn-primary d-flex align-items-center gap-1" style="height:38px;font-size:.85rem;padding:0 16px;">
                    <i class="fas fa-search"></i> Cari
                </button>
                <a href="{{ route('barang.index') }}" class="btn btn-light border" style="height:38px;" title="Reset">
                    <i class="fas fa-undo-alt"></i>
                </a>
            </div>
        </form>
    </div>

    {{-- Table --}}
    <div class="table-card">
        <div class="table-card-header">
            <h2 class="table-card-title"><i class="fas fa-list"></i> Daftar Master Barang</h2>
            <span class="table-card-meta">
                {{ $barangs->total() }} data
                @if(request()->hasAny(['search','kategori']))
                &nbsp;·&nbsp;
                <a href="{{ route('barang.index') }}" style="color:#DC2626;font-size:.75rem;">
                    <i class="fas fa-times"></i> Hapus Filter
                </a>
                @endif
            </span>
        </div>

        {{-- Bulk action bar --}}
        <div class="bulk-bar" id="bulkBar">
            <span class="bulk-bar-info"><span id="bulkCount">0</span> barang dipilih</span>
            <div class="bulk-bar-actions">
                <button type="button" class="bulk-btn bulk-btn-danger" onclick="bulkDelete()">
                    <i class="fas fa-trash-alt"></i> Hapus Terpilih
                </button>
            </div>
        </div>

        <div style="overflow-x:auto;">
            <form id="bulkForm" method="POST" action="#" onsubmit="return false;">
                @csrf
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width:40px;padding-left:16px;text-align:center;">
                                <input type="checkbox" class="bulk-checkbox" id="checkAll" title="Pilih semua">
                            </th>
                            <th style="width:110px;">Kode</th>
                            <th>Nama Barang</th>
                            <th style="width:130px;">Kategori</th>
                            <th style="width:80px;text-align:center;">Jumlah</th>
                            <th>Keterangan</th>
                            <th style="width:80px;text-align:center;">Aset</th>
                            
                            <th style="width:100px;text-align:right;padding-right:20px;">Aksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        @forelse($barangs as $b)
                        <tr>
                            <td style="padding-left:16px;text-align:center;">
                                <input type="checkbox" class="bulk-checkbox row-check" name="kodes[]" value="{{ $b->kode_barang }}" data-name="{{ $b->nama_barang }}">
                            </td>
                            <td><span class="kode-chip">{{ $b->kode_barang }}</span></td>
                            <td><div style="font-weight:600;color:#111827;">{{ $b->nama_barang }}</div></td>
                            <td>
                                @if($b->kategori)
                                    <span class="cat-chip"><i class="fas fa-tag" style="font-size:.6rem;"></i> {{ $b->kategori }}</span>
                                @else
                                    <span style="color:#D1D5DB;">—</span>
                                @endif
                            </td>
                            <td style="text-align:center;font-weight:700;color:#374151;">
                                {{ $b->jumlah ?? 0 }}
                            </td>
                            <td>
                                @if($b->keterangan)
                                    <span style="font-size:.8rem;color:#6B7280;" title="{{ $b->keterangan }}">
                                        {{ Str::limit($b->keterangan, 50) }}
                                    </span>
                                @else
                                    <span style="color:#D1D5DB;">—</span>
                                @endif
                            </td>
                            <td style="text-align:center;">
                                @php $jmlAset = $b->aset()->count(); @endphp
                                <span style="font-weight:700;color:{{ $jmlAset > 0 ? '#059669' : '#9CA3AF' }};font-size:.9rem;">{{ $jmlAset }}</span>
                                <span style="font-size:.7rem;color:#9CA3AF;"> unit</span>
                            </td>
                            
                            <td style="padding-right:20px;">
                                <div class="act-group">
                                    <a href="{{ route('barang.show', $b->kode_barang) }}" class="act-btn act-view" title="Detail"><i class="fas fa-eye"></i></a>
                                    <a href="{{ route('barang.edit', $b->kode_barang) }}" class="act-btn act-edit" title="Edit"><i class="fas fa-pencil-alt"></i></a>
                                    <button type="button" class="act-btn act-del" title="Hapus"
                                        onclick="singleDeleteBarang('{{ route('barang.destroy', $b->kode_barang) }}', '{{ addslashes($b->nama_barang) }}')">
                                        <i class="fas fa-trash-alt"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                        @empty
                        <tr>
                            <td colspan="8">
                                <div class="empty-state">
                                    <i class="fas fa-box-open empty-icon"></i>
                                    <h4>{{ request()->hasAny(['search','kategori']) ? 'Tidak Ada Hasil' : 'Belum Ada Data Barang' }}</h4>
                                    <p>{{ request()->hasAny(['search','kategori']) ? 'Tidak ada barang yang cocok dengan filter.' : 'Mulai dengan menambahkan barang pertama.' }}</p>
                                    @if(request()->hasAny(['search','kategori']))
                                        <a href="{{ route('barang.index') }}" class="btn btn-light border btn-sm"><i class="fas fa-undo-alt me-1"></i> Reset Filter</a>
                                    @else
                                        <a href="{{ route('barang.create') }}" class="btn btn-primary btn-sm"><i class="fas fa-plus me-1"></i> Tambah Barang</a>
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
                @if($barangs->total() > 0)
                    Menampilkan <strong>{{ $barangs->firstItem() }}</strong>–<strong>{{ $barangs->lastItem() }}</strong>
                    dari <strong>{{ number_format($barangs->total()) }}</strong> data
                @else
                    Menampilkan 0 data
                @endif
            </span>
            @if($barangs->hasPages())
                {{ $barangs->withQueryString()->links() }}
            @endif
        </div>
    </div>

</div>

{{-- Modal Import Barang --}}
<div class="modal fade" id="modalImportBarang" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title"><i class="fas fa-file-import me-2" style="color:#7C3AED;"></i>Import Barang</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form action="{{ route('import.store') }}" method="POST" enctype="multipart/form-data">
                @csrf
                <input type="hidden" name="type" value="barang">
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label fw-semibold">File Excel / CSV</label>
                        <input type="file" name="file" class="form-control" accept=".xlsx,.xls,.csv" required>
                        <div class="form-text">Format: .xlsx, .xls, atau .csv</div>
                    </div>
                    <div class="alert alert-info py-2 px-3" style="font-size:.82rem;">
                        <i class="fas fa-info-circle me-1"></i>
                        Belum punya template?
                        <a href="{{ route('import.template') }}?type=barang" class="fw-semibold">Download template barang</a>
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

{{-- Hidden form untuk single & bulk delete barang --}}
<form id="singleDeleteBarangForm" method="POST" style="display:none;">
    @csrf
    @method('DELETE')
</form>

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

function singleDeleteBarang(actionUrl, namaBarang) {
    deleteConfirm(namaBarang, 'Barang ini akan dihapus permanen.').then(ok => {
        if (ok) {
            const form = document.getElementById('singleDeleteBarangForm');
            form.action = actionUrl;
            form.submit();
        }
    });
}

function bulkDelete() {
    const checked = document.querySelectorAll('.row-check:checked');
    if (checked.length === 0) return;
    const names = Array.from(checked).map(cb => cb.dataset.name || cb.value).slice(0,3).join(', ');
    deleteConfirm(
        checked.length + ' barang terpilih',
        (checked.length > 3 ? names + '...' : names)
    ).then(ok => {
        if (!ok) return;
        const token = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '{{ csrf_token() }}';
        const items = Array.from(checked);
        let idx = 0;
        function deleteNext() {
            if (idx >= items.length) { window.location.reload(); return; }
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/barang/' + items[idx].value;
            form.innerHTML = '<input type="hidden" name="_token" value="' + token + '">'
                           + '<input type="hidden" name="_method" value="DELETE">';
            document.body.appendChild(form);
            idx++;
            form.submit();
        }
        deleteNext();
    });
}
</script>
@endpush
@endsection
