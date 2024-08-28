def find_smaller_and_larger(num1, num2):
    if num1 < num2:
        smaller = num1
        larger = num2
    elif num1 > num2:
        smaller = num2
        larger = num1
    else:
        smaller = larger = num1 
    
    return smaller, larger

number1 = 55
number2 = 60

smaller, larger = find_smaller_and_larger(number1, number2)

if smaller == larger:
    print("Both numbers are equal.")
else:
    print(f"Smaller number: {smaller}")
    print(f"Larger number: {larger}")
