def sequential_search(arr, target):
    
    # arr: List yang akan dicari
    # target Nilai yang dicari
    
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    
    return -1, comparisons

def sequential_python():
    print("=" * 60)
    print("SEQUENTIAL PYTHON IMPLEMENTATION")
    print("=" * 60)
    
    data = [5, 11, 12, 22, 25, 30, 34, 64, 77, 90]
    target = 30
    
    print(f"Data: {data}")
    print(f"Target: {target}")
    print()
    
    result, comp = sequential_search(data, target)
    print("Sequential Search:")
    print(f"  Result: Index {result}, Comparisons: {comp}")

if __name__ == "__main__":
    sequential_python()
