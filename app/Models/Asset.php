<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Asset extends Model
{
    protected $table      = 'aset';
    protected $primaryKey = 'kode_aset';
    public    $incrementing = false;
    protected $keyType    = 'string';

    protected $fillable = [
        'kode_aset',
        'kode_barang',
        'kode_ruangan',
        'id_user',
        'serial_number',
        'kondisi',
        'status',
        'harga',
        'keterangan',
        'foto',
    ];

    protected $casts = [
        'harga'      => 'decimal:2',
        'created_at' => 'datetime',
        'updated_at' => 'datetime',
    ];

    // ── Relationships ──────────────────────────────────────────────

    public function barang()
    {
        return $this->belongsTo(Barang::class, 'kode_barang', 'kode_barang');
    }

    public function ruangan()
    {
        return $this->belongsTo(Ruangan::class, 'kode_ruangan', 'kode_ruangan');
    }

    public function user()
    {
        return $this->belongsTo(User::class, 'id_user', 'id_user');
    }

    // ── Accessors ──────────────────────────────────────────────────

    public function getNamaBarangAttribute(): string
    {
        return $this->barang?->nama_barang ?? '—';
    }

    public function getKategoriAttribute(): string
    {
        return $this->barang?->kategori ?? '—';
    }

    public function getNamaRuanganAttribute(): string
    {
        return $this->ruangan?->nama_ruangan ?? '—';
    }

    // ── Helpers ────────────────────────────────────────────────────

    public static function generateKode(): string
    {
        $existing = self::pluck('kode_aset')
            ->map(fn($k) => (int) str_replace('AST-', '', $k))
            ->filter(fn($n) => $n > 0)
            ->sort()
            ->values();

        $next = 1;
        foreach ($existing as $num) {
            if ($num > $next) break;
            if ($num === $next) $next++;
        }

        return 'AST-' . str_pad($next, 3, '0', STR_PAD_LEFT);
    }
}
