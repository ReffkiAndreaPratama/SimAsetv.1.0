<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class AdminSeeder extends Seeder
{
    public function run(): void
    {
        User::updateOrCreate(
            ['email' => 'admin@rbtv.co.id'],
            [
                'nama'          => 'Admin RBTV',
                'password_hash' => Hash::make('Admin@123'),
                'role'          => 'admin',
            ]
        );

        User::updateOrCreate(
            ['email' => 'magangrbtv@gmail.com'],
            [
                'nama'          => 'Admin Magang',
                'password_hash' => Hash::make('Admin@123'),
                'role'          => 'admin',
            ]
        );
    }
}
