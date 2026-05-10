<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Asset;
use App\Models\Barang;
use App\Models\Ruangan;
use App\Helpers\ActivityLogger;

class AssetController extends Controller
{
    // ── INDEX ──────────────────────────────────────────────────────

    public function index(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan'])
            ->orderBy('kode_aset');

        if ($request->filled('search')) {
            $s = $request->search;
            $query->where(function ($q) use ($s) {
                $q->where('kode_aset',      'like', "%{$s}%")
                  ->orWhere('serial_number', 'like', "%{$s}%")
                  ->orWhereHas('barang',    fn($q2) => $q2->where('nama_barang', 'like', "%{$s}%")
                                                           ->orWhere('kode_barang', 'like', "%{$s}%"))
                  ->orWhereHas('ruangan',   fn($q2) => $q2->where('nama_ruangan', 'like', "%{$s}%"));
            });
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }
        if ($request->filled('kondisi')) {
            $query->where('kondisi', $request->kondisi);
        }
        if ($request->filled('kategori')) {
            $query->whereHas('barang', fn($q) => $q->where('kategori', $request->kategori));
        }

        $assets = $query->paginate(15)->withQueryString();

        $stats = [
            'total'       => Asset::count(),
            'aktif'       => Asset::where('status', 'Aktif')->count(),
            'maintenance' => Asset::where('status', 'Maintenance')->count(),
            'non_aktif'   => Asset::where('status', 'Non-Aktif')->count(),
        ];

        $kategoriList = Barang::whereHas('aset')
            ->whereNotNull('kategori')
            ->distinct()
            ->orderBy('kategori')
            ->pluck('kategori');

        return view('aset.index', compact('assets', 'stats', 'kategoriList'));
    }

    // ── CREATE ─────────────────────────────────────────────────────

    public function create()
    {
        $barangs  = Barang::orderBy('nama_barang')->get(['kode_barang', 'nama_barang', 'kategori']);
        $ruangans = Ruangan::orderBy('nama_ruangan')->get();
        return view('aset.create', compact('barangs', 'ruangans'));
    }

    // ── STORE ──────────────────────────────────────────────────────

    public function store(Request $request)
    {
        $request->validate([
            'kode_barang'   => 'required|exists:barang,kode_barang',
            'kode_ruangan'  => 'required|exists:ruangan,kode_ruangan',
            'kondisi'       => 'required|in:Baik,Rusak Ringan,Rusak Berat',
            'status'        => 'required|in:Aktif,Maintenance,Non-Aktif',
            'serial_number' => 'nullable|string|max:100|unique:aset,serial_number',
            'harga'         => 'nullable|numeric|min:0',
            'keterangan'    => 'nullable|string',
            'foto'          => 'nullable|image|mimes:jpeg,png,gif|max:2048',
        ]);

        $kode_aset = Asset::generateKode();

        $fotoName = null;
        if ($request->hasFile('foto')) {
            $fotoDir = public_path('foto_aset');
            if (!file_exists($fotoDir)) mkdir($fotoDir, 0755, true);
            $fotoName = $kode_aset . '_' . time() . '.' . $request->file('foto')->getClientOriginalExtension();
            $request->file('foto')->move($fotoDir, $fotoName);
        }

        $asset = Asset::create([
            'kode_aset'     => $kode_aset,
            'kode_barang'   => $request->kode_barang,
            'kode_ruangan'  => $request->kode_ruangan,
            'id_user'       => auth()->id(),
            'serial_number' => $request->serial_number,
            'kondisi'       => $request->kondisi,
            'status'        => $request->status,
            'harga'         => $request->harga ?: null,
            'keterangan'    => $request->keterangan,
            'foto'          => $fotoName,
        ]);

        try {
            ActivityLogger::logAsset('Create', "Menambahkan aset baru: {$kode_aset}", $asset);
        } catch (\Exception $e) {}

        return redirect()->route('aset.index')
            ->with('success', "Aset berhasil ditambahkan. Kode: {$kode_aset}");
    }

    // ── SHOW ───────────────────────────────────────────────────────

    public function show(string $kode_aset)
    {
        $asset = Asset::with(['barang', 'ruangan', 'user'])
            ->where('kode_aset', $kode_aset)
            ->firstOrFail();
        return view('aset.show', compact('asset'));
    }

    // ── EDIT ───────────────────────────────────────────────────────

    public function edit(string $kode_aset)
    {
        $asset    = Asset::where('kode_aset', $kode_aset)->firstOrFail();
        $barangs  = Barang::orderBy('nama_barang')->get(['kode_barang', 'nama_barang', 'kategori']);
        $ruangans = Ruangan::orderBy('nama_ruangan')->get();
        return view('aset.edit', compact('asset', 'barangs', 'ruangans'));
    }

    // ── UPDATE ─────────────────────────────────────────────────────

