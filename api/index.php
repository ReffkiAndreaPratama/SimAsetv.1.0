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

require $root . '/vendor/autoload.php';

$app = require_once $root . '/bootstrap/app.php';
$app->useStoragePath('/tmp/storage');
$app->instance('path.bootstrap', '/tmp/bootstrap');

// Bootstrap manual step by step
try {
    $app->bootstrapWith([
        Illuminate\Foundation\Bootstrap\LoadEnvironmentVariables::class,
        Illuminate\Foundation\Bootstrap\LoadConfiguration::class,
        Illuminate\Foundation\Bootstrap\HandleExceptions::class,
        Illuminate\Foundation\Bootstrap\RegisterFacades::class,
        Illuminate\Foundation\Bootstrap\RegisterProviders::class,
        Illuminate\Foundation\Bootstrap\BootProviders::class,
    ]);
} catch (\Throwable $e) {
    die("BOOTSTRAP ERROR: " . $e->getMessage() . "\nFILE: " . $e->getFile() . ":" . $e->getLine());
}

// Dispatch request manual
$request = Illuminate\Http\Request::capture();
$router = $app->make('router');

// Load routes
$app->make(Illuminate\Contracts\Http\Kernel::class);

try {
    // Coba dispatch langsung
    $response = $router->dispatch($request);
    $response->send();
} catch (Symfony\Component\HttpKernel\Exception\HttpException $e) {
    header('Content-Type: text/plain');
    echo "HTTP EXCEPTION: " . $e->getStatusCode() . " - " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo $e->getTraceAsString();
} catch (\Throwable $e) {
    header('Content-Type: text/plain');
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo $e->getTraceAsString();
}