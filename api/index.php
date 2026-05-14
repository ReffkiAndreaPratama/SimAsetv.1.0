<?php
$root = '/var/task/user';
chdir($root);

// Setup /tmp dirs
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

// Salin cache files ke /tmp jika ada
foreach (['packages.php', 'services.php', 'config.php', 'routes-v7.php', 'events.php'] as $file) {
    $src = $root . '/bootstrap/cache/' . $file;
    $dst = '/tmp/bootstrap/cache/' . $file;
    if (file_exists($src) && !file_exists($dst)) {
        copy($src, $dst);
    }
}

// Patch: buat wrapper autoloader yang intercept PackageManifest
require $root . '/vendor/autoload.php';

// Monkey-patch: override bootstrap cache path via env
putenv('APP_BOOTSTRAP_CACHE=/tmp/bootstrap/cache');
$_ENV['APP_BOOTSTRAP_CACHE'] = '/tmp/bootstrap/cache';

$app = require_once $root . '/bootstrap/app.php';
$app->useStoragePath('/tmp/storage');

// Override package manifest path
$app->instance('path.bootstrap', '/tmp/bootstrap');

try {
    $app->handleRequest(Illuminate\Http\Request::capture());
} catch (\Throwable $e) {
    http_response_code(500);
    header('Content-Type: text/plain');
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo $e->getTraceAsString();
}