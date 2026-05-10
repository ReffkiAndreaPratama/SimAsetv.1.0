@if ($paginator->hasPages())
<nav style="display:flex;align-items:center;gap:4px;">
    {{-- Previous --}}
    @if ($paginator->onFirstPage())
        <span style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:7px;background:#f3f4f6;color:#d1d5db;font-size:13px;cursor:not-allowed;">
            <i class="fas fa-chevron-left"></i>
        </span>
    @else
        <a href="{{ $paginator->previousPageUrl() }}" style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:7px;background:#fff;border:1px solid #e5e7eb;color:#374151;font-size:13px;text-decoration:none;transition:all .15s;" onmouseover="this.style.borderColor='#2563eb';this.style.color='#2563eb'" onmouseout="this.style.borderColor='#e5e7eb';this.style.color='#374151'">
            <i class="fas fa-chevron-left"></i>
        </a>
    @endif

    {{-- Pages --}}
    @foreach ($elements as $element)
        @if (is_string($element))
            <span style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;color:#9ca3af;font-size:13px;">…</span>
        @endif
        @if (is_array($element))
            @foreach ($element as $page => $url)
                @if ($page == $paginator->currentPage())
                    <span style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:7px;background:#2563eb;color:#fff;font-size:13px;font-weight:600;">{{ $page }}</span>
                @else
                    <a href="{{ $url }}" style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:7px;background:#fff;border:1px solid #e5e7eb;color:#374151;font-size:13px;text-decoration:none;transition:all .15s;" onmouseover="this.style.borderColor='#2563eb';this.style.color='#2563eb'" onmouseout="this.style.borderColor='#e5e7eb';this.style.color='#374151'">{{ $page }}</a>
                @endif
            @endforeach
        @endif
    @endforeach

    {{-- Next --}}
    @if ($paginator->hasMorePages())
        <a href="{{ $paginator->nextPageUrl() }}" style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:7px;background:#fff;border:1px solid #e5e7eb;color:#374151;font-size:13px;text-decoration:none;transition:all .15s;" onmouseover="this.style.borderColor='#2563eb';this.style.color='#2563eb'" onmouseout="this.style.borderColor='#e5e7eb';this.style.color='#374151'">
            <i class="fas fa-chevron-right"></i>
        </a>
    @else
        <span style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:7px;background:#f3f4f6;color:#d1d5db;font-size:13px;cursor:not-allowed;">
            <i class="fas fa-chevron-right"></i>
        </span>
    @endif
</nav>
@endif
