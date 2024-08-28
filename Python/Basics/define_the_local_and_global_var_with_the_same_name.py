var_name = "I am a global variable"

def my_function():
    var_name = "I am a local variable"    
    print("Inside the function:", var_name)

my_function()
print("Outside the function:", var_name)
