<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code — {{ $asset->barang?->nama_barang ?? $asset->kode_aset }}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { font-family: 'Inter', Arial, sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: #f1f5f9;
            min-height: 100vh;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            padding: 20px;
        }
        .label-card {
            background: #fff;
            border: 2px solid #1e3a8a;
            border-radius: 14px;
            padding: 24px 28px;
            text-align: center;
            width: 280px;
            box-shadow: 0 8px 24px rgba(30,58,138,.12);
        }
        .label-header {
            display: flex; align-items: center; justify-content: center; gap: 8px;
            margin-bottom: 16px; padding-bottom: 12px;
            border-bottom: 1px solid #e2e8f0;
        }
        .label-header img { height: 28px; object-fit: contain; }
        .label-header span { font-size: 13px; font-weight: 800; color: #1e3a8a; text-transform: uppercase; letter-spacing: .08em; }
        .qr-wrapper { margin: 4px 0 16px; }
        .qr-wrapper svg { width: 160px; height: 160px; }
        .asset-kode { font-size: 18px; font-weight: 800; color: #1d4ed8; font-family: monospace; margin-bottom: 4px; }
        .asset-nama { font-size: 13px; color: #374151; font-weight: 600; margin-bottom: 3px; }
        .asset-ruangan { font-size: 11px; color: #6b7280; }
        .label-footer { margin-top: 14px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 10px; color: #94a3b8; }

        .actions {
            margin-top: 20px; display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;
        }
        .btn {
            padding: 10px 22px; border: none; border-radius: 8px;
            cursor: pointer; font-size: 13px; font-weight: 700;
            text-decoration: none; color: white; display: inline-flex; align-items: center; gap: 6px;
            transition: .2s;
        }
        .btn-print { background: #1d4ed8; }
        .btn-print:hover { background: #1e40af; }
        .btn-close { background: #6b7280; }
        .btn-close:hover { background: #4b5563; }

        @media print {
            body { background: none; padding: 0; display: block; }
            .label-card { box-shadow: none; width: 7cm; margin: 0; page-break-inside: avoid; border: 2px solid #000; }
            .actions { display: none; }
        }
    </style>
</head>
<body>
    <div class="label-card">
        <div class="label-header">
            <img src="{{ asset('logoweb.png') }}" alt="RBTV" onerror="this.style.display='none'">
            <span>RBTV Bengkulu</span>
        </div>
        <div class="qr-wrapper">{!! $qrCode !!}</div>
        <div class="asset-kode">{{ $asset->kode_aset }}</div>
        <div class="asset-nama">{{ $asset->barang?->nama_barang ?? '—' }}</div>
        <div class="asset-ruangan">📍 {{ $asset->ruangan?->nama_ruangan ?? '—' }}</div>
        <div class="label-footer">Scan untuk melihat detail aset · SimAset v1.0</div>
    </div>

    <div class="actions">
        <button onclick="window.print()" class="btn btn-print">🖨️ Cetak / Simpan PDF</button>
        <button onclick="window.close()" class="btn btn-close">✕ Tutup</button>
    </div>

    @if($autoPrint)
    <script>
        window.onload = function() { setTimeout(function() { window.print(); }, 600); };
    </script>
    @endif
</body>
</html>

