---
# LAMPIRAN

## Lampiran 1. Kerangka Acuan Kerja Praktik

*(Terlampir dokumen Kerangka Acuan Kerja Praktik yang telah disetujui oleh Dosen Pembimbing, Pembimbing Lapangan, dan Ketua Program Studi Informatika)*

---

## Lampiran 2. Lembar Persetujuan Seminar Kerja Praktik

**LEMBAR PERSETUJUAN SEMINAR KERJA PRAKTIK**

**RANCANG BANGUN SISTEM INFORMASI MANAJEMEN ASET BARANG KANTOR RBTV BENGKULU**

disusun oleh

| Nama | : | Reffki Andrea Pratama |
|---|---|---|
| NPM | : | G1A023039 |

Telah diuji di lokasi Kerja Praktik dan disetujui untuk dapat mengikuti seminar Kerja Praktik yang bertempat di Dekanat Fakultas Teknik Universitas Bengkulu.

&nbsp;

| Bengkulu, .................. 2026 | |
|---|---|
| Dosen Pembimbing | Pembimbing Lapangan |
| &nbsp; | &nbsp; |
| &nbsp; | &nbsp; |
| &nbsp; | &nbsp; |
| **Ir. Kurnia Anggriani, S.T., M.T., Ph.D.** | **Septi Fitriani, M.Pd.** |
| NIP. 197308142006042001 | NIP. .................. |

---

## Lampiran 3. Lembar Konsultasi Bimbingan Kerja Praktik

**LEMBAR KONSULTASI BIMBINGAN KERJA PRAKTIK**

| Nama Mahasiswa | : | Reffki Andrea Pratama |
|---|---|---|
| Nomor Pokok Mahasiswa | : | G1A023039 |
| Semester/Tahun Akademik | : | VI/2025-2026 |
| Program Studi/Fakultas | : | Informatika/Teknik |
| Lembaga/Perusahaan/Tempat KP | : | RBTV Bengkulu |
| Judul/Topik KP | : | Rancang Bangun Sistem Informasi Manajemen Aset Barang Kantor RBTV Bengkulu |

&nbsp;

| No. | Tanggal | Uraian Konsultasi | Paraf Pembimbing |
|---|---|---|---|
| 1. | | | |
| 2. | | | |
| 3. | | | |
| 4. | | | |
| 5. | | | |
| 6. | | | |
| 7. | | | |
| 8. | | | |
| 9. | | | |
| 10. | | | |

*Nb. Setiap mahasiswa sedikitnya melakukan 10 kali pertemuan bimbingan dengan Dosen Pembimbing.*

&nbsp;

| Mahasiswa Kerja Praktik | Dosen Pembimbing |
|---|---|
| &nbsp; | &nbsp; |
| &nbsp; | &nbsp; |
| &nbsp; | &nbsp; |
| **Reffki Andrea Pratama** | **Ir. Kurnia Anggriani, S.T., M.T., Ph.D.** |
| G1A023039 | NIP. 197308142006042001 |

---

## Lampiran 4. Listing Kode Program

*(Terlampir potongan kode program utama sistem, meliputi kode controller, model, dan view yang relevan)*

**a. AssetController.php (Fungsi Store)**

```php
public function store(Request $request)
{
    $validated = $request->validate([
        'kode_aset'        => 'required|unique:aset,kode_aset',
        'nama_aset'        => 'required|string|max:255',
        'kode_barang'      => 'required|exists:barang,kode_barang',
        'id_ruangan'       => 'required|exists:ruangan,id',
        'kondisi'          => 'required|in:Baik,Rusak Ringan,Rusak Berat',
        'tahun_perolehan'  => 'required|digits:4',
        'harga_perolehan'  => 'nullable|numeric|min:0',
        'sumber_perolehan' => 'nullable|string|max:100',
        'foto'             => 'nullable|image|max:2048',
        'keterangan'       => 'nullable|string',
    ]);

    if ($request->hasFile('foto')) {
        $validated['foto'] = $request->file('foto')
            ->store('aset/foto', 'public');
    }

    $aset = Asset::create($validated);

    // Generate QR Code
    $qrPath = 'aset/qr/' . $aset->kode_aset . '.png';
    QrCode::format('png')
        ->size(200)
        ->generate(route('aset.show', $aset->id), storage_path('app/public/' . $qrPath));
    $aset->update(['qr_code' => $qrPath]);

    ActivityLogger::log('Tambah Aset', 'Menambahkan aset baru: ' . $aset->nama_aset);

    return redirect()->route('aset.index')
        ->with('success', 'Data aset berhasil ditambahkan.');
}
```

**b. Asset.php (Model)**

```php
class Asset extends Model
{
    use HasFactory, SoftDeletes;

    protected $table = 'aset';

    protected $fillable = [
        'kode_aset', 'nama_aset', 'kode_barang', 'id_ruangan',
        'kondisi', 'tahun_perolehan', 'harga_perolehan',
        'sumber_perolehan', 'foto', 'qr_code', 'keterangan',
    ];

    public function barang()
    {
        return $this->belongsTo(Barang::class, 'kode_barang', 'kode_barang');
    }

    public function ruangan()
    {
        return $this->belongsTo(Ruangan::class, 'id_ruangan');
    }

    public function maintenances()
    {
        return $this->hasMany(Maintenance::class, 'aset_id');
    }
}
```

---

## Lampiran 5. Surat Keterangan Pelaksanaan Kerja Praktik

*(Terlampir surat keterangan dari RBTV Bengkulu yang menyatakan bahwa mahasiswa telah melaksanakan Kerja Praktik di instansi tersebut)*

---

## Lampiran 6. Form Penilaian Pembimbing Lapangan

*(Terlampir form penilaian yang telah diisi dan ditandatangani oleh Pembimbing Lapangan RBTV Bengkulu)*
