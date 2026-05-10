
import re

# Fix aset/create.blade.php - hapus field jumlah
with open('resources/views/aset/create.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = re.sub(r'<div class="col-md-4">\s*<label class="field-label">Jumlah</label>.*?</div>\s*</div>', '', c, flags=re.DOTALL)
with open('resources/views/aset/create.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: aset/create')

# Fix aset/edit.blade.php - hapus field jumlah
with open('resources/views/aset/edit.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = re.sub(r'<div class="col-md-4">\s*<label class="field-label">Jumlah</label>.*?</div>\s*</div>', '', c, flags=re.DOTALL)
with open('resources/views/aset/edit.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: aset/edit')

# Fix aset/show.blade.php - hapus info-row jumlah
with open('resources/views/aset/show.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = re.sub(r'<div class="info-row">\s*<span class="info-label">Jumlah</span>.*?</div>\s*</div>', '', c, flags=re.DOTALL)
with open('resources/views/aset/show.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: aset/show')

# Fix aset/index.blade.php - hapus kolom jumlah di tabel
with open('resources/views/aset/index.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
# Hapus header kolom Jml
c = re.sub(r'<th style="width:42px;text-align:center;">Jml</th>', '', c)
# Hapus cell jumlah di tbody
c = re.sub(r'<td style="text-align:center;font-weight:700;font-size:\.85rem;color:#374151;">\s*1\s*</td>', '', c)
with open('resources/views/aset/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: aset/index')

print('All done')
