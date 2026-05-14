<?php
$root = '/var/task/user';
chdir($root);

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

$bootstrapCache = $root . '/bootstrap/cache';
if (!is_link($bootstrapCache) && is_dir($bootstrapCache)) {
    foreach (glob($bootstrapCache . '/*') as $file) {
        copy($file, '/tmp/bootstrap/cache/' . basename($file));
    }
    rmdir($bootstrapCache);
    symlink('/tmp/bootstrap/cache', $bootstrapCache);
}

require $root . '/vendor/autoload.php';

$app = require_once $root . '/bootstrap/app.php';
$app->useStoragePath('/tmp/storage');

// Bootstrap manual
$app->bootstrapWith([
    Illuminate\Foundation\Bootstrap\LoadEnvironmentVariables::class,
    Illuminate\Foundation\Bootstrap\LoadConfiguration::class,
    Illuminate\Foundation\Bootstrap\HandleExceptions::class,
    Illuminate\Foundation\Bootstrap\RegisterFacades::class,
    Illuminate\Foundation\Bootstrap\RegisterProviders::class,
    Illuminate\Foundation\Bootstrap\BootProviders::class,
]);

// Cek apakah view service terdaftar
$hasView = $app->bound('view');
echo "view bound: " . ($hasView ? 'YES' : 'NO') . "\n";
echo "APP_KEY: " . (config('app.key') ? 'SET' : 'NOT SET') . "\n";
echo "DB: " . config('database.default') . "\n";
echo "DB_HOST: " . config('database.connections.mysql.host') . "\n";

// Coba resolve view
try {
    $view = $app->make('view');
    echo "view resolved: OK\n";
} catch (\Throwable $e) {
    echo "view error: " . $e->getMessage() . "\n";
}

// Coba route
$router = $app->make('router');
$request = Illuminate\Http\Request::capture();
echo "URI: " . $request->getRequestUri() . "\n";

try {
    $response = $router->dispatch($request);
    echo "route OK: " . $response->getStatusCode() . "\n";
} catch (\Throwable $e) {
    echo "ROUTE ERROR: " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
}