def find_min_max(arr):
    if not arr:  # Check if the array is empty
        return None, None

    min_value = arr[0]
    max_value = arr[0]

    for num in arr[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
min_value, max_value = find_min_max(array)
print(f"Minimum value: {min_value}, Maximum value: {max_value}")
