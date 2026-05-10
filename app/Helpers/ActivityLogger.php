<?php

namespace App\Helpers;

use App\Models\ActivityLog;
use Illuminate\Support\Facades\Auth;

class ActivityLogger
{
    public static function log(string $aktivitas, string $keterangan = '')
    {
        try {
            return ActivityLog::create([
                'id_user'    => Auth::id(),
                'aktivitas'  => $aktivitas,
                'keterangan' => $keterangan,
                'ip_address' => request()->ip(),
            ]);
        } catch (\Exception $e) {
            \Log::warning('ActivityLogger failed: ' . $e->getMessage());
            return null;
        }
    }

    public static function logAuth(string $aktivitas, string $keterangan = '')
    {
        return self::log($aktivitas, $keterangan);
    }

    public static function logAsset(string $aktivitas, string $keterangan = '', $asset = null)
    {
        return self::log($aktivitas, $keterangan);
    }

    public static function logMutasi(string $aktivitas, string $keterangan = '', $asset = null)
    {
        return self::log($aktivitas, $keterangan);
    }

    public static function logUser(string $aktivitas, string $keterangan = '', $user = null)
    {
        return self::log($aktivitas, $keterangan);
    }
}
