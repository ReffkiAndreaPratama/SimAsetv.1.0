<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Barang extends Model
{
    protected $table = 'barang';

    protected $primaryKey = 'kode_barang';
    public $incrementing = false;
    protected $keyType = 'string';

    protected $fillable = [
        'kode_barang',
        'nama_barang',
        'kategori',
        'jumlah',
        'keterangan',
    ];

    protected $casts = [
        'jumlah' => 'integer',
    ];

    public function aset()
    {
        return $this->hasMany(Asset::class, 'kode_barang', 'kode_barang');
    }

    public static function generateKode(): string
    {
        $existing = self::pluck('kode_barang')
            ->map(fn($k) => (int) str_replace('BRG-', '', $k))
            ->filter(fn($n) => $n > 0)
            ->sort()
            ->values();

        $next = 1;
        foreach ($existing as $num) {
            if ($num > $next) break;
            if ($num === $next) $next++;
        }

        return 'BRG-' . str_pad($next, 3, '0', STR_PAD_LEFT);
    }
}
