def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start] 
        start += 1
        end -= 1

    return arr

array = [55, 60, 3, 55, 60]
reversed_array = reverse_array(array)
print(f"Reversed array: {reversed_array}")
