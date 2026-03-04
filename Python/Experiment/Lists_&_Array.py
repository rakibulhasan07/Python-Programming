# # Programe no 1
# # Python Program to find largest and Smalleset Number in a List
# NumList = []
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of Element %d: " % i))
#     NumList.append(value)
# print("The Largest Number in the List is: ", max(NumList))
# print("The Smallest Number in the List is: ", min(NumList))



# # Programe no 2
# # Python Program to find to find Largest and Smallest Number in a List
# NumList = []
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of Element %d: " % i))
#     NumList.append(value)
# i =1
# max = NumList[0]
# while i<Number :
#     if max < NumList[i]:
#         max = NumList[i]
#         loc=i
#     i=i+1
# print(' The Largest Number in the List is: ',max,' at location ',loc+1 )




# # # Programe no 3
# # Step 1: Start

# # Step 2-4: Initialize list and handle comma-separated input
# input_string = input("Enter comma-separated values (digits or alphabets): ")
# duplicate = [item.strip() for item in input_string.split(',')]

# # Step 5: Define the 'Remove' function
# def Remove(input_list):
#     # Step 6: Initialize an empty list for unique elements
#     final_list = []
    
#     # Step 7: Iterate through the input list
#     for element in input_list:
#         # Step 7a: If element is not in final_list, append it
#         if element not in final_list:
#             final_list.append(element)
            
#     # Step 8: Return the unique elements
#     return final_list

# # Step 9: Call the 'Remove' function and store the result
# unique_elements = Remove(duplicate)

# # Step 10: Print the original list
# print("\nOriginal list ('duplicate'):", duplicate)

# # Step 11: Print the list after removing duplicates
# print("List after removing duplicates:", unique_elements)

# # Step 12: End




# Programe no 3
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = input("Enter comma-separated numbers: ").split(",")
print("Original List: ", duplicate)
print("List after removing duplicates: ", Remove(duplicate))