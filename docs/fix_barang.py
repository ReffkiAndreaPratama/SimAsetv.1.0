import re

# Fix barang/index.blade.php
with open('resources/views/barang/index.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Hapus stat cards aktif/nonaktif
c = re.sub(r'<div class="stat-card">\s*<div class="stat-icon"[^>]*><i class="fas fa-check-circle"></i></div>\s*<div>.*?</div>\s*</div>\s*</div>', '', c, flags=re.DOTALL)
c = re.sub(r'<div class="stat-card">\s*<div class="stat-icon"[^>]*><i class="fas fa-ban"></i></div>\s*<div>.*?</div>\s*</div>\s*</div>', '', c, flags=re.DOTALL)

# Hapus filter status block
c = re.sub(r'<div class="filter-group">\s*<label class="filter-label">Status</label>.*?</select>\s*</div>', '', c, flags=re.DOTALL)

# Hapus kolom Status di thead
c = c.replace('<th style="width:100px;text-align:center;">Status</th>', '')

# Hapus kolom status di tbody
c = re.sub(r'<td style="text-align:center;">\s*@if\(\$b->status.*?@endif\s*</td>', '', c, flags=re.DOTALL)

# Fix hasAny
c = c.replace("request()->hasAny(['search','kategori','status'])", "request()->hasAny(['search','kategori'])")

with open('resources/views/barang/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('barang/index fixed')

# Fix barang/create.blade.php
with open('resources/views/barang/create.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = re.sub(r'<div class="col-md-2">\s*<label class="field-label">Status.*?</div>\s*</div>', '', c, flags=re.DOTALL)
with open('resources/views/barang/create.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('barang/create fixed')

# Fix barang/edit.blade.php
with open('resources/views/barang/edit.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = re.sub(r'<div class="col-md-2">\s*<label class="field-label">Status.*?</div>\s*</div>', '', c, flags=re.DOTALL)
with open('resources/views/barang/edit.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('barang/edit fixed')

# Fix barang/show.blade.php
with open('resources/views/barang/show.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = re.sub(r'@if\(\$barang->status == .aktif.\).*?@endif', 'Aktif', c, flags=re.DOTALL)
c = re.sub(r'<div class="info-row">\s*<span class="info-label">Status</span>.*?</div>\s*</div>', '', c, flags=re.DOTALL)
with open('resources/views/barang/show.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('barang/show fixed')

print('All done')
