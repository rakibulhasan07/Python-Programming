# #Programe No: 1
# #print even number
# n = int(input ('Enter the end of the range: '))
# for i in range(1,n+1):
#     if(i % 2 == 0):
#         print(i, end=' ')

# #Programe No: 2
# n = int(input ('Enter the Range:  '))
# for num in range(1,n+1):
#     count = 0
#     for i in range (2,int((num*0.5)+1)):
#         if(num % i == 0):
#             count = count + 1
#             break
#     if(count == 0 and num!=1):
#         print(num, end=' ')

# #program No: 3
# n_terms = int(input("How many terms the user wants to print? "))
# # first two terms
# n1, n2 = 0, 1
# count = 0

# #Now, we will check if the number of terms is valid or not
# if n_terms <= 0:
#    print("Please enter a positive integer, the given number is invalid")
# # if there is only one term, return n1
# elif n_terms == 1:
#    print("The Fibonacci sequence of the numbers up to",n_terms,":")
#    print(n1)
# # Then, we will generate Fibonacci sequence of number
# else:
#    print("Fibonacci sequence of the numbers is:")
#    while count < n_terms:
#        print(n1, end=' ')
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# Program No: 4
#2+4+6+...+n
n = int(input("Enter the value of range: "))
sum = 0
for i in range (1, n+1,2):
   sum = sum + i
print("2+4+6+...+n = ", sum) 



# n = int(input("Enter a number: "))
# total_sum = 0

# # range(start, stop + 1, step)
# for i in range(2, n + 1, 2):
#     total_sum += i

# print("The sum of even numbers is:", total_sum)+