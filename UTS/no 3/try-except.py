try:
    angka = int(input("Masukkan angka pembagi: "))
    hasil = 10 / angka
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")
except ValueError:
    print("Input harus berupa angka!")
