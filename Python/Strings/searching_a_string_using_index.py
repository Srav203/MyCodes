my_string = "Hello, World! Welcome to Python."

index1 = my_string.index("World")  
print("Index of 'World':", index1) 

index2 = my_string.index("Welcome", 10)  
print("Index of 'Welcome':", index2)  

index3 = my_string.index("Python", 15, 30)  
print("Index of 'Python':", index3)  

try:
    index4 = my_string.index("NotFound")
except ValueError:
    index4 = "Substring not found"

print("Index of 'NotFound':", index4)  
