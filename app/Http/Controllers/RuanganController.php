<?php

namespace App\Http\Controllers;

use App\Models\Ruangan;
use Illuminate\Http\Request;

class RuanganController extends Controller
{
    public function index()
    {
        $ruangans = Ruangan::withCount('assets')->paginate(15);

        $totalRuangan  = Ruangan::count();
        $totalAset     = \App\Models\Asset::count();
        $ruanganKosong = Ruangan::whereDoesntHave('assets')->count();
        $ruanganTerisi = Ruangan::has('assets')->count();

        // All ruangans for PDF modal dropdown (unpaginated)
        $allRuangans = Ruangan::withCount('assets')->orderBy('nama_ruangan')->get();

        return view('ruangan.index', compact(
            'ruangans', 'totalRuangan', 'totalAset', 'ruanganKosong', 'ruanganTerisi', 'allRuangans'
        ));
    }

    public function create()
    {
        return view('ruangan.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'nama_ruangan' => 'required|string|max:100',
            'lantai'       => 'nullable|string|max:20',
            'keterangan'   => 'nullable|string',
        ]);

        $kode = Ruangan::generateKode();
        $validated['kode_ruangan'] = $kode;

        $ruangan = Ruangan::create($validated);

        return redirect()->route('ruangan.index')
            ->with('success', "Ruangan '{$ruangan->nama_ruangan}' berhasil ditambahkan.");
    }

    public function show(Ruangan $ruangan)
    {
        $ruangan->load('assets.barang');
        return view('ruangan.show', compact('ruangan'));
    }

    public function edit(Ruangan $ruangan)
    {
        return view('ruangan.edit', compact('ruangan'));
    }

    public function update(Request $request, Ruangan $ruangan)
    {
        $validated = $request->validate([
            'nama_ruangan' => 'required|string|max:100',
            'lantai'       => 'nullable|string|max:20',
            'keterangan'   => 'nullable|string',
        ]);

        $ruangan->update($validated);

        return redirect()->route('ruangan.index')
            ->with('success', "Ruangan '{$ruangan->nama_ruangan}' berhasil diperbarui.");
    }

    public function destroy(Ruangan $ruangan)
    {
        $jumlahAset = $ruangan->assets()->count();
        if ($jumlahAset > 0) {
            return redirect()->route('ruangan.index')
                ->with('error', "Ruangan '{$ruangan->nama_ruangan}' tidak bisa dihapus karena masih memiliki {$jumlahAset} aset terdaftar.");
        }

        $nama = $ruangan->nama_ruangan;
        $ruangan->delete();
        return redirect()->route('ruangan.index')
            ->with('success', "Ruangan '{$nama}' berhasil dihapus.");
    }
}
