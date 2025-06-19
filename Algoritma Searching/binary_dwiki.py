def binary_search_recursive(arr, target, left=0, right=None):

    #arr: List yang sudah terurut
    #target: Nilai yang dicari
    #left: Index kiri
    #right: Index kanan

    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_python():
    print("=" * 60)
    print("BINARY PYTHON IMPLEMENTATION")
    print("=" * 60)
    
    data = [5, 11, 12, 22, 25, 30, 34, 64, 77, 90]
    target = 34
    
    print(f"Data: {data}")
    print(f"Target: {target}")
    print()
    
    # Binary Search Recursive
    result = binary_search_recursive(data, target)
    print("Binary Search (Recursive):")
    print(f"  Result: Index {result}")
    print()


if __name__ == "__main__":
    binary_python()