def sum_of_integers(arr):
    total = 0
    for num in arr:
        total += num
    return total
    
numbers = [41, 255, 56, 214, 632]
result = sum_of_integers(numbers)
print(f"The sum of the integers is: {result}")
