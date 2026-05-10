<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Barang;
use App\Models\Ruangan;
use App\Models\Asset;
use App\Models\User;

class BarangSeeder extends Seeder
{
    public function run(): void
    {
        // ── 1. Seed Ruangan ──────────────────────────────────────────
        $ruanganData = [
            ['kode_ruangan' => 'RNG-001', 'nama_ruangan' => 'Studio Utama',     'lantai' => 'Lantai 1'],
            ['kode_ruangan' => 'RNG-002', 'nama_ruangan' => 'Ruang Editing',    'lantai' => 'Lantai 1'],
            ['kode_ruangan' => 'RNG-003', 'nama_ruangan' => 'Ruang Kontrol',    'lantai' => 'Lantai 1'],
            ['kode_ruangan' => 'RNG-004', 'nama_ruangan' => 'Ruang Audio',      'lantai' => 'Lantai 2'],
            ['kode_ruangan' => 'RNG-005', 'nama_ruangan' => 'Ruang Server',     'lantai' => 'Lantai 2'],
            ['kode_ruangan' => 'RNG-006', 'nama_ruangan' => 'Gudang Peralatan', 'lantai' => 'Lantai 1'],
            ['kode_ruangan' => 'RNG-007', 'nama_ruangan' => 'Ruang Direktur',   'lantai' => 'Lantai 3'],
        ];

        foreach ($ruanganData as $r) {
            Ruangan::firstOrCreate(['kode_ruangan' => $r['kode_ruangan']], $r);
        }

        // ── 2. Seed Master Barang ────────────────────────────────────
        $barangs = [
            // Kamera & Video
            ['kode_barang' => 'BRG-001', 'nama_barang' => 'Kamera Studio Sony HDC-5500',    'kategori' => 'Kamera',           'jumlah' => 0],
            ['kode_barang' => 'BRG-002', 'nama_barang' => 'Kamera Liputan Sony PXW-Z280',   'kategori' => 'Kamera',           'jumlah' => 0],
            ['kode_barang' => 'BRG-003', 'nama_barang' => 'Kamera Cinema Sony FX9',         'kategori' => 'Kamera',           'jumlah' => 0],
            ['kode_barang' => 'BRG-004', 'nama_barang' => 'Action Cam GoPro Hero 12',       'kategori' => 'Kamera',           'jumlah' => 0],
            ['kode_barang' => 'BRG-005', 'nama_barang' => 'Tripod Studio Manfrotto 509HD',  'kategori' => 'Kamera',           'jumlah' => 0],
            // Audio
            ['kode_barang' => 'BRG-006', 'nama_barang' => 'Mikrofon Studio Shure SM7B',     'kategori' => 'Audio',            'jumlah' => 0],
            ['kode_barang' => 'BRG-007', 'nama_barang' => 'Mikrofon Wireless Rode GO II',   'kategori' => 'Audio',            'jumlah' => 0],
            ['kode_barang' => 'BRG-008', 'nama_barang' => 'Audio Mixer Yamaha MG12XU',      'kategori' => 'Audio',            'jumlah' => 0],
            ['kode_barang' => 'BRG-009', 'nama_barang' => 'Headset Broadcast Sony MDR-7506','kategori' => 'Audio',            'jumlah' => 0],
            // Komputer
            ['kode_barang' => 'BRG-010', 'nama_barang' => 'PC Editing Workstation',         'kategori' => 'Komputer',         'jumlah' => 0],
            ['kode_barang' => 'BRG-011', 'nama_barang' => 'Laptop Dell XPS 17',             'kategori' => 'Komputer',         'jumlah' => 0],
            ['kode_barang' => 'BRG-012', 'nama_barang' => 'Laptop MacBook Pro 14',          'kategori' => 'Komputer',         'jumlah' => 0],
            ['kode_barang' => 'BRG-013', 'nama_barang' => 'Monitor Broadcast Sony OLED',    'kategori' => 'Komputer',         'jumlah' => 0],
            // Lighting
            ['kode_barang' => 'BRG-014', 'nama_barang' => 'Lampu Studio LED Aputure 600D',  'kategori' => 'Lighting',         'jumlah' => 0],
            ['kode_barang' => 'BRG-015', 'nama_barang' => 'Lampu Studio LED Godox SL-200W', 'kategori' => 'Lighting',         'jumlah' => 0],
            ['kode_barang' => 'BRG-016', 'nama_barang' => 'Screen Chroma Key Green',        'kategori' => 'Lighting',         'jumlah' => 0],
            ['kode_barang' => 'BRG-017', 'nama_barang' => 'Teleprompter Studio',            'kategori' => 'Lighting',         'jumlah' => 0],
            // Furniture
            ['kode_barang' => 'BRG-018', 'nama_barang' => 'Meja Newsroom Presenter',        'kategori' => 'Furniture',        'jumlah' => 0],
            ['kode_barang' => 'BRG-019', 'nama_barang' => 'Kursi Anchor Studio',            'kategori' => 'Furniture',        'jumlah' => 0],
            ['kode_barang' => 'BRG-020', 'nama_barang' => 'Rak Server Broadcast',           'kategori' => 'Furniture',        'jumlah' => 0],
            // Peralatan Kantor
            ['kode_barang' => 'BRG-021', 'nama_barang' => 'Printer HP LaserJet',            'kategori' => 'Peralatan Kantor', 'jumlah' => 0],
            ['kode_barang' => 'BRG-022', 'nama_barang' => 'AC Split Studio 2 PK',           'kategori' => 'Peralatan Kantor', 'jumlah' => 0],
            ['kode_barang' => 'BRG-023', 'nama_barang' => 'UPS Broadcast 3000VA',           'kategori' => 'Peralatan Kantor', 'jumlah' => 0],
        ];

        foreach ($barangs as $b) {
            Barang::firstOrCreate(['kode_barang' => $b['kode_barang']], $b);
        }

        // ── 3. Seed Aset ─────────────────────────────────────────────
        if (Asset::count() > 0) {
            return;
        }

        $adminId = User::where('email', 'admin@rbtv.co.id')->value('id_user');

        $asets = [
            ['kode_barang' => 'BRG-001', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Kamera studio utama untuk broadcast'],
            ['kode_barang' => 'BRG-001', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Rusak Ringan',  'status' => 'Maintenance', 'keterangan' => 'Sedang diperbaiki — lensa berembun'],
            ['kode_barang' => 'BRG-002', 'kode_ruangan' => 'RNG-006', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Kamera liputan luar'],
            ['kode_barang' => 'BRG-003', 'kode_ruangan' => 'RNG-002', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Kamera cinema produksi'],
            ['kode_barang' => 'BRG-004', 'kode_ruangan' => 'RNG-006', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Action cam angle khusus'],
            ['kode_barang' => 'BRG-005', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Tripod heavy duty studio'],
            ['kode_barang' => 'BRG-006', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Mikrofon broadcast studio'],
            ['kode_barang' => 'BRG-007', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Wireless mic untuk anchor'],
            ['kode_barang' => 'BRG-008', 'kode_ruangan' => 'RNG-003', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Mixer audio analog'],
            ['kode_barang' => 'BRG-009', 'kode_ruangan' => 'RNG-003', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Headset untuk operator'],
            ['kode_barang' => 'BRG-010', 'kode_ruangan' => 'RNG-002', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Workstation editing video'],
            ['kode_barang' => 'BRG-011', 'kode_ruangan' => 'RNG-002', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Laptop portable editor'],
            ['kode_barang' => 'BRG-012', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Laptop untuk reporter'],
            ['kode_barang' => 'BRG-013', 'kode_ruangan' => 'RNG-002', 'kondisi' => 'Rusak Berat',  'status' => 'Non-Aktif',   'keterangan' => 'Panel rusak — menunggu spare part'],
            ['kode_barang' => 'BRG-014', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'LED daylight 600W'],
            ['kode_barang' => 'BRG-015', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'LED 200W studio'],
            ['kode_barang' => 'BRG-016', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Green screen portable'],
            ['kode_barang' => 'BRG-017', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Teleprompter untuk anchor'],
            ['kode_barang' => 'BRG-018', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Meja presenter studio'],
            ['kode_barang' => 'BRG-019', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Kursi putar studio'],
            ['kode_barang' => 'BRG-020', 'kode_ruangan' => 'RNG-005', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Server rack 42U'],
            ['kode_barang' => 'BRG-021', 'kode_ruangan' => 'RNG-006', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'Printer dokumen'],
            ['kode_barang' => 'BRG-022', 'kode_ruangan' => 'RNG-001', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'AC studio utama'],
            ['kode_barang' => 'BRG-023', 'kode_ruangan' => 'RNG-005', 'kondisi' => 'Baik',         'status' => 'Aktif',       'keterangan' => 'UPS backup power'],
        ];

        foreach ($asets as $a) {
            $kode = Asset::generateKode();
            Asset::create(array_merge($a, [
                'kode_aset' => $kode,
                'id_user'   => $adminId,
            ]));
        }
    }
}
