import math

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Kuadrat (x^2)")
    print("6. Akar Kuadrat (√x)")
    print("7. Invers (1/x)")
    print("8. Logaritma Basis 10 (log)")
    print("9. Logaritma Natural (ln)")
    print("10. e^x")
    print("0. Keluar")
    
    while True:
        pilihan = input("\nPilih operasi (0-10): ")
        
        if pilihan == '0':
            print("Terima kasih. Program selesai.")
            break
        
        if pilihan in ['1', '2', '3', '4']:
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                print(f"Hasil: {x + y}")
            elif pilihan == '2':
                print(f"Hasil: {x - y}")
            elif pilihan == '3':
                print(f"Hasil: {x * y}")
            elif pilihan == '4':
                if y != 0:
                    print(f"Hasil: {x / y}")
                else:
                    print("Error: Pembagian dengan nol!")
            else:
                x = float(input("Masukkan angka: "))
                
                if pilihan == '5':
                    print(f"Hasil: {x**2}")
                elif pilihan == '6':
                    if x >+ 0:
                        print(f"Hasil: {math.sqrt(x)}")
                    else:
                        print("Error: Akar dari bilangan negatif!")
                elif pilihan == '7':
                    if x != 0:
                        print(f"Hasil: {1/x}")
                    else:
                        print("Error: Tidak dapat membagi 1 dengan nol!")
                elif pilihan == '8':
                    if x > 0:
                        print(f"Hasil: {math.log10(x)}")
                    else:
                        print("Error: Log hanya untuk angka > 0!")
                elif pilihan == '9':
                    if x > 0:
                        print(f"Hasil: {math.log(x)}")
                    else: print("Error: ln hanya untuk angka > 0!")
                elif pilihan ==  '10':
                    print(f"Hasil: {math.exp(x)}")
                else:
                    print("Pilihan tidak valid!")
                    
kalkulator()