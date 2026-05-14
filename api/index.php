<?php
$root = '/var/task/user';
chdir($root);

foreach ([
    '/tmp/storage/framework/cache/data',
    '/tmp/storage/framework/sessions',
    '/tmp/storage/framework/views',
    '/tmp/storage/logs',
    '/tmp/storage/app/public',
    '/tmp/bootstrap/cache',
] as $dir) {
    is_dir($dir) || mkdir($dir, 0755, true);
}

// Copy bootstrap cache files ke /tmp agar bisa ditulis
foreach (['packages.php', 'services.php'] as $file) {
    $src = $root . '/bootstrap/cache/' . $file;
    $dst = '/tmp/bootstrap/cache/' . $file;
    if (file_exists($src) && !file_exists($dst)) {
        copy($src, $dst);
    }
}

// Symlink bootstrap/cache -> /tmp/bootstrap/cache
$cacheDir = $root . '/bootstrap/cache';
if (is_dir($cacheDir) && !is_link($cacheDir)) {
    // Hapus isi direktori dulu
    array_map('unlink', glob($cacheDir . '/*'));
    rmdir($cacheDir);
    symlink('/tmp/bootstrap/cache', $cacheDir);
} elseif (!file_exists($cacheDir)) {
    symlink('/tmp/bootstrap/cache', $cacheDir);
}

require $root . '/vendor/autoload.php';

$app = require_once $root . '/bootstrap/app.php';
$app->useStoragePath('/tmp/storage');

try {
    $app->handleRequest(Illuminate\Http\Request::capture());
} catch (\Throwable $e) {
    http_response_code(500);
    header('Content-Type: text/plain');
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo $e->getTraceAsString();
}