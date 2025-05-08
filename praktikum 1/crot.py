# Menghitung luas persegi panjang
panjang = float(input('masukkan panjang = '))
lebar = float(input('masukkan lebar = '))

# hitung luas
luas = panjang * lebar

#Cetak luas
print('Luas persegi panjang = ', luas,'m2')

#Menghitung luas segitiga
tinggi = float(input('input tinggi segitiga: '))
alas = float(input('input alas segitiga: '))

luas = 0.5 * tinggi * alas
print('Luas segitiga = ', luas)

#Menghitung Faktorial
n = int(input('Masukkan nilai n = '))
faktorial = 1

for i in range(1, n + 1):
    faktorial *= i
    
print(f'{n}! = {faktorial}')

# menghitung volume balok
print("Menghitung Volume Balok")
print("-" * 30)

# Input dari user
panjang = float(input("Masukkan panjang balok : "))
lebar = float(input("Masukkan lebar balok : "))
tinggi = float(input("Masukkan tinggi balok : "))

# Proses perhitungan
volume = panjang * lebar * tinggi

# Output hasil
print("-" * 30)
print(f"Volume balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {volume} cm³")