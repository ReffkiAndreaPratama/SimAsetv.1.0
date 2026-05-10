<?php

namespace App\Http\Controllers;

use App\Models\Asset;
use App\Models\Barang;
use App\Exports\AssetExportFile;
use App\Exports\BarangExportFile;
use Barryvdh\DomPDF\Facade\Pdf;
use Maatwebsite\Excel\Facades\Excel;
use Illuminate\Http\Request;
use App\Models\Ruangan;

class ExportController extends Controller
{
    public function excelAset(Request $request)
    {
        $filters  = $request->query();
        $filename = 'aset_' . now()->format('Y-m-d_H-i') . '.xlsx';
        return Excel::download(new AssetExportFile($filters), $filename);
    }

    public function pdfAset(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan', 'user']);
        $this->applyAssetFilters($query, $request);
        $assets = $query->get();

        $periode = $this->periodeLabel($request);
        $pdf = Pdf::loadView('laporan.aset_pdf', compact('assets', 'periode'));
        return $pdf->download('aset_' . now()->format('Y-m-d_H-i') . '.pdf');
    }

    public function excelBarang(Request $request)
    {
        $filters  = $request->query();
        $filename = 'barang_' . now()->format('Y-m-d_H-i') . '.xlsx';
        return Excel::download(new BarangExportFile($filters), $filename);
    }

    public function pdfBarang(Request $request)
    {
        $query = Barang::withCount('aset');
        $this->applyBarangFilters($query, $request);
        $barangs = $query->orderBy('kode_barang')->get();

        $pdf = Pdf::loadView('laporan.barang_pdf', compact('barangs'));
        return $pdf->download('barang_' . now()->format('Y-m-d_H-i') . '.pdf');
    }

    private function periodeLabel(Request $request): string
    {
        $dari   = $request->filled('tanggal_dari')
            ? \Carbon\Carbon::parse($request->tanggal_dari)->format('d/m/Y') : null;
        $sampai = $request->filled('tanggal_sampai')
            ? \Carbon\Carbon::parse($request->tanggal_sampai)->format('d/m/Y') : null;
        if ($dari && $sampai) return "{$dari} s/d {$sampai}";
        if ($dari)            return "Mulai {$dari}";
        if ($sampai)          return "Sampai {$sampai}";
        return 'Semua Periode';
    }

    private function applyAssetFilters($query, Request $request)
    {
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }
        if ($request->filled('kondisi')) {
            $query->where('kondisi', $request->kondisi);
        }
        if ($request->filled('kode_ruangan')) {
            $query->where('kode_ruangan', $request->kode_ruangan);
        }
        if ($request->filled('search')) {
            $query->whereHas('barang', function ($q) use ($request) {
                $q->where('nama_barang', 'like', '%' . $request->search . '%');
            });
        }
        if ($request->filled('kategori')) {
            $query->whereHas('barang', function ($q) use ($request) {
                $q->where('kategori', 'like', '%' . $request->kategori . '%');
            });
        }
        if ($request->filled('tanggal_dari')) {
            $query->whereDate('created_at', '>=', $request->tanggal_dari);
        }
        if ($request->filled('tanggal_sampai')) {
            $query->whereDate('created_at', '<=', $request->tanggal_sampai);
        }
    }

    private function applyBarangFilters($query, Request $request)
    {
        if ($request->filled('kategori')) {
            $query->where('kategori', 'like', '%' . $request->kategori . '%');
        }
        if ($request->filled('search')) {
            $query->where('nama_barang', 'like', '%' . $request->search . '%');
        }
        if ($request->filled('tanggal_dari')) {
            $query->whereDate('created_at', '>=', $request->tanggal_dari);
        }
        if ($request->filled('tanggal_sampai')) {
            $query->whereDate('created_at', '<=', $request->tanggal_sampai);
        }
    }
}
