# Function to add 5 numbers from a list

def sum_list(numbers):
    sum = 0

    for i in numbers:
        sum += i
    return sum

# list of 5 numbers
my_list = [10, 20, 30, 40, 50]
print("Sum of numbers in the list is:", sum_list(my_list))
