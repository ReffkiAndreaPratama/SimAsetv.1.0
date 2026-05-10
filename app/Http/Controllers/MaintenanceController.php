<?php

namespace App\Http\Controllers;

use App\Models\Asset;
use App\Models\User;
use App\Mail\MaintenanceAlert;
use App\Helpers\ActivityLogger;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class MaintenanceController extends Controller
{
    public function index(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan'])
            ->where('status', 'Maintenance');

        if ($request->filled('search')) {
            $s = $request->search;
            $query->where(function ($q) use ($s) {
                $q->where('kode_aset', 'like', "%{$s}%")
                  ->orWhereHas('barang', fn($q2) => $q2->where('nama_barang', 'like', "%{$s}%"));
            });
        }

        if ($request->filled('kondisi')) {
            $query->where('kondisi', $request->kondisi);
        }

        $assets = $query->orderBy('updated_at', 'desc')->paginate(15)->withQueryString();

        $totalMaintenance = Asset::where('status', 'Maintenance')->count();
        $rusakBerat       = Asset::where('kondisi', 'Rusak Berat')->count();
        $rusakRingan      = Asset::where('kondisi', 'Rusak Ringan')->count();
        $totalRusak       = $rusakBerat + $rusakRingan;

        return view('maintenance.index', compact(
            'assets', 'totalMaintenance', 'rusakBerat', 'rusakRingan', 'totalRusak'
        ));
    }

    public function complete(Request $request, string $kode_aset)
    {
        $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

        $request->validate([
            'kondisi'    => 'required|in:Baik,Rusak Ringan,Rusak Berat',
            'keterangan' => 'nullable|string|max:500',
        ]);

        $asset->update([
            'status'     => 'Aktif',
            'kondisi'    => $request->kondisi,
            'keterangan' => $request->keterangan ?? $asset->keterangan,
        ]);

        try {
            ActivityLogger::logAsset(
                'Update',
                "Maintenance selesai: {$kode_aset} — kondisi: {$request->kondisi}",
                $asset
            );
        } catch (\Exception $e) {}

        try {
            $admins = User::where('role', 'admin')->get();
            foreach ($admins as $admin) {
                Mail::to($admin->email)->send(new MaintenanceAlert($asset, 'selesai'));
            }
        } catch (\Exception $e) {}

        return redirect()->route('maintenance.index')
            ->with('success', "Maintenance aset {$kode_aset} selesai. Status kembali Aktif.");
    }

    public function setMaintenance(Request $request, string $kode_aset)
    {
        $asset = Asset::where('kode_aset', $kode_aset)->firstOrFail();

        $request->validate([
            'keterangan' => 'nullable|string|max:500',
        ]);

        $asset->update([
            'status'     => 'Maintenance',
            'keterangan' => $request->keterangan ?? $asset->keterangan,
        ]);

        try {
            ActivityLogger::logAsset(
                'Update',
                "Aset masuk maintenance: {$kode_aset}",
                $asset
            );
        } catch (\Exception $e) {}

        return redirect()->back()
            ->with('success', "Aset {$kode_aset} berhasil ditandai sebagai Maintenance.");
    }
}
