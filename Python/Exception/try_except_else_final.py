# IndexError Handling
numbers = [10, 20, 30]
try:
    # Accessing valid index
    print("Element at index 1 =", numbers[1])
    
    # Attempting to access an invalid index
    print("Element at index 4 =", numbers[4])
except IndexError:
    print("IndexError: The index is out of range.")

print()

# Value Comparison with try-except-else
list1 = [5, 4, 3]
list2 = [3, 4, 5]
try:
    # Comparing two lists
    if list1 == list2:
        print("The lists are equal.")
    else:
        raise ValueError("Lists are not equal.")
except ValueError as e:
    print(f"ValueError: {e}")
else:
    print("Comparison completed successfully.")

print()

# ZeroDivisionError Handling with finally
try:
    # Attempting division by zero
    result = 10 / 0
    print("Result =", result)
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
finally:
    print("Execution of finally block: Cleanup actions or final statements.")
