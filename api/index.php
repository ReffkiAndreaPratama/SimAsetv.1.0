<?php

// Set working directory ke root project
$root = dirname(__DIR__);
chdir($root);

// Load autoloader
require $root . '/vendor/autoload.php';

// Bootstrap Laravel
$app = require_once $root . '/bootstrap/app.php';

// Handle request
$app->handleRequest(Illuminate\Http\Request::capture());
