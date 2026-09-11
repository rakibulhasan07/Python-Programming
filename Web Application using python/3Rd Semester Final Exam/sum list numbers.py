def my_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total 

my_list = [1, 2, 3, 4, 5]
result = my_sum(my_list)
print("The sum of the list numbers is:", result)
