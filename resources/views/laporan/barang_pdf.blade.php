<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Laporan Master Barang — RBTV Bengkulu</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: DejaVu Sans, sans-serif; font-size: 9px; color: #1e293b; background: #fff; }
        @page { margin: 14mm 12mm 18mm 12mm; }
        .page-number {
            position: fixed; bottom: -14mm; right: 0; left: 0;
            text-align: center; font-size: 7.5px; color: #94a3b8;
        }
        .page-number::after { content: "Halaman " counter(page) " dari " counter(pages); }
    </style>
</head>
<body>

<div class="page-number"></div>

{{-- HEADER --}}
<table width="100%" cellpadding="0" cellspacing="0" style="background:#1a3470;margin-bottom:0;">
    <tr>
        <td style="padding:12px 16px 8px;">
            <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                    <td width="52" valign="middle">
                        <img src="{{ public_path('logo.png') }}" alt="RBTV" width="44" height="44"
                             style="border-radius:8px;background:rgba(255,255,255,0.15);padding:3px;display:block;">
                    </td>
                    <td style="padding-left:10px;" valign="middle">
                        <div style="font-size:11px;font-weight:700;color:#fff;">RAKYAT BENGKULU TELEVISI (RBTV)</div>
                        <div style="font-size:7.5px;color:rgba(255,255,255,0.65);margin-top:2px;">Sistem Informasi Manajemen Aset Barang Kantor &mdash; SimAset v1.0</div>
                    </td>
                    <td align="right" valign="middle">
                        <div style="font-size:7.5px;color:rgba(255,255,255,0.65);">Tanggal Cetak</div>
                        <div style="font-size:10px;font-weight:700;color:#fff;">{{ date('d-m-Y H:i') }}</div>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td align="center" style="padding:8px 16px 10px;border-top:1px solid rgba(255,255,255,0.15);">
            <div style="font-size:13px;font-weight:900;color:#fff;text-transform:uppercase;letter-spacing:0.08em;">LAPORAN MASTER BARANG</div>
            <div style="font-size:7.5px;color:rgba(255,255,255,0.6);margin-top:2px;">Dokumen resmi katalog jenis barang kantor &mdash; dicetak oleh sistem SimAset</div>
        </td>
    </tr>
</table>

{{-- ACCENT BAR --}}
<table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:10px;">
    <tr><td height="3" style="background:#059669;font-size:0;line-height:0;">&nbsp;</td></tr>
</table>

{{-- SUMMARY --}}
@php
    $total     = $barangs->count();
    $totalUnit = $barangs->sum(fn($b) => $b->aset_count ?? 0);
    $katCount  = $barangs->pluck('kategori')->filter()->unique()->count();
    $adaAset   = $barangs->filter(fn($b) => ($b->aset_count ?? 0) > 0)->count();
