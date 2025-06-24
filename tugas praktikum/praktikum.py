import time
import random
import copy

# ===== BAGIAN 1: PENGELOLAAN DATA MAHASISWA =====

def hitung_rata_nilai(nilai_list):
    """Menghitung dan mengembalikan rata-rata dari daftar nilai"""
    if len(nilai_list) == 0:
        return 0
    return sum(nilai_list) / len(nilai_list)

def konversi_nilai(nilai):
    """Mengembalikan nilai huruf berdasarkan nilai angka"""
    if 80 <= nilai <= 100:
        return "A"
    elif 77 <= nilai <= 79.99:
        return "A-"
    elif 74 <= nilai <= 76.99:
        return "B+"
    elif 68 <= nilai <= 73.99:
        return "B"
    elif 65 <= nilai <= 67.99:
        return "B-"
    elif 62 <= nilai <= 64.99:
        return "C+"
    elif 60 <= nilai <= 61.99:
        return "C"
    elif 45 <= nilai <= 59.99:
        return "D"
    else:  # 0 <= nilai <= 44.99
        return "E"

def tampilkan_data_mahasiswa(nama, nilai):
    """Menampilkan data mahasiswa lengkap"""
    nilai_huruf = konversi_nilai(nilai)
    status = "LULUS" if nilai >= 60 else "TIDAK LULUS"
    
    print(f"Nama: {nama}")
    print(f"Nilai Angka: {nilai}")
    print(f"Nilai Huruf: {nilai_huruf}")
    print(f"Status: {status}")
    print("-" * 30)

def input_data_mahasiswa():
    """Meminta input dari user berupa nama dan nilai"""
    nama = input("Masukkan nama mahasiswa: ")
    while True:
        try:
            nilai = float(input("Masukkan nilai mahasiswa (0-100): "))
            if 0 <= nilai <= 100:
                break
            else:
                print("Nilai harus antara 0-100!")
        except ValueError:
            print("Masukkan nilai yang valid!")
    
    return (nama, nilai)

# ===== BAGIAN 2: ALGORITMA PENGURUTAN =====

def bubble_sort(arr):
    """Implementasi Bubble Sort"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """Implementasi Selection Sort"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    """Implementasi Merge Sort"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function untuk merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    """Implementasi Insertion Sort"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    """Implementasi Quick Sort"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def test_sorting_algorithms():
    """Menguji dan membandingkan waktu eksekusi algoritma sorting"""
    print("\n" + "="*50)
    print("PERBANDINGAN ALGORITMA PENGURUTAN")
    print("="*50)
    
    # Generate 1000 bilangan acak
    print("Menghasilkan 1000 bilangan acak...")
    original_data = [random.randint(1, 1000) for _ in range(1000)]
    
    # Dictionary untuk menyimpan hasil waktu
    hasil_waktu = {}
    
    # Daftar algoritma
    algoritma = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }
    
    print("\nMenguji algoritma pengurutan...")
    print("-" * 50)
    
    for nama_algoritma, fungsi_sort in algoritma.items():
        # Copy data agar tidak mengubah data asli
        data_copy = copy.deepcopy(original_data)
        
        # Catat waktu mulai
        start_time = time.perf_counter()
        
        # Jalankan algoritma
        fungsi_sort(data_copy)
        
        # Catat waktu selesai
        end_time = time.perf_counter()
        
        # Hitung durasi
        durasi = end_time - start_time
        hasil_waktu[nama_algoritma] = durasi
        
        print(f"{nama_algoritma:<15}: {durasi:.4f} detik")
    
    # Urutkan berdasarkan waktu tercepat
    print("\n" + "="*50)
    print("RANKING ALGORITMA (TERCEPAT KE TERLAMBAT)")
    print("="*50)
    
    sorted_hasil = sorted(hasil_waktu.items(), key=lambda x: x[1])
    
    for i, (nama, waktu) in enumerate(sorted_hasil, 1):
        print(f"{i}. {nama:<15}: {waktu:.4f} detik")

# ===== PROGRAM UTAMA =====

def main():
    print("="*50)
    print("PROGRAM PENGELOLAAN DATA MAHASISWA")
    print("="*50)
    
    # Input data 10 mahasiswa
    data_mahasiswa = []
    nilai_list = []
    
    print("Silakan masukkan data 10 mahasiswa:\n")
    
    for i in range(10):
        print(f"Data Mahasiswa ke-{i+1}:")
        nama, nilai = input_data_mahasiswa()
        data_mahasiswa.append((nama, nilai))
        nilai_list.append(nilai)
        print()
    
    # Tampilkan data semua mahasiswa
    print("\n" + "="*50)
    print("DATA SEMUA MAHASISWA")
    print("="*50)
    
    for nama, nilai in data_mahasiswa:
        tampilkan_data_mahasiswa(nama, nilai)
    
    # Hitung dan tampilkan rata-rata
    rata_rata = hitung_rata_nilai(nilai_list)
    print(f"RATA-RATA NILAI SEMUA MAHASISWA: {rata_rata:.2f}")
    
    # Jalankan test algoritma sorting
    test_sorting_algorithms()
    
    print("\n" + "="*50)
    print("PROGRAM SELESAI")
    print("="*50)

if __name__ == "__main__":
    main()