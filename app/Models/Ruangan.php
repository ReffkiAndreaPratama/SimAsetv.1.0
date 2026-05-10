<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Ruangan extends Model
{
    protected $table = 'ruangan';

    protected $primaryKey = 'kode_ruangan';
    public $incrementing = false;
    protected $keyType = 'string';

    protected $fillable = [
        'kode_ruangan',
        'nama_ruangan',
        'lantai',
        'keterangan',
    ];

    public function assets()
    {
        return $this->hasMany(Asset::class, 'kode_ruangan', 'kode_ruangan');
    }

    public static function generateKode(): string
    {
        $existing = self::pluck('kode_ruangan')
            ->map(fn($k) => (int) str_replace('RNG-', '', $k))
            ->filter(fn($n) => $n > 0)
            ->sort()
            ->values();

        $next = 1;
        foreach ($existing as $num) {
            if ($num > $next) break;
            if ($num === $next) $next++;
        }

        return 'RNG-' . str_pad($next, 3, '0', STR_PAD_LEFT);
    }
}
