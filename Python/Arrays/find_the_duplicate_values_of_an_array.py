def find_duplicates(arr):
    duplicates = []
    seen = set()
    
    for value in arr:
        if value in seen:
            if value not in duplicates:
                duplicates.append(value)
        else:
            seen.add(value)
    
    return duplicates

array = [10, 22, 51, 42, 51, 33, 62, 81, 22]
duplicates = find_duplicates(array)
print("Duplicates:", duplicates)
