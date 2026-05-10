<?php

namespace App\Http\Controllers;

use App\Models\Asset;
use App\Models\Barang;
use App\Models\Ruangan;
use App\Models\ActivityLog;
use Illuminate\Support\Facades\DB;
use Carbon\Carbon;

class DashboardController extends Controller
{
    public function index()
    {
        $totalAset       = Asset::count();
        $asetAktif       = Asset::where('status', 'Aktif')->count();
        $asetNonaktif    = Asset::where('status', 'Non-Aktif')->count();
        $asetMaintenance = Asset::where('status', 'Maintenance')->count();
        $asetRusak       = Asset::whereIn('kondisi', ['Rusak Ringan', 'Rusak Berat'])->count();
        $totalBarang     = Barang::count();
        $totalRuangan    = Ruangan::count();

        $now = Carbon::now();
        $asetBulanIni = Asset::whereMonth('created_at', $now->month)
            ->whereYear('created_at', $now->year)->count();

        $kondisiDistribusi = Asset::select('kondisi', DB::raw('count(*) as total'))
            ->whereNotNull('kondisi')
            ->groupBy('kondisi')->get();

        $kategoriDistribusi = Asset::select('barang.kategori', DB::raw('count(*) as total'))
            ->join('barang', 'aset.kode_barang', '=', 'barang.kode_barang')
            ->whereNotNull('barang.kategori')
            ->groupBy('barang.kategori')
            ->orderByDesc('total')->limit(5)->get();

        $recentAssets = Asset::with(['barang', 'ruangan'])
            ->orderByDesc('created_at')->take(10)->get();

        $recentLogs = ActivityLog::with('user')
            ->orderByDesc('created_at')->take(8)->get();

        $maintCount = Asset::where('status', 'Maintenance')->count();

        return view('dashboard', compact(
            'totalAset', 'asetAktif', 'asetNonaktif', 'asetMaintenance', 'asetRusak',
            'totalBarang', 'totalRuangan', 'asetBulanIni',
            'kondisiDistribusi', 'kategoriDistribusi', 'recentAssets',
            'recentLogs', 'maintCount'
        ));
    }
}
