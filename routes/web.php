<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\ProfileController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\AssetController;
use App\Http\Controllers\BarangController;
use App\Http\Controllers\RuanganController;
use App\Http\Controllers\ExportController;
use App\Http\Controllers\ImportController;
use App\Http\Controllers\UserController;
use App\Http\Controllers\AuditLogController;
use App\Http\Controllers\LaporanController;
use App\Http\Controllers\QrCodeController;
use App\Http\Controllers\MaintenanceController;

/*
|--------------------------------------------------------------------------
| AUTH ROUTES (BREEZE)
|--------------------------------------------------------------------------
*/
require __DIR__.'/auth.php';

/*
|--------------------------------------------------------------------------
| FALLBACK
|--------------------------------------------------------------------------
*/
Route::fallback(function () {
    return redirect()->route('dashboard');
});

Route::get('/', function () {
    return redirect()->route('dashboard');
});

/*
|--------------------------------------------------------------------------
| AUTHENTICATED ROUTES
|
| Pembagian role:
|   Semua login  → seluruh fitur operasional (aset, barang, ruangan, QR,
|                  maintenance, import, export, laporan, dashboard)
|   role:admin   → tambahan: kelola pengguna & audit log
|--------------------------------------------------------------------------
*/
Route::middleware(['auth'])->group(function () {

    // LOGOUT
    Route::post('/logout', function () {
        Auth::logout();
        return redirect('/login');
    })->name('logout');

    // PROFIL — semua pengguna
    Route::get('/profile',    [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile',  [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    // DASHBOARD
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');

    // KELOLA ASET
    Route::get('/aset/check-new',        [AssetController::class, 'checkNew'])->name('aset.check-new');
    Route::post('/aset/batch-destroy',   [AssetController::class, 'batchDestroy'])->name('aset.batch-destroy');
    Route::resource('aset', AssetController::class)->parameters(['aset' => 'kode_aset']);
    Route::post('/aset/{kode_aset}/generate-qr', [AssetController::class, 'generateQr'])->name('aset.generateQr');
    Route::get('/aset/{kode_aset}/qr',           [AssetController::class, 'showQr'])->name('aset.showQr');
    Route::get('/aset/{kode_aset}/detail',        [AssetController::class, 'detail'])->name('assets.detail');

    // KELOLA BARANG
    Route::resource('barang', BarangController::class);

    // KELOLA RUANGAN
    Route::resource('ruangan', RuanganController::class);

    // QR CODE
    Route::get('/qrcode/batch-print',          [QrCodeController::class, 'batchPrint'])->name('qrcode.batch-print');
    Route::get('/qrcode/scanner',              [QrCodeController::class, 'scanner'])->name('qrcode.scanner');
    Route::get('/qrcode/search',               [QrCodeController::class, 'search'])->name('qrcode.search');
    Route::get('/qrcode/{kode_aset}/download', [QrCodeController::class, 'download'])->name('qrcode.download');

    // MAINTENANCE
    Route::get('/maintenance',                        [MaintenanceController::class, 'index'])->name('maintenance.index');
    Route::post('/maintenance/{kode_aset}/set',       [MaintenanceController::class, 'setMaintenance'])->name('maintenance.set');
    Route::patch('/maintenance/{kode_aset}/complete', [MaintenanceController::class, 'complete'])->name('maintenance.complete');

    // IMPORT — hanya store dan template (tidak ada halaman terpisah)
    Route::post('/import',         [ImportController::class, 'store'])->name('import.store');
    Route::get('/import/template', [ImportController::class, 'template'])->name('import.template');

    // EXPORT — langsung download, tidak ada halaman index terpisah
    Route::get('/export/aset/excel',   [ExportController::class, 'excelAset'])->name('export.aset.excel');
    Route::get('/export/aset/pdf',     [ExportController::class, 'pdfAset'])->name('export.aset.pdf');
    Route::get('/export/barang/excel', [ExportController::class, 'excelBarang'])->name('export.barang.excel');
    Route::get('/export/barang/pdf',   [ExportController::class, 'pdfBarang'])->name('export.barang.pdf');

    // LAPORAN — laporan per ruangan dan maintenance
    Route::get('/laporan',                 [LaporanController::class, 'index'])->name('laporan.index');
    Route::get('/laporan/assets/cetak',    [LaporanController::class, 'cetakAset'])->name('laporan.aset.cetak');
    Route::get('/laporan/assets/export',   [LaporanController::class, 'exportAset'])->name('laporan.aset.export');
    Route::get('/laporan/ruangan/{kode_ruangan}', [LaporanController::class, 'laporanRuangan'])->name('laporan.ruangan');
    Route::get('/laporan/maintenance/pdf', [LaporanController::class, 'exportMaintenancePdf'])->name('laporan.maintenance.pdf');
    Route::get('/laporan/maintenance/csv', [LaporanController::class, 'exportMaintenanceCsv'])->name('laporan.maintenance.csv');

    /*
    |----------------------------------------------------------------------
    | ADMIN ONLY — kelola pengguna & audit log
    |----------------------------------------------------------------------
    */
    Route::middleware('role:admin')->group(function () {
        Route::resource('users', UserController::class);
        Route::get('/audit-log', [AuditLogController::class, 'index'])->name('audit-log.index');
    });
});