    public function update(Request $request, string $kode_aset)
    {
        $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

        $request->validate([
            'kode_barang'   => 'required|exists:barang,kode_barang',
            'kode_ruangan'  => 'required|exists:ruangan,kode_ruangan',
            'kondisi'       => 'required|in:Baik,Rusak Ringan,Rusak Berat',
            'status'        => 'required|in:Aktif,Maintenance,Non-Aktif',
            'serial_number' => 'nullable|string|max:100|unique:aset,serial_number,' . $asset->kode_aset . ',kode_aset',
            'harga'         => 'nullable|numeric|min:0',
            'keterangan'    => 'nullable|string',
            'foto'          => 'nullable|image|mimes:jpeg,png,gif|max:2048',
        ]);

        $data = [
            'kode_barang'   => $request->kode_barang,
            'kode_ruangan'  => $request->kode_ruangan,
            'serial_number' => $request->serial_number,
            'kondisi'       => $request->kondisi,
            'status'        => $request->status,
            'harga'         => $request->harga ?: null,
            'keterangan'    => $request->keterangan,
        ];

        // Hapus foto lama
        if ($request->boolean('remove_photo') && $asset->foto) {
            $oldPath = public_path('foto_aset/' . $asset->foto);
            if (file_exists($oldPath)) @unlink($oldPath);
            $data['foto'] = null;
        }

        // Upload foto baru
        if ($request->hasFile('foto')) {
            // Hapus foto lama kalau ada
            if ($asset->foto) {
                $oldPath = public_path('foto_aset/' . $asset->foto);
                if (file_exists($oldPath)) @unlink($oldPath);
            }
            $fotoDir = public_path('foto_aset');
            if (!file_exists($fotoDir)) mkdir($fotoDir, 0755, true);
            $fotoName = $kode_aset . '_' . time() . '.' . $request->file('foto')->getClientOriginalExtension();
            $request->file('foto')->move($fotoDir, $fotoName);
            $data['foto'] = $fotoName;
        }

        $asset->update($data);

        try {
            ActivityLogger::logAsset('Update', "Mengupdate aset: {$kode_aset}", $asset);
        } catch (\Exception $e) {}

        return redirect()->route('aset.index')
            ->with('success', 'Data aset berhasil diperbarui.');
    }

    // ── DESTROY ────────────────────────────────────────────────────

    public function destroy(string $kode_aset)
    {
        $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

        // Hapus foto kalau ada
        if ($asset->foto) {
            $fotoPath = public_path('foto_aset/' . $asset->foto);
            if (file_exists($fotoPath)) @unlink($fotoPath);
        }

        $asset->delete();

        try {
            ActivityLogger::logAsset('Delete', "Menghapus aset: {$kode_aset}", $asset);
        } catch (\Exception $e) {}

        return redirect()->route('aset.index')
            ->with('success', "Aset ({$kode_aset}) berhasil dihapus.");
    }

    // ── BATCH DESTROY ──────────────────────────────────────────────

    public function batchDestroy(Request $request)
    {
        $kodes = $request->input('kodes', []);
        $count = 0;

        foreach ($kodes as $kode) {
            $asset = Asset::where('kode_aset', $kode)->first();
            if ($asset) {
                if ($asset->foto) {
                    $fotoPath = public_path('foto_aset/' . $asset->foto);
                    if (file_exists($fotoPath)) @unlink($fotoPath);
                }
                $asset->delete();
                $count++;
                try {
                    ActivityLogger::logAsset('Delete', "Batch delete: {$kode}", $asset);
                } catch (\Exception $e) {}
            }
        }

        return redirect()->route('aset.index')
            ->with('success', "Berhasil menghapus {$count} aset.");
    }

    // ── QR CODE ────────────────────────────────────────────────────

    public function generateQr(string $kode_aset)
    {
        $asset  = Asset::where('kode_aset', $kode_aset)->firstOrFail();
        $qrDir  = public_path('qr_codes');
        $files  = file_exists($qrDir) ? glob($qrDir . '/qr_' . $kode_aset . '*.png') : [];
        if (!empty($files)) {
            return redirect()->back()->with('info', 'QR Code sudah ada.');
        }
        $success = $this->generateQrCodeImage($asset);
        return $success
            ? redirect()->back()->with('success', 'QR Code berhasil di-generate.')
            : redirect()->back()->with('error', 'Gagal generate QR Code. Pastikan koneksi internet tersedia.');
    }

    public function showQr(string $kode_aset)
    {
        $asset = Asset::with(['barang', 'ruangan'])->where('kode_aset', $kode_aset)->firstOrFail();
        $qrDir = public_path('qr_codes');
        $files = file_exists($qrDir) ? glob($qrDir . '/qr_' . $kode_aset . '*.png') : [];
        if (empty($files)) $this->generateQrCodeImage($asset);
        return view('aset.qr', compact('asset'));
    }

    public function checkNew(Request $request)
    {
        $hasNew = Asset::where('updated_at', '>', $request->query('lastUpdate'))->exists();
        return response()->json(['hasNew' => $hasNew]);
    }

    public function detail(string $kode_aset)
    {
        $asset = Asset::with(['barang', 'ruangan', 'user'])->where('kode_aset', $kode_aset)->firstOrFail();
        return view('aset.show', compact('asset'));
    }

    // ── PRIVATE ────────────────────────────────────────────────────

    private function generateQrCodeImage(Asset $asset): bool
    {
        try {
            $qrDir = public_path('qr_codes');
            if (!file_exists($qrDir)) mkdir($qrDir, 0755, true);
            $qrData   = route('assets.detail', $asset->kode_aset);
            $filename = 'qr_' . $asset->kode_aset . '_' . time() . '.png';
            $qrUrl    = 'https://api.qrserver.com/v1/create-qr-code/?size=300x300&format=png&data=' . urlencode($qrData);
            $qrImage  = @file_get_contents($qrUrl);
            if ($qrImage === false) return false;
            file_put_contents($qrDir . '/' . $filename, $qrImage);
            return true;
        } catch (\Exception $e) {
            \Log::error('QR Code generation failed: ' . $e->getMessage());
            return false;
        }
    }
}
