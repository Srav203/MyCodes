def copy_array(arr):
    return arr[:]

original_list = ["teja", "sravs", "manu"]
copied_list = copy_array(original_list)

print(f"Original list: {original_list}")
print(f"Copied list: {copied_list}")
