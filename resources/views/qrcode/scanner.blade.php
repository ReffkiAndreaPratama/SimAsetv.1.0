@extends('layouts.app')
@section('title', 'QR Scanner')
@push('styles')
@include('components.page-styles')
<style>
/* Scanner specific */
.scanner-area {
    width: 100%; background: #1e293b; border-radius: 12px;
    overflow: hidden; position: relative; margin-bottom: 14px;
    min-height: 220px; display: flex; align-items: center; justify-content: center;
}
#scannerVideo { width: 100%; display: block; }
.scanner-placeholder {
    position: absolute; inset: 0;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: #64748b; gap: 10px; background: #1e293b;
}
.scanner-placeholder i { font-size: 52px; color: #334155; }
.scanner-placeholder span { font-size: 13px; color: #64748b; }
.scan-frame { position: absolute; inset: 0; pointer-events: none; display: none; }
.scan-frame::before {
    content: ''; position: absolute; inset: 18%;
    border: 2px solid #06b6d4; border-radius: 10px;
    box-shadow: 0 0 0 9999px rgba(0,0,0,.55);
}
.scan-line {
    position: absolute; left: 18%; right: 18%; height: 2px;
    background: #06b6d4; box-shadow: 0 0 10px #06b6d4;
    animation: scanAnim 2s linear infinite; display: none;
}
@keyframes scanAnim {
    0%   { top: 18%; opacity: 0; }
    5%   { opacity: 1; }
    95%  { opacity: 1; }
    100% { top: 82%; opacity: 0; }
}
.or-div { display: flex; align-items: center; gap: 10px; margin: 14px 0; color: #9ca3af; font-size: 12px; }
.or-div::before, .or-div::after { content: ''; flex: 1; height: 1px; background: #e5e7eb; }
.scan-input { width: 100%; padding: 9px 12px; border-radius: 8px; border: 1px solid #e5e7eb; font-size: 13px; color: #374151; outline: none; transition: border-color .15s; }
.scan-input:focus { border-color: #2563eb; box-shadow: 0 0 0 3px rgba(37,99,235,.1); }
#statusBar { font-size: 12px; color: #6b7280; text-align: center; padding: 6px 0; min-height: 24px; }
#statusBar.ok  { color: #059669; }
#statusBar.err { color: #dc2626; }
.result-area { min-height: 280px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.result-empty { text-align: center; color: #9ca3af; padding: 20px; }
.result-empty i { font-size: 44px; color: #e2e8f0; display: block; margin-bottom: 12px; }
.result-empty h5 { font-size: 15px; font-weight: 600; color: #374151; margin-bottom: 6px; }
.result-empty p  { font-size: 13px; margin: 0; }
.result-found { width: 100%; border: 1px solid #e5e7eb; border-radius: 10px; overflow: hidden; }
.result-found-top { padding: 12px 16px; background: #ecfdf5; border-bottom: 1px solid #d1fae5; display: flex; align-items: center; gap: 8px; }
.result-found-top i { color: #059669; font-size: 16px; }
.result-found-top span { font-size: 13px; font-weight: 600; color: #065f46; }
.result-row { display: flex; justify-content: space-between; align-items: center; padding: 9px 16px; border-bottom: 1px solid #f3f4f6; gap: 10px; }
.result-row:last-child { border-bottom: none; }
.result-key { font-size: 12px; color: #6b7280; }
.result-val { font-size: 13px; color: #111827; font-weight: 600; text-align: right; }
.loading-wrap { text-align: center; padding: 30px; }
.spinner { width: 34px; height: 34px; border-radius: 50%; border: 3px solid #e5e7eb; border-top-color: #2563eb; animation: spin .7s linear infinite; margin: 0 auto 12px; }
@keyframes spin { to { transform: rotate(360deg); } }
</style>
@endpush

@section('content')
<div class="page-container">

    {{-- Hero --}}
    <div class="page-hero">
        <div class="page-hero-left">
            <div class="page-hero-badge"><i class="fas fa-qrcode"></i> QR Code</div>
            <h1 class="page-hero-title">QR Code Scanner</h1>
            <p class="page-hero-sub">Pindai QR code, upload gambar, atau masukkan kode aset secara manual</p>
        </div>
        <div class="page-hero-right">
            <a href="{{ route('aset.index') }}" class="btn btn-light border d-flex align-items-center gap-2" style="font-size:.85rem;">
                <i class="fas fa-arrow-left"></i> Kembali ke Aset
            </a>
        </div>
    </div>

    <div class="row g-3">

        {{-- Kolom Kiri: Scanner --}}
        <div class="col-lg-6">
            <div class="detail-card" style="height:100%;">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(59,130,246,.1);--ic-color:#2563EB;"><i class="fas fa-camera"></i></div>
                    <h2 class="detail-card-title">Area Pindai</h2>
                </div>
                <div style="padding:20px;">

                    <div class="scanner-area" id="scannerArea">
                        <video id="scannerVideo" autoplay playsinline muted></video>
                        <div class="scanner-placeholder" id="scannerPlaceholder">
                            <i class="fas fa-qrcode"></i>
                            <span>Kamera akan tampil di sini</span>
                        </div>
                        <div class="scan-frame" id="scanFrame"></div>
                        <div class="scan-line" id="scanLine"></div>
                    </div>
                    <canvas id="scanCanvas" style="display:none;"></canvas>
                    <div id="statusBar"></div>

                    <div style="display:flex;gap:8px;margin-bottom:14px;">
                        <button id="btnStart" onclick="startCamera()" class="btn btn-primary d-flex align-items-center gap-1" style="flex:1;justify-content:center;font-size:.85rem;">
                            <i class="fas fa-camera"></i> Buka Kamera
                        </button>
                        <button id="btnStop" onclick="stopCamera()" class="btn btn-danger d-flex align-items-center gap-1" style="flex:1;justify-content:center;font-size:.85rem;display:none!important;">
                            <i class="fas fa-stop-circle"></i> Hentikan
                        </button>
                    </div>

                    <div class="or-div">ATAU</div>

                    <div style="margin-bottom:14px;">
                        <label style="font-size:.72rem;font-weight:700;color:#6B7280;text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:5px;">Upload Foto QR Code</label>
                        <input type="file" id="qrFile" accept="image/*" class="scan-input" onchange="scanUpload()">
                        <div style="font-size:.7rem;color:#9ca3af;margin-top:4px;">Pilih gambar QR code untuk dipindai otomatis</div>
                    </div>

                    <div class="or-div">ATAU</div>

                    <div>
                        <label style="font-size:.72rem;font-weight:700;color:#6B7280;text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:5px;">Masukkan Kode Aset Manual</label>
                        <div style="display:flex;gap:8px;">
                            <input type="text" id="manualInput" class="scan-input" style="flex:1;"
                                placeholder="Contoh: AST-001"
                                onkeydown="if(event.key==='Enter'){event.preventDefault();searchManual();}">
                            <button onclick="searchManual()" class="btn btn-primary d-flex align-items-center gap-1" style="white-space:nowrap;font-size:.85rem;">
                                <i class="fas fa-search"></i> Cari
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        {{-- Kolom Kanan: Hasil --}}
        <div class="col-lg-6">
            <div class="detail-card" style="height:100%;">
                <div class="detail-card-header">
                    <div class="detail-card-icon" style="--ic-bg:rgba(16,185,129,.1);--ic-color:#10B981;"><i class="fas fa-box-open"></i></div>
                    <h2 class="detail-card-title">Hasil Pencarian</h2>
                </div>
                <div style="padding:20px;">
                    <div class="result-area" id="resultArea">
                        <div class="result-empty">
                            <i class="fas fa-search-location"></i>
                            <h5>Belum Ada Hasil</h5>
                            <p>Gunakan salah satu metode di kiri untuk mencari aset.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.min.js"></script>

@push('scripts')
<script>
const video       = document.getElementById('scannerVideo');
const canvas      = document.getElementById('scanCanvas');
const scanFrame   = document.getElementById('scanFrame');
const scanLine    = document.getElementById('scanLine');
const placeholder = document.getElementById('scannerPlaceholder');
const resultArea  = document.getElementById('resultArea');
const statusBar   = document.getElementById('statusBar');
let scanning = false, stream = null, rafId = null;

function setStatus(msg, type = '') { statusBar.textContent = msg; statusBar.className = type; }

async function startCamera() {
    setStatus('Meminta izin kamera...', '');
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        setStatus('Browser tidak mendukung akses kamera.', 'err');
        showError('Browser ini tidak mendukung akses kamera. Gunakan Chrome/Firefox terbaru.');
        return;
    }
    try {
        try { stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: { ideal: 'environment' } } }); }
        catch { stream = await navigator.mediaDevices.getUserMedia({ video: true }); }
        video.srcObject = stream;
        await video.play();
        placeholder.style.display = 'none';
        scanFrame.style.display = 'block';
        scanLine.style.display = 'block';
        document.getElementById('btnStart').style.display = 'none';
        document.getElementById('btnStop').style.display = 'flex';
        scanning = true;
        setStatus('Kamera aktif — arahkan ke QR code', 'ok');
        rafId = requestAnimationFrame(scanFrame_loop);
    } catch (err) {
        let msg = 'Gagal membuka kamera.';
        if (err.name === 'NotAllowedError')  msg = 'Izin kamera ditolak.';
        if (err.name === 'NotFoundError')    msg = 'Kamera tidak ditemukan.';
        if (err.name === 'NotReadableError') msg = 'Kamera sedang digunakan aplikasi lain.';
        setStatus(msg, 'err'); showError(msg);
    }
}

function stopCamera() {
    scanning = false;
    if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
    if (stream) { stream.getTracks().forEach(t => t.stop()); stream = null; }
    video.srcObject = null;
    placeholder.style.display = 'flex';
    scanFrame.style.display = 'none';
    scanLine.style.display = 'none';
    document.getElementById('btnStart').style.display = 'flex';
    document.getElementById('btnStop').style.display = 'none';
    setStatus('', '');
}

function scanFrame_loop() {
    if (!scanning) return;
    if (video.readyState === video.HAVE_ENOUGH_DATA && video.videoWidth > 0) {
        const ctx = canvas.getContext('2d');
        canvas.width = video.videoWidth; canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0);
        try {
            const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const code = jsQR(imgData.data, imgData.width, imgData.height, { inversionAttempts: 'dontInvert' });
            if (code && code.data) { stopCamera(); setStatus('QR terdeteksi!', 'ok'); handleQrData(code.data); return; }
        } catch (e) {}
    }
    rafId = requestAnimationFrame(scanFrame_loop);
}

function scanUpload() {
    const file = document.getElementById('qrFile').files[0];
    if (!file) return;
    setStatus('Memproses gambar...', '');
    showLoading('gambar');
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
            const c = document.createElement('canvas');
            c.width = img.width; c.height = img.height;
            const ctx = c.getContext('2d');
            ctx.drawImage(img, 0, 0);
            try {
                const imgData = ctx.getImageData(0, 0, c.width, c.height);
                const code = jsQR(imgData.data, imgData.width, imgData.height, { inversionAttempts: 'attemptBoth' });
                if (code && code.data) { setStatus('QR terdeteksi dari gambar', 'ok'); handleQrData(code.data); }
                else { setStatus('QR tidak terdeteksi', 'err'); showError('QR code tidak terdeteksi. Pastikan gambar jelas.'); }
            } catch (err) { setStatus('Gagal memproses gambar', 'err'); showError('Gagal: ' + err.message); }
        };
        img.onerror = () => showError('Gagal memuat gambar.');
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}

function searchManual() {
    const code = document.getElementById('manualInput').value.trim();
    if (!code) { setStatus('Masukkan kode aset terlebih dahulu', 'err'); return; }
    doSearch(code);
}

function handleQrData(raw) {
    const m = raw.match(/\/aset\/([A-Za-z0-9\-]+)/);
    if (m && m[1]) { doSearch(m[1]); return; }
    doSearch(raw.trim());
}

function doSearch(code) {
    setStatus('Mencari aset: ' + code, '');
    showLoading(code);
    fetch('/qrcode/search?code=' + encodeURIComponent(code), { headers: { 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json' } })
    .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
    .then(data => {
        if (data.success && data.data) { setStatus('Aset ditemukan!', 'ok'); showResult(data.data); }
        else { setStatus('Aset tidak ditemukan', 'err'); showNotFound(code); }
    })
    .catch(err => { setStatus('Error: ' + err.message, 'err'); showError('Gagal menghubungi server. Pastikan Anda sudah login.'); });
}

function showLoading(code) {
    resultArea.innerHTML = '<div class="loading-wrap"><div class="spinner"></div><div style="font-size:13px;color:#6b7280;">Mencari <strong>' + escHtml(code) + '</strong>...</div></div>';
}
function showNotFound(code) {
    resultArea.innerHTML = '<div class="result-empty"><i class="fas fa-exclamation-triangle" style="color:#fbbf24;"></i><h5>Aset Tidak Ditemukan</h5><p>Tidak ada aset dengan kode <strong>' + escHtml(code) + '</strong>.</p></div>';
}
function showError(msg) {
    resultArea.innerHTML = '<div class="result-empty"><i class="fas fa-times-circle" style="color:#ef4444;"></i><h5>Terjadi Kesalahan</h5><p>' + escHtml(msg) + '</p></div>';
}
function showResult(d) {
    const kb = { 'Baik': '<span class="status-pill pill-baik" style="font-size:.7rem;padding:2px 8px;"><span class="pill-dot"></span> Baik</span>', 'Rusak Ringan': '<span class="status-pill pill-rusak-r" style="font-size:.7rem;padding:2px 8px;"><span class="pill-dot"></span> Rusak Ringan</span>', 'Rusak Berat': '<span class="status-pill pill-rusak-b" style="font-size:.7rem;padding:2px 8px;"><span class="pill-dot"></span> Rusak Berat</span>' };
    const sb = { 'Aktif': '<span class="status-pill pill-aktif" style="font-size:.7rem;padding:2px 8px;"><span class="pill-dot"></span> Aktif</span>', 'Maintenance': '<span class="status-pill pill-maintenance" style="font-size:.7rem;padding:2px 8px;"><span class="pill-dot"></span> Maintenance</span>', 'Non-Aktif': '<span class="status-pill pill-nonaktif" style="font-size:.7rem;padding:2px 8px;"><span class="pill-dot"></span> Non-Aktif</span>' };
    const rows = [
        ['Kode Aset', '<span class="kode-chip">' + escHtml(d.kode_aset || '—') + '</span>'],
        ['Nama Barang', escHtml(d.nama_barang || '—')],
        ['Kategori', escHtml(d.kategori || '—')],
        ['Ruangan', '<i class="fas fa-map-marker-alt" style="color:#93c5fd;font-size:.65rem;margin-right:3px;"></i>' + escHtml(d.ruangan || '—')],
        ['Kondisi', kb[d.kondisi] || escHtml(d.kondisi || '—')],
        ['Status', sb[d.status] || escHtml(d.status || '—')],
        ['Jumlah', escHtml(String(d.jumlah || '—')) + ' unit'],
    ];
    let rowsHtml = rows.map(r => '<div class="result-row"><span class="result-key">' + r[0] + '</span><span class="result-val">' + r[1] + '</span></div>').join('');
    resultArea.innerHTML = '<div class="result-found" style="width:100%;"><div class="result-found-top"><i class="fas fa-check-circle"></i><span>Aset Ditemukan</span></div>' + rowsHtml + '<div style="padding:12px 16px;"><a href="' + escHtml(d.url) + '" class="btn btn-primary d-flex align-items-center justify-content-center gap-2" style="font-size:.85rem;"><i class="fas fa-eye"></i> Lihat Detail Lengkap</a></div></div>';
}
function escHtml(str) { return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
</script>
@endpush
@endsection
