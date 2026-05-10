<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Laporan Aset Ruangan — {{ $ruangan->nama_ruangan }}</title>
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
            <div style="font-size:13px;font-weight:900;color:#fff;text-transform:uppercase;letter-spacing:0.08em;">LAPORAN ASET PER RUANGAN</div>
            <div style="font-size:7.5px;color:rgba(255,255,255,0.6);margin-top:2px;">Dokumen inventarisasi aset berdasarkan lokasi &mdash; SimAset v1.0</div>
        </td>
    </tr>
</table>

{{-- ACCENT BAR --}}
<table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:10px;">
    <tr><td height="3" style="background:#2563eb;font-size:0;line-height:0;">&nbsp;</td></tr>
</table>

{{-- INFO RUANGAN --}}
@php
    $totalAset = $assets->count();
    $baik      = $assets->where('kondisi', 'Baik')->count();
    $rusakR    = $assets->where('kondisi', 'Rusak Ringan')->count();
    $rusakB    = $assets->where('kondisi', 'Rusak Berat')->count();
    $aktif     = $assets->where('status', 'Aktif')->count();
    $maint     = $assets->where('status', 'Maintenance')->count();
@endphp

<table width="100%" cellpadding="0" cellspacing="0"
       style="background:#eff6ff;border:1.5px solid #bfdbfe;border-collapse:collapse;margin-bottom:10px;">
    <tr>
        <td style="padding:10px 14px;">
            <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                    <td valign="middle">
                        <div style="font-size:13px;font-weight:800;color:#1a3470;">{{ $ruangan->nama_ruangan }}</div>
                        @if($ruangan->lantai)
                        <div style="font-size:8px;color:#3b82f6;margin-top:2px;">
                            <span style="background:#dbeafe;padding:1px 6px;border-radius:4px;">{{ $ruangan->lantai }}</span>
                        </div>
                        @endif
                        @if($ruangan->keterangan)
                        <div style="font-size:7.5px;color:#64748b;margin-top:4px;">{{ $ruangan->keterangan }}</div>
                        @endif
                    </td>
                    <td align="right" valign="middle" width="200">
                        <div style="font-size:7.5px;color:#64748b;">Total: <strong style="color:#1a3470;font-size:9px;">{{ $totalAset }}</strong> aset</div>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>

{{-- SUMMARY --}}
<table width="100%" cellpadding="0" cellspacing="0"
       style="border:1px solid #e2e8f0;border-collapse:collapse;margin-bottom:10px;">
    <tr>
        <td width="20%" align="center" style="padding:6px 4px;border-right:1px solid #e2e8f0;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Kondisi Baik</span>
            <span style="font-size:15px;font-weight:900;color:#059669;display:block;line-height:1.2;">{{ $baik }}</span>
        </td>
        <td width="20%" align="center" style="padding:6px 4px;border-right:1px solid #e2e8f0;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Rusak Ringan</span>
            <span style="font-size:15px;font-weight:900;color:#d97706;display:block;line-height:1.2;">{{ $rusakR }}</span>
        </td>
        <td width="20%" align="center" style="padding:6px 4px;border-right:1px solid #e2e8f0;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Rusak Berat</span>
            <span style="font-size:15px;font-weight:900;color:#dc2626;display:block;line-height:1.2;">{{ $rusakB }}</span>
        </td>
        <td width="20%" align="center" style="padding:6px 4px;border-right:1px solid #e2e8f0;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Aktif</span>
            <span style="font-size:15px;font-weight:900;color:#059669;display:block;line-height:1.2;">{{ $aktif }}</span>
        </td>
        <td width="20%" align="center" style="padding:6px 4px;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;display:block;">Maintenance</span>
            <span style="font-size:15px;font-weight:900;color:#0e7490;display:block;line-height:1.2;">{{ $maint }}</span>
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
            <strong style="color:#1e293b;">Ruangan:</strong> {{ $ruangan->nama_ruangan }}@if($ruangan->lantai) ({{ $ruangan->lantai }})@endif
        </td>
    </tr>
