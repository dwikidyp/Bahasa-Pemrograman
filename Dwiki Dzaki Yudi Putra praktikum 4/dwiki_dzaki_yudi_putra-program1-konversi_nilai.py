def konversi_nilai_ke_huruf(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 77:
        return "A-"
    elif nilai >= 74:
        return "B+"
    elif nilai >= 68:
        return "B"
    elif nilai >= 65:
        return "B-"
    elif nilai >= 62:
        return "C+"
    elif nilai >= 60:
        return "C"
    elif nilai >= 45:
        return "D"
    else:
        return "E"
    
nilai_angka = float(input("Masukkan nilai numerik (0-100): "))
nilai_kamu = konversi_nilai_ke_huruf(nilai_angka)
print(f"Nilai kamu: {nilai_kamu}")