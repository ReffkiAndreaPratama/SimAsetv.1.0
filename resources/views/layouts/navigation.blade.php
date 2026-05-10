<div class="sidebar" id="sidebar" aria-label="Main navigation" aria-hidden="true">

    {{-- â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
         HEADER â€” Logo & Nama Aplikasi
    â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• --}}
    <div class="sidebar-header">
        <a href="{{ route('dashboard') }}" class="sidebar-logo">
            <div class="sidebar-logo-img-wrap">
                <img src="{{ asset('logoweb.png') }}" alt="SimAset Logo">
            </div>
            <div style="width:1px;height:40px;background:rgba(255,255,255,0.15);flex-shrink:0;"></div>
            <div class="sidebar-logo-text">
                <span class="sidebar-logo-title">SimAset</span>
                <span class="sidebar-tagline">RBTV Bengkulu</span>
            </div>
        </a>

        {{-- Badge role pengguna --}}
        <div style="padding: 0 16px 14px; position:relative; z-index:1;">
            @if(auth()->check())
                @if(auth()->user()->isAdmin())
                    <span style="display:inline-flex;align-items:center;gap:5px;background:rgba(185,28,28,0.25);border:1px solid rgba(248,113,113,0.35);color:#fca5a5;font-size:10px;font-weight:700;padding:3px 10px;border-radius:20px;letter-spacing:0.08em;text-transform:uppercase;">
                        <i class="fas fa-shield-alt" style="font-size:9px;"></i> Administrator
                    </span>
                @else
                    <span style="display:inline-flex;align-items:center;gap:5px;background:rgba(29,78,216,0.25);border:1px solid rgba(96,165,250,0.35);color:#93c5fd;font-size:10px;font-weight:700;padding:3px 10px;border-radius:20px;letter-spacing:0.08em;text-transform:uppercase;">
                        <i class="fas fa-user-check" style="font-size:9px;"></i> Staff
                    </span>
                @endif
            @endif
        </div>
    </div>

    {{-- â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
         MENU
    â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• --}}
    <div class="sidebar-menu">

        @if(auth()->check() && auth()->user()->isAdmin())
        {{-- â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
             MENU ADMIN â€” semua operasional + administrasi
        â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ --}}

            {{-- Dashboard --}}
            <a href="{{ route('dashboard') }}" class="sidebar-link {{ request()->routeIs('dashboard') ? 'active' : '' }}">
                <i class="fas fa-chart-pie"></i><span>Dashboard</span>
            </a>

            {{-- Separator --}}
            <div style="padding:10px 14px 4px;font-size:9.5px;font-weight:700;color:rgba(255,255,255,0.3);letter-spacing:0.12em;text-transform:uppercase;">Data Master</div>

            {{-- Master Data dropdown --}}
            <div class="sidebar-dropdown">
                <button class="sidebar-link dropdown-toggle w-100 text-start d-flex align-items-center {{ request()->routeIs('aset.*') || request()->routeIs('barang.*') || request()->routeIs('ruangan.*') ? 'active' : '' }}"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#adminMasterSubmenu"
                        aria-expanded="{{ request()->routeIs('aset.*') || request()->routeIs('barang.*') || request()->routeIs('ruangan.*') ? 'true' : 'false' }}"
                        aria-controls="adminMasterSubmenu">
                    <i class="fas fa-database"></i><span>Master Data</span>
                    <i class="fas fa-chevron-down ms-auto"></i>
                </button>
                <div id="adminMasterSubmenu" class="collapse {{ request()->routeIs('aset.*') || request()->routeIs('barang.*') || request()->routeIs('ruangan.*') ? 'show' : '' }}">
                    <a href="{{ route('aset.index') }}" class="sidebar-link submenu {{ request()->routeIs('aset.*') ? 'active' : '' }}">
                        <i class="fas fa-boxes"></i><span>Aset</span>
                    </a>
                    <a href="{{ route('barang.index') }}" class="sidebar-link submenu {{ request()->routeIs('barang.*') ? 'active' : '' }}">
                        <i class="fas fa-cubes"></i><span>Barang</span>
                    </a>
                    <a href="{{ route('ruangan.index') }}" class="sidebar-link submenu {{ request()->routeIs('ruangan.*') ? 'active' : '' }}">
                        <i class="fas fa-building"></i><span>Ruangan</span>
                    </a>
                </div>
            </div>

            {{-- Separator --}}
            <div style="padding:10px 14px 4px;font-size:9.5px;font-weight:700;color:rgba(255,255,255,0.3);letter-spacing:0.12em;text-transform:uppercase;">Operasional</div>

            {{-- QR Code --}}
            <a href="{{ route('qrcode.scanner') }}" class="sidebar-link {{ request()->routeIs('qrcode.*') ? 'active' : '' }}">
                <i class="fas fa-qrcode"></i><span>QR Scanner</span>
            </a>

            {{-- Maintenance --}}
            <a href="{{ route('maintenance.index') }}" class="sidebar-link {{ request()->routeIs('maintenance.*') ? 'active' : '' }}">
                <i class="fas fa-tools"></i><span>Maintenance</span>
                @php $maintCount = \App\Models\Asset::where('status','Maintenance')->count(); @endphp
                @if($maintCount > 0)
                    <span style="margin-left:auto;background:rgba(245,158,11,.25);color:#fbbf24;font-size:10px;font-weight:700;padding:2px 7px;border-radius:10px;">{{ $maintCount }}</span>
                @endif
            </a>

            {{-- Separator --}}
            <div style="padding:10px 14px 4px;font-size:9.5px;font-weight:700;color:rgba(255,255,255,0.3);letter-spacing:0.12em;text-transform:uppercase;">Administrasi</div>

            {{-- Kelola Pengguna & Audit Log --}}
            <a href="{{ route('users.index') }}" class="sidebar-link {{ request()->routeIs('users.*') ? 'active' : '' }}">
                <i class="fas fa-users-cog"></i><span>Kelola Pengguna</span>
            </a>
            <a href="{{ route('audit-log.index') }}" class="sidebar-link {{ request()->routeIs('audit-log.*') ? 'active' : '' }}">
                <i class="fas fa-history"></i><span>Log Aktivitas</span>
            </a>

        @elseif(auth()->check() && auth()->user()->isStaff())
        {{-- â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
             MENU STAFF â€” seluruh operasional
        â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ --}}

            {{-- Dashboard --}}
            <a href="{{ route('dashboard') }}" class="sidebar-link {{ request()->routeIs('dashboard') ? 'active' : '' }}">
                <i class="fas fa-chart-pie"></i><span>Dashboard</span>
            </a>

            {{-- Separator --}}
            <div style="padding:10px 14px 4px;font-size:9.5px;font-weight:700;color:rgba(255,255,255,0.3);letter-spacing:0.12em;text-transform:uppercase;">Data Master</div>

            {{-- Master Data dropdown --}}
            <div class="sidebar-dropdown">
                <button class="sidebar-link dropdown-toggle w-100 text-start d-flex align-items-center {{ request()->routeIs('aset.*') || request()->routeIs('barang.*') || request()->routeIs('ruangan.*') ? 'active' : '' }}"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#masterDataSubmenu"
                        aria-expanded="{{ request()->routeIs('aset.*') || request()->routeIs('barang.*') || request()->routeIs('ruangan.*') ? 'true' : 'false' }}"
                        aria-controls="masterDataSubmenu">
                    <i class="fas fa-database"></i><span>Master Data</span>
                    <i class="fas fa-chevron-down ms-auto"></i>
                </button>
                <div id="masterDataSubmenu" class="collapse {{ request()->routeIs('aset.*') || request()->routeIs('barang.*') || request()->routeIs('ruangan.*') ? 'show' : '' }}">
                    <a href="{{ route('aset.index') }}" class="sidebar-link submenu {{ request()->routeIs('aset.*') ? 'active' : '' }}">
                        <i class="fas fa-boxes"></i><span>Aset</span>
                    </a>
                    <a href="{{ route('barang.index') }}" class="sidebar-link submenu {{ request()->routeIs('barang.*') ? 'active' : '' }}">
                        <i class="fas fa-cubes"></i><span>Barang</span>
                    </a>
                    <a href="{{ route('ruangan.index') }}" class="sidebar-link submenu {{ request()->routeIs('ruangan.*') ? 'active' : '' }}">
                        <i class="fas fa-building"></i><span>Ruangan</span>
                    </a>
                </div>
            </div>

            {{-- Separator --}}
            <div style="padding:10px 14px 4px;font-size:9.5px;font-weight:700;color:rgba(255,255,255,0.3);letter-spacing:0.12em;text-transform:uppercase;">Operasional</div>

            {{-- QR Code --}}
            <a href="{{ route('qrcode.scanner') }}" class="sidebar-link {{ request()->routeIs('qrcode.*') ? 'active' : '' }}">
                <i class="fas fa-qrcode"></i><span>QR Scanner</span>
            </a>

            {{-- Maintenance --}}
            <a href="{{ route('maintenance.index') }}" class="sidebar-link {{ request()->routeIs('maintenance.*') ? 'active' : '' }}">
                <i class="fas fa-tools"></i><span>Maintenance</span>
                @php $maintCount = \App\Models\Asset::where('status','Maintenance')->count(); @endphp
                @if($maintCount > 0)
                    <span style="margin-left:auto;background:rgba(245,158,11,.25);color:#fbbf24;font-size:10px;font-weight:700;padding:2px 7px;border-radius:10px;">{{ $maintCount }}</span>
                @endif
            </a>

        @endif
    </div>

    {{-- â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
         FOOTER â€” info versi
    â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• --}}
    <div class="sidebar-footer">
        <div class="brand">
            <div class="brand-icon" style="overflow:hidden;padding:0;">
                <img src="{{ asset('logo.png') }}" alt="RBTV"
                     style="width:100%;height:100%;object-fit:contain;padding:4px;"
                     onerror="this.style.display='none';this.parentElement.innerHTML='<i class=\'fas fa-tv\' style=\'font-size:14px;\'></i>'">
            </div>
            <div class="sidebar-footer-text">
                <span class="sidebar-footer-title">RBTV Bengkulu</span>
                <span class="sidebar-footer-meta">SimAset v1.0</span>
            </div>
        </div>
    </div>

    {{-- â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
         LOGOUT
    â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• --}}
    <div class="sidebar-logout">
        <form method="POST" action="{{ route('logout') }}">
            @csrf
            <button type="submit" class="btn">
                <i class="fas fa-sign-out-alt me-2"></i>Logout
            </button>
        </form>
    </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" role="button" tabindex="0" aria-label="Close menu" aria-hidden="true"></div>


