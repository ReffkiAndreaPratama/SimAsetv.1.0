<?php

namespace App\Http\Controllers;

use App\Models\Barang;
use Illuminate\Http\Request;

class BarangController extends Controller
{
    public function index(Request $request)
    {
        $query = Barang::query();

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('kode_barang', 'like', "%{$search}%")
                  ->orWhere('nama_barang', 'like', "%{$search}%");
            });
        }

        if ($request->filled('kategori')) {
            $query->where('kategori', $request->kategori);
        }

        $barangs = $query->orderBy('kode_barang')->paginate(15)->withQueryString();

        return view('barang.index', compact('barangs'));
    }

    public function create()
    {
        return view('barang.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'nama_barang' => 'required|string|max:100',
            'kategori'    => 'nullable|string|max:100',
            'jumlah'      => 'nullable|integer|min:0',
            'keterangan'  => 'nullable|string',
        ]);

        $kode = Barang::generateKode();
        $validated['kode_barang'] = $kode;
        $validated['jumlah']      = $validated['jumlah'] ?? 0;

        Barang::create($validated);

        return redirect()->route('barang.index')
            ->with('success', "Barang '{$validated['nama_barang']}' berhasil ditambahkan dengan kode {$kode}.");
    }

    public function show(Barang $barang)
    {
        return view('barang.show', compact('barang'));
    }

    public function edit(Barang $barang)
    {
        return view('barang.edit', compact('barang'));
    }

    public function update(Request $request, Barang $barang)
    {
        $validated = $request->validate([
            'nama_barang' => 'required|string|max:100',
            'kategori'    => 'nullable|string|max:100',
            'jumlah'      => 'nullable|integer|min:0',
            'keterangan'  => 'nullable|string',
        ]);

        $barang->update($validated);

        return redirect()->route('barang.index')
            ->with('success', "Barang '{$validated['nama_barang']}' berhasil diperbarui.");
    }

    public function destroy(Barang $barang)
    {
        $nama = $barang->nama_barang;
        $barang->delete();
        return redirect()->route('barang.index')
            ->with('success', "Barang '{$nama}' berhasil dihapus.");
    }
}
