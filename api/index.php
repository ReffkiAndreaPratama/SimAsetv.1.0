<?php
$root = '/var/task/user';
chdir($root);

// Buat semua direktori yang diperlukan di /tmp
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

// Symlink bootstrap/cache ke /tmp/bootstrap/cache
$bootstrapCache = $root . '/bootstrap/cache';
if (!is_link($bootstrapCache) && is_dir($bootstrapCache)) {
    // Copy existing files ke /tmp dulu
    foreach (glob($bootstrapCache . '/*') as $file) {
        copy($file, '/tmp/bootstrap/cache/' . basename($file));
    }
    // Hapus direktori asli dan buat symlink
    rmdir($bootstrapCache);
    symlink('/tmp/bootstrap/cache', $bootstrapCache);
}

require $root . '/vendor/autoload.php';

$app = require_once $root . '/bootstrap/app.php';
$app->useStoragePath('/tmp/storage');

try {
    $app->handleRequest(Illuminate\Http\Request::capture());
} catch (\Throwable $e) {
    http_response_code(500);
    header('Content-Type: text/plain');
    echo "ERROR: " . $e->getMessage() . "\n\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n\n";
    echo "TRACE:\n" . $e->getTraceAsString();
}