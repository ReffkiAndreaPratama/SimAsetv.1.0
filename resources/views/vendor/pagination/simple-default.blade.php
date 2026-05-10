@if ($paginator->hasPages())
<nav style="display:flex;align-items:center;gap:8px;">
    @if ($paginator->onFirstPage())
        <span style="display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;background:#f3f4f6;color:#d1d5db;font-size:13px;cursor:not-allowed;">
            <i class="fas fa-chevron-left"></i> Sebelumnya
        </span>
    @else
        <a href="{{ $paginator->previousPageUrl() }}" style="display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;background:#fff;border:1px solid #e5e7eb;color:#374151;font-size:13px;text-decoration:none;">
            <i class="fas fa-chevron-left"></i> Sebelumnya
        </a>
    @endif

    @if ($paginator->hasMorePages())
        <a href="{{ $paginator->nextPageUrl() }}" style="display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;background:#fff;border:1px solid #e5e7eb;color:#374151;font-size:13px;text-decoration:none;">
            Berikutnya <i class="fas fa-chevron-right"></i>
        </a>
    @else
        <span style="display:inline-flex;align-items:center;gap:5px;padding:6px 12px;border-radius:7px;background:#f3f4f6;color:#d1d5db;font-size:13px;cursor:not-allowed;">
            Berikutnya <i class="fas fa-chevron-right"></i>
        </span>
    @endif
</nav>
@endif
