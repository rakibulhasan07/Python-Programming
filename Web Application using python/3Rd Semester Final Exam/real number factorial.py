def find_factorial(n):
    '''This function calculates the factorial of a given number n.'''
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

#user input for the number to calculate factorial
try:
    num = int(input('Enter your real number: '))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = find_factorial(num)
        print(f"The factorial of {num} is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")