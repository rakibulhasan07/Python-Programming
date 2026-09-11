# Function to calculate sum of odd numbers from 1 to 100
def sum_of_odd_numbers():
    sum = 0

    for i in range(1, 101, 2):
        sum += i
    return sum
print("Sum of odd numbers from 1 to 100 is:", sum_of_odd_numbers())