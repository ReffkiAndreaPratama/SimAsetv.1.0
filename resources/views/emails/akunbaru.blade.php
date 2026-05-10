<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Akun Baru — SimAset RBTV</title>
    <!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
</head>
<body style="margin:0;padding:0;background:#F0F4F8;font-family:'Segoe UI',Arial,sans-serif;-webkit-font-smoothing:antialiased;">

<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background:#F0F4F8;">
<tr><td align="center" style="padding:32px 16px;">

    <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="max-width:600px;width:100%;">

        {{-- ── TOP ACCENT BAR ── --}}
        <tr>
            <td style="background:linear-gradient(90deg,#1e3a8a,#2563eb,#3b82f6);height:5px;border-radius:8px 8px 0 0;"></td>
        </tr>

        {{-- ── HEADER ── --}}
        <tr>
            <td style="background:#1e3a8a;padding:36px 40px 28px;text-align:center;">
                {{-- Logo circle --}}
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

        {{-- ── BODY ── --}}
        <tr>
            <td style="background:#ffffff;padding:40px 40px 32px;">

                {{-- Greeting --}}
                <p style="font-size:22px;font-weight:700;color:#0f172a;margin:0 0 8px;">Selamat datang, {{ $name }}! 👋</p>
                <p style="font-size:14px;color:#64748b;margin:0 0 28px;line-height:1.7;">
                    Akun Anda telah berhasil dibuat di <strong style="color:#1e3a8a;">SimAset RBTV</strong>.
                    Berikut informasi login Anda — simpan dengan aman.
                </p>

                {{-- Credential card --}}
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
                       style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;overflow:hidden;margin:0 0 28px;">
                    <tr>
                        <td style="background:linear-gradient(135deg,#eff6ff,#dbeafe);padding:14px 20px;border-bottom:1px solid #e2e8f0;">
                            <p style="font-size:11px;font-weight:700;color:#1e40af;margin:0;letter-spacing:1.2px;text-transform:uppercase;">Detail Akun</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:0 20px;">
                            {{-- Email row --}}
                            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td style="padding:14px 0;border-bottom:1px solid #f1f5f9;">
                                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                            <tr>
                                                <td style="width:80px;font-size:12px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.8px;">Email</td>
                                                <td style="font-size:14px;color:#0f172a;font-weight:500;">{{ $email }}</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                {{-- Password row --}}
                                <tr>
                                    <td style="padding:14px 0;border-bottom:1px solid #f1f5f9;">
                                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                            <tr>
                                                <td style="width:80px;font-size:12px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.8px;">Password</td>
                                                <td>
                                                    <span style="display:inline-block;background:#1e3a8a;color:#ffffff;font-family:'Courier New',monospace;font-size:14px;font-weight:700;padding:5px 14px;border-radius:6px;letter-spacing:1.5px;">{{ $password }}</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                {{-- Role row --}}
                                <tr>
                                    <td style="padding:14px 0;">
                                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                            <tr>
                                                <td style="width:80px;font-size:12px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.8px;">Role</td>
                                                <td>
                                                    @if($role === 'admin')
                                                        <span style="display:inline-block;background:#ede9fe;color:#5b21b6;font-size:12px;font-weight:700;padding:4px 12px;border-radius:20px;letter-spacing:.5px;">Administrator</span>
                                                    @else
                                                        <span style="display:inline-block;background:#dcfce7;color:#166534;font-size:12px;font-weight:700;padding:4px 12px;border-radius:20px;letter-spacing:.5px;">Staff</span>
                                                    @endif
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>

                {{-- CTA button --}}
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:0 auto 28px;">
                    <tr>
                        <td style="border-radius:8px;background:linear-gradient(135deg,#2563eb,#1d4ed8);box-shadow:0 4px 14px rgba(37,99,235,0.35);">
                            <a href="{{ url('/login') }}"
                               style="display:inline-block;padding:14px 36px;color:#ffffff;font-size:15px;font-weight:600;text-decoration:none;letter-spacing:0.3px;">
                                Masuk ke SimAset &rarr;
                            </a>
                        </td>
                    </tr>
                </table>

                {{-- Warning notice --}}
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
                       style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;overflow:hidden;">
                    <tr>
                        <td style="width:4px;background:#f59e0b;"></td>
                        <td style="padding:14px 16px;">
                            <p style="font-size:13px;color:#78350f;margin:0;line-height:1.6;">
                                <strong>Penting:</strong> Segera ganti password Anda setelah login pertama melalui menu <em>Edit Profil</em> di pojok kanan atas.
                            </p>
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
        <tr>
            <td style="background:linear-gradient(90deg,#1e3a8a,#2563eb,#3b82f6);height:4px;border-radius:0 0 8px 8px;"></td>
        </tr>

    </table>
</td></tr>
</table>

</body>
</html>
