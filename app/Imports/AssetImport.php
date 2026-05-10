<?php

namespace App\Imports;

use App\Models\Asset;
use App\Models\Barang;
use App\Models\Ruangan;
use Maatwebsite\Excel\Concerns\ToModel;
use Maatwebsite\Excel\Concerns\WithHeadingRow;
use Maatwebsite\Excel\Concerns\SkipsEmptyRows;

class AssetImport implements ToModel, WithHeadingRow, SkipsEmptyRows
{
    protected $errors = [];
    protected $row    = 0;

    public function model(array $row)
    {
        $this->row++;

        try {
            if (empty($row['kode_barang']) || empty($row['kode_ruangan'])) {
                throw new \Exception("Baris {$this->row}: Kode barang dan kode ruangan diperlukan");
            }

            $barang = Barang::where('kode_barang', $row['kode_barang'])->first();
            if (! $barang) {
                throw new \Exception("Baris {$this->row}: Barang dengan kode {$row['kode_barang']} tidak ditemukan");
            }

            $ruangan = Ruangan::where('kode_ruangan', $row['kode_ruangan'])->first();
            if (! $ruangan) {
                throw new \Exception("Baris {$this->row}: Ruangan dengan kode {$row['kode_ruangan']} tidak ditemukan");
            }

            if (! empty($row['serial_number'])) {
                $exists = Asset::where('serial_number', $row['serial_number'])->exists();
                if ($exists) {
                    throw new \Exception("Baris {$this->row}: Serial number {$row['serial_number']} sudah terdaftar");
                }
            }

            $kodeAset = Asset::generateKode();

            return new Asset([
                'kode_aset'     => $kodeAset,
                'kode_barang'   => $row['kode_barang'],
                'kode_ruangan'  => $row['kode_ruangan'],
                'id_user'       => auth()->id(),
                'serial_number' => $row['serial_number'] ?? null,
                'kondisi'       => $row['kondisi'] ?? 'Baik',
                'status'        => $row['status'] ?? 'Aktif',
                'harga'         => $row['harga'] ?? null,
                'keterangan'    => $row['keterangan'] ?? null,
            ]);
        } catch (\Exception $e) {
            $this->errors[] = $e->getMessage();
            return null;
        }
    }

    public function getErrors()
    {
        return $this->errors;
    }
}
