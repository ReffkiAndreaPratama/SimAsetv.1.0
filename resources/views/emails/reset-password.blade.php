<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Reset Password — SimAset RBTV</title>
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

                {{-- Icon + title --}}
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:0 auto 24px;">
                    <tr>
                        <td style="width:56px;height:56px;background:#eff6ff;border-radius:50%;text-align:center;vertical-align:middle;border:2px solid #bfdbfe;">
                            <span style="font-size:24px;">🔐</span>
                        </td>
                    </tr>
                </table>

                <p style="font-size:22px;font-weight:700;color:#0f172a;margin:0 0 8px;text-align:center;">Reset Password</p>
                <p style="font-size:14px;color:#64748b;margin:0 0 28px;line-height:1.7;text-align:center;">
                    Halo <strong style="color:#0f172a;">{{ $user->nama }}</strong>, kami menerima permintaan untuk mereset password akun Anda.
                </p>

                {{-- CTA button --}}
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:0 auto 28px;">
                    <tr>
                        <td style="border-radius:8px;background:linear-gradient(135deg,#2563eb,#1d4ed8);box-shadow:0 4px 14px rgba(37,99,235,0.35);">
                            <a href="{{ $url }}"
                               style="display:inline-block;padding:14px 40px;color:#ffffff;font-size:15px;font-weight:600;text-decoration:none;letter-spacing:0.3px;">
                                Buat Password Baru &rarr;
                            </a>
                        </td>
                    </tr>
                </table>

                {{-- Expiry notice --}}
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
                       style="background:#fef2f2;border:1px solid #fecaca;border-radius:8px;overflow:hidden;margin:0 0 24px;">
                    <tr>
                        <td style="width:4px;background:#ef4444;"></td>
                        <td style="padding:14px 16px;">
                            <p style="font-size:13px;color:#991b1b;margin:0;line-height:1.6;">
                                <strong>Perhatian:</strong> Tautan ini hanya berlaku selama <strong>60 menit</strong>.
                                Jika Anda tidak meminta reset password, abaikan email ini — akun Anda tetap aman.
                            </p>
                        </td>
                    </tr>
                </table>

                {{-- Fallback URL --}}
                <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
                       style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:14px 16px;">
                    <tr>
                        <td>
                            <p style="font-size:12px;color:#94a3b8;margin:0 0 6px;">Jika tombol tidak berfungsi, salin tautan berikut ke browser:</p>
                            <p style="font-size:12px;color:#2563eb;word-break:break-all;margin:0;font-family:'Courier New',monospace;">{{ $url }}</p>
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

