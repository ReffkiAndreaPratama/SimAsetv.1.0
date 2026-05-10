<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>500 — Kesalahan Server · SimAset RBTV</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #0d1f4e 0%, #1a3470 50%, #1c3d9e 100%);
            display: flex; align-items: center; justify-content: center; padding: 20px;
        }
        .wrap {
            text-align: center; max-width: 520px; width: 100%;
            background: #fff; border-radius: 24px;
            padding: 48px 40px;
            box-shadow: 0 24px 64px rgba(0,0,0,.25);
        }
        .brand-row {
            display: flex; align-items: center; justify-content: center; gap: 10px;
            margin-bottom: 32px; padding-bottom: 24px;
            border-bottom: 1px solid #F1F5F9;
        }
        .brand-logo {
            width: 40px; height: 40px; border-radius: 10px;
            background: #EFF6FF; border: 1.5px solid #BFDBFE;
            display: flex; align-items: center; justify-content: center; overflow: hidden;
        }
        .brand-logo img { width: 100%; height: 100%; object-fit: contain; padding: 6px; }
        .brand-name { font-size: .95rem; font-weight: 800; color: #1E3A8A; letter-spacing: .04em; text-transform: uppercase; }
        .brand-sub  { font-size: .62rem; color: #94A3B8; letter-spacing: .08em; text-transform: uppercase; }

        .code {
            font-size: 100px; font-weight: 900; line-height: 1;
            background: linear-gradient(135deg, #dc2626, #ef4444);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text; margin-bottom: 6px; letter-spacing: -4px;
        }
        .divider { width: 48px; height: 4px; background: linear-gradient(90deg, #dc2626, #ef4444); border-radius: 2px; margin: 0 auto 20px; }
        .icon-wrap {
            width: 72px; height: 72px; border-radius: 50%;
            background: #FEF2F2; border: 2px solid #FECACA;
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 20px; font-size: 28px; color: #DC2626;
        }
        h1 { font-size: 1.4rem; font-weight: 800; color: #111827; margin-bottom: 10px; }
        p  { font-size: .9rem; color: #6B7280; line-height: 1.65; margin-bottom: 28px; }
        .btn-row { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
        .btn-home {
            display: inline-flex; align-items: center; gap: 7px;
            padding: 11px 24px; background: linear-gradient(135deg,#1d4ed8,#3b82f6); color: #fff;
            border-radius: 10px; text-decoration: none; font-weight: 700;
            font-size: .875rem; transition: all .2s;
            box-shadow: 0 4px 12px rgba(59,130,246,.3);
        }
        .btn-home:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(59,130,246,.38); color: #fff; }
        .btn-back {
            display: inline-flex; align-items: center; gap: 7px;
            padding: 11px 24px; background: #fff; color: #374151;
            border: 1.5px solid #E5E7EB; border-radius: 10px;
            text-decoration: none; font-weight: 600; font-size: .875rem; transition: all .2s;
        }
        .btn-back:hover { background: #F8FAFC; border-color: #BFDBFE; color: #1D4ED8; }
    </style>
</head>
<body>
    <div class="wrap">
        <div class="brand-row">
            <div class="brand-logo">
                <img src="{{ asset('logoweb.png') }}" alt="RBTV" onerror="this.style.display='none'">
            </div>
            <div>
                <div class="brand-name">SimAset</div>
                <div class="brand-sub">RBTV Bengkulu</div>
            </div>
        </div>
        <div class="code">500</div>
        <div class="divider"></div>
        <div class="icon-wrap"><i class="fas fa-exclamation-triangle"></i></div>
        <h1>Terjadi Kesalahan Server</h1>
        <p>Maaf, terjadi kesalahan pada server kami.<br>Tim teknis telah diberitahu. Silakan coba lagi beberapa saat.</p>
        <div class="btn-row">
            <a href="{{ url('/dashboard') }}" class="btn-home"><i class="fas fa-home"></i> Ke Dashboard</a>
            <a href="javascript:history.back()" class="btn-back"><i class="fas fa-arrow-left"></i> Kembali</a>
        </div>
    </div>
</body>
</html>
