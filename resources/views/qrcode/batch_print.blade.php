<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cetak Label QR — SimAset RBTV</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f0f0f0; }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(6cm, 1fr));
            gap: 15px; max-width: 21cm; margin: 0 auto;
            background: white; padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,.1);
        }
        .label-card {
            border: 2px solid #1e3a8a; border-radius: 8px;
            padding: 10px; text-align: center;
            page-break-inside: avoid; background: #fff;
        }
        .qr-wrapper { margin: 8px 0; }
        .qr-wrapper svg { width: 100px; height: 100px; }
        .company-name {
            font-size: 12px; font-weight: bold; margin-bottom: 5px;
            border-bottom: 1px solid #ccc; padding-bottom: 5px;
            color: #1e3a8a; text-transform: uppercase; letter-spacing: .05em;
        }
        .asset-kode { font-size: 15px; font-weight: bold; margin: 5px 0; color: #1d4ed8; font-family: monospace; }
        .asset-nama { font-size: 11px; color: #374151; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .asset-ruangan { font-size: 10px; color: #6b7280; margin-top: 3px; }
        .print-btn {
            display: block; margin: 20px auto; padding: 10px 30px;
            background: #1d4ed8; color: white; border: none;
            border-radius: 5px; font-size: 15px; cursor: pointer;
        }
        .print-btn:hover { background: #1e40af; }
        @media print {
            body { background: none; padding: 0; }
            .container { box-shadow: none; padding: 0; width: 100%; max-width: none; grid-template-columns: repeat(3, 1fr); gap: 10px; }
            .print-btn { display: none; }
        }
    </style>
</head>
<body>
    <button onclick="window.print()" class="print-btn">🖨️ Cetak Sekarang (Ctrl+P)</button>
    <div class="container">
        @foreach($assets as $asset)
        <div class="label-card">
            <div class="company-name">SimAset · RBTV Bengkulu</div>
            <div class="qr-wrapper">
                {!! $qrcodes[$asset->kode_aset] ?? '' !!}
            </div>
            <div class="asset-kode">{{ $asset->kode_aset }}</div>
            <div class="asset-nama">{{ $asset->barang?->nama_barang ?? '—' }}</div>
            <div class="asset-ruangan">📍 {{ $asset->ruangan?->nama_ruangan ?? '—' }}</div>
        </div>
        @endforeach
    </div>
</body>
</html>

