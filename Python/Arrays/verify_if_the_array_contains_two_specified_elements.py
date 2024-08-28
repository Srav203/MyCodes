def contains_both_elements(arr, elem1, elem2):
    found_elem1 = False
    found_elem2 = False
    
    for num in arr:
        if num == elem1:
            found_elem1 = True
        elif num == elem2:
            found_elem2 = True
        
        if found_elem1 and found_elem2:
            return True
    
    return found_elem1 and found_elem2

array = [1, 12, 34, 23, 45]
result = contains_both_elements(array, 12, 23)
print("Contains both 12 and 23:", result)
