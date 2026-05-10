<div class="modal fade" id="{{ $id }}" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content" style="border-radius:16px;border:1px solid #E5E7EB;">
            <div class="modal-header" style="border-bottom:1px solid #F3F4F6;padding:18px 24px 14px;">
                <h5 class="modal-title fw-bold" style="font-size:.95rem;">
                    <i class="fas fa-filter text-primary me-2"></i> {{ $title }}
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>

            <form action="{{ $action }}" method="{{ strtoupper($method) === 'GET' ? 'GET' : 'POST' }}" target="_blank">
                @if(strtoupper($method) !== 'GET') @csrf @endif

                <div class="modal-body" style="padding:20px 24px;">

                    {{-- Rentang Tanggal --}}
                    <div class="filter-date-row">
                        <div>
                            <label>Tanggal Dari</label>
                            <input type="date" name="tanggal_dari" max="{{ date('Y-m-d') }}">
                            <div class="filter-hint">Kosongkan untuk semua</div>
                        </div>
                        <div>
                            <label>Tanggal Sampai</label>
                            <input type="date" name="tanggal_sampai" max="{{ date('Y-m-d') }}">
                            <div class="filter-hint">Kosongkan untuk semua</div>
                        </div>
                    </div>

                    {{-- Filter Ruangan --}}
                    @if(!empty($showRuangan) && $showRuangan)
                    <div class="filter-select-row">
                        <label>Ruangan</label>
                        <select name="kode_ruangan">
                            <option value="">Semua Ruangan</option>
                            @foreach(\App\Models\Ruangan::orderBy('nama_ruangan')->get() as $r)
                            <option value="{{ $r->kode_ruangan }}">{{ $r->nama_ruangan }}</option>
                            @endforeach
                        </select>
                    </div>
                    @endif

                    {{-- Filter Kondisi --}}
                    @if(!empty($showKondisi) && $showKondisi)
                    <div class="filter-select-row">
                        <label>Kondisi</label>
                        <select name="kondisi">
                            <option value="">Semua Kondisi</option>
                            <option value="Baik">Baik</option>
                            <option value="Rusak Ringan">Rusak Ringan</option>
                            <option value="Rusak Berat">Rusak Berat</option>
                        </select>
                    </div>
                    @endif

                    {{-- Filter Status --}}
                    @if(!empty($showStatus) && $showStatus)
                    <div class="filter-select-row">
                        <label>Status</label>
                        <select name="status">
                            <option value="">Semua Status</option>
                            <option value="Aktif">Aktif</option>
                            <option value="Maintenance">Maintenance</option>
                            <option value="Non-Aktif">Non-Aktif</option>
                        </select>
                    </div>
                    @endif

                    {{-- Info --}}
                    <div style="background:#F0F9FF;border:1px solid #BAE6FD;border-radius:9px;padding:10px 13px;font-size:.76rem;color:#0369A1;">
                        <i class="fas fa-info-circle me-1"></i>
                        Kosongkan semua filter untuk mengambil seluruh data.
                    </div>

                </div>

                <div class="modal-footer" style="border-top:1px solid #F3F4F6;padding:14px 24px 18px;">
                    <button type="button" class="btn btn-light border" data-bs-dismiss="modal">Batal</button>
                    <button type="submit" class="btn {{ $btnClass ?? 'btn-primary' }} d-flex align-items-center gap-2">
                        <i class="fas fa-download"></i> {{ $btnLabel ?? 'Download' }}
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
