<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Http\Requests\Auth\LoginRequest;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\View\View;

class AuthenticatedSessionController extends Controller
{
    public function create(): View
    {
        return view('auth.login');
    }

    public function store(LoginRequest $request): RedirectResponse
    {
        $request->authenticate();
        $request->session()->regenerate();

        try {
            \App\Helpers\ActivityLogger::logAuth(
                'Login',
                'User berhasil login: ' . Auth::user()->nama . ' (' . Auth::user()->email . ')'
            );
        } catch (\Exception $e) {}

        return redirect()->route('dashboard');
    }

    public function destroy(Request $request): RedirectResponse
    {
        $nama = Auth::user()?->nama ?? 'Unknown';

        try {
            \App\Helpers\ActivityLogger::logAuth('Logout', "User logout: {$nama}");
        } catch (\Exception $e) {}

        Auth::guard('web')->logout();
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        return redirect('/');
    }
}
