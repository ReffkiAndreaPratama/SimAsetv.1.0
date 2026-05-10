<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        // ── users ──────────────────────────────────────────────────
        Schema::create('users', function (Blueprint $table) {
            $table->integer('id_user')->autoIncrement()->primary();
            $table->string('nama', 100);
            $table->string('email', 100)->unique();
            $table->string('password_hash', 255);
            $table->enum('role', ['admin', 'staff']);
            $table->timestamp('created_at')->useCurrent();
            $table->timestamp('updated_at')->useCurrent()->useCurrentOnUpdate();
        });

        // ── password_reset_tokens ──────────────────────────────────
        Schema::create('password_reset_tokens', function (Blueprint $table) {
            $table->string('email')->primary();
            $table->string('token');
            $table->timestamp('created_at')->nullable();
        });

        // ── sessions ───────────────────────────────────────────────
        Schema::create('sessions', function (Blueprint $table) {
            $table->string('id')->primary();
            $table->foreignId('user_id')->nullable()->index();
            $table->string('ip_address', 45)->nullable();
            $table->text('user_agent')->nullable();
            $table->longText('payload');
            $table->integer('last_activity')->index();
        });

        // ── cache ──────────────────────────────────────────────────
        Schema::create('cache', function (Blueprint $table) {
            $table->string('key')->primary();
            $table->mediumText('value');
            $table->integer('expiration');
        });

        // ── cache_locks ────────────────────────────────────────────
        Schema::create('cache_locks', function (Blueprint $table) {
            $table->string('key')->primary();
            $table->string('owner');
            $table->integer('expiration');
        });

        // ── barang ─────────────────────────────────────────────────
        Schema::create('barang', function (Blueprint $table) {
            $table->string('kode_barang', 20)->primary();
            $table->string('nama_barang', 100);
            $table->string('kategori', 100)->nullable();
            $table->integer('jumlah')->default(0);
            $table->text('keterangan')->nullable();
            $table->timestamp('created_at')->useCurrent();
            $table->timestamp('updated_at')->useCurrent()->useCurrentOnUpdate();
        });

        // ── ruangan ────────────────────────────────────────────────
        Schema::create('ruangan', function (Blueprint $table) {
            $table->string('kode_ruangan', 20)->primary();
            $table->string('nama_ruangan', 100);
            $table->string('lantai', 20)->nullable();
            $table->text('keterangan')->nullable();
            $table->timestamp('created_at')->useCurrent();
            $table->timestamp('updated_at')->useCurrent()->useCurrentOnUpdate();
        });

        // ── aset ───────────────────────────────────────────────────
        Schema::create('aset', function (Blueprint $table) {
            $table->string('kode_aset', 20)->primary();
            $table->string('kode_barang', 20)->nullable();
            $table->string('kode_ruangan', 20)->nullable();
            $table->integer('id_user')->nullable();
            $table->string('serial_number', 100)->nullable();
            $table->string('kondisi', 100)->nullable();
            $table->string('status', 50)->nullable();
            $table->decimal('harga', 15, 2)->nullable();
            $table->text('keterangan')->nullable();
            $table->timestamp('created_at')->useCurrent();
            $table->timestamp('updated_at')->useCurrent()->useCurrentOnUpdate();

            $table->foreign('kode_barang', 'fk_aset_barang')
                ->references('kode_barang')->on('barang')
                ->onDelete('cascade')->onUpdate('cascade');

            $table->foreign('kode_ruangan', 'fk_aset_ruangan')
                ->references('kode_ruangan')->on('ruangan')
                ->onDelete('cascade')->onUpdate('cascade');

            $table->foreign('id_user', 'fk_aset_user')
                ->references('id_user')->on('users')
                ->onDelete('set null')->onUpdate('cascade');
        });

        // ── log_aktivitas ──────────────────────────────────────────
        Schema::create('log_aktivitas', function (Blueprint $table) {
            $table->integer('id_log')->autoIncrement()->primary();
            $table->integer('id_user');
            $table->string('aktivitas', 255);
            $table->string('ip_address', 45)->nullable();
            $table->text('keterangan')->nullable();
            $table->timestamp('created_at')->useCurrent();

            $table->foreign('id_user', 'fk_log_user')
                ->references('id_user')->on('users')
                ->onDelete('cascade')->onUpdate('cascade');
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('log_aktivitas');
        Schema::dropIfExists('aset');
        Schema::dropIfExists('ruangan');
        Schema::dropIfExists('barang');
        Schema::dropIfExists('cache_locks');
        Schema::dropIfExists('cache');
        Schema::dropIfExists('sessions');
        Schema::dropIfExists('password_reset_tokens');
        Schema::dropIfExists('users');
    }
};