@endphp
<table width="100%" cellpadding="0" cellspacing="0"
       style="border:1px solid #d1fae5;border-collapse:collapse;margin-bottom:10px;">
    <tr>
        <td width="25%" align="center" style="padding:7px 4px;border-right:1px solid #d1fae5;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Total Jenis</span>
            <span style="font-size:16px;font-weight:900;color:#1a3470;display:block;line-height:1.2;">{{ $total }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">jenis terdaftar</span>
        </td>
        <td width="25%" align="center" style="padding:7px 4px;border-right:1px solid #d1fae5;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Total Unit Aset</span>
            <span style="font-size:16px;font-weight:900;color:#059669;display:block;line-height:1.2;">{{ $totalUnit }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">unit tercatat</span>
        </td>
        <td width="25%" align="center" style="padding:7px 4px;border-right:1px solid #d1fae5;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Ada Aset</span>
            <span style="font-size:16px;font-weight:900;color:#1a3470;display:block;line-height:1.2;">{{ $adaAset }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">jenis punya aset</span>
        </td>
        <td width="25%" align="center" style="padding:7px 4px;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Kategori</span>
            <span style="font-size:16px;font-weight:900;color:#7c3aed;display:block;line-height:1.2;">{{ $katCount }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">jenis kategori</span>
        </td>
    </tr>
</table>

{{-- META --}}
<table width="100%" cellpadding="0" cellspacing="0"
       style="background:#f8fafc;border:1px solid #e2e8f0;border-collapse:collapse;margin-bottom:10px;">
    <tr>
        <td style="padding:5px 12px;font-size:8px;color:#64748b;">
            <strong style="color:#1e293b;">Dicetak oleh:</strong> {{ auth()->user()?->nama ?? 'System' }}
            &nbsp;&nbsp;&nbsp;
            <strong style="color:#1e293b;">Tanggal:</strong> {{ date('d F Y') }}
            &nbsp;&nbsp;&nbsp;
            <strong style="color:#1e293b;">Periode:</strong> {{ $periode ?? 'Semua Periode' }}
            &nbsp;&nbsp;&nbsp;
            <strong style="color:#1e293b;">Total:</strong> {{ $total }} jenis barang
        </td>
    </tr>
</table>

{{-- DATA TABLE --}}
<table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-bottom:12px;">
    <thead>
        <tr>
            <th width="24" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">No</th>
            <th width="90" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Kode Barang</th>
            <th style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Nama Barang</th>
            <th width="90" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Kategori</th>
            <th width="45" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Jml</th>
            <th width="45" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Aset</th>
            <th style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Keterangan</th>
            <th width="65" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Terdaftar</th>
        </tr>
    </thead>
    <tbody>
        @foreach($barangs as $item)
        @php
            $jmlAset = $item->aset_count ?? 0;
            $rowBg   = $loop->even ? '#f0fdf4' : '#ffffff';
        @endphp
        <tr>
            <td align="center" style="padding:5px;font-size:8px;color:#94a3b8;border:1px solid #e2e8f0;background:{{ $rowBg }};">{{ $loop->iteration }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-family:DejaVu Sans Mono,monospace;font-size:8px;font-weight:700;color:#065f46;">{{ $item->kode_barang }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-weight:600;font-size:8.5px;">{{ $item->nama_barang }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};">
                @if($item->kategori)
                    <span style="background:#eff6ff;color:#1d4ed8;padding:1px 5px;border-radius:6px;font-size:7px;font-weight:600;">{{ $item->kategori }}</span>
                @else
                    <span style="color:#94a3b8;font-size:8px;">—</span>
                @endif
            </td>
            <td align="center" style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-weight:700;font-size:9px;color:#374151;">
                {{ $item->jumlah ?? 0 }}
            </td>
            <td align="center" style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-weight:700;font-size:9px;color:{{ $jmlAset > 0 ? '#059669' : '#94a3b8' }};">
                {{ $jmlAset }}
            </td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:7.5px;color:#64748b;">
                {{ $item->keterangan ? \Illuminate\Support\Str::limit($item->keterangan, 60) : '—' }}
            </td>
            <td align="center" style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:7.5px;color:#64748b;">
                {{ $item->created_at?->format('d/m/Y') ?? '—' }}
            </td>
        </tr>
        @endforeach
    </tbody>
    <tfoot>
        <tr>
            <td colspan="5" align="right"
                style="padding:6px 8px;background:#f1f5f9;font-weight:700;font-size:9px;border:1px solid #cbd5e1;color:#1e293b;">
                Total Unit Aset:
            </td>
            <td align="center"
                style="padding:6px 5px;background:#f1f5f9;font-weight:900;font-size:11px;color:#059669;border:1px solid #cbd5e1;">
                {{ $totalUnit }}
            </td>
            <td colspan="2" style="background:#f1f5f9;border:1px solid #cbd5e1;"></td>
        </tr>
    </tfoot>
</table>

{{-- FOOTER --}}
<table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-top:16px;">
    <tr><td style="border-top:1.5px solid #e2e8f0;font-size:0;line-height:0;" colspan="2">&nbsp;</td></tr>
    <tr>
        <td valign="top" style="padding:10px 12px 0 0;font-size:8px;color:#94a3b8;line-height:1.8;">
            <strong style="color:#334155;font-size:8.5px;">SimAset &mdash; Sistem Informasi Manajemen Aset Barang Kantor</strong><br>
            RBTV Bengkulu &copy; {{ date('Y') }}<br>
            <span style="font-size:7.5px;">Dicetak otomatis pada {{ date('d-m-Y H:i') }}</span>
        </td>
        <td width="220" valign="top" style="padding:10px 0 0 12px;text-align:center;">
            <div style="font-size:9px;color:#475569;margin-bottom:4px;">Bengkulu, {{ date('d F Y') }}</div>
            <div style="font-size:8.5px;color:#64748b;margin-bottom:40px;">Mengetahui,</div>
            <table width="180" cellpadding="0" cellspacing="0" style="margin:0 auto 6px;">
                <tr><td style="border-top:1.5px solid #475569;font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>
            <div style="font-size:9.5px;font-weight:700;color:#0f172a;">Petugas Aset</div>
            <div style="font-size:8px;color:#94a3b8;margin-top:2px;">Nama &amp; Tanda Tangan</div>
        </td>
    </tr>
</table>

</body>
</html>
