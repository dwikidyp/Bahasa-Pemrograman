def cari_nilai(data, target):
    if target in data:
        indeks = data.index(target)
        return f"Nilai {target} ditemukan pada indeks ke-{indeks}."
    else:
        return f"Nilai {target} tidak ditemukan dalam data."


daftar_nilai = [70, 85, 90, 75, 88, 60, 13, 28, 49, 64]

# Input nilai yang ingin dicari dari pengguna
try:
    cari = int(input("Masukkan nilai yang ingin dicari: "))
    hasil = cari_nilai(daftar_nilai, cari)
    print(hasil)
except ValueError:
    print("Input harus berupa angka!")
