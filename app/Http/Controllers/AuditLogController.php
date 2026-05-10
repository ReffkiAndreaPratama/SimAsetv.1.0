<?php

namespace App\Http\Controllers;

use App\Models\ActivityLog;
use Illuminate\Http\Request;

class AuditLogController extends Controller
{
    public function index(Request $request)
    {
        $query = ActivityLog::with('user')->orderBy('created_at', 'desc');

        if ($request->filled('search')) {
            $s = $request->search;
            $query->where(function ($q) use ($s) {
                $q->where('aktivitas',   'like', "%{$s}%")
                  ->orWhere('keterangan', 'like', "%{$s}%");
            });
        }

        if ($request->filled('user_id')) {
            $query->where('id_user', $request->user_id);
        }

        if ($request->filled('module')) {
            $query->where('aktivitas', 'like', '%' . $request->module . '%');
        }

        $logs    = $query->paginate(20)->withQueryString();
        $users   = \App\Models\User::orderBy('nama')->get(['id_user', 'nama']);
        $modules = ['Login', 'Logout', 'Create', 'Update', 'Delete'];

        return view('audit_log.index', compact('logs', 'users', 'modules'));
    }
}
