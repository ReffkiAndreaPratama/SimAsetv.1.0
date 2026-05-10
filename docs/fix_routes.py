
# Fix ruangan/index.blade.php - $r->id -> $r->kode_ruangan
with open('resources/views/ruangan/index.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = c.replace("$r->id)", "$r->kode_ruangan)")
c = c.replace('$r->nama"', '$r->nama_ruangan"')
with open('resources/views/ruangan/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: ruangan/index')

# Fix users/index.blade.php - $u->id -> $u->id_user
with open('resources/views/users/index.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = c.replace("$u->id)", "$u->id_user)")
c = c.replace("auth()->id() != $u->id_user)", "auth()->id() != $u->id_user)")
with open('resources/views/users/index.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: users/index')

# Fix ruangan/show.blade.php - $ruangan->id -> $ruangan->kode_ruangan
with open('resources/views/ruangan/show.blade.php', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
c = c.replace("$ruangan->id)", "$ruangan->kode_ruangan)")
c = c.replace("route('ruangan.destroy', $ruangan->id)", "route('ruangan.destroy', $ruangan->kode_ruangan)")
with open('resources/views/ruangan/show.blade.php', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed: ruangan/show')

print('All done')
