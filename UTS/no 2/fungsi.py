# Variabel global
x = 10

def fungsi_lokal():
    # Variabel lokal
    y = 5
    print("Di dalam fungsi, x (global):", x)  # Bisa diakses
    print("Di dalam fungsi, y (lokal):", y)

def fungsi_global():
    global x  # Memodifikasi variabel global
    x = 20
    print("Di dalam fungsi_global, x dimodifikasi menjadi:", x)

fungsi_lokal()

print("Setelah fungsi_lokal, x masih:", x)
# print(y)  ❌ Error: y adalah variabel lokal, tidak bisa diakses di luar fungsi

fungsi_global()

print("Setelah fungsi_global, x menjadi:", x)
