<style>
/* ══════════════════════════════════════
   Shared Form Page Styles — SimAset
   Dipakai di: create/edit aset, barang, ruangan, user
══════════════════════════════════════ */

/* ── Page Hero Mini ── */
.page-hero-mini {
    background: linear-gradient(135deg, #0d1f4e 0%, #1a3470 40%, #1c3d9e 75%, #1e45b8 100%);
    border-radius: 16px;
    padding: 26px 32px;
    margin-bottom: 22px;
    color: #fff;
    position: relative;
    overflow: hidden;
    box-shadow: 0 6px 24px rgba(13,31,78,.28);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
}
.page-hero-mini::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: rgba(255,255,255,.05);
    border-radius: 50%;
    pointer-events: none;
}
.page-hero-mini::after {
    content: '';
    position: absolute;
    bottom: -50px; left: -30px;
    width: 220px; height: 220px;
    background: rgba(185,28,28,.1);
    border-radius: 50%;
    pointer-events: none;
}
.hero-accent-bar {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #dc2626, #ef4444, rgba(255,255,255,.1));
}
.hero-mini-left { position: relative; z-index: 2; }
.hero-mini-right { position: relative; z-index: 2; }

.hero-mini-badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 4px 12px;
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 20px;
    font-size: .7rem; font-weight: 600; color: #fff;
    margin-bottom: 10px;
    backdrop-filter: blur(4px);
    letter-spacing: .04em;
}
.hero-mini-title {
    font-size: 1.3rem; font-weight: 800; color: #fff;
    margin: 0 0 5px; letter-spacing: -.02em;
    text-shadow: 0 2px 8px rgba(0,0,0,.15);
}
.hero-mini-sub { font-size: .82rem; color: rgba(255,255,255,.75); margin: 0; }
.kode-chip-white {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 3px 10px;
    background: rgba(255,255,255,.2);
    border: 1px solid rgba(255,255,255,.3);
    border-radius: 6px;
    font-family: 'Fira Code', monospace;
    font-size: .78rem; font-weight: 600; color: #fff;
}

/* ── Form Card ── */
.form-card {
    background: #fff;
    border: 1px solid #E5E7EB;
    border-radius: 14px;
    box-shadow: 0 1px 4px rgba(0,0,0,.04);
    overflow: hidden;
    margin-bottom: 16px;
    transition: box-shadow .2s;
}
.form-card:focus-within {
    box-shadow: 0 4px 16px rgba(59,130,246,.08);
    border-color: #BFDBFE;
}
.form-card-header {
    padding: 14px 22px;
    background: #FAFAFA;
    border-bottom: 1px solid #F3F4F6;
    display: flex; align-items: center; gap: 10px;
}
.form-card-header-icon {
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: .82rem;
    background: var(--ic-bg, rgba(29,78,216,.1));
    color: var(--ic-color, #1d4ed8);
    flex-shrink: 0;
}
.form-card-header-title {
    font-size: .72rem; font-weight: 700; color: #374151;
    text-transform: uppercase; letter-spacing: .07em; margin: 0;
}
.form-card-header-badge {
    margin-left: auto;
    font-size: .68rem; color: #9CA3AF;
    background: #F3F4F6; border: 1px solid #E5E7EB;
    border-radius: 4px; padding: 2px 8px; font-weight: 600;
}
.form-card-body { padding: 22px 24px; }

/* ── Field styles ── */
.field-label {
    font-size: .8rem; font-weight: 600; color: #374151;
    margin-bottom: 6px; display: block;
}
.field-label .req { color: #DC2626; margin-left: 2px; }
.field-hint {
    font-size: .72rem; color: #9CA3AF;
    margin-top: 5px; display: flex; align-items: center; gap: 5px;
}

/* Input group icon */
.input-group-text {
    background: #F9FAFB !important;
    border-color: #D1D5DB !important;
    color: #6B7280;
    min-width: 42px;
    justify-content: center;
    font-size: .85rem;
}

/* Override Bootstrap form-control for consistency */
.form-card .form-control,
.form-card .form-select {
    border-color: #D1D5DB;
    border-radius: 8px;
    padding: 9px 12px;
    font-size: .875rem;
    min-height: 42px;
    background: #fff;
    color: #111827;
    transition: border-color .15s, box-shadow .15s;
}
.form-card .form-control:focus,
.form-card .form-select:focus {
    border-color: #3B82F6;
    box-shadow: 0 0 0 3px rgba(59,130,246,.1);
    outline: none;
}
.form-card .input-group .form-control,
.form-card .input-group .form-select {
    border-radius: 0 8px 8px 0;
}
.form-card .input-group .input-group-text {
    border-radius: 8px 0 0 8px;
}

/* ── Foto preview ── */
.foto-preview-box {
    width: 100%; height: 110px;
    background: #F9FAFB;
    border: 2px dashed #E5E7EB;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    color: #9CA3AF; font-size: .82rem; overflow: hidden;
    transition: border-color .2s;
}
.foto-preview-box:hover { border-color: #93C5FD; }

/* ── Action footer ── */
.form-actions {
    display: flex; justify-content: flex-end; align-items: center;
    gap: 10px; padding: 6px 0 10px;
}
.form-actions .btn { min-height: 42px; font-size: .875rem; }

/* ── Responsive ── */
@media (max-width: 640px) {
    .page-hero-mini { padding: 20px; }
    .hero-mini-title { font-size: 1.1rem; }
    .form-card-body { padding: 16px; }
    .form-actions { flex-direction: column-reverse; }
    .form-actions .btn { width: 100%; justify-content: center; }
}
</style>
