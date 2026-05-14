<?php
echo json_encode([
    'status' => 'ok',
    'php' => PHP_VERSION,
    'dir' => __DIR__,
    'root' => dirname(__DIR__),
    'files' => scandir(dirname(__DIR__)),
]);