</table>

{{-- DATA TABLE --}}
@if($assets->count() > 0)
<table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-bottom:12px;">
    <thead>
        <tr>
            <th width="22" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">No</th>
            <th width="70" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Kode Aset</th>
            <th style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Nama Barang</th>
            <th width="80" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Kategori</th>
            <th width="65" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Kondisi</th>
            <th width="58" align="center" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Status</th>
            <th width="80" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Harga</th>
            <th width="75" style="background:#1a3470;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;border:1px solid #1a3470;">Serial No.</th>
        </tr>
    </thead>
    <tbody>
        @foreach($assets as $a)
        @php $rowBg = $loop->even ? '#f0f9ff' : '#ffffff'; @endphp
        <tr>
            <td align="center" style="padding:5px;font-size:8px;color:#94a3b8;border:1px solid #e2e8f0;background:{{ $rowBg }};">{{ $loop->iteration }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-family:DejaVu Sans Mono,monospace;font-size:8px;font-weight:700;color:#1a3470;">{{ $a->kode_aset }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-weight:600;font-size:8.5px;">{{ $a->barang?->nama_barang ?? '-' }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:8px;">{{ $a->barang?->kategori ?? '-' }}</td>
            <td align="center" style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};">
                @if($a->kondisi == 'Baik')
                    <span style="background:#d1fae5;color:#065f46;padding:1px 5px;border-radius:8px;font-size:7px;font-weight:700;">Baik</span>
                @elseif($a->kondisi == 'Rusak Ringan')
                    <span style="background:#fef3c7;color:#92400e;padding:1px 5px;border-radius:8px;font-size:7px;font-weight:700;">Rusak Ringan</span>
                @elseif($a->kondisi == 'Rusak Berat')
                    <span style="background:#fee2e2;color:#991b1b;padding:1px 5px;border-radius:8px;font-size:7px;font-weight:700;">Rusak Berat</span>
                @else
                    <span style="color:#94a3b8;">—</span>
                @endif
            </td>
            <td align="center" style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};">
                @if($a->status == 'Aktif')
                    <span style="background:#d1fae5;color:#065f46;padding:1px 5px;border-radius:8px;font-size:7px;font-weight:700;">Aktif</span>
                @elseif($a->status == 'Maintenance')
                    <span style="background:#cffafe;color:#0e7490;padding:1px 5px;border-radius:8px;font-size:7px;font-weight:700;">Maintenance</span>
                @else
                    <span style="background:#f1f5f9;color:#475569;padding:1px 5px;border-radius:8px;font-size:7px;font-weight:700;">Non-Aktif</span>
                @endif
            </td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:7.5px;color:#374151;">
                @if($a->harga)Rp {{ number_format($a->harga, 0, ',', '.') }}@else<span style="color:#94a3b8;">—</span>@endif
            </td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:7.5px;color:#64748b;">{{ $a->serial_number ?? '—' }}</td>
        </tr>
        @endforeach
    </tbody>
    <tfoot>
        <tr>
            <td colspan="7" align="right"
                style="padding:6px 8px;background:#f1f5f9;font-weight:700;font-size:9px;border:1px solid #cbd5e1;color:#1e293b;">
                Total Aset di Ruangan Ini:
            </td>
            <td align="center"
                style="padding:6px 5px;background:#f1f5f9;font-weight:900;font-size:11px;color:#1a3470;border:1px solid #cbd5e1;">
                {{ $totalAset }}
            </td>
        </tr>
    </tfoot>
</table>
@else
<table width="100%" cellpadding="0" cellspacing="0"
       style="border:1px solid #e2e8f0;border-collapse:collapse;margin-bottom:12px;">
    <tr>
        <td align="center" style="padding:30px;font-size:9px;color:#94a3b8;">
            Tidak ada aset terdaftar di ruangan ini.
        </td>
    </tr>
</table>
@endif

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
