try:
    file = open("data.txt", "r")
    isi = file.read()
    print(isi)
except FileNotFoundError:
    print("File tidak ditemukan!")
finally:
    print("Menutup file (jika dibuka).")
    try:
        file.close()
    except:
        pass
