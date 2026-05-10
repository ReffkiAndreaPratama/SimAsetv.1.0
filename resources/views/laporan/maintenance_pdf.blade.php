<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Laporan Maintenance — RBTV Bengkulu</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: DejaVu Sans, sans-serif; font-size: 9px; color: #1e293b; background: #fff; }

        /* ── NOMOR HALAMAN ── */
        @page { margin: 14mm 12mm 18mm 12mm; }
        .page-number {
            position: fixed;
            bottom: -14mm;
            right: 0;
            left: 0;
            text-align: center;
            font-size: 7.5px;
            color: #94a3b8;
        }
        .page-number::after { content: "Halaman " counter(page) " dari " counter(pages); }
    </style>
</head>
<body>

<div class="page-number"></div>

{{-- ── HEADER ── --}}
<table width="100%" cellpadding="0" cellspacing="0" style="background:#78350f;margin-bottom:0;">
    <tr>
        <td style="padding:12px 16px 8px;">
            <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                    <td width="52" valign="middle">
                        <img src="{{ public_path('logo.png') }}" alt="RBTV"
                             width="44" height="44"
                             style="border-radius:8px;background:rgba(255,255,255,0.15);padding:3px;display:block;">
                    </td>
                    <td style="padding-left:10px;" valign="middle">
                        <div style="font-size:11px;font-weight:700;color:#fff;letter-spacing:0.02em;">
                            RAKYAT BENGKULU TELEVISI (RBTV)
                        </div>
                        <div style="font-size:7.5px;color:rgba(255,255,255,0.65);margin-top:2px;">
                            Sistem Informasi Manajemen Aset Barang Kantor &mdash; SimAset v1.0
                        </div>
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
            <div style="font-size:13px;font-weight:900;color:#fff;text-transform:uppercase;letter-spacing:0.08em;">
                LAPORAN ASET MAINTENANCE
            </div>
            <div style="font-size:7.5px;color:rgba(255,255,255,0.6);margin-top:2px;">
                Daftar aset yang sedang dalam proses perbaikan &mdash; SimAset v1.0
            </div>
        </td>
    </tr>
</table>

{{-- ── ACCENT BAR (oranye untuk maintenance) ── --}}
<table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:10px;">
    <tr><td height="3" style="background:#d97706;font-size:0;line-height:0;">&nbsp;</td></tr>
</table>

{{-- ── SUMMARY ── --}}
@php
    $total   = $assets->count();
    $baik    = $assets->where('kondisi', 'Baik')->count();
    $rusakR  = $assets->where('kondisi', 'Rusak Ringan')->count();
    $rusakB  = $assets->where('kondisi', 'Rusak Berat')->count();
    $ruangans = $assets->pluck('ruangan.nama_ruangan')->filter()->unique()->count();
