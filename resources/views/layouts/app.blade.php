<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>@yield('title') - SimAset</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ asset('css/glass-ui.css') }}">

    <style>
    /* Base Styles */
    * { font-family: 'Inter', sans-serif; margin: 0; padding: 0; box-sizing: border-box; }
    html, body { height: 100%; width: 100%; overflow-x: hidden; }
    body {
        background-color: #F8FAFC;
        color: #1F2937;
        min-height: 100vh;
        min-height: 100dvh;
        overflow-y: auto;
    }
        body.sidebar-open {
            overflow: hidden;
        }
        a { color: inherit; text-decoration: none; }
        a:hover { text-decoration: none; }

        /* Smooth Transitions */
        * { transition: background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease; }

        /* Card Styles */
        .card {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            overflow: hidden;
        }
        .card-header { background: transparent; border-bottom: none; padding-bottom: 0; }
        .card-body { background: transparent; }
        .card-footer { background: #F8FAFC; border-top: 1px solid #E2E8F0; }

        /* Form Controls */
        .form-control, .form-select {
            background: #FFFFFF;
            border-color: #CBD5E1;
            color: #1F2937;
            border-radius: 12px;
            padding: 12px 16px;
            font-size: 1rem;
            min-height: 48px;
            transition: border-color 0.15s ease, box-shadow 0.15s ease;
        }
        .form-control:focus, .form-select:focus {
            border-color: #3B82F6;
            box-shadow: 0 0 0 0.2rem rgba(59, 130, 246, 0.18);
            outline: none;
        }
        .form-control::placeholder { color: #94A3B8; }
        .input-group-text {
            border-color: #CBD5E1;
            background: #FFFFFF;
            padding: 0 16px;
            font-size: 1rem;
        }

        /* Badges - Enhanced */
        .badge { 
            font-weight: 600; 
            padding: 6px 12px; 
            border-radius: 8px; 
            font-size: 0.75rem;
            letter-spacing: 0.03em;
        }
        .badge-lg {
            font-size: 0.875rem;
            padding: 8px 16px;
            border-radius: 10px;
        }
        .bg-primary { background-color: #3B82F6 !important; }
        .bg-success { background-color: #10B981 !important; }
        .bg-warning { background-color: #F59E0B !important; }
        .bg-danger { background-color: #EF4444 !important; }
        .bg-secondary { background-color: #6B7280 !important; }
        .bg-info { background-color: #0EA5E9 !important; }

        /* Badge Outline Variants */
        .badge-outline-primary {
            background: transparent;
            border: 1px solid #3B82F6;
            color: #3B82F6;
        }
        .badge-outline-success {
            background: transparent;
            border: 1px solid #10B981;
            color: #059669;
        }
        .badge-outline-warning {
            background: transparent;
            border: 1px solid #F59E0B;
            color: #D97706;
        }
        .badge-outline-danger {
            background: transparent;
            border: 1px solid #EF4444;
            color: #DC2626;
        }

        /* Alerts */
        .alert { border-radius: 14px; border: none; }
        .alert-success { background: rgba(16, 163, 127, 0.12); color: #059669; }
        .alert-danger { background: rgba(220, 38, 38, 0.12); color: #B91C1C; }
        .alert-info { background: rgba(14, 165, 233, 0.12); color: #0284C7; }
        .alert-warning { background: rgba(245, 158, 11, 0.12); color: #B45309; }

        /* Buttons - Enhanced */
        .btn-primary {
            background: #3B82F6;
            border-color: #3B82F6;
            border-radius: 8px;
            padding: 10px 20px;
            box-shadow: 0 4px 10px rgba(59, 130, 246, 0.15);
            font-weight: 600;
            min-height: 44px;
            font-size: 0.95rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .btn-primary:hover {
            background: #2563EB;
            border-color: #2563EB;
            box-shadow: 0 6px 14px rgba(59, 130, 246, 0.2);
            transform: translateY(-1px);
        }
        .btn-primary:active {
            transform: translateY(0);
            box-shadow: 0 2px 6px rgba(59, 130, 246, 0.15);
        }
        .btn-outline-primary {
            border-radius: 8px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .btn-outline-primary:hover {
            background: #3B82F6;
            border-color: #3B82F6;
        }
        .btn-light {
            background: #FFFFFF;
            border-color: #E5E7EB;
            color: #374151;
            font-weight: 600;
            min-height: 44px;
        }
        .btn-light:hover {
            background: #F8FAFC;
            border-color: #D1D5DB;
        }

        /* Tables */
        .table { background: #FFFFFF; color: #1F2937; }
        .table thead th {
            background: #F8FAFC;
            border-bottom: 1px solid #E5E7EB;
            color: #475569;
            font-weight: 600;
            letter-spacing: 0.02em;
            font-size: 0.75rem;
            text-transform: uppercase;
            padding: 14px 16px;
        }
        .table td { border-color: #E2E8F0; vertical-align: middle; }
        .table-hover tbody tr:hover { background-color: #F8FAFC; }

        /* Modal */
        .modal-content { border-radius: 20px; border: 1px solid #E5E7EB; }
        .modal-header { border-bottom: none; padding-bottom: 0; }
        .modal-footer { border-top: none; padding-top: 0; }

        /* Dropdown */
        .dropdown-menu {
            border-radius: 14px;
            border-color: #E5E7EB;
            box-shadow: 0 20px 60px rgba(15, 23, 42, 0.12);
            padding: 8px 0;
            font-size: 0.9rem;
        }
        .dropdown-item {
            color: #374151;
            padding: 10px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .dropdown-item:hover {
            background: #EFF6FF;
            color: #1D4ED8;
        }
        .dropdown-header {
            font-size: 0.8rem;
            font-weight: 600;
            color: #6B7280;
            padding: 8px 20px;
        }
        .dropdown-divider { margin: 8px 0; border-color: #E5E7EB; }

        /* ── Sidebar Layout ── */
        .wrapper {
            display: flex;
            min-height: 100vh;
            min-height: 100dvh;
            width: 100%;
        }
         /* ── Sidebar core ── */
         .sidebar {
             width: 280px;
             background: linear-gradient(180deg, #1a3470 0%, #1c3d9e 55%, #1e45b8 100%);
             height: 100vh;
             height: 100dvh;
             display: flex;
             flex-direction: column;
             position: fixed;
             left: 0;
             top: 0;
             z-index: 1040;
             overflow-y: auto;
             overflow-x: hidden;
             transform: translateX(-100%);
             transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
             will-change: transform;
             box-shadow: 4px 0 28px rgba(15,30,80,0.35);
         }
        .sidebar.active { transform: translateX(0); }
        .sidebar:focus-visible { outline: 2px solid rgba(255,255,255,0.5); outline-offset: -2px; }

        /* ── Sidebar Header — Logo area spesial ── */
        .sidebar-header {
            padding: 0;
            border-bottom: none;
            background: transparent;
            position: relative;
            flex-shrink: 0;
        }
        /* Gradient overlay di header */
        .sidebar-header::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(0,0,0,0.25) 0%, rgba(30,58,138,0.15) 100%);
            pointer-events: none;
        }
        /* Garis aksen merah di bawah header */
        .sidebar-header::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 2px;
            background: linear-gradient(90deg, #b91c1c 0%, #ef4444 40%, rgba(255,255,255,0.15) 100%);
        }
        .sidebar-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            padding: 18px 16px 20px;
            position: relative;
            z-index: 1;
        }

        /* Logo image — hanya logoweb.png */
        .sidebar-logo-img-wrap {
            position: relative;
            flex-shrink: 0;
        }
        .sidebar-logo-img-wrap::before {
            content: '';
            position: absolute;
            inset: -2px;
            border-radius: 50%;
            background: rgba(255,255,255,0.15);
            border: 1.5px solid rgba(255,255,255,0.25);
            z-index: 0;
        }
        .sidebar-logo-img-wrap::after {
            content: '';
            position: absolute;
            inset: -1px;
            border-radius: 50%;
            background: linear-gradient(180deg, #1a3470, #1c3d9e);
            z-index: 1;
        }
        .sidebar-logo-img-wrap img {
            width: 56px;
            height: 56px;
            object-fit: contain;
            border-radius: 50%;
            background: rgba(255,255,255,0.12);
            padding: 7px;
            position: relative;
            z-index: 2;
            transition: transform 0.3s ease;
            display: block;
        }
        .sidebar-logo:hover .sidebar-logo-img-wrap img {
            transform: scale(1.08);
        }

        /* Logo text */
        .sidebar-logo-text {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 3px;
        }
        .sidebar-logo-title {
            font-size: 20px;
            font-weight: 800;
            color: #FFFFFF;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            line-height: 1.15;
        }
        .sidebar-tagline {
            font-size: 10px;
            color: rgba(255,255,255,0.55);
            letter-spacing: 0.14em;
            text-transform: uppercase;
            font-weight: 500;
        }

        /* ── Sidebar Menu ── */
        .sidebar-menu {
            padding: 16px 12px;
            display: flex;
            flex-direction: column;
            flex: 1 0 auto;
            gap: 2px;
            min-height: 0;
        }

        /* ── Sidebar Link — ukuran konsisten ── */
        .sidebar-link {
            display: flex;
            align-items: center;
            gap: 12px;
            color: rgba(255,255,255,0.78);
            text-decoration: none;
            padding: 11px 14px;
            border-radius: 10px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 0.875rem;
            font-weight: 500;
            position: relative;
            overflow: hidden;
            /* Reset button styles */
            background: transparent;
            border: none;
            width: 100%;
            text-align: left;
            cursor: pointer;
            line-height: 1.4;
            min-height: 42px;
        }
        .sidebar-link::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 3px;
            height: 0;
            background: #f87171;
            border-radius: 0 3px 3px 0;
            transition: height 0.2s ease;
        }
        .sidebar-link:hover,
        .sidebar-link:focus {
            background: rgba(255,255,255,0.1) !important;
            color: #FFFFFF !important;
            transform: translateX(4px);
            outline: none;
            box-shadow: none;
        }
        .sidebar-link:hover::before,
        .sidebar-link:focus::before {
            height: 65%;
        }
        .sidebar-link:focus-visible {
            outline: 2px solid rgba(255,255,255,0.4);
            outline-offset: 1px;
        }
        .sidebar-link i {
            width: 22px;
            text-align: center;
            font-size: 15px;
            color: rgba(255,255,255,0.75);
            flex-shrink: 0;
            transition: transform 0.2s ease, color 0.2s ease;
        }
        .sidebar-link:hover i,
        .sidebar-link:focus i {
            transform: scale(1.12);
            color: rgba(255,255,255,0.95);
        }
        /* Active state */
        .sidebar-link.active {
            background: rgba(255,255,255,0.12) !important;
            border-left: 3px solid #f87171 !important;
            color: #FFFFFF !important;
            font-weight: 600;
            padding-left: 11px;
        }
        .sidebar-link.active::before {
            height: 65%;
            background: #f87171;
        }
        .sidebar-link.active i {
            color: #fca5a5 !important;
        }

        /* ── Dropdown toggle — fix Bootstrap override ── */
        button.sidebar-link,
        button.sidebar-link.dropdown-toggle {
            background: transparent !important;
            border: none !important;
            color: rgba(255,255,255,0.78) !important;
            box-shadow: none !important;
        }
        button.sidebar-link:hover,
        button.sidebar-link:focus,
        button.sidebar-link.dropdown-toggle:hover,
        button.sidebar-link.dropdown-toggle:focus {
            background: rgba(255,255,255,0.1) !important;
            color: #FFFFFF !important;
            box-shadow: none !important;
            border: none !important;
        }
        button.sidebar-link.active,
        button.sidebar-link.dropdown-toggle.active {
            background: rgba(255,255,255,0.12) !important;
            color: #FFFFFF !important;
            border-left: 3px solid #f87171 !important;
            border-top: none !important;
            border-right: none !important;
            border-bottom: none !important;
        }
        /* Remove Bootstrap dropdown-toggle arrow */
        .sidebar-link.dropdown-toggle::after { display: none !important; }

        /* ── Submenu items ── */
        .sidebar-link.submenu {
            padding: 9px 14px 9px 44px;
            font-size: 0.84rem;
            color: rgba(255,255,255,0.65);
            min-height: 38px;
            border-radius: 8px;
        }
        .sidebar-link.submenu:hover,
        .sidebar-link.submenu:focus {
            background: rgba(255,255,255,0.08) !important;
            color: rgba(255,255,255,0.95) !important;
            transform: translateX(3px);
        }
        .sidebar-link.submenu.active {
            background: rgba(248,113,113,0.15) !important;
            color: #fca5a5 !important;
            border-left: 2px solid #f87171 !important;
            padding-left: 42px;
        }
        .sidebar-link.submenu i {
            font-size: 13px;
            width: 18px;
        }

        /* Submenu container */
        .collapse .sidebar-link.submenu {
            margin: 1px 0;
        }

        /* Chevron rotation */
        .sidebar-link .fa-chevron-down {
            transition: transform 0.25s ease !important;
            color: rgba(255,255,255,0.45) !important;
            font-size: 10px !important;
        }
        .sidebar-link[aria-expanded="true"] .fa-chevron-down {
            transform: rotate(180deg) !important;
        }

        /* ── Sidebar Footer ── */
        .sidebar-footer {
            padding: 16px 20px;
            border-top: 1px solid rgba(255,255,255,0.08);
            margin-top: auto;
            background: rgba(0,0,0,0.12);
        }
        .sidebar-footer .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            color: rgba(255,255,255,0.8);
            padding: 6px 8px;
            border-radius: 8px;
            transition: background 0.2s ease;
        }
        .sidebar-footer .brand:hover { background: rgba(255,255,255,0.07); }
        .sidebar-footer .brand-icon {
            width: 34px;
            height: 34px;
            border-radius: 9px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #1d4ed8, #3b82f6);
            color: white;
            font-size: 13px;
            box-shadow: 0 3px 8px rgba(29,78,216,0.35);
            flex-shrink: 0;
            transition: transform 0.2s ease;
        }
        .sidebar-footer .brand:hover .brand-icon { transform: scale(1.08); }
        .sidebar-footer-text { display: flex; flex-direction: column; }
        .sidebar-footer-title { font-size: 12.5px; font-weight: 700; color: rgba(255,255,255,0.9); }
        .sidebar-footer-meta { font-size: 10px; color: rgba(255,255,255,0.5); font-style: italic; }

        /* ── Sidebar Logout ── */
        .sidebar-logout {
            padding: 14px 16px 18px;
            margin: 0 10px 10px;
            background: rgba(185,28,28,0.1);
            border-radius: 10px;
            border: 1px solid rgba(185,28,28,0.2);
        }
        .sidebar-logout .btn {
            width: 100%;
            padding: 10px 0;
            background: linear-gradient(135deg, #b91c1c, #dc2626);
            border: 1px solid rgba(220,38,38,0.35);
            color: #FFFFFF;
            font-weight: 600;
            border-radius: 9px;
            font-size: 0.875rem;
            transition: all 0.22s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .sidebar-logout .btn:hover {
            background: linear-gradient(135deg, #991b1b, #b91c1c);
            transform: translateY(-1px);
            box-shadow: 0 4px 14px rgba(185,28,28,0.35);
        }
        .sidebar-logout .btn:active { transform: translateY(0); }

        /* ── Sidebar Overlay ── */
        .sidebar-overlay {
            position: fixed;
            inset: 0;
            background: rgba(15,23,42,0.45);
            z-index: 1030;
            display: none;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .sidebar-overlay.active { display: block; opacity: 1; }
        .sidebar-overlay[aria-hidden="true"] { display: none !important; }
        body.sidebar-open { overflow: hidden; touch-action: none; }

        /* Header - Modern & Responsive */
        .header {
            background: #FFFFFF;
            border-bottom: 1px solid #E5E7EB;
            padding: 14px 20px;
            position: sticky;
            top: 0;
            z-index: 1020;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
            min-height: 64px;
            transition: all 0.2s ease;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 100%;
            gap: 12px;
            height: 100%;
        }
        .header-left {
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
            min-width: 0;
        }
        .hamburger {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            border: 1px solid #bfdbfe;
            background: linear-gradient(135deg, #eff6ff, #dbeafe);
            color: #1d4ed8;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s ease;
            flex-shrink: 0;
            z-index: 1;
        }
        .hamburger:hover,
        .hamburger:focus {
            background: linear-gradient(135deg, #dbeafe, #bfdbfe);
            border-color: #2563eb;
            transform: scale(1.05);
            outline: none;
        }
        .hamburger:active { transform: scale(0.98); }
        .hamburger:focus-visible {
            outline: 2px solid #2563eb;
            outline-offset: 2px;
        }
        .header-title-group {
            display: flex;
            flex-direction: column;
            min-width: 0;
            flex: 1;
        }
        .header-title {
            font-size: clamp(1.05rem, 3.5vw, 1.5rem);
            font-weight: 700;
            color: #0F172A;
            margin: 0;
            line-height: 1.3;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            letter-spacing: -0.01em;
        }
        .header-subtitle {
            font-size: clamp(0.7rem, 2vw, 0.85rem);
            color: #6B7280;
            font-weight: 500;
            letter-spacing: 0.02em;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            opacity: 0.9;
        }
        .header-right {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
        }
        .btn-icon {
            position: relative;
            width: 44px;
            height: 44px;
            border: 1px solid #bfdbfe;
            background: linear-gradient(135deg, #eff6ff, #dbeafe);
            color: #1d4ed8;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }
        .btn-icon:hover,
        .btn-icon:focus {
            background: linear-gradient(135deg, #dbeafe, #bfdbfe);
            border-color: #2563eb;
            transform: scale(1.08);
            outline: none;
        }
        .btn-icon:active { transform: scale(0.98); }
        .btn-icon:focus-visible {
            outline: 2px solid #2563eb;
            outline-offset: 2px;
        }
        .notification-badge {
            position: absolute;
            top: 8px;
            right: 8px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #DC2626;
            border: 2px solid #FFFFFF;
            box-shadow: 0 0 0 2px rgba(220, 38, 38, 0.15);
        }
        .notification-badge::after {
            content: '';
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            width: 4px; height: 4px;
            background: white;
            border-radius: 50%;
            animation: pulse-badge 1.5s infinite;
        }
        @keyframes pulse-badge {
            0%, 100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.6; transform: translate(-50%, -50%) scale(1.2); }
        }
        .user-profile-btn {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            border: 1px solid #bfdbfe;
            background: linear-gradient(135deg, #FFFFFF, #f0f9ff);
            border-radius: 12px;
            color: #1F2937;
            font-weight: 500;
            transition: all 0.2s ease;
            min-width: 140px;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(29,78,216,0.07);
        }
        .user-profile-btn:hover,
        .user-profile-btn:focus {
            background: linear-gradient(135deg, #dbeafe, #bfdbfe);
            border-color: #2563eb;
            outline: none;
            box-shadow: 0 3px 12px rgba(29,78,216,0.12);
        }
        .user-profile-btn:focus-visible {
            outline: 2px solid #2563eb;
            outline-offset: 2px;
        }
        .user-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1d4ed8, #3b82f6);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFFFFF;
            font-weight: 700;
            font-size: 0.9rem;
            flex-shrink: 0;
            border: 2px solid rgba(255,255,255,0.8);
        }
        .user-info {
            display: flex;
            flex-direction: column;
            min-width: 0;
            flex: 1;
        }
        .user-name {
            font-weight: 600;
            font-size: 0.85rem;
            color: #0F172A;
            line-height: 1.2;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .user-role {
            font-size: 0.75rem;
            color: #6B7280;
            text-transform: capitalize;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .chevron-down {
            font-size: 0.75rem;
            color: #6B7280;
            flex-shrink: 0;
            transition: transform 0.2s ease;
        }
        .user-dropdown .dropdown-toggle[aria-expanded="true"] .chevron-down {
            transform: rotate(180deg);
        }

        /* Responsive header handled in layout section below */

        /* ── Layout Core ── */
        .wrapper {
            display: flex;
            min-height: 100vh;
            min-height: 100dvh;
            width: 100%;
        }

        /* Sidebar width token — ubah di sini untuk semua */
        :root { --sidebar-w: 280px; }

        .main-content {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            min-height: 100dvh;
            width: 100%;
            /* Desktop: geser kanan sejauh sidebar */
            margin-left: var(--sidebar-w);
            transition: margin-left 0.3s cubic-bezier(0.4,0,0.2,1);
        }

        /* ── Content Area — padding konsisten ── */
        .content-area {
            flex: 1;
            /* Padding konsisten: atas 24px, kiri-kanan 28px, bawah 32px */
            padding: 24px 28px 32px;
            background: #F8FAFC;
            width: 100%;
        }

        /* Page container — satu definisi, dipakai semua halaman */
        .page-container {
            width: 100%;
            max-width: 1320px;
            margin: 0 auto;
        }

        /* ── Header ── */
        .header {
            background: #FFFFFF;
            border-bottom: 1px solid #F1F5F9;
            padding: 0 28px;
            position: sticky;
            top: 0;
            z-index: 1020;
            box-shadow: 0 1px 0 #F1F5F9, 0 2px 8px rgba(15,23,42,0.04);
            height: 64px;
            flex-shrink: 0;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 100%;
            gap: 16px;
        }
        .header-left {
            display: flex;
            align-items: center;
            gap: 14px;
            flex: 1;
            min-width: 0;
        }
        .hamburger {
            display: none;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            border: 1px solid #E5E7EB;
            background: #F8FAFC;
            color: #374151;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }
        .hamburger:hover { background: #EFF6FF; border-color: #BFDBFE; color: #1d4ed8; }
        .hamburger:active { transform: scale(0.96); }
        .header-title-group { display: flex; flex-direction: column; min-width: 0; flex: 1; }
        .header-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0F172A;
            margin: 0;
            line-height: 1.3;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            letter-spacing: -0.01em;
        }
        .header-subtitle {
            font-size: 0.72rem;
            color: #9CA3AF;
            font-weight: 400;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .header-right { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }

        /* Header icon buttons — tidak dipakai lagi, tapi tetap ada untuk kompatibilitas */
        .btn-icon {
            position: relative;
            width: 38px;
            height: 38px;
            border: 1px solid #E5E7EB;
            background: #F8FAFC;
            color: #374151;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
            cursor: pointer;
        }
        .btn-icon:hover { background: #EFF6FF; border-color: #BFDBFE; color: #1d4ed8; }
        .btn-icon:active { transform: scale(0.96); }

        .notification-badge {
            position: absolute;
            top: 7px; right: 7px;
            width: 8px; height: 8px;
            border-radius: 50%;
            background: #DC2626;
            border: 2px solid #FFFFFF;
        }

        /* User profile button */
        .user-profile-btn {
            display: flex;
            align-items: center;
            gap: 9px;
            padding: 5px 12px 5px 5px;
            border: 1px solid #E5E7EB;
            background: #FFFFFF;
            border-radius: 40px;
            color: #1F2937;
            font-weight: 500;
            transition: all 0.2s ease;
            cursor: pointer;
            min-width: 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        }
        .user-profile-btn:hover {
            border-color: #BFDBFE;
            background: #F8FAFC;
            box-shadow: 0 2px 8px rgba(29,78,216,0.1);
        }
        .user-profile-btn:focus { outline: none; }
        .user-avatar {
            width: 32px; height: 32px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1d4ed8, #3b82f6);
            display: flex; align-items: center; justify-content: center;
            color: #FFFFFF; font-weight: 700; font-size: 0.82rem;
            flex-shrink: 0;
            box-shadow: 0 2px 6px rgba(29,78,216,0.25);
        }
        .user-info { display: flex; flex-direction: column; min-width: 0; }
        .user-name { font-weight: 600; font-size: 0.82rem; color: #0F172A; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 110px; line-height: 1.3; }
        .user-role { font-size: 0.7rem; color: #9CA3AF; text-transform: capitalize; line-height: 1.2; }
        .user-dropdown .dropdown-toggle[aria-expanded="true"] .fa-chevron-down { transform: rotate(180deg); }
        .fa-chevron-down { transition: transform 0.2s ease; font-size: 0.65rem; color: #9CA3AF; }

        /* Profile dropdown menu */
        .profile-dropdown-menu {
            min-width: 220px;
            border-radius: 14px !important;
            border: 1px solid #E5E7EB !important;
            box-shadow: 0 10px 40px rgba(15,23,42,0.12) !important;
            padding: 0 !important;
            overflow: hidden;
            margin-top: 6px !important;
        }
        .profile-dropdown-menu .dropdown-item {
            padding: 10px 16px;
            font-size: 0.875rem;
            font-weight: 500;
            border-radius: 0;
            transition: background 0.15s ease;
        }
        .profile-dropdown-menu .dropdown-item:hover {
            background: #F1F5F9;
        }
        .profile-dropdown-menu .dropdown-item.text-danger:hover {
            background: #FEF2F2;
        }

        /* ── Footer ── */
        .footer {
            background: #FFFFFF;
            border-top: 2px solid #E5E7EB;
            padding: 14px 28px;
            flex-shrink: 0;
        }
        .footer-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .footer-brand { display: flex; align-items: center; gap: 10px; }
        .footer-logo-wrap {
            display: flex; align-items: center; justify-content: center;
            width: 40px; height: 40px;
            border-radius: 9px;
            background: #EFF6FF;
            border: 1.5px solid #BFDBFE;
            overflow: hidden; flex-shrink: 0;
        }
        .footer-logo { height: 32px; width: 32px; object-fit: contain; padding: 2px; }
        .footer-text { display: flex; flex-direction: column; line-height: 1.4; }
        .footer-text strong { font-size: 0.8rem; font-weight: 800; color: #1E3A8A; letter-spacing: 0.01em; }
        .footer-text span   { font-size: 0.7rem; color: #6B7280; font-weight: 500; }
        .footer-right { display: flex; align-items: center; gap: 8px; font-size: 0.75rem; color: #9CA3AF; }
        .footer-dot { width: 3px; height: 3px; border-radius: 50%; background: #D1D5DB; display: inline-block; }
        .footer-version {
            display: inline-flex; align-items: center; gap: 5px;
            background: #EFF6FF; border: 1px solid #BFDBFE;
            border-radius: 20px; padding: 3px 10px;
            font-size: 0.7rem; font-weight: 700; color: #1E3A8A;
        }

        /* ── Responsive ── */

        /* Desktop ≥1024px: sidebar visible, hamburger hidden */
        @media (min-width: 1024px) {
            .sidebar { transform: translateX(0) !important; }
            .sidebar-overlay { display: none !important; }
            .hamburger { display: none !important; }
        }

        /* Tablet & Mobile <1024px: sidebar hidden, hamburger visible */
        @media (max-width: 1023px) {
            .main-content { margin-left: 0; }
            .hamburger { display: flex; }
            .header { padding: 0 16px; }
            .content-area { padding: 16px 16px 24px; }
            .footer { padding: 12px 16px; }
            .user-info { display: none; }
        }

        @media (max-width: 767px) {
            .header { height: 56px; }
            .header-title { font-size: 1rem; }
            .header-subtitle { display: none; }
            .content-area { padding: 12px 12px 20px; }
            .footer-container { flex-direction: column; align-items: flex-start; gap: 6px; }
            .footer-right { flex-wrap: wrap; }
        }

        @media (max-width: 479px) {
            .header { padding: 0 12px; height: 52px; }
            .hamburger { width: 36px; height: 36px; }
            .btn-icon { width: 36px; height: 36px; }
            .content-area { padding: 10px 10px 16px; }
            .footer { padding: 10px 12px; }
        }

        /* ── Sidebar Dropdown ── */
        .sidebar-dropdown .sidebar-link.submenu {
            padding-left: 48px;
            font-size: 0.84rem;
            margin: 1px 8px;
            position: relative;
        }
        .sidebar-dropdown .sidebar-link.submenu::before {
            left: 20px; width: 3px;
            background: rgba(248,113,113,0.3);
        }
        .sidebar-dropdown .sidebar-link.submenu:hover::before,
        .sidebar-dropdown .sidebar-link.submenu.active::before {
            background: #f87171; height: 50%;
        }
        .sidebar-dropdown .sidebar-link.submenu.active {
            background: rgba(248,113,113,0.15) !important;
            color: #fca5a5 !important;
            border-left: 2px solid #f87171 !important;
        }
        .sidebar-dropdown .collapse {
            overflow: hidden;
            transition: max-height 0.3s cubic-bezier(0.4,0,0.2,1);
        }
        .sidebar-dropdown .dropdown-toggle[aria-expanded="true"] .fa-chevron-down {
            transform: rotate(180deg);
        }

        /* ── Utilities ── */
        ::-webkit-scrollbar { width: 5px; height: 5px; }
        ::-webkit-scrollbar-track { background: #F1F5F9; }
        ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #94A3B8; }

        @@keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in { animation: fadeIn 0.22s ease-out; }

        @media print {
            .header, .footer, .sidebar, .no-print { display: none !important; }
            .main-content { margin: 0; }
            .content-area { padding: 0; }
        }
    </style>
    @stack('styles')
</head>
<body>
<div class="wrapper">
    @include('layouts.navigation')

    <div class="main-content" id="mainContent">
        <header class="header">
            <div class="header-container">
                <div class="header-left">
                     <button class="hamburger" id="sidebarToggle" aria-label="Toggle sidebar menu" aria-controls="sidebar" aria-expanded="false">
                         <i class="fas fa-bars" aria-hidden="true"></i>
                     </button>
                    <div class="header-title-group">
                        <h1 class="header-title">@yield('title')</h1>
                        <span class="header-subtitle">Sistem Informasi Aset · RBTV Bengkulu</span>
                    </div>
                </div>
                <div class="header-right">
                    <div class="dropdown user-dropdown">
                        <button class="user-profile-btn dropdown-toggle" type="button" id="profileDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                            <div class="user-avatar">{{ strtoupper(substr(auth()->user()->nama, 0, 1)) }}</div>
                            <div class="user-info">
                                <span class="user-name">{{ auth()->user()->nama }}</span>
                                <span class="user-role">{{ ucfirst(auth()->user()->role) }}</span>
                            </div>
                            <i class="fas fa-chevron-down ms-2"></i>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end profile-dropdown-menu" aria-labelledby="profileDropdown">
                            <li>
                                <div class="px-4 py-3 border-bottom">
                                    <div class="d-flex align-items-center gap-3">
                                        <div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#1d4ed8,#3b82f6);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1rem;flex-shrink:0;">
                                            {{ strtoupper(substr(auth()->user()->nama, 0, 1)) }}
                                        </div>
                                        <div style="min-width:0;">
                                            <div style="font-weight:700;font-size:0.875rem;color:#0F172A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:160px;">{{ auth()->user()->nama }}</div>
                                            <div style="font-size:0.72rem;color:#6B7280;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:160px;">{{ auth()->user()->email }}</div>
                                        </div>
                                    </div>
                                </div>
                            </li>
                            <li><a class="dropdown-item" href="{{ route('profile.edit') }}"><i class="fas fa-user-edit me-2 text-primary"></i>Edit Profil</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li>
                                <form method="POST" action="{{ route('logout') }}" class="m-0">
                                    @csrf
                                    <button type="submit" class="dropdown-item text-danger">
                                        <i class="fas fa-sign-out-alt me-2"></i>Keluar
                                    </button>
                                </form>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </header>

        <main class="content-area">
            @yield('content')
        </main>

        <footer class="footer">
            <div class="footer-container">
                <div class="footer-brand">
                    <div class="footer-logo-wrap">
                        <img src="{{ asset('logo.png') }}" alt="RBTV" class="footer-logo"
                             onerror="this.style.display='none'">
                    </div>
                    <div class="footer-text">
                        <strong>SimAset &mdash; Rakyat Bengkulu Televisi</strong>
                        <span>Sistem Informasi Manajemen Aset Barang Kantor</span>
                    </div>
                </div>
                <div class="footer-right">
                    <span class="footer-version">
                        <i class="fas fa-code-branch" style="font-size:0.6rem;"></i>
                        v1.0
                    </span>
                    <span class="footer-dot"></span>
                    <span>&copy; {{ date('Y') }} RBTV Bengkulu</span>
                </div>
            </div>
        </footer>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script>
// ── SweetAlert2 Global Helpers ──────────────────────────────────────────────

/**
 * Konfirmasi hapus — kembalikan Promise<boolean>
 * Gunakan: deleteConfirm('Nama Item').then(ok => { if(ok) form.submit() })
 */
function deleteConfirm(itemName = '', extraText = '') {
    return Swal.fire({
        title: 'Hapus Data?',
        html: itemName
            ? `<span style="color:#374151;">Anda akan menghapus <strong style="color:#dc2626;">${itemName}</strong>.<br>${extraText || 'Tindakan ini tidak dapat dibatalkan.'}</span>`
            : `<span style="color:#374151;">${extraText || 'Tindakan ini tidak dapat dibatalkan.'}</span>`,
        icon: 'warning',
        iconColor: '#f59e0b',
        showCancelButton: true,
        confirmButtonColor: '#dc2626',
        cancelButtonColor: '#6b7280',
        confirmButtonText: '<i class="fas fa-trash-alt me-1"></i> Ya, Hapus',
        cancelButtonText: '<i class="fas fa-times me-1"></i> Batal',
        reverseButtons: true,
        focusCancel: true,
        customClass: {
            popup:         'swal-popup-custom',
            title:         'swal-title-custom',
            confirmButton: 'swal-confirm-custom',
            cancelButton:  'swal-cancel-custom',
        },
    }).then(r => r.isConfirmed);
}

/**
 * Konfirmasi aksi umum (non-hapus)
 */
function actionConfirm(title, text, confirmText = 'Ya, Lanjutkan', confirmColor = '#2563eb') {
    return Swal.fire({
        title,
        html: `<span style="color:#374151;">${text}</span>`,
        icon: 'question',
        iconColor: confirmColor,
        showCancelButton: true,
        confirmButtonColor: confirmColor,
        cancelButtonColor: '#6b7280',
        confirmButtonText: confirmText,
        cancelButtonText: '<i class="fas fa-times me-1"></i> Batal',
        reverseButtons: true,
        focusCancel: true,
    }).then(r => r.isConfirmed);
}

/**
 * Notifikasi sukses / error / info ringan (toast)
 */
function showToast(icon, title, timer = 3000) {
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon,
        title,
        showConfirmButton: false,
        timer,
        timerProgressBar: true,
        customClass: { popup: 'swal-toast-custom' },
    });
}

/**
 * Toggle show/hide password field
 */
function togglePwField(fieldId, btn) {
    const input = document.getElementById(fieldId);
    const icon  = btn.querySelector('i');
    if (!input) return;
    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.replace('fa-eye', 'fa-eye-slash');
        icon.style.color = '#3B82F6';
    } else {
        input.type = 'password';
        icon.classList.replace('fa-eye-slash', 'fa-eye');
        icon.style.color = '#94A3B8';
    }
}

// Pasang handler ke semua form[data-confirm]
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('form[data-confirm]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const name  = form.dataset.confirmName  || '';
            const extra = form.dataset.confirmExtra || '';
            deleteConfirm(name, extra).then(ok => { if (ok) form.submit(); });
        });
    });
});
</script>
<style>
.swal-popup-custom  { border-radius: 16px !important; font-family: 'Inter', sans-serif !important; padding: 28px 24px !important; }
.swal-title-custom  { font-size: 1.1rem !important; font-weight: 700 !important; color: #0f172a !important; }
.swal-confirm-custom, .swal-cancel-custom { border-radius: 8px !important; font-weight: 600 !important; font-size: 0.875rem !important; padding: 10px 20px !important; }
.swal-toast-custom  { border-radius: 12px !important; font-family: 'Inter', sans-serif !important; }
</style>
</script>
<script>
// Toggle sidebar with body scroll lock
const sidebar = document.querySelector('.sidebar');
const overlay = document.getElementById('sidebarOverlay');
const body = document.body;

function toggleSidebar(show) {
    if (show) {
        sidebar.classList.add('active');
        overlay.classList.add('active');
        body.classList.add('sidebar-open');
        // Focus trap for accessibility
        sidebar.setAttribute('aria-hidden', 'false');
        overlay.setAttribute('aria-hidden', 'false');
    } else {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        body.classList.remove('sidebar-open');
        sidebar.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('aria-hidden', 'true');
    }
}

document.getElementById('sidebarToggle').addEventListener('click', () => {
    const isActive = sidebar.classList.contains('active');
    toggleSidebar(!isActive);
});

document.getElementById('sidebarOverlay').addEventListener('click', () => {
    toggleSidebar(false);
});

// Keyboard support for overlay
document.getElementById('sidebarOverlay').addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleSidebar(false);
    }
});

// Close sidebar with Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && sidebar.classList.contains('active')) {
        toggleSidebar(false);
    }
});

// Handle window resize - close mobile sidebar on desktop
window.addEventListener('resize', () => {
    if (window.innerWidth >= 1024 && sidebar.classList.contains('active')) {
        toggleSidebar(false);
    }
});

// Initialize
sidebar.setAttribute('aria-hidden', 'true');
overlay.setAttribute('aria-hidden', 'true');

// Dropdown functionality for sidebar on mobile
document.querySelectorAll('.sidebar-dropdown .dropdown-toggle').forEach(button => {
    button.addEventListener('click', function(e) {
        if (window.innerWidth < 1024) {
            e.preventDefault();
            const target = this.getAttribute('data-bs-target');
            const dropdown = document.querySelector(target);
            const isExpanded = this.getAttribute('aria-expanded') === 'true';

            // Close all other dropdowns
            document.querySelectorAll('.sidebar-dropdown .collapse.show').forEach(open => {
                if (open !== dropdown) {
                    open.classList.remove('show');
                    open.previousElementSibling.setAttribute('aria-expanded', 'false');
            }
            });

            // Toggle current
            dropdown.classList.toggle('show');
            this.setAttribute('aria-expanded', !isExpanded);
        }
    });
});
</script>
@stack('scripts')

{{-- ── Global Flash Toast (SweetAlert2) ── --}}
@if(session('success'))
<script>
document.addEventListener('DOMContentLoaded', function() {
    showToast('success', @json(session('success')), 4000);
});
</script>
@endif
@if(session('error'))
<script>
document.addEventListener('DOMContentLoaded', function() {
    showToast('error', @json(session('error')), 5000);
});
</script>
@endif
@if(session('info'))
<script>
document.addEventListener('DOMContentLoaded', function() {
    showToast('info', @json(session('info')), 4000);
});
</script>
@endif
@if(session('warning'))
<script>
document.addEventListener('DOMContentLoaded', function() {
    showToast('warning', @json(session('warning')), 4500);
});
</script>
@endif
</body>
</html>
