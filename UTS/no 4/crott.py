def hitung_jumlah_genap(n):
    jumlah = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            jumlah += i
    return jumlah

# Input dari pengguna
try:
    batas = int(input("Masukkan angka batas atas (N): "))
    if batas < 1:
        print("Masukkan angka lebih besar dari 0.")
    else:
        hasil = hitung_jumlah_genap(batas)
        print(f"Jumlah bilangan genap dari 1 sampai {batas} adalah: {hasil}")
except ValueError:
    print("Input harus berupa angka bulat!")
