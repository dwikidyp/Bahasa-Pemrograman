# Membuat dictionary
mahasiswa = {
    'nama': 'Dwiki',
    'umur': 20,
    'jurusan': 'Informatika'
}

# Akses nilai
print(mahasiswa['nama'])  # Output: Budi

# Menambah atau mengubah nilai
mahasiswa['umur'] = 30
mahasiswa['angkatan'] = 2024

# Menghapus pasangan key-value
del mahasiswa['jurusan']

print(mahasiswa)
# Output: {'nama': 'Dwiki', 'umur': 30, 'angkatan': 2024}
