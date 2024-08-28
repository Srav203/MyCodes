def remove_all_occurrences(arr, element):
    return [item for item in arr if item != element]

numbers = [150, 240, 310, 120, 550, 510]
element_to_remove = 310
updated_list = remove_all_occurrences(numbers, element_to_remove)

print(f"Updated list with all occurrences of {element_to_remove} removed: {updated_list}")
