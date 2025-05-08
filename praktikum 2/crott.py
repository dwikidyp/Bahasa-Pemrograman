print ("Nama : Dwiki Dzaki Yudi Putra")
print ("NIM : 20240801115")
print ("Jurusan : Teknik Informatika")

# Menghitung Luas dan Keliling Lingkaran
print ("")
print ("1. Menghitung Luas dan Keliling Lingkaran")
r = float(input("Masukan jari jari = "))
luas = (3.14 * r * r)
keliling = (2 * 3.14 * r)
print ('Luas lingkaran = ', luas)
print ('Keliling lingkaran = ', keliling)

# Menghitung Kecepatan jarak
print("")
print("2. Menghitung Kecepatan jarak")
def hitung_kecepatan():
    jarak = float(input("Masukan jarak = "))
    waktu = float(input("Masukan Waktu : "))
    kecepatan = jarak * waktu
    print("Kecepatan : ", kecepatan)
hitung_kecepatan()

# Menghitung konversi detik
print("")
print("3. Menghitung konversi detik")
detik = float(input("Masukan nilai detik = "))
menit = float(detik/60)
jam = float(detik/3600)
print (detik, 'detik dirubah ke menit = ', menit, 'menit')
print (detik, 'detik dirubah ke jam', jam, 'jam')

# Menghitung konversi jam
print("")
print("4. Menghitung konversi jam")
Jam = float(input(" Masukan nilai jam = "))
Menit = float(Jam * 60)
Detik = float(Jam * 3600)
print (Jam, 'jam dirubah ke menit = ', Menit, 'menit')
print (Jam, 'jam dirubah ke detik', Detik, 'detik')

# Menghitung konversi tahun
print("")
print("5. Menghitung konversi tahun")
tahun = int (input("Masukan Jumlah tahun = "))
bulan = int (tahun * 12)
hari = int (tahun * 365)
print(tahun, 'tahun dirubah ke bulan', bulan, 'bulan')
print(tahun, 'tahun dirubah ke hari', hari, 'hari')

# Menghitung Konversi suhu
print("")
print("6. Menghitung konversi suhu")
celcius = float(input("Masukan celcius = "))
reamur = float(0.8 * celcius)
fahrenheit = float(1.8 * celcius)+32
kelvin = float(celcius + 273.15)
rankine = float(celcius + 273.15)*1.8
print('Derajat Reamur = ', reamur)
print('Derajat Fahrenheit = ', fahrenheit)
print('Derajat Kelvin = ', kelvin)
print('Derajat Rankine = ', rankine)