@extends('layouts.app')
@section('title', 'Audit Log Aktivitas')
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-history"></i> Audit Log</div>
            <h1 class="page-hero-title">Log Aktivitas Sistem</h1>
            <p class="page-hero-sub">Rekam jejak seluruh aktivitas pengguna di sistem SimAset</p>
        </div>
        <div class="page-hero-right">
            <span style="font-size:.82rem;color:rgba(255,255,255,.7);">
                <i class="fas fa-database me-1"></i> {{ number_format($logs->total()) }} log tercatat
            </span>
        </div>
    </div>

    {{-- Filter --}}
    <div class="filter-bar">
        <form method="GET" action="{{ route('audit-log.index') }}">
            <div class="filter-group wide">
                <label class="filter-label">Pencarian</label>
                <input type="text" name="search" class="filter-input"
                    placeholder="Cari aktivitas atau keterangan..." value="{{ request('search') }}">
            </div>
            <div class="filter-group">
                <label class="filter-label">Pengguna</label>
                <select name="user_id" class="filter-select">
                    <option value="">Semua Pengguna</option>
                    @foreach($users as $u)
                    <option value="{{ $u->id_user }}" {{ request('user_id') == $u->id_user ? 'selected' : '' }}>
                        {{ $u->nama }}
                    </option>
                    @endforeach
                </select>
            </div>
            <div class="filter-group">
                <label class="filter-label">Modul</label>
                <select name="module" class="filter-select">
                    <option value="">Semua Modul</option>
                    @foreach($modules as $m)
                    <option value="{{ $m }}" {{ request('module') == $m ? 'selected' : '' }}>{{ $m }}</option>
                    @endforeach
                </select>
            </div>
            <div class="filter-actions">
                <button type="submit" class="btn btn-primary d-flex align-items-center gap-1" style="height:38px;font-size:.85rem;padding:0 16px;">
                    <i class="fas fa-search"></i> Cari
                </button>
                <a href="{{ route('audit-log.index') }}" class="btn btn-light border" style="height:38px;" title="Reset">
                    <i class="fas fa-undo-alt"></i>
                </a>
            </div>
        </form>
    </div>

    {{-- Table --}}
    <div class="table-card">
        <div class="table-card-header">
            <h2 class="table-card-title"><i class="fas fa-list-alt"></i> Daftar Log Aktivitas</h2>
            <span class="table-card-meta">
                {{ $logs->total() }} log
                @if(request()->hasAny(['search','user_id','module']))
                &nbsp;·&nbsp;
                <a href="{{ route('audit-log.index') }}" style="color:#DC2626;font-size:.75rem;">
                    <i class="fas fa-times"></i> Hapus Filter
                </a>
                @endif
            </span>
        </div>

        <div style="overflow-x:auto;">
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width:40px;padding-left:20px;">#</th>
                        <th style="width:160px;">Waktu</th>
                        <th style="width:160px;">Pengguna</th>
                        <th style="width:110px;text-align:center;">Aktivitas</th>
                        <th>Keterangan</th>
                        <th style="width:130px;">IP Address</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse($logs as $log)
                    @php
                        $badgeStyle = match(true) {
                            str_contains($log->aktivitas, 'Login')   => 'background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;',
                            str_contains($log->aktivitas, 'Logout')  => 'background:#F1F5F9;color:#475569;border:1px solid #CBD5E1;',
                            str_contains($log->aktivitas, 'Create')  => 'background:#ECFDF5;color:#059669;border:1px solid #A7F3D0;',
                            str_contains($log->aktivitas, 'Update')  => 'background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;',
                            str_contains($log->aktivitas, 'Delete')  => 'background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;',
                            default                                   => 'background:#F9FAFB;color:#6B7280;border:1px solid #E5E7EB;',
                        };
                    @endphp
                    <tr>
                        <td style="padding-left:20px;color:#9CA3AF;font-size:.75rem;">
                            {{ $loop->iteration + ($logs->currentPage()-1) * $logs->perPage() }}
                        </td>
                        <td style="font-size:.78rem;color:#6B7280;white-space:nowrap;">
                            <div>{{ $log->created_at?->format('d M Y') ?? '—' }}</div>
                            <div style="color:#9CA3AF;font-size:.72rem;">{{ $log->created_at?->format('H:i:s') ?? '' }}</div>
                        </td>
                        <td>
                            <div style="font-weight:600;font-size:.82rem;color:#111827;">
                                {{ $log->user?->nama ?? 'System' }}
                            </div>
                            <div style="font-size:.72rem;color:#9CA3AF;">
                                {{ $log->user?->role ? ucfirst($log->user->role) : '' }}
                            </div>
                        </td>
                        <td style="text-align:center;">
                            <span style="font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:8px;{{ $badgeStyle }}">
                                {{ $log->aktivitas }}
                            </span>
                        </td>
                        <td style="font-size:.82rem;color:#374151;max-width:300px;">
                            {{ $log->keterangan ?? '—' }}
                        </td>
                        <td style="font-size:.78rem;color:#6B7280;font-family:monospace;">
                            {{ $log->ip_address ?? '—' }}
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="6">
                            <div class="empty-state">
                                <i class="fas fa-history empty-icon"></i>
                                <h4>Belum Ada Log Aktivitas</h4>
                                <p>
                                    @if(request()->hasAny(['search','user_id','module']))
                                        Tidak ada log yang cocok dengan filter.
                                    @else
                                        Aktivitas sistem akan tercatat di sini.
                                    @endif
                                </p>
                                @if(request()->hasAny(['search','user_id','module']))
                                    <a href="{{ route('audit-log.index') }}" class="btn btn-light border btn-sm">
                                        <i class="fas fa-undo-alt me-1"></i> Reset Filter
                                    </a>
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
                @if($logs->total() > 0)
                    Menampilkan <strong>{{ $logs->firstItem() }}</strong>–<strong>{{ $logs->lastItem() }}</strong>
                    dari <strong>{{ number_format($logs->total()) }}</strong> log
                @else
                    Menampilkan 0 data
                @endif
            </span>
            @if($logs->hasPages())
                {{ $logs->withQueryString()->links() }}
            @endif
        </div>
    </div>

</div>
@endsection
