<?php

namespace App\Http\Controllers;

use App\Models\Asset;
use App\Models\Ruangan;
use Barryvdh\DomPDF\Facade\Pdf;
use Illuminate\Http\Request;

class LaporanController extends Controller
{
    public function index()
    {
        $ruangans = Ruangan::withCount('assets')->orderBy('nama_ruangan')->get();
        return view('laporan.index', compact('ruangans'));
    }

    // ── Helper: apply common filters ──────────────────────────────
    private function applyFilters($query, Request $request): void
    {
        if ($request->filled('kode_ruangan')) {
            $query->where('kode_ruangan', $request->kode_ruangan);
        }
        if ($request->filled('kondisi')) {
            $query->where('kondisi', $request->kondisi);
        }
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }
        if ($request->filled('tanggal_dari')) {
            $query->whereDate('created_at', '>=', $request->tanggal_dari);
        }
        if ($request->filled('tanggal_sampai')) {
            $query->whereDate('created_at', '<=', $request->tanggal_sampai);
        }
    }

    private function periodeLabel(Request $request): string
    {
        $dari    = $request->filled('tanggal_dari')
            ? \Carbon\Carbon::parse($request->tanggal_dari)->format('d/m/Y')
            : null;
        $sampai  = $request->filled('tanggal_sampai')
            ? \Carbon\Carbon::parse($request->tanggal_sampai)->format('d/m/Y')
            : null;

        if ($dari && $sampai) return "{$dari} s/d {$sampai}";
        if ($dari)            return "Mulai {$dari}";
        if ($sampai)          return "Sampai {$sampai}";
        return 'Semua Periode';
    }

    // ── Cetak PDF Aset ─────────────────────────────────────────────
    public function cetakAset(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan'])->orderBy('kode_aset');
        $this->applyFilters($query, $request);

        $assets  = $query->get();
        $periode = $this->periodeLabel($request);

        $pdf = Pdf::loadView('laporan.aset_pdf', compact('assets', 'periode'))
            ->setPaper('a4', 'landscape');
        return $pdf->download('laporan_aset_' . date('d-m-Y') . '.pdf');
    }

    // ── Export CSV Aset ────────────────────────────────────────────
    public function exportAset(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan', 'user'])->orderBy('kode_aset');
        $this->applyFilters($query, $request);

        $assets   = $query->get();
        $filename = 'laporan_aset_' . date('d-m-Y') . '.csv';
        $dicetak  = auth()->user()?->nama ?? 'System';
        $periode  = $this->periodeLabel($request);

        $callback = function () use ($assets, $dicetak, $periode) {
            $handle = fopen('php://output', 'w');
            fprintf($handle, chr(0xEF) . chr(0xBB) . chr(0xBF));

            fputcsv($handle, ['LAPORAN DATA ASET BARANG KANTOR'], ';');
            fputcsv($handle, ['Rakyat Bengkulu Televisi (RBTV) — SimAset v1.0'], ';');
            fputcsv($handle, [''], ';');
            fputcsv($handle, ['Dicetak oleh', $dicetak], ';');
            fputcsv($handle, ['Tanggal cetak', date('d-m-Y H:i')], ';');
            fputcsv($handle, ['Periode', $periode], ';');
            fputcsv($handle, ['Total aset', $assets->count() . ' record'], ';');
            fputcsv($handle, [''], ';');

            fputcsv($handle, [
                'No', 'Kode Aset', 'Kode Barang', 'Nama Barang', 'Kategori',
                'Ruangan', 'Kondisi', 'Status',
                'Harga', 'Serial Number', 'Keterangan', 'Dibuat Oleh', 'Tanggal Input',
            ], ';');

            $no = 1;
            foreach ($assets as $item) {
                fputcsv($handle, [
                    $no++,
                    $item->kode_aset,
                    $item->kode_barang,
                    $item->barang?->nama_barang ?? '-',
                    $item->barang?->kategori ?? '-',
                    $item->ruangan?->nama_ruangan ?? '-',
                    $item->kondisi ?? '-',
                    $item->status ?? '-',
                    $item->harga ? 'Rp ' . number_format($item->harga, 0, ',', '.') : '-',
                    $item->serial_number ?? '-',
                    $item->keterangan ?? '-',
                    $item->user?->nama ?? '-',
                    $item->created_at?->format('d-m-Y H:i') ?? '-',
                ], ';');
            }

            fclose($handle);
        };

        return response()->stream($callback, 200, [
            'Content-Type'        => 'text/csv; charset=UTF-8',
            'Content-Disposition' => "attachment; filename=\"{$filename}\"",
        ]);
    }

    // ── Laporan Per Ruangan ────────────────────────────────────────
    public function laporanRuangan(string $kode_ruangan)
    {
        $ruangan = Ruangan::with(['assets.barang'])->where('kode_ruangan', $kode_ruangan)->firstOrFail();
        $assets  = $ruangan->assets()->with('barang')->orderBy('kode_aset')->get();
        $periode = 'Semua Periode';

        $pdf = Pdf::loadView('laporan.ruangan_pdf', compact('ruangan', 'assets', 'periode'))
            ->setPaper('a4', 'portrait');

        $namaFile = 'laporan_ruangan_' . \Illuminate\Support\Str::slug($ruangan->nama_ruangan) . '_' . date('d-m-Y') . '.pdf';
        return $pdf->download($namaFile);
    }

    // ── Export PDF Maintenance ─────────────────────────────────────
    public function exportMaintenancePdf(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan'])
            ->where('status', 'Maintenance');

        if ($request->filled('tanggal_dari')) {
            $query->whereDate('updated_at', '>=', $request->tanggal_dari);
        }
        if ($request->filled('tanggal_sampai')) {
            $query->whereDate('updated_at', '<=', $request->tanggal_sampai);
        }

        $assets  = $query->orderBy('updated_at', 'desc')->get();
        $periode = $this->periodeLabel($request);

        $pdf = Pdf::loadView('laporan.maintenance_pdf', compact('assets', 'periode'))
            ->setPaper('a4', 'portrait');

        return $pdf->download('laporan_maintenance_' . date('d-m-Y') . '.pdf');
    }

    // ── Export CSV Maintenance ─────────────────────────────────────
    public function exportMaintenanceCsv(Request $request)
    {
        $query = Asset::with(['barang', 'ruangan'])
            ->where('status', 'Maintenance');

        if ($request->filled('tanggal_dari')) {
            $query->whereDate('updated_at', '>=', $request->tanggal_dari);
        }
        if ($request->filled('tanggal_sampai')) {
            $query->whereDate('updated_at', '<=', $request->tanggal_sampai);
        }

        $assets   = $query->orderBy('updated_at', 'desc')->get();
        $filename = 'laporan_maintenance_' . date('d-m-Y') . '.csv';
        $dicetak  = auth()->user()?->nama ?? 'System';
        $periode  = $this->periodeLabel($request);

        $callback = function () use ($assets, $dicetak, $periode) {
            $handle = fopen('php://output', 'w');
            fprintf($handle, chr(0xEF) . chr(0xBB) . chr(0xBF));

            fputcsv($handle, ['LAPORAN ASET MAINTENANCE'], ';');
            fputcsv($handle, ['Rakyat Bengkulu Televisi (RBTV) — SimAset v1.0'], ';');
            fputcsv($handle, [''], ';');
            fputcsv($handle, ['Dicetak oleh', $dicetak], ';');
            fputcsv($handle, ['Tanggal cetak', date('d-m-Y H:i')], ';');
            fputcsv($handle, ['Periode', $periode], ';');
            fputcsv($handle, ['Total aset maintenance', $assets->count() . ' unit'], ';');
            fputcsv($handle, [''], ';');

            fputcsv($handle, [
                'No', 'Kode Aset', 'Nama Barang', 'Kategori',
                'Ruangan', 'Kondisi', 'Serial Number',
                'Keterangan', 'Terakhir Diperbarui',
            ], ';');

            $no = 1;
            foreach ($assets as $item) {
                fputcsv($handle, [
                    $no++,
                    $item->kode_aset,
                    $item->barang?->nama_barang ?? '-',
                    $item->barang?->kategori ?? '-',
                    $item->ruangan?->nama_ruangan ?? '-',
                    $item->kondisi ?? '-',
                    $item->serial_number ?? '-',
                    $item->keterangan ?? '-',
                    $item->updated_at?->format('d-m-Y H:i') ?? '-',
                ], ';');
            }

            fclose($handle);
        };

        return response()->stream($callback, 200, [
            'Content-Type'        => 'text/csv; charset=UTF-8',
            'Content-Disposition' => "attachment; filename=\"{$filename}\"",
        ]);
    }
}
