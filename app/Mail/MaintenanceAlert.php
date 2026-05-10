<?php

namespace App\Mail;

use App\Models\Asset;
use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class MaintenanceAlert extends Mailable
{
    use Queueable, SerializesModels;

    public Asset $asset;
    public string $tipe; // 'masuk' atau 'selesai'

    public function __construct(Asset $asset, string $tipe = 'masuk')
    {
        $this->asset = $asset;
        $this->tipe  = $tipe;
    }

    public function envelope(): Envelope
    {
        $subject = $this->tipe === 'masuk'
            ? '[SimAset] Aset ' . $this->asset->kode_aset . ' Masuk Maintenance'
            : '[SimAset] Maintenance Selesai: ' . $this->asset->kode_aset;

        return new Envelope(subject: $subject);
    }

    public function content(): Content
    {
        return new Content(
            view: 'emails.maintenance-alert',
            with: [
                'asset' => $this->asset,
                'tipe'  => $this->tipe,
            ]
        );
    }

    public function attachments(): array
    {
        return [];
    }
}
