def insert_element(arr, index, element):
    if index < 0 or index > len(arr):
        raise IndexError("Index out of range. Must be between 0 and the length of the list.")

    arr.insert(index, element)
    return arr

numbers = [100, 92, 74, 63, 41]
position = 2
element_to_insert = 99
updated_list = insert_element(numbers, position, element_to_insert)
print(f"Updated list: {updated_list}")