@endphp
<table width="100%" cellpadding="0" cellspacing="0"
       style="border:1px solid #fde68a;border-radius:6px;border-collapse:collapse;margin-bottom:10px;">
    <tr>
        <td width="25%" align="center" style="padding:7px 4px;border-right:1px solid #fde68a;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;display:block;">Total Maintenance</span>
            <span style="font-size:16px;font-weight:900;color:#d97706;display:block;line-height:1.2;">{{ $total }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">aset</span>
        </td>
        <td width="25%" align="center" style="padding:7px 4px;border-right:1px solid #fde68a;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;display:block;">Kondisi Baik</span>
            <span style="font-size:16px;font-weight:900;color:#059669;display:block;line-height:1.2;">{{ $baik }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">unit</span>
        </td>
        <td width="25%" align="center" style="padding:7px 4px;border-right:1px solid #fde68a;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;display:block;">Rusak Ringan</span>
            <span style="font-size:16px;font-weight:900;color:#d97706;display:block;line-height:1.2;">{{ $rusakR }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">unit</span>
        </td>
        <td width="25%" align="center" style="padding:7px 4px;">
            <span style="font-size:7px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.05em;display:block;">Rusak Berat</span>
            <span style="font-size:16px;font-weight:900;color:#dc2626;display:block;line-height:1.2;">{{ $rusakB }}</span>
            <span style="font-size:6.5px;color:#94a3b8;display:block;">unit</span>
        </td>
    </tr>
</table>

{{-- ── META ── --}}
<table width="100%" cellpadding="0" cellspacing="0"
       style="background:#fffbeb;border:1px solid #fde68a;border-radius:5px;border-collapse:collapse;margin-bottom:10px;">
    <tr>
        <td style="padding:5px 12px;font-size:8px;color:#92400e;">
            <strong style="color:#78350f;">Dicetak oleh:</strong> {{ auth()->user()?->nama ?? 'System' }}
            &nbsp;&nbsp;&nbsp;
            <strong style="color:#78350f;">Tanggal:</strong> {{ date('d F Y') }}
            &nbsp;&nbsp;&nbsp;
            <strong style="color:#78350f;">Periode:</strong> {{ $periode ?? 'Semua Periode' }}
            &nbsp;&nbsp;&nbsp;
            <strong style="color:#78350f;">Total record:</strong> {{ $total }} aset maintenance
        </td>
    </tr>
</table>

{{-- ── DATA TABLE ── --}}
@if($assets->count() > 0)
<table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-bottom:12px;">
    <thead>
        <tr>
            <th width="22" align="center" style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">No</th>
            <th width="70"              style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Kode Aset</th>
            <th                         style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Nama Barang</th>
            <th width="80"              style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Kategori</th>
            <th width="90"              style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Ruangan</th>
            <th width="65" align="center" style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Kondisi</th>
            <th width="75"              style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Serial No.</th>
            <th width="70" align="center" style="background:#78350f;color:#fff;padding:6px 5px;font-size:7.5px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;border:1px solid #78350f;">Diperbarui</th>
        </tr>
    </thead>
    <tbody>
        @foreach($assets as $a)
        @php $rowBg = $loop->even ? '#fffbeb' : '#ffffff'; @endphp
        <tr>
            <td align="center" style="padding:5px;font-size:8px;color:#94a3b8;border:1px solid #e2e8f0;background:{{ $rowBg }};">{{ $loop->iteration }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-family:DejaVu Sans Mono,monospace;font-size:8px;font-weight:700;color:#92400e;">{{ $a->kode_aset }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-weight:600;font-size:8.5px;">{{ $a->barang?->nama_barang ?? '-' }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:8px;">{{ $a->barang?->kategori ?? '-' }}</td>
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:8px;">{{ $a->ruangan?->nama_ruangan ?? '-' }}</td>
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
            <td style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:7.5px;color:#64748b;">{{ $a->serial_number ?? '—' }}</td>
            <td align="center" style="padding:5px;border:1px solid #e2e8f0;background:{{ $rowBg }};font-size:7.5px;color:#64748b;">
                {{ $a->updated_at?->format('d/m/Y') ?? '—' }}
            </td>
        </tr>
        @if($a->keterangan)
        <tr>
            <td style="padding:0;border:none;background:{{ $rowBg }};"></td>
            <td colspan="7" style="padding:2px 5px 5px;border:1px solid #e2e8f0;border-top:none;background:{{ $rowBg }};font-size:7.5px;color:#64748b;">
                <em>Catatan: {{ $a->keterangan }}</em>
            </td>
        </tr>
        @endif
        @endforeach
    </tbody>
</table>
@else
<table width="100%" cellpadding="0" cellspacing="0"
       style="border:1px solid #fde68a;border-radius:8px;border-collapse:collapse;margin-bottom:12px;">
    <tr>
        <td align="center" style="padding:30px;font-size:9px;color:#94a3b8;">
            Tidak ada aset yang sedang dalam maintenance saat ini.
        </td>
    </tr>
</table>
@endif

{{-- ── FOOTER ── --}}
<table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-top:16px;">
    <tr>
        <td style="border-top:1.5px solid #e2e8f0;padding-top:0;font-size:0;line-height:0;" colspan="2">&nbsp;</td>
    </tr>
    <tr>
        <td valign="top" style="padding:10px 12px 0 0;font-size:8px;color:#94a3b8;line-height:1.8;">
            <strong style="color:#334155;font-size:8.5px;">SimAset &mdash; Sistem Informasi Manajemen Aset Barang Kantor</strong><br>
            RBTV Bengkulu &copy; {{ date('Y') }}<br>
            <span style="font-size:7.5px;">Dokumen ini dicetak secara otomatis oleh sistem pada {{ date('d-m-Y H:i') }}</span>
        </td>
        <td width="220" valign="top" style="padding:10px 0 0 12px;text-align:center;">
            <div style="font-size:9px;color:#475569;margin-bottom:4px;">Bengkulu, {{ date('d F Y') }}</div>
            <div style="font-size:8.5px;color:#64748b;margin-bottom:40px;">Mengetahui,</div>
            <table width="180" cellpadding="0" cellspacing="0" style="margin:0 auto 6px;">
                <tr><td style="border-top:1.5px solid #475569;font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>
            <div style="font-size:9.5px;font-weight:700;color:#0f172a;letter-spacing:0.02em;">Petugas Aset</div>
            <div style="font-size:8px;color:#94a3b8;margin-top:2px;">Nama &amp; Tanda Tangan</div>
        </td>
    </tr>
</table>

</body>
</html>


