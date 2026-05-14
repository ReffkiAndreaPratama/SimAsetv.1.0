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

// Copy bootstrap cache ke /tmp agar bisa ditulis ulang
foreach (['packages.php', 'services.php'] as $file) {
    $src = $root . '/bootstrap/cache/' . $file;
    $dst = '/tmp/bootstrap/cache/' . $file;
    if (file_exists($src) && !file_exists($dst)) {
        copy($src, $dst);
    }
}

require $root . '/vendor/autoload.php';

// Patch PackageManifest sebelum app dibuat
// dengan override class menggunakan runkit atau eval trick
// Cara paling clean: extend Application dan override manifestPath

class VercelApplication extends Illuminate\Foundation\Application
{
    public function getCachedPackagesPath(): string
    {
        return '/tmp/bootstrap/cache/packages.php';
    }

    public function getCachedServicesPath(): string
    {
        return '/tmp/bootstrap/cache/services.php';
    }

    public function bootstrapPath($path = ''): string
    {
        return '/tmp/bootstrap' . ($path ? DIRECTORY_SEPARATOR . $path : $path);
    }
}

// Buat app manual karena bootstrap/app.php pakai Application::configure()
// Kita perlu intercept setelah configure tapi sebelum create

// Load bootstrap/app.php tapi ganti class Application
$bootstrapContent = file_get_contents($root . '/bootstrap/app.php');
$bootstrapContent = str_replace(
    'use Illuminate\Foundation\Application;',
    'use VercelApplication as Application;',
    $bootstrapContent
);

$app = eval('?>' . $bootstrapContent);
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