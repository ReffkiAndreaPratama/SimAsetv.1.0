<?php
$root = '/var/task/user';
chdir($root);

try {
    require $root . '/vendor/autoload.php';
    echo "1. autoload OK\n";
    
    $app = require_once $root . '/bootstrap/app.php';
    echo "2. bootstrap OK\n";
    
    echo "3. app class: " . get_class($app) . "\n";
    echo "4. storage path: " . $app->storagePath() . "\n";
    echo "5. base path: " . $app->basePath() . "\n";
    
} catch (\Throwable $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "FILE: " . $e->getFile() . ":" . $e->getLine() . "\n";
    echo "TRACE:\n" . $e->getTraceAsString();
}