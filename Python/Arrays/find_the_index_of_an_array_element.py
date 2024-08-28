def find_index(arr, element):
    try:
        index = arr.index(element)
        return index
    except ValueError:
        return -1

numbers = [71, 23, 65, 82, 50]
element_to_find = 23
index = find_index(numbers, element_to_find)

if index != -1:
    print(f"The index of {element_to_find} is: {index}")
else:
    print(f"{element_to_find} is not in the list.")

