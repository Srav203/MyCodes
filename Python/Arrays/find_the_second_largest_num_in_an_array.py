def find_second_largest(arr):
    if len(arr) < 2:
        return None  
    
    first, second = float('-inf'), float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None

array = [10, 21, 4, 5, 23, 60, 55]
second_largest = find_second_largest(array)
print("Second largest number:", second_largest)
