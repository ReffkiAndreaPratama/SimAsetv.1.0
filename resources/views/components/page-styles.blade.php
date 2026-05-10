<style>
/* ═══════════════════════════════════════════════════════════════
   SimAset — Shared Page Styles
   Dipakai di semua halaman index, show, create, edit
   ═══════════════════════════════════════════════════════════════ */

/* ── Page Hero (index pages) ── */
.page-hero {
    background: linear-gradient(135deg, #0d1f4e 0%, #1a3470 40%, #1c3d9e 75%, #1e45b8 100%);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 20px;
    color: #fff;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    box-shadow: 0 6px 24px rgba(13,31,78,.22);
}
.page-hero::before {
    content: '';
    position: absolute;
    top: -50px; right: -50px;
    width: 200px; height: 200px;
    background: rgba(255,255,255,.05);
    border-radius: 50%;
    pointer-events: none;
}
.page-hero::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #b91c1c, #ef4444, rgba(255,255,255,.1));
}
.page-hero-left { position: relative; z-index: 2; }
.page-hero-right { position: relative; z-index: 2; display: flex; gap: 10px; flex-wrap: wrap; }
.page-hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 3px 12px;
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 20px;
    font-size: .68rem; font-weight: 600; color: rgba(255,255,255,.9);
    margin-bottom: 8px; letter-spacing: .04em;
}
.page-hero-title { font-size: 1.35rem; font-weight: 800; color: #fff; margin: 0 0 4px; letter-spacing: -.02em; }
.page-hero-sub   { font-size: .82rem; color: rgba(255,255,255,.75); margin: 0; }

/* ── Stats Grid ── */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 14px;
    margin-bottom: 18px;
}
.stat-card {
    background: #fff;
    border-radius: 14px;
    padding: 18px 20px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 4px rgba(0,0,0,.04);
    display: flex;
    align-items: center;
    gap: 14px;
    transition: all .2s;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.07); }
