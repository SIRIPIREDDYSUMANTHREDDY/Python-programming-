def find_duplicates(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print("Original Array:", arr)
print("Duplicate Elements:", find_duplicates(arr))
