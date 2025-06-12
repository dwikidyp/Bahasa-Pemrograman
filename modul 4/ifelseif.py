def main():
    print("Input Nilai Anda (A - E): ", end="")
    nilai = input()
    
    if nilai == 'A':
        print("Pertahankan!")
    elif nilai == 'B':
        print("Harus lebih baik lagi")
    elif nilai == 'C':
        print("Perbanyak belajar")
    elif nilai == 'D':
        print("Jangan keseringan main")
    elif nilai == 'E':
        print("Kebanyakan bolos...")
    else:
        print("Maaf, format nilai tidak sesuai")

if __name__ == "__main__":
    main()