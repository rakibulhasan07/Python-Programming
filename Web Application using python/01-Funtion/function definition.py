def sum_list_numbers(Numbers):
    """This function takes a list of numbers and returns their sum."""
    total = 0
    for num in Numbers:
        total += num
    return total

#step 2: 5ta numbers ektu list tori
my_list =[10,20,30,40,50]

#step 3: function call kori
result = sum_list_numbers(my_list)

#step 4: result print kori
print(f"The sum of the numbers in the list is: {result}")