def average_of_integers(arr):
    if not arr:
        raise ValueError("The list is empty and the average cannot be calculated.")
    
    total = sum(arr)
    count = len(arr)
    average = total / count
    return average

numbers = [156, 213, 143, 342, 531]
result = average_of_integers(numbers)
print(f"The average of the integers is: {result:.2f}")
