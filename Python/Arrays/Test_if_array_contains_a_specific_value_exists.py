def contains_value(arr, value):
    return value in arr

numbers = [20, 60, 55, 40, 44]
value_to_check = 55
result = contains_value(numbers, value_to_check)

if result:
    print(f"The list contains the value {value_to_check}.")
else:
    print(f"The list does not contain the value {value_to_check}.")
