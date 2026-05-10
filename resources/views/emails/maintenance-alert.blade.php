<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ $tipe === 'masuk' ? 'Aset Masuk Maintenance' : 'Maintenance Selesai' }} — SimAset RBTV</title>
</head>
<body style="margin:0;padding:0;background:#F0F4F8;font-family:'Segoe UI',Arial,sans-serif;-webkit-font-smoothing:antialiased;">

<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#F0F4F8;">
<tr><td align="center" style="padding:32px 16px;">

    <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="max-width:600px;width:100%;">

        {{-- ── TOP ACCENT BAR ── --}}
        @if($tipe === 'masuk')
        <tr><td style="background:linear-gradient(90deg,#b45309,#f59e0b,#fbbf24);height:5px;border-radius:8px 8px 0 0;"></td></tr>
        @else
        <tr><td style="background:linear-gradient(90deg,#065f46,#059669,#34d399);height:5px;border-radius:8px 8px 0 0;"></td></tr>
        @endif

        {{-- ── HEADER ── --}}
        <tr>
            <td style="background:#1e3a8a;padding:36px 40px 28px;text-align:center;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:0 auto 18px;">
                    <tr>
                        <td style="width:64px;height:64px;background:linear-gradient(135deg,#3b82f6,#60a5fa);border-radius:50%;text-align:center;vertical-align:middle;box-shadow:0 4px 16px rgba(0,0,0,0.25);">
                            <span style="color:#fff;font-size:22px;font-weight:800;letter-spacing:-1px;">SA</span>
                        </td>
                    </tr>
                </table>
                <p style="color:#ffffff;font-size:24px;font-weight:700;margin:0 0 6px;letter-spacing:0.3px;">SimAset</p>
                <p style="color:rgba(255,255,255,0.6);font-size:12px;margin:0;letter-spacing:1.5px;text-transform:uppercase;">Sistem Manajemen Aset · RBTV Bengkulu</p>
            </td>
        </tr>

        {{-- ── STATUS BANNER ── --}}
        @if($tipe === 'masuk')
        <tr>
            <td style="background:#fffbeb;border-bottom:3px solid #f59e0b;padding:16px 40px;text-align:center;">
                <p style="margin:0;font-size:15px;font-weight:700;color:#92400e;">
                    🔧 &nbsp;Aset Masuk Status Maintenance
                </p>
            </td>
        </tr>
        @else
        <tr>
            <td style="background:#f0fdf4;border-bottom:3px solid #10b981;padding:16px 40px;text-align:center;">
                <p style="margin:0;font-size:15px;font-weight:700;color:#065f46;">
                    ✅ &nbsp;Maintenance Selesai — Aset Kembali Aktif
                </p>
            </td>
        </tr>
        @endif

        {{-- ── BODY ── --}}
        <tr>
            <td style="background:#ffffff;padding:36px 40px 32px;">

                <p style="font-size:14px;color:#475569;margin:0 0 24px;line-height:1.75;">
                    @if($tipe === 'masuk')
                        Aset berikut telah ditandai masuk ke status <strong style="color:#92400e;">Maintenance</strong> dan memerlukan tindak lanjut dari tim teknis.
                    @else
                        Proses maintenance untuk aset berikut telah <strong style="color:#065f46;">selesai</strong>. Status aset kembali menjadi <strong>Aktif</strong>.
                    @endif
                </p>

                {{-- Asset detail card --}}
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
                       style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;overflow:hidden;margin:0 0 24px;">
                    <tr>
                        <td style="background:linear-gradient(135deg,#eff6ff,#dbeafe);padding:12px 20px;border-bottom:1px solid #e2e8f0;">
                            <p style="font-size:11px;font-weight:700;color:#1e40af;margin:0;letter-spacing:1.2px;text-transform:uppercase;">Informasi Aset</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:0 20px;">
                            @php
                                $rows = [
                                    ['label' => 'Kode Aset',   'value' => $asset->kode_aset,                       'mono' => true],
                                    ['label' => 'Nama Barang', 'value' => $asset->barang?->nama_barang ?? '—',      'mono' => false],
                                    ['label' => 'Kategori',    'value' => $asset->barang?->kategori ?? '—',         'mono' => false],
                                    ['label' => 'Ruangan',     'value' => $asset->ruangan?->nama_ruangan ?? '—',            'mono' => false],
                                    ['label' => 'Kondisi',     'value' => $asset->kondisi ?? '—',                   'mono' => false],
                                ];
                            @endphp
                            @foreach($rows as $i => $row)
                            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td style="padding:12px 0;{{ !$loop->last ? 'border-bottom:1px solid #f1f5f9;' : '' }}">
                                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                            <tr>
                                                <td style="width:110px;font-size:12px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.8px;vertical-align:middle;">{{ $row['label'] }}</td>
                                                <td style="font-size:14px;color:#0f172a;font-weight:{{ $row['mono'] ? '700' : '500' }};{{ $row['mono'] ? 'font-family:\'Courier New\',monospace;' : '' }}vertical-align:middle;">{{ $row['value'] }}</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            @endforeach
                        </td>
                    </tr>
                </table>

                {{-- Keterangan (jika ada) --}}
                @if($asset->keterangan)
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
                       style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;overflow:hidden;margin:0 0 24px;">
                    <tr>
                        <td style="width:4px;background:#f59e0b;"></td>
                        <td style="padding:14px 16px;">
                            <p style="font-size:13px;color:#78350f;margin:0;line-height:1.6;">
                                <strong>Keterangan:</strong> {{ $asset->keterangan }}
                            </p>
                        </td>
                    </tr>
                </table>
                @endif

                {{-- CTA --}}
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:0 auto;">
                    <tr>
                        <td style="border-radius:8px;background:linear-gradient(135deg,#2563eb,#1d4ed8);box-shadow:0 4px 14px rgba(37,99,235,0.3);">
                            <a href="{{ url('/aset/'.$asset->kode_aset.'/detail') }}"
                               style="display:inline-block;padding:13px 32px;color:#ffffff;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.3px;">
                                Lihat Detail Aset &rarr;
                            </a>
                        </td>
                    </tr>
                </table>

            </td>
        </tr>

        {{-- ── DIVIDER ── --}}
        <tr>
            <td style="background:#ffffff;padding:0 40px;">
                <hr style="border:none;border-top:1px solid #f1f5f9;margin:0;">
            </td>
        </tr>

        {{-- ── FOOTER ── --}}
        <tr>
            <td style="background:#ffffff;padding:24px 40px 32px;text-align:center;">
                <p style="font-size:13px;color:#94a3b8;margin:0 0 4px;">
                    Email ini dikirim otomatis oleh sistem. Jangan balas email ini.
                </p>
                <p style="font-size:12px;color:#cbd5e1;margin:0;">
                    &copy; {{ date('Y') }} &nbsp;·&nbsp; <strong style="color:#94a3b8;">SimAset</strong> &nbsp;·&nbsp; Rakyat Bengkulu Televisi
                </p>
            </td>
        </tr>

        {{-- ── BOTTOM ACCENT BAR ── --}}
        @if($tipe === 'masuk')
        <tr><td style="background:linear-gradient(90deg,#b45309,#f59e0b,#fbbf24);height:4px;border-radius:0 0 8px 8px;"></td></tr>
        @else
        <tr><td style="background:linear-gradient(90deg,#065f46,#059669,#34d399);height:4px;border-radius:0 0 8px 8px;"></td></tr>
        @endif

    </table>
</td></tr>
</table>

</body>
</html>

