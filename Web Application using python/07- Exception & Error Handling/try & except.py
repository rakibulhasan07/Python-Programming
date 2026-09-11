try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")