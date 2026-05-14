<?php

define('LARAVEL_START', microtime(true));

// Tampilkan semua error untuk debug
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$root = dirname(__DIR__);
chdir($root);

// Buat direktori yang diperlukan di /tmp (Vercel read-only)
$dirs = [
    '/tmp/storage/framework/cache/data',
    '/tmp/storage/framework/sessions',
    '/tmp/storage/framework/views',
    '/tmp/storage/logs',
    '/tmp/storage/app/public',
    '/tmp/bootstrap/cache',
];
foreach ($dirs as $dir) {
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
}

// Override storage path ke /tmp
if (!defined('LARAVEL_STORAGE_PATH')) {
    define('LARAVEL_STORAGE_PATH', '/tmp/storage');
}

require $root . '/vendor/autoload.php';

$app = require_once $root . '/bootstrap/app.php';

// Override storage path
$app->useStoragePath('/tmp/storage');

$app->handleRequest(Illuminate\Http\Request::capture());