<?php

namespace App\Http\Controllers;

use App\Models\Asset;
use Illuminate\Http\Request;
use SimpleSoftwareIO\QrCode\Facades\QrCode;

class QrCodeController extends Controller
{
    /**
     * Halaman scanner QR code
     */
    public function scanner()
    {
        return view('qrcode.scanner');
    }

    /**
     * Batch print QR codes
     */
    public function batchPrint(Request $request)
    {
        $kodes = $request->input('asset_ids', []);

        // Handle comma-separated string dari GET query
        if (is_string($kodes) && !empty($kodes)) {
            $kodes = explode(',', $kodes);
        } elseif (is_array($kodes) && count($kodes) === 1 && str_contains($kodes[0], ',')) {
            $kodes = explode(',', $kodes[0]);
        }

        if (empty($kodes)) {
            return redirect()->back()->with('error', 'Tidak ada aset yang dipilih.');
        }

        $assets = Asset::with(['barang', 'ruangan'])
            ->whereIn('kode_aset', $kodes)
            ->get();

        if ($assets->isEmpty()) {
            return redirect()->back()->with('error', 'Aset tidak ditemukan.');
        }

        $qrcodes = [];
        foreach ($assets as $asset) {
            $qrcodes[$asset->kode_aset] = QrCode::size(120)
                ->format('svg')
                ->generate(route('assets.detail', $asset->kode_aset));
        }

        return view('qrcode.batch_print', compact('assets', 'qrcodes'));
    }

    /**
     * Download / cetak QR code satu aset
     */
    public function download(string $kode_aset)
    {
        $asset = Asset::with(['barang', 'ruangan'])
            ->where('kode_aset', $kode_aset)
            ->firstOrFail();

        $qrCode   = QrCode::size(200)->format('svg')->generate(route('assets.detail', $asset->kode_aset));
        $autoPrint = true;

        return view('qrcode.single', compact('asset', 'qrCode', 'autoPrint'));
    }

    /**
     * Search aset by kode_aset (untuk scanner)
     */
    public function search(Request $request)
    {
        $kode = trim($request->query('code', ''));

        if (!$kode) {
            return response()->json(['success' => false, 'message' => 'Kode tidak boleh kosong']);
        }

        $asset = Asset::with(['barang', 'ruangan'])
            ->where('kode_aset', $kode)
            ->first();

        if (!$asset) {
            $asset = Asset::with(['barang', 'ruangan'])
                ->where('kode_aset', 'like', "%{$kode}%")
                ->first();
        }

        if (!$asset) {
            return response()->json(['success' => false, 'message' => 'Aset tidak ditemukan']);
        }

        return response()->json([
            'success' => true,
            'data'    => [
                'kode_aset'     => $asset->kode_aset,
                'kode_barang'   => $asset->kode_barang,
                'nama_barang'   => $asset->barang?->nama_barang ?? '—',
                'kategori'      => $asset->barang?->kategori ?? '—',
                'ruangan'       => $asset->ruangan?->nama_ruangan ?? '—',
                'kondisi'       => $asset->kondisi ?? '—',
                'status'        => $asset->status ?? '—',
                'jumlah'        => $asset->jumlah ?? 1,
                'serial_number' => $asset->serial_number ?? '—',
                'url'           => route('aset.show', $asset->kode_aset),
            ],
        ]);
    }
}
