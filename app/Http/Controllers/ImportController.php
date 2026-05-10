<?php

namespace App\Http\Controllers;

use App\Models\Asset;
use App\Models\Barang;
use App\Models\Ruangan;
use Illuminate\Http\Request;
use Maatwebsite\Excel\Facades\Excel;

class ImportController extends Controller
{
    public function store(Request $request)
    {
        $request->validate([
            'file' => 'required|file|mimes:xlsx,xls,csv',
            'type' => 'required|in:aset,barang',
        ], [
            'file.required' => 'File harus dipilih',
            'file.mimes'    => 'File harus berformat Excel atau CSV',
            'type.required' => 'Tipe import harus dipilih',
            'type.in'       => 'Tipe import tidak valid',
        ]);

        $type = $request->input('type', 'aset');
        return $this->processImport($request, $type);
    }

    private function processImport(Request $request, $type)
    {
        try {
            $file   = $request->file('file');
            $data   = [];
            $errors = [];
            $count  = 0;

            if ($file->getClientOriginalExtension() === 'csv') {
                $data = $this->readCSV($file);
            } else {
                $data = Excel::toArray([], $file)[0];
            }

            foreach ($data as $index => $row) {
                if ($index === 0) continue;

                if ($type === 'aset') {
                    $result = $this->validateAndCreateAsset($row, $index + 1);
                } else {
                    $result = $this->validateAndCreateBarang($row, $index + 1);
                }

                if ($result['success']) {
                    $count++;
                } else {
                    $errors[] = $result['error'];
                }
            }

            $typeName = $type === 'aset' ? 'aset' : 'barang';
            return back()->with([
                'success'  => true,
                'message'  => "Berhasil import $count data $typeName. " . (count($errors) > 0 ? 'Error: ' . implode(', ', $errors) : ''),
                'imported' => $count,
                'failed'   => count($errors),
            ]);

        } catch (\Exception $e) {
            return back()->with([
                'success' => false,
                'message' => 'Error: ' . $e->getMessage(),
            ]);
        }
    }

    public function template(Request $request)
    {
        $type     = $request->query('type', 'aset');
        $filename = $type . '_import_template.csv';

        $callback = function () use ($type) {
            $handle = fopen('php://output', 'w');
            fprintf($handle, chr(0xEF) . chr(0xBB) . chr(0xBF));

            if ($type === 'aset') {
                $header = [
                    'Kode Barang',
                    'Kode Ruangan',
                    'Kondisi (Baik/Rusak Ringan/Rusak Berat)',
                    'Status (Aktif/Maintenance/Non-Aktif)',
                    'Serial Number',
                    'Harga',
                    'Keterangan',
                ];
                fputcsv($handle, $header, ';');
                fputcsv($handle, ['BRG-001', 'RNG-001', 'Baik', 'Aktif', 'SN-001', '5000000', 'Catatan'], ';');
            } else {
                $header = ['Kode Barang', 'Nama Barang', 'Kategori', 'Jumlah', 'Keterangan'];
                fputcsv($handle, $header, ';');
                fputcsv($handle, ['BRG-001', 'Laptop Dell', 'Komputer', '1', 'Catatan'], ';');
            }

            fclose($handle);
        };

        return response()->stream($callback, 200, [
            'Content-Type'        => 'text/csv; charset=UTF-8',
            'Content-Disposition' => "attachment; filename=\"$filename\"",
        ]);
    }

    private function readCSV($file)
    {
        $data   = [];
        $handle = fopen($file->getRealPath(), 'r');

        while (($line = fgetcsv($handle, 1000, ';')) !== false) {
            if (count($line) == 1 && strpos($line[0], ',') !== false) {
                $line = explode(',', $line[0]);
            }
            $data[] = $line;
        }

        fclose($handle);
        return $data;
    }

    /**
     * Columns: A=kode_barang, B=kode_ruangan, C=kondisi, D=status, E=serial_number, F=harga, G=keterangan
     */
    private function validateAndCreateAsset($row, $lineNumber)
    {
        try {
            if (empty($row[0])) {
                return ['success' => false, 'error' => "Baris $lineNumber: Kode Barang wajib diisi"];
            }

            $kodeBarang = trim($row[0]);
            $barang     = Barang::where('kode_barang', $kodeBarang)->first();
            if (! $barang) {
                return ['success' => false, 'error' => "Baris $lineNumber: Barang dengan kode {$kodeBarang} tidak ditemukan"];
            }

            $kodeRuangan = null;
            if (! empty($row[1])) {
                $ruangan     = Ruangan::where('kode_ruangan', trim($row[1]))->first();
                $kodeRuangan = $ruangan?->kode_ruangan;
            }

            if (! empty($row[4])) {
                $exists = Asset::where('serial_number', trim($row[4]))->exists();
                if ($exists) {
                    return ['success' => false, 'error' => "Baris $lineNumber: Serial number {$row[4]} sudah terdaftar"];
                }
            }

            $kode_aset = Asset::generateKode();

            Asset::create([
                'kode_aset'     => $kode_aset,
                'kode_barang'   => $kodeBarang,
                'kode_ruangan'  => $kodeRuangan,
                'id_user'       => auth()->id(),
                'kondisi'       => $this->normalizeKondisi(trim($row[2] ?? 'Baik')),
                'status'        => $this->normalizeStatus(trim($row[3] ?? 'Aktif')),
                'serial_number' => ! empty($row[4]) ? trim($row[4]) : null,
                'harga'         => ! empty($row[5]) ? (float) str_replace(['.', ','], ['', '.'], trim($row[5])) : null,
                'keterangan'    => trim($row[6] ?? ''),
            ]);

            return ['success' => true];

        } catch (\Exception $e) {
            return ['success' => false, 'error' => "Baris $lineNumber: " . $e->getMessage()];
        }
    }

    private function validateAndCreateBarang($row, $lineNumber)
    {
        try {
            if (empty($row[0]) || empty($row[1])) {
                return ['success' => false, 'error' => "Baris $lineNumber: Kode/Nama Barang wajib diisi"];
            }

            $kodeBarang = trim($row[0]);
            if (Barang::where('kode_barang', $kodeBarang)->exists()) {
                return ['success' => false, 'error' => "Baris $lineNumber: Kode Barang '$kodeBarang' sudah ada"];
            }

            Barang::create([
                'kode_barang' => $kodeBarang,
                'nama_barang' => trim($row[1]),
                'kategori'    => trim($row[2] ?? ''),
                'jumlah'      => intval($row[3] ?? 0),
                'keterangan'  => trim($row[4] ?? ''),
            ]);

            return ['success' => true];

        } catch (\Exception $e) {
            return ['success' => false, 'error' => "Baris $lineNumber: " . $e->getMessage()];
        }
    }

    private function normalizeKondisi($value)
    {
        $map = [
            'baik'         => 'Baik',
            'rusak ringan' => 'Rusak Ringan',
            'rusak_ringan' => 'Rusak Ringan',
            'rusak berat'  => 'Rusak Berat',
            'rusak_berat'  => 'Rusak Berat',
        ];
        return $map[strtolower(str_replace('_', ' ', $value))] ?? 'Baik';
    }

    private function normalizeStatus($value)
    {
        $map = [
            'aktif'       => 'Aktif',
            'active'      => 'Aktif',
            'maintenance' => 'Maintenance',
            'non-aktif'   => 'Non-Aktif',
            'nonaktif'    => 'Non-Aktif',
            'non aktif'   => 'Non-Aktif',
        ];
        return $map[strtolower($value)] ?? 'Aktif';
    }
}
