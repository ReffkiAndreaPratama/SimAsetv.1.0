<?php

define('LARAVEL_START', microtime(true));

// Vercel menaruh file di /var/task/user, tapi __DIR__ = /var/task/user/api
// Jadi root = dirname(__DIR__) = /var/task/user
$root = dirname(__DIR__);

// Set working directory
chdir($root);

// Pastikan storage & cache bisa ditulis (Vercel read-only, pakai /tmp)
$storagePath = '/tmp/storage';
$dirs = [
    $storagePath . '/framework/cache/data',
    $storagePath . '/framework/sessions',
    $storagePath . '/framework/views',
    $storagePath . '/logs',
    $storagePath . '/app/public',
];
foreach ($dirs as $dir) {
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
}

// Symlink storage ke /tmp jika belum ada
if (!is_dir($root . '/storage/framework/views')) {
    @mkdir($root . '/storage/framework/views', 0755, true);
}
if (!is_dir($root . '/storage/framework/sessions')) {
    @mkdir($root . '/storage/framework/sessions', 0755, true);
}
if (!is_dir($root . '/storage/framework/cache/data')) {
    @mkdir($root . '/storage/framework/cache/data', 0755, true);
}
if (!is_dir($root . '/storage/logs')) {
    @mkdir($root . '/storage/logs', 0755, true);
}
if (!is_dir($root . '/bootstrap/cache')) {
    @mkdir($root . '/bootstrap/cache', 0755, true);
}

// Load autoloader
require $root . '/vendor/autoload.php';

// Bootstrap Laravel
$app = require_once $root . '/bootstrap/app.php';

// Handle request
$app->handleRequest(Illuminate\Http\Request::capture());