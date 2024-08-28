even_count, odd_count = len([x for x in [11, 24, 60, 45, 18, 12, 7, 8, 9] if x % 2 == 0]), len([x for x in [11, 24, 60, 45, 18, 12, 7, 8, 9] if x % 2 != 0])

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