.stat-icon {
    width: 44px; height: 44px;
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; flex-shrink: 0;
}
.stat-label { font-size: .7rem; font-weight: 700; color: #6B7280; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 2px; }
.stat-val   { font-size: 1.7rem; font-weight: 800; color: #111827; line-height: 1.1; }
.stat-sub   { font-size: .72rem; color: #9CA3AF; margin-top: 1px; }

/* ── Filter Bar ── */
.filter-bar {
    background: #fff;
    border-radius: 12px;
    padding: 14px 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 4px rgba(0,0,0,.04);
    margin-bottom: 18px;
}
.filter-bar form {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: flex-end;
}
.filter-group { display: flex; flex-direction: column; flex: 1; min-width: 140px; }
.filter-group.wide { flex: 2; min-width: 200px; }
.filter-label {
    font-size: .68rem; font-weight: 700; color: #6B7280;
    text-transform: uppercase; letter-spacing: .05em;
    margin-bottom: 4px; display: block;
}
.filter-input, .filter-select {
    width: 100%; padding: 8px 12px;
    border-radius: 8px; border: 1px solid #E2E8F0;
    font-size: .85rem; color: #374151;
    background: #fff; outline: none;
    height: 38px; transition: border-color .15s;
}
.filter-input:focus, .filter-select:focus {
    border-color: #3B82F6;
    box-shadow: 0 0 0 3px rgba(59,130,246,.1);
}
.filter-actions { display: flex; gap: 8px; align-items: flex-end; flex-shrink: 0; }

/* ── Table Card ── */
.table-card {
    background: #fff;
    border-radius: 14px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 4px rgba(0,0,0,.04);
    overflow: hidden;
}
.table-card-header {
    padding: 14px 20px;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid #F3F4F6;
}
.table-card-title {
    font-size: .95rem; font-weight: 700; color: #111827;
    margin: 0; display: flex; align-items: center; gap: 8px;
}
.table-card-title i { color: #3B82F6; }
.table-card-meta { font-size: .78rem; color: #9CA3AF; }

/* ── Data Table ── */
.data-table { width: 100%; border-collapse: collapse; }
.data-table thead th {
    text-align: left; font-size: .67rem; font-weight: 700;
    padding: 10px 16px; color: #6B7280;
    border-bottom: 1px solid #E5E7EB;
    background: #F9FAFB; white-space: nowrap;
    text-transform: uppercase; letter-spacing: .06em;
}
.data-table tbody td {
    padding: 13px 16px; border-bottom: 1px solid #F3F4F6;
    font-size: .875rem; color: #374151; vertical-align: middle;
}
.data-table tbody tr:last-child td { border-bottom: none; }
.data-table tbody tr:hover td { background: #F8FAFC; }

/* ── Pagination Bar ── */
.pagi-bar {
    padding: 12px 20px;
    border-top: 1px solid #F3F4F6;
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 8px;
    background: #FAFAFA;
}
.pagi-info { font-size: .8rem; color: #6B7280; }

/* ── Chips & Badges ── */
.kode-chip {
    display: inline-flex; align-items: center;
    padding: 3px 9px;
    background: #EFF6FF; border: 1px solid #BFDBFE;
    border-radius: 6px; font-family: monospace;
    font-size: .78rem; font-weight: 700; color: #1D4ED8;
}
.kode-chip-sm {
    display: inline-flex; align-items: center;
    padding: 2px 7px;
    background: #EFF6FF; border: 1px solid #BFDBFE;
    border-radius: 5px; font-family: monospace;
    font-size: .72rem; font-weight: 700; color: #1D4ED8;
}
.cat-chip {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 3px 9px;
    background: #F1F5F9; border: 1px solid #E2E8F0;
    border-radius: 6px; font-size: .75rem; font-weight: 600; color: #475569;
}
.status-pill {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 4px 10px; border-radius: 20px;
    font-size: .72rem; font-weight: 600;
}
.pill-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
.pill-aktif      { background: #ECFDF5; color: #059669; border: 1px solid rgba(16,185,129,.2); }
.pill-nonaktif   { background: #F9FAFB; color: #6B7280; border: 1px solid #E5E7EB; }
.pill-maintenance{ background: #ECFEFF; color: #0E7490; border: 1px solid rgba(6,182,212,.2); }
.pill-baik       { background: #ECFDF5; color: #059669; border: 1px solid rgba(16,185,129,.2); }
.pill-rusak-r    { background: #FFFBEB; color: #D97706; border: 1px solid rgba(245,158,11,.2); }
.pill-rusak-b    { background: #FEF2F2; color: #DC2626; border: 1px solid rgba(220,38,38,.2); }

/* ── Action Buttons (table) ── */
.act-group { display: flex; gap: 5px; align-items: center; justify-content: flex-end; }
.act-btn {
    width: 30px; height: 30px; border-radius: 7px;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: .75rem; text-decoration: none; border: none; cursor: pointer;
    transition: all .15s;
}
.act-btn:hover { transform: translateY(-1px); filter: brightness(.88); }
.act-view { background: #EFF6FF; color: #2563EB; }
.act-edit { background: #FFFBEB; color: #D97706; }
.act-del  { background: #FEF2F2; color: #DC2626; }
.act-qr   { background: #ECFEFF; color: #0E7490; }

/* ── Empty State ── */
.empty-state { text-align: center; padding: 56px 20px; }
.empty-state .empty-icon { font-size: 3rem; color: #BFDBFE; display: block; margin-bottom: 14px; }
.empty-state h4 { font-size: .95rem; font-weight: 700; color: #111827; margin-bottom: 6px; }
.empty-state p  { font-size: .82rem; color: #9CA3AF; margin-bottom: 16px; }

/* ── Detail Page Hero ── */
.detail-hero {
    background: linear-gradient(135deg, #0d1f4e 0%, #1a3470 40%, #1c3d9e 75%, #1e45b8 100%);
    border-radius: 16px;
    padding: 26px 32px;
    margin-bottom: 22px;
    color: #fff;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    box-shadow: 0 6px 24px rgba(13,31,78,.22);
}
.detail-hero::before { content:''; position:absolute; top:-30px; right:-30px; width:160px; height:160px; background:rgba(255,255,255,.05); border-radius:50%; pointer-events:none; }
.detail-hero::after  { content:''; position:absolute; bottom:0; left:0; right:0; height:3px; background:linear-gradient(90deg,#dc2626,#ef4444,rgba(255,255,255,.1)); }
.detail-hero-left  { position: relative; z-index: 2; }
.detail-hero-right { position: relative; z-index: 2; display: flex; gap: 8px; flex-wrap: wrap; }
.detail-hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 3px 12px;
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 20px;
    font-size: .68rem; font-weight: 600; color: rgba(255,255,255,.9);
    margin-bottom: 8px;
}
.detail-hero-title { font-size: 1.25rem; font-weight: 800; color: #fff; margin: 0 0 4px; letter-spacing: -.02em; }
.detail-hero-sub   { font-size: .82rem; color: rgba(255,255,255,.75); margin: 0; }
.kode-chip-white {
    display: inline-flex; align-items: center;
    padding: 2px 9px;
    background: rgba(255,255,255,.2);
    border: 1px solid rgba(255,255,255,.3);
    border-radius: 5px; font-family: monospace;
    font-size: .78rem; font-weight: 700; color: #fff;
}

/* ── Detail Card ── */
.detail-card {
    background: #fff;
    border: 1px solid #E5E7EB;
    border-radius: 14px;
    box-shadow: 0 1px 4px rgba(0,0,0,.04);
    overflow: hidden;
    margin-bottom: 16px;
}
.detail-card-header {
    padding: 13px 20px;
    background: #FAFAFA;
    border-bottom: 1px solid #F3F4F6;
    display: flex; align-items: center; gap: 10px;
}
.detail-card-icon {
    width: 30px; height: 30px; border-radius: 7px;
    display: flex; align-items: center; justify-content: center;
    font-size: .8rem;
    background: var(--ic-bg, rgba(29,78,216,.1));
    color: var(--ic-color, #1d4ed8);
    flex-shrink: 0;
}
.detail-card-title {
    font-size: .72rem; font-weight: 700; color: #374151;
    text-transform: uppercase; letter-spacing: .07em; margin: 0;
}
.detail-card-badge {
    margin-left: auto;
    font-size: .68rem; color: #9CA3AF;
    background: #F3F4F6; border: 1px solid #E5E7EB;
    border-radius: 4px; padding: 2px 8px; font-weight: 600;
}

/* ── Info Rows (detail page) ── */
.info-row {
    display: flex; align-items: baseline;
    padding: 11px 20px;
    border-bottom: 1px solid #F9FAFB;
    gap: 14px;
}
.info-row:last-child { border-bottom: none; }
.info-row:hover { background: #FAFAFA; }
.info-label { font-size: .78rem; font-weight: 600; color: #6B7280; min-width: 150px; flex-shrink: 0; }
.info-value { font-size: .875rem; color: #111827; flex: 1; }

/* ── Sys Rows ── */
.sys-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 10px 20px;
    border-bottom: 1px solid #F9FAFB;
    gap: 10px;
}
.sys-row:last-child { border-bottom: none; }
.sys-label { font-size: .76rem; color: #6B7280; font-weight: 500; }
.sys-value { font-size: .8rem; font-weight: 600; color: #374151; text-align: right; }

/* ── Foto Placeholder ── */
.foto-placeholder {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 32px 20px;
    background: #F9FAFB; border-radius: 10px;
    border: 2px dashed #E5E7EB; color: #9CA3AF; gap: 8px;
}

/* ── Responsive ── */
@media (max-width: 1024px) {
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
    .page-hero { flex-direction: column; align-items: flex-start; }
    .filter-bar form { flex-direction: column; }
    .filter-group, .filter-group.wide { min-width: 100%; }
    .stats-grid { grid-template-columns: 1fr 1fr; gap: 10px; }
    .detail-hero { flex-direction: column; align-items: flex-start; }
    .info-label { min-width: 110px; }
}
@media (max-width: 480px) {
    .stats-grid { grid-template-columns: 1fr; }
    .info-row { flex-direction: column; gap: 3px; }
}
</style>

<style>
/* ── Bulk Select / Checkbox ── */
.bulk-checkbox {
    width: 16px; height: 16px;
    border-radius: 4px; border: 1.5px solid #CBD5E1;
    cursor: pointer; accent-color: #3B82F6;
    flex-shrink: 0;
}
.bulk-checkbox:checked { accent-color: #3B82F6; }

/* Bulk action bar */
.bulk-bar {
    display: none;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    background: #EFF6FF;
    border-bottom: 1px solid #BFDBFE;
    flex-wrap: wrap;
}
.bulk-bar.show { display: flex; }
.bulk-bar-info { font-size: .82rem; font-weight: 600; color: #1D4ED8; }
.bulk-bar-actions { display: flex; gap: 8px; margin-left: auto; }
.bulk-btn {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 6px 14px; border-radius: 8px; border: none;
    font-size: .78rem; font-weight: 600; cursor: pointer; transition: all .15s;
    text-decoration: none;
}
.bulk-btn:hover { transform: translateY(-1px); filter: brightness(.92); }
.bulk-btn-danger  { background: #FEF2F2; color: #DC2626; border: 1px solid #FECACA; }
.bulk-btn-qr      { background: #ECFEFF; color: #0E7490; border: 1px solid rgba(6,182,212,.2); }
.bulk-btn-export  { background: #ECFDF5; color: #059669; border: 1px solid rgba(16,185,129,.2); }
</style>
