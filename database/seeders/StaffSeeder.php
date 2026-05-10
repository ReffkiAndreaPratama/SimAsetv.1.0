<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class StaffSeeder extends Seeder
{
    public function run(): void
    {
        User::updateOrCreate(
            ['email' => 'staff@rbtv.co.id'],
            [
                'nama'          => 'Staff RBTV',
                'password_hash' => Hash::make('Staff@123'),
                'role'          => 'staff',
            ]
        );

        User::updateOrCreate(
            ['email' => 'reffkip@gmail.com'],
            [
                'nama'          => 'reffki',
                'password_hash' => Hash::make('Staff@123'),
                'role'          => 'staff',
            ]
        );
    }
}
