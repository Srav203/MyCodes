def compare_numbers(num1, num2):
    results = {
        "<": num1 < num2,
        "<=": num1 <= num2,
        ">": num1 > num2,
        ">=": num1 >= num2
    }
    return results

number1 = 55
number2 = 60

comparison_results = compare_numbers(number1, number2)

print(f"{number1} < {number2}: {comparison_results['<']}")
print(f"{number1} <= {number2}: {comparison_results['<=']}")
print(f"{number1} > {number2}: {comparison_results['>']}")
print(f"{number1} >= {number2}: {comparison_results['>=']}")
