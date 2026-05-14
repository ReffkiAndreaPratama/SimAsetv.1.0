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

// Salin packages.php dan services.php ke /tmp/bootstrap/cache jika ada
foreach (['packages.php', 'services.php'] as $file) {
    $src = $root . '/bootstrap/cache/' . $file;
    $dst = '/tmp/bootstrap/cache/' . $file;
    if (file_exists($src) && !file_exists($dst)) {
        copy($src, $dst);
    }
}

require $root . '/vendor/autoload.php';

// Override bootstrap/cache path sebelum app dibuat
// dengan cara patch PackageManifest
$app = new class($root, $root . '/public') extends Illuminate\Foundation\Application {
    public function bootstrapPath($path = ''): string
    {
        return '/tmp/bootstrap' . ($path ? '/' . $path : '');
    }
};

$app->useStoragePath('/tmp/storage');
$app->singleton(
    Illuminate\Contracts\Http\Kernel::class,
    App\Http\Kernel::class
);
$app->singleton(
    Illuminate\Contracts\Console\Kernel::class,
    App\Console\Kernel::class
);
$app->singleton(
    Illuminate\Contracts\Debug\ExceptionHandler::class,
    App\Exceptions\Handler::class
);

try {
    $app->handleRequest(Illuminate\Http\Request::capture());
} catch (\Throwable $e) {
    http_response_code(500);
    header('Content-Type: text/plain');
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo $e->getTraceAsString();
}