@extends('layouts.app')
@section('title', 'Kelola Pengguna')
@push('styles')
@include('components.page-styles')
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-users-cog"></i> Pengguna</div>
            <h1 class="page-hero-title">Kelola Pengguna</h1>
            <p class="page-hero-sub">Atur hak akses admin dan staff sistem RBTV Bengkulu</p>
        </div>
        <div class="page-hero-right">
            <a href="{{ route('users.create') }}" class="btn btn-warning d-flex align-items-center gap-2" style="color:#fff;font-size:.85rem;">
                <i class="fas fa-user-plus"></i> Tambah Pengguna
            </a>
        </div>
    </div>

    {{-- Stats --}}
    @php
        $totalUsers  = $users->count();
        $totalAdmins = $users->where('role','admin')->count();
        $totalStaffs = $users->where('role','staff')->count();
    @endphp
    <div class="stats-grid" style="grid-template-columns:repeat(3,1fr);">
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(59,130,246,.1);color:#3B82F6;"><i class="fas fa-users"></i></div>
            <div>
                <div class="stat-label">Total Pengguna</div>
                <div class="stat-val">{{ $totalUsers }}</div>
                <div class="stat-sub">Semua akun aktif</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(220,38,38,.1);color:#DC2626;"><i class="fas fa-user-shield"></i></div>
            <div>
                <div class="stat-label">Admin</div>
                <div class="stat-val" style="color:#DC2626;">{{ $totalAdmins }}</div>
                <div class="stat-sub">Akses penuh</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="background:rgba(59,130,246,.1);color:#2563EB;"><i class="fas fa-user-tie"></i></div>
            <div>
                <div class="stat-label">Staff</div>
                <div class="stat-val" style="color:#2563EB;">{{ $totalStaffs }}</div>
                <div class="stat-sub">Akses terbatas</div>
            </div>
        </div>
    </div>

    {{-- Table --}}
    <div class="table-card">
        <div class="table-card-header">
            <h2 class="table-card-title"><i class="fas fa-users"></i> Daftar Pengguna Sistem</h2>
            <span class="table-card-meta">{{ $totalUsers }} pengguna</span>
        </div>

        <div style="overflow-x:auto;">
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width:40px;padding-left:20px;">#</th>
                        <th>Pengguna</th>
                        <th style="width:110px;text-align:center;">Role</th>
                        <th style="width:110px;text-align:center;">Status</th>
                        <th style="width:120px;">Terdaftar</th>
                        <th style="width:130px;">Login Terakhir</th>
                        <th style="width:90px;text-align:right;padding-right:20px;">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse($users as $u)
                    @php
                        $colors = ['#3B82F6','#EF4444','#10B981','#F59E0B','#8B5CF6','#EC4899'];
                        $color  = $colors[$u->id_user % count($colors)];
                    @endphp
                    <tr>
                        <td style="padding-left:20px;color:#9CA3AF;font-size:.75rem;">{{ $loop->iteration }}</td>
                        <td>
                            <div style="display:flex;align-items:center;gap:12px;">
                                <div style="width:38px;height:38px;border-radius:50%;background:{{ $color }}20;color:{{ $color }};border:2px solid {{ $color }}40;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;">
                                    {{ strtoupper(substr($u->nama, 0, 1)) }}
                                </div>
                                <div>
                                    <div style="font-weight:600;color:#111827;font-size:.875rem;">
                                        {{ $u->nama }}
                                        @if(auth()->id() == $u->id_user)
                                        <span style="font-size:.62rem;background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;border-radius:4px;padding:1px 6px;margin-left:4px;font-weight:700;">Anda</span>
                                        @endif
                                    </div>
                                    <div style="font-size:.75rem;color:#9CA3AF;margin-top:1px;">{{ $u->email }}</div>
                                </div>
                            </div>
                        </td>
                        <td style="text-align:center;">
                            @if($u->role == 'admin')
                                <span class="status-pill" style="background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;">
                                    <i class="fas fa-shield-alt" style="font-size:.6rem;"></i> Admin
                                </span>
                            @else
                                <span class="status-pill" style="background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;">
                                    <i class="fas fa-user-tie" style="font-size:.6rem;"></i> Staff
                                </span>
                            @endif
                        </td>
                        <td style="text-align:center;">
                            @if(true)
                                <span class="status-pill pill-aktif"><span class="pill-dot"></span> Aktif</span>
                            @else
                                <span class="status-pill pill-nonaktif"><span class="pill-dot"></span> Nonaktif</span>
                            @endif
                        </td>
                        <td style="font-size:.78rem;color:#6B7280;">{{ $u->created_at?->format('d M Y') ?? '—' }}</td>
                        <td style="font-size:.78rem;">
                            <span style="color:#D1D5DB;font-size:.75rem;">—</span>
                        </td>
                        <td style="padding-right:20px;">
                            <div class="act-group">
                                <a href="{{ route('users.edit', $u->id_user) }}" class="act-btn act-edit" title="Edit">
                                    <i class="fas fa-user-edit"></i>
                                </a>
                                @if(auth()->id() != $u->id_user)
                                <form action="{{ route('users.destroy', $u->id_user) }}" method="POST" style="display:inline;margin:0;"
                                    data-confirm data-confirm-name="{{ $u->nama }}" data-confirm-extra="Akun ini akan dihapus dari sistem.">
                                    @csrf @method('DELETE')
                                    <button type="submit" class="act-btn act-del" title="Hapus">
                                        <i class="fas fa-user-times"></i>
                                    </button>
                                </form>
                                @endif
                            </div>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="7">
                            <div class="empty-state">
                                <i class="fas fa-users-slash empty-icon"></i>
                                <h4>Belum Ada Pengguna</h4>
                                <p>Sistem belum memiliki data pengguna lain.</p>
                                <a href="{{ route('users.create') }}" class="btn btn-primary btn-sm"><i class="fas fa-user-plus me-1"></i> Tambah Pengguna</a>
                            </div>
                        </td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>

</div>
@endsection



