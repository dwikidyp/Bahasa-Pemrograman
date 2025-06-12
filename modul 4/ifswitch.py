def tampilkan():
    pilih = int(input())
    
    if pilih == 1:
        print("Ini Satu", end="")
    elif pilih == 2:
        print("Ini Dua", end="")
    else:
        print("Selain Satu atau Dua", end="")

def tampilkan_if(pilih):
    if pilih == 1:
        print("Ini Satu", end="")
    elif pilih == 2:
        print("Ini Dua", end="")
    else:
        print("Selain Satu atau Dua", end="")

# Pemanggilan Pada Program Utama
def main():
    kondisi_switch = tampilkan()
    pilih = 2
    tampilkan_if(pilih)

if __name__ == "__main__":
    main()