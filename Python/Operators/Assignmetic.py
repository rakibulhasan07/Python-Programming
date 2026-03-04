print('Hey Assignmetic Operators')

# The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

numbers = [1, 2, 3, 4, 5] # List of numbers
count = len(numbers)  # Get the length of the list
if count> 3: # Check if the count is greater than 3
    print(f'List has {count} elements') # Traditional way
# Using the walrus operator to assign and check in one line
if (count := len(numbers)) > 3: # Check if the count is greater than 3
    print(f'List has {count} elements') # Using the walrus operator