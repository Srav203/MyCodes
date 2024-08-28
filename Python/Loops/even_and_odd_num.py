even_numbers = []
odd_numbers = []

for x in range(1, 21):
    if x % 2 == 0:
        even_numbers.append(x) 
    else:
        odd_numbers.append(x) 

print("Even:", even_numbers)
print("Odd:", odd_numbers)
