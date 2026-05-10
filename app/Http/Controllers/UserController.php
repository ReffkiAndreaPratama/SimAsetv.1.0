<?php

namespace App\Http\Controllers;

use App\Models\User;
use App\Mail\AkunBaruMail;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Mail;

class UserController extends Controller
{
    public function index()
    {
        $users = User::orderBy('role')->get();
        return view('users.index', compact('users'));
    }

    public function create()
    {
        return view('users.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'nama'        => 'required|string|max:100',
            'email'       => 'required|email|unique:users,email',
            'password'    => 'required|min:8|regex:/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/',
            'role'        => 'required|in:admin,staff',
            'kirim_email' => 'nullable|boolean',
        ], [
            'password.regex' => 'Password minimal 8 karakter, mengandung huruf besar, huruf kecil, dan angka.',
        ]);

        $plainPassword = $request->password;

        $user = User::create([
            'nama'          => $request->nama,
            'email'         => $request->email,
            'password_hash' => Hash::make($plainPassword),
            'role'          => $request->role,
        ]);

        if ($request->boolean('kirim_email')) {
            try {
                Mail::to($user->email)->send(new AkunBaruMail(
                    $user->nama,
                    $user->email,
                    $plainPassword,
                    $user->role
                ));
            } catch (\Exception $e) {
                // Email gagal, akun tetap dibuat
            }
        }

        return redirect()->route('users.index')
            ->with('success', 'User berhasil ditambahkan' . ($request->boolean('kirim_email') ? ' & email notifikasi dikirim' : ''));
    }

    public function show(User $user)
    {
        return redirect()->route('users.index');
    }

    public function edit(User $user)
    {
        return view('users.edit', compact('user'));
    }

    public function update(Request $request, User $user)
    {
        $request->validate([
            'nama'     => 'required|string|max:100',
            'email'    => 'required|email|unique:users,email,' . $user->id_user . ',id_user',
            'role'     => 'required|in:admin,staff',
            'password' => 'nullable|min:8|regex:/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/',
        ], [
            'password.regex' => 'Password minimal 8 karakter, mengandung huruf besar, huruf kecil, dan angka.',
        ]);

        $data = [
            'nama'  => $request->nama,
            'email' => $request->email,
            'role'  => $request->role,
        ];

        if ($request->filled('password')) {
            $data['password_hash'] = Hash::make($request->password);
        }

        $user->update($data);

        return redirect()->route('users.index')
            ->with('success', 'User berhasil diupdate');
    }

    public function destroy(User $user)
    {
        if (auth()->id() === $user->id_user) {
            return back()->with('error', 'Tidak bisa menghapus akun sendiri');
        }

        $user->delete();

        return redirect()->route('users.index')
            ->with('success', 'User berhasil dihapus');
    }
}
