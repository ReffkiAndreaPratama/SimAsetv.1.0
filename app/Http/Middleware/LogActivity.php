<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Helpers\ActivityLogger;
use Symfony\Component\HttpFoundation\Response;

class LogActivity
{
    public function handle(Request $request, Closure $next): Response
    {
        return $next($request);
    }

    public function terminate($request, $response)
    {
        if (!Auth::check()) return;
        if ($response->getStatusCode() < 200 || $response->getStatusCode() >= 400) return;

        $method = $request->method();
        $path   = $request->path();

        // Auth
        if ($path === 'login' && $method === 'POST') {
            ActivityLogger::log('Login', 'User login ke sistem');
            return;
        }
        if ($path === 'logout' && $method === 'POST') {
            ActivityLogger::log('Logout', 'User logout dari sistem');
            return;
        }

        // Aset
        if (preg_match('#^aset$#', $path) && $method === 'POST') {
            ActivityLogger::log('Create', 'Menambahkan aset baru');
        } elseif (preg_match('#^aset/([^/]+)$#', $path, $m) && $method === 'PUT') {
            ActivityLogger::log('Update', 'Memperbarui aset: ' . $m[1]);
        } elseif (preg_match('#^aset/([^/]+)$#', $path, $m) && $method === 'DELETE') {
            ActivityLogger::log('Delete', 'Menghapus aset: ' . $m[1]);
        }

        // Barang
        if (preg_match('#^barang$#', $path) && $method === 'POST') {
            ActivityLogger::log('Create', 'Menambahkan barang baru');
        } elseif (preg_match('#^barang/([^/]+)$#', $path, $m) && $method === 'PUT') {
            ActivityLogger::log('Update', 'Memperbarui barang: ' . $m[1]);
        } elseif (preg_match('#^barang/([^/]+)$#', $path, $m) && $method === 'DELETE') {
            ActivityLogger::log('Delete', 'Menghapus barang: ' . $m[1]);
        }

        // Ruangan
        if (preg_match('#^ruangan$#', $path) && $method === 'POST') {
            ActivityLogger::log('Create', 'Menambahkan ruangan baru');
        } elseif (preg_match('#^ruangan/([^/]+)$#', $path, $m) && $method === 'PUT') {
            ActivityLogger::log('Update', 'Memperbarui ruangan: ' . $m[1]);
        } elseif (preg_match('#^ruangan/([^/]+)$#', $path, $m) && $method === 'DELETE') {
            ActivityLogger::log('Delete', 'Menghapus ruangan: ' . $m[1]);
        }
    }
}
