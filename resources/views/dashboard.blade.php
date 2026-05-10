@extends('layouts.app')

@section('title', 'Dashboard SimAset')

@section('content')

@php
    $kategoriList = $recentAssets->pluck('barang.kategori')->filter()->unique()->sort()->values();
    $maintCount   = \App\Models\Asset::where('status','Maintenance')->count();
    $recentLogs   = \App\Models\ActivityLog::with('user')->orderBy('created_at','desc')->take(6)->get();
@endphp

<style>
:root { --glass-border: #E5E7EB; --glass-shadow: 0 2px 8px rgba(0,0,0,0.04); }

/* Hero */
.hero-date-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(255,255,255,0.15); color: #FFFFFF;
    padding: 10px 18px; border-radius: 10px; font-weight: 600; font-size: 0.875rem;
    border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(8px);
}

/* Metric cards */
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 14px; margin-bottom: 18px;
}
.metric-card {
    background: #FFFFFF; border-radius: 14px; padding: 20px 22px;
    border: 1px solid var(--glass-border); box-shadow: var(--glass-shadow);
    transition: all 0.2s ease; display: flex; flex-direction: column;
    position: relative; overflow: hidden;
}
.metric-card::after {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: var(--card-color, #3B82F6); border-radius: 14px 14px 0 0;
}
.metric-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.07); }
.metric-icon-wrapper {
    width: 42px; height: 42px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center; font-size: 17px;
    background: var(--icon-bg); color: var(--icon-color); margin-bottom: 12px;
}
.metric-label { font-size: 0.75rem; color: #6B7280; font-weight: 600; margin-bottom: 2px; text-transform: uppercase; letter-spacing: 0.04em; }
.metric-value { font-size: 1.9rem; font-weight: 700; color: #111827; line-height: 1.1; margin: 0 0 5px; letter-spacing: -0.02em; }
.metric-desc  { font-size: 0.75rem; color: #9CA3AF; font-weight: 500; }

/* Alert banner */
.maint-alert {
    background: linear-gradient(135deg, #fffbeb, #fef3c7);
    border: 1px solid #fde68a; border-radius: 12px;
    padding: 14px 20px; margin-bottom: 18px;
    display: flex; align-items: center; gap: 14px;
}
.maint-alert-icon { width: 38px; height: 38px; border-radius: 9px; background: #f59e0b; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0; }
.maint-alert-text strong { font-size: 0.9rem; color: #92400e; display: block; }
.maint-alert-text span   { font-size: 0.8rem; color: #b45309; }

/* Cards */
.card { background: #FFFFFF; border: 1px solid var(--glass-border); border-radius: 14px; box-shadow: var(--glass-shadow); overflow: hidden; }
.card-header { background: #FFFFFF; border-bottom: 1px solid #F3F4F6; padding: 16px 20px; }
.card-header-inner { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
.card-header h5 { font-weight: 700; color: #111827; margin: 0 0 2px; font-size: 0.95rem; }
.card-icon { width: 34px; height: 34px; border-radius: 8px; display: flex; align-items: center; justify-content: center; background: #F3F4F6; color: #4B5563; font-size: 13px; }

/* Table */
.table { margin-bottom: 0; }
.table thead th { background: #F9FAFB; border-bottom: 1px solid #E5E7EB; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 12px 18px; font-size: 0.7rem; color: #6B7280; white-space: nowrap; }
.table td { padding: 14px 18px; vertical-align: middle; border-color: #F3F4F6; font-size: 0.875rem; color: #374151; }
.table tbody tr:hover { background: #F9FAFB; }

/* Activity log */
.activity-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 20px; border-bottom: 1px solid #F9FAFB; }
.activity-item:last-child { border-bottom: none; }
.activity-dot { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; }
.activity-dot.login   { background: #ecfdf5; color: #059669; }
.activity-dot.logout  { background: #fffbeb; color: #d97706; }
.activity-dot.create  { background: #eff6ff; color: #2563eb; }
.activity-dot.update  { background: #fef9c3; color: #ca8a04; }
.activity-dot.delete  { background: #fef2f2; color: #dc2626; }
.activity-dot.default { background: #F3F4F6; color: #6B7280; }
.activity-body { flex: 1; min-width: 0; }
.activity-title { font-size: 0.82rem; font-weight: 600; color: #111827; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.activity-meta  { font-size: 0.72rem; color: #9CA3AF; margin-top: 2px; }

/* Quick links */
.quick-links { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 16px; }
.quick-link {
    display: flex; align-items: center; gap: 10px;
    padding: 12px 14px; border-radius: 10px; border: 1px solid #E5E7EB;
    text-decoration: none; color: #374151; font-size: 0.82rem; font-weight: 600;
    transition: all 0.15s ease; background: #FAFAFA;
}
.quick-link:hover { background: #EFF6FF; border-color: #BFDBFE; color: #1d4ed8; transform: translateY(-1px); }
.quick-link i { width: 28px; height: 28px; border-radius: 7px; display: flex; align-items: center; justify-content: center; font-size: 12px; background: var(--ql-bg, #EFF6FF); color: var(--ql-color, #2563eb); flex-shrink: 0; }

.form-select-sm { height: 34px; padding: 0.2rem 1.8rem 0.2rem 0.75rem; font-size: 0.82rem; border-radius: 8px; border-color: #E2E8F0; }

@media (max-width: 768px) {
    .metrics-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .quick-links  { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
    .metrics-grid { grid-template-columns: 1fr 1fr; gap: 8px; }
    .metric-value { font-size: 1.6rem; }
}
</style>

{{-- Hero --}}
<div class="dashboard-hero mb-4" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px;">
    <div style="position:relative;z-index:2;">
        <span class="hero-badge"><i class="fas fa-tachometer-alt"></i> &nbsp;Dashboard</span>
        <h2 class="hero-title">Selamat Datang, {{ auth()->user()->nama }}! 👋</h2>
        <p class="hero-subtitle">Ringkasan aset, kondisi, dan aktivitas terbaru di RBTV Bengkulu.</p>
    </div>
    <div style="position:relative;z-index:2;">
        <div class="hero-date-badge">
            <i class="fas fa-calendar-alt"></i>
            {{ now()->locale('id')->isoFormat('dddd, D MMMM Y') }}
        </div>
    </div>
</div>

{{-- Maintenance Alert --}}
@if($maintCount > 0)
<div class="maint-alert">
    <div class="maint-alert-icon"><i class="fas fa-tools"></i></div>
    <div class="maint-alert-text">
        <strong>{{ $maintCount }} Aset Sedang Maintenance</strong>
        <span>Terdapat aset yang memerlukan perhatian. Klik untuk melihat detail.</span>
    </div>
    <a href="{{ route('maintenance.index') }}" class="btn btn-warning btn-sm ms-auto d-flex align-items-center gap-1" style="color:#fff;white-space:nowrap;font-size:12px;">
        <i class="fas fa-arrow-right"></i> Lihat
    </a>
</div>
@endif

{{-- Key Metrics --}}
<div class="metrics-grid">
    <div class="metric-card" style="--card-color:#3B82F6;--icon-bg:rgba(59,130,246,.1);--icon-color:#3B82F6;">
        <div class="metric-icon-wrapper"><i class="fas fa-boxes"></i></div>
        <div class="metric-label">Total Aset</div>
        <div class="metric-value">{{ number_format($totalAset) }}</div>
        <div class="metric-desc">{{ number_format($totalBarang) }} master barang</div>
    </div>
    <div class="metric-card" style="--card-color:#10B981;--icon-bg:rgba(16,185,129,.1);--icon-color:#10B981;">
        <div class="metric-icon-wrapper"><i class="fas fa-check-circle"></i></div>
        <div class="metric-label">Aset Aktif</div>
        <div class="metric-value">{{ number_format($asetAktif) }}</div>
        <div class="metric-desc">{{ $totalAset > 0 ? round(($asetAktif/$totalAset)*100,1) : 0 }}% dari total</div>
    </div>
    <div class="metric-card" style="--card-color:#F59E0B;--icon-bg:rgba(245,158,11,.1);--icon-color:#F59E0B;">
        <div class="metric-icon-wrapper"><i class="fas fa-tools"></i></div>
        <div class="metric-label">Maintenance</div>
        <div class="metric-value">{{ number_format($asetMaintenance) }}</div>
        <div class="metric-desc">Sedang diperbaiki</div>
    </div>
    <div class="metric-card" style="--card-color:#EF4444;--icon-bg:rgba(239,68,68,.1);--icon-color:#EF4444;">
        <div class="metric-icon-wrapper"><i class="fas fa-exclamation-triangle"></i></div>
        <div class="metric-label">Kondisi Rusak</div>
        <div class="metric-value">{{ number_format($asetRusak) }}</div>
        <div class="metric-desc">{{ $totalAset > 0 ? round(($asetRusak/$totalAset)*100,1) : 0 }}% dari total</div>
    </div>
    <div class="metric-card" style="--card-color:#8B5CF6;--icon-bg:rgba(139,92,246,.1);--icon-color:#8B5CF6;">
        <div class="metric-icon-wrapper"><i class="fas fa-ban"></i></div>
        <div class="metric-label">Non-Aktif</div>
        <div class="metric-value">{{ number_format($asetNonaktif) }}</div>
        <div class="metric-desc">{{ $totalAset > 0 ? round(($asetNonaktif/$totalAset)*100,1) : 0 }}% dari total</div>
    </div>
    <div class="metric-card" style="--card-color:#06B6D4;--icon-bg:rgba(6,182,212,.1);--icon-color:#06B6D4;">
        <div class="metric-icon-wrapper"><i class="fas fa-building"></i></div>
        <div class="metric-label">Ruangan</div>
        <div class="metric-value">{{ number_format($totalRuangan) }}</div>
        <div class="metric-desc">Lokasi terdaftar</div>
    </div>
</div>

{{-- Charts Row --}}
<div class="row g-3 mb-3">
    <div class="col-lg-5">
        <div class="card h-100">
            <div class="card-header">
                <div class="card-header-inner">
                    <div>
                        <h5>Distribusi Kondisi</h5>
                        <p class="text-muted small mb-0">Status kondisi aset saat ini</p>
                    </div>
                    <div class="card-icon"><i class="fas fa-chart-pie"></i></div>
                </div>
            </div>
            <div class="card-body d-flex align-items-center justify-content-center" style="height:300px;position:relative;">
                <canvas id="kondisiChart"></canvas>
            </div>
        </div>
    </div>
    <div class="col-lg-7">
        <div class="card h-100">
            <div class="card-header">
                <div class="card-header-inner">
                    <div>
                        <h5>Top 5 Kategori Aset</h5>
                        <p class="text-muted small mb-0">Kategori dengan jumlah aset terbanyak</p>
                    </div>
                    <div class="card-icon"><i class="fas fa-chart-bar"></i></div>
                </div>
            </div>
            <div class="card-body" style="height:300px;position:relative;">
                <canvas id="kategoriChart"></canvas>
            </div>
        </div>
    </div>
</div>

{{-- Bottom Row: Recent Assets + Activity + Quick Links --}}
<div class="row g-3">
    {{-- Recent Assets --}}
    <div class="col-lg-7">
        <div class="card">
            <div class="card-header">
                <div class="card-header-inner">
                    <div>
                        <h5>Aset Terbaru</h5>
                        <p class="text-muted small mb-0">10 aset terakhir ditambahkan</p>
                    </div>
                    <div class="d-flex gap-2 align-items-center">
                        <select id="filterKondisi" class="form-select form-select-sm" style="width:auto;min-width:130px;">
                            <option value="">Semua Kondisi</option>
                            <option value="Baik">Baik</option>
                            <option value="Rusak Ringan">Rusak Ringan</option>
                            <option value="Rusak Berat">Rusak Berat</option>
                        </select>
                        <a href="{{ route('aset.index') }}" class="btn btn-primary btn-sm rounded-pill px-3" style="font-size:12px;">
                            Lihat Semua <i class="fas fa-arrow-right ms-1"></i>
                        </a>
                    </div>
                </div>
            </div>
            <div class="card-body p-0">
                @if($recentAssets->count() > 0)
                <div style="overflow-x:auto;">
                    <table class="table table-hover align-middle mb-0">
                        <thead>
                            <tr>
                                <th class="ps-4" style="width:110px;">Kode</th>
                                <th>Barang</th>
                                <th style="width:100px;">Kondisi</th>
                                <th style="width:90px;">Status</th>
                                <th class="pe-4" style="width:120px;">Ruangan</th>
                            </tr>
                        </thead>
                        <tbody id="recentAssetsBody">
                            @foreach($recentAssets as $asset)
                            <tr data-kondisi="{{ $asset->kondisi }}">
                                <td class="ps-4">
                                    <span class="badge bg-primary bg-opacity-10 text-primary px-2 py-1 rounded-pill fw-semibold" style="font-size:11px;">
                                        {{ $asset->kode_aset }}
                                    </span>
                                </td>
                                <td>
                                    <div class="fw-semibold text-dark" style="font-size:13px;">{{ $asset->barang?->nama_barang ?? '—' }}</div>
                                    <div class="small text-muted" style="font-size:11px;">{{ $asset->barang?->kategori ?? '' }}</div>
                                </td>
                                <td>
                                    @php
                                        $k = strtolower($asset->kondisi ?? '');
                                        $kc = $k === 'baik' ? 'bg-success bg-opacity-10 text-success' : (str_contains($k,'rusak') ? 'bg-danger bg-opacity-10 text-danger' : 'bg-secondary bg-opacity-10 text-secondary');
                                    @endphp
                                    <span class="badge {{ $kc }}" style="font-size:11px;">{{ $asset->kondisi ?? '-' }}</span>
                                </td>
                                <td>
                                    @php
                                        $s = strtolower($asset->status ?? '');
                                        $sc = $s === 'aktif' ? 'bg-success bg-opacity-10 text-success' : ($s === 'maintenance' ? 'bg-warning bg-opacity-10 text-warning' : 'bg-secondary bg-opacity-10 text-secondary');
                                    @endphp
                                    <span class="badge {{ $sc }}" style="font-size:11px;">{{ $asset->status ?? '-' }}</span>
                                </td>
                                <td class="pe-4 text-muted" style="font-size:12px;">{{ $asset->ruangan?->nama_ruangan ?? '—' }}</td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
                @else
                <div class="text-center py-5">
                    <i class="fas fa-box-open fa-3x text-muted opacity-25 mb-3 d-block"></i>
                    <p class="text-muted small mb-2">Belum ada aset terdaftar</p>
                    <a href="{{ route('aset.create') }}" class="btn btn-primary btn-sm">
                        <i class="fas fa-plus me-1"></i>Tambah Aset
                    </a>
                </div>
                @endif
            </div>
        </div>
    </div>

    {{-- Right Column --}}
    <div class="col-lg-5">
        {{-- Recent Activity --}}
        <div class="card mb-3">
            <div class="card-header">
                <div class="card-header-inner">
                    <div>
                        <h5>Aktivitas Terbaru</h5>
                        <p class="text-muted small mb-0">Log aktivitas pengguna</p>
                    </div>
                    @if(auth()->user()->isAdmin())
                    <a href="{{ route('audit-log.index') }}" class="btn btn-outline-secondary btn-sm" style="font-size:11px;">
                        Lihat Semua
                    </a>
                    @endif
                </div>
            </div>
            <div class="card-body p-0">
                @forelse($recentLogs as $log)
                @php
                    $act = strtolower($log->aktivitas ?? '');
                    $dotClass = 'default';
                    if (str_contains($act,'login'))                                     $dotClass = 'login';
                    elseif (str_contains($act,'logout'))                                $dotClass = 'logout';
                    elseif (str_contains($act,'create') || str_contains($act,'tambah')) $dotClass = 'create';
                    elseif (str_contains($act,'update') || str_contains($act,'edit'))   $dotClass = 'update';
                    elseif (str_contains($act,'delete') || str_contains($act,'hapus'))  $dotClass = 'delete';
                    $icons = ['login'=>'fa-sign-in-alt','logout'=>'fa-sign-out-alt','create'=>'fa-plus','update'=>'fa-pencil-alt','delete'=>'fa-trash-alt','default'=>'fa-circle'];
                @endphp
                <div class="activity-item">
                    <div class="activity-dot {{ $dotClass }}">
                        <i class="fas {{ $icons[$dotClass] ?? 'fa-circle' }}" style="font-size:11px;"></i>
                    </div>
                    <div class="activity-body">
                        <div class="activity-title">{{ Str::limit($log->keterangan ?? $log->aktivitas, 55) }}</div>
                        <div class="activity-meta">
                            <span>{{ $log->user?->nama ?? 'System' }}</span>
                            &nbsp;·&nbsp;
                            <span>{{ $log->created_at->diffForHumans() }}</span>
                        </div>
                    </div>
                </div>
                @empty
                <div class="text-center py-4">
                    <i class="fas fa-clipboard-list fa-2x text-muted opacity-25 mb-2 d-block"></i>
                    <p class="text-muted small mb-0">Belum ada aktivitas tercatat</p>
                </div>
                @endforelse
            </div>
        </div>

        {{-- Quick Links --}}
        <div class="card">
            <div class="card-header">
                <div class="card-header-inner">
                    <h5>Akses Cepat</h5>
                    <div class="card-icon"><i class="fas fa-bolt"></i></div>
                </div>
            </div>
            <div class="quick-links">
                <a href="{{ route('aset.create') }}" class="quick-link" style="--ql-bg:rgba(59,130,246,.1);--ql-color:#2563eb;">
                    <i class="fas fa-plus-circle"></i> Tambah Aset
                </a>
                <a href="{{ route('qrcode.scanner') }}" class="quick-link" style="--ql-bg:rgba(6,182,212,.1);--ql-color:#0e7490;">
                    <i class="fas fa-qrcode"></i> QR Scanner
                </a>
                <a href="{{ route('export.aset.excel') }}" class="quick-link" style="--ql-bg:rgba(16,185,129,.1);--ql-color:#059669;">
                    <i class="fas fa-file-excel"></i> Export Excel
                </a>
                <a href="{{ route('export.aset.pdf') }}" class="quick-link" style="--ql-bg:rgba(239,68,68,.1);--ql-color:#dc2626;">
                    <i class="fas fa-file-pdf"></i> Export PDF
                </a>
                <a href="{{ route('aset.index') }}" class="quick-link" style="--ql-bg:rgba(139,92,246,.1);--ql-color:#7c3aed;">
                    <i class="fas fa-file-import"></i> Import Data
                </a>
                <a href="{{ route('maintenance.index') }}" class="quick-link" style="--ql-bg:rgba(245,158,11,.1);--ql-color:#d97706;">
                    <i class="fas fa-tools"></i> Maintenance
                    @if($maintCount > 0)
                        <span class="ms-auto badge bg-warning text-dark" style="font-size:10px;">{{ $maintCount }}</span>
                    @endif
                </a>
            </div>
        </div>
    </div>
</div>

{{-- Data chart di-pass via hidden element agar di-escape Blade (aman dari XSS) --}}
<div id="chartData"
    data-kondisi-labels="{{ e(json_encode($kondisiDistribusi->pluck('kondisi')->toArray())) }}"
    data-kondisi-values="{{ e(json_encode($kondisiDistribusi->pluck('total')->toArray())) }}"
    data-kategori-labels="{{ e(json_encode($kategoriDistribusi->pluck('kategori')->toArray())) }}"
    data-kategori-values="{{ e(json_encode($kategoriDistribusi->pluck('total')->toArray())) }}"
    style="display:none;">
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    const cd = document.getElementById('chartData');
    const kondisiLabels = JSON.parse(cd.dataset.kondisiLabels);
    const kondisiValues = JSON.parse(cd.dataset.kondisiValues);
    const kategoriLabels = JSON.parse(cd.dataset.kategoriLabels);
    const kategoriValues = JSON.parse(cd.dataset.kategoriValues);

    // Kondisi Chart
    const ctxK = document.getElementById('kondisiChart').getContext('2d');
    new Chart(ctxK, {
        type: 'doughnut',
        data: {
            labels: kondisiLabels,
            datasets: [{
                data: kondisiValues,
                backgroundColor: ['#10B981','#F59E0B','#EF4444','#94A3B8','#6366F1'],
                borderWidth: 0, hoverOffset: 6
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false, cutout: '68%',
            plugins: {
                legend: { position: 'bottom', labels: { usePointStyle: true, padding: 18, boxWidth: 9, font: { size: 11, weight: '500' }, color: '#475569' } },
                tooltip: { backgroundColor: 'rgba(15,23,42,.9)', padding: 10, cornerRadius: 8 }
            },
            animation: { animateRotate: true, duration: 900 }
        }
    });

    // Kategori Chart
    const ctxKat = document.getElementById('kategoriChart').getContext('2d');
    new Chart(ctxKat, {
        type: 'bar',
        data: {
            labels: kategoriLabels,
            datasets: [{
                data: kategoriValues,
                backgroundColor: ['rgba(59,130,246,.75)','rgba(16,185,129,.75)','rgba(245,158,11,.75)','rgba(239,68,68,.75)','rgba(139,92,246,.75)'],
                borderRadius: 8, maxBarThickness: 48,
                hoverBackgroundColor: ['rgba(59,130,246,1)','rgba(16,185,129,1)','rgba(245,158,11,1)','rgba(239,68,68,1)','rgba(139,92,246,1)']
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: { backgroundColor: 'rgba(15,23,42,.9)', padding: 10, cornerRadius: 8 }
            },
            scales: {
                y: { beginAtZero: true, grid: { color: '#F1F5F9' }, ticks: { color: '#94A3B8', font: { size: 11 } } },
                x: { grid: { display: false }, ticks: { color: '#94A3B8', font: { size: 11 } } }
            },
            animation: { duration: 900, easing: 'easeOutQuart' }
        }
    });

    // Filter kondisi tabel
    document.getElementById('filterKondisi').addEventListener('change', function() {
        const val = this.value;
        document.querySelectorAll('#recentAssetsBody tr').forEach(row => {
            row.style.display = (!val || row.dataset.kondisi === val) ? '' : 'none';
        });
    });
});
</script>

@endsection


