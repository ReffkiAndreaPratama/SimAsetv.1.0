
# Fix ruangan/index.blade.php - $r->nama -> $r->nama_ruangan
with open('resources/views/ruangan/index.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = c.replace("$r->nama}", "$r->nama_ruangan}")
c = c.replace("$r->nama<", "$r->nama_ruangan<")
c = c.replace("$r->nama ", "$r->nama_ruangan ")
with open('resources/views/ruangan/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: ruangan/index')

# Fix aset/create.blade.php - $r->id -> $r->kode_ruangan, $r->nama -> $r->nama_ruangan
with open('resources/views/aset/create.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = c.replace("value=\"{{ $r->id }}\"", "value=\"{{ $r->kode_ruangan }}\"")
c = c.replace("== $r->id ?", "== $r->kode_ruangan ?")
c = c.replace("$r->nama }}", "$r->nama_ruangan }}")
with open('resources/views/aset/create.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: aset/create')

# Fix aset/edit.blade.php - same fixes
with open('resources/views/aset/edit.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = c.replace("value=\"{{ $r->id }}\"", "value=\"{{ $r->kode_ruangan }}\"")
c = c.replace("== $r->id ?", "== $r->kode_ruangan ?")
c = c.replace("$r->nama }}", "$r->nama_ruangan }}")
# Also fix old('kode_ruangan') == $asset->ruangan_id comparisons
c = c.replace("$asset->ruangan_id", "$asset->kode_ruangan")
with open('resources/views/aset/edit.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: aset/edit')

print('All done')
