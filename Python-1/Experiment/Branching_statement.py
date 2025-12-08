#Programe No: 1
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
if (a > b):
    if(a>c):
        print(a,'a is the largest number')
    else:
        print(c,'c is the largest number')
elif(b > c):
    print(b,'b is the largest number')
else:
    print(c,'c is the largest number')

#Programe No: 2

#Check given number is even or odd
num = int(input('Enter a number: '))
if(num % 2 == 0):
    print(num,'is an even number')
else:
    print(num,'is an odd number')

#Programe No: 3
# input net amount
amt = int(input('Enter Amount: '))
# calculate amount with discount
if(amt>0):
    if amt <= 5000:
        disc = amt*0.10
    elif amt <= 15000:
        disc = amt*0.15
    else:
        disc=0.5*amt

    print('Discount Amount is:',disc)
    print('To be paid by Customer:',amt-disc)
else:
    print('Please enter valid amount')

# #Programe No: 4
def grade(m):
    if(m>=80):
        return 'A+'
    elif(m>=75):
        return 'A'
    elif(m>=70):
        return 'A-'
    elif(m>=65):
        return 'B+'
    elif(m>=60):
        return 'B'
    elif(m>=55):
        return 'B-'
    elif(m>=50):
        return 'C+'
    elif(m>=45):
        return 'C'
    elif(m>=40):
        return 'D'
    else:
        return 'F'
def point(m):
    if(m>=80):
        return 4.00
    elif(m>=75):
        return 3.75
    elif(m>=70):
        return 3.50
    elif(m>=65):
        return 3.25
    elif(m>=60):
        return 3.00
    elif(m>=55):
        return 2.75
    elif(m>=50):
        return 2.50
    elif(m>=45):
        return 2.25
    elif(m>=40):
        return 2.00
    else:
        return 0.00
marks = int(input('Enter your marks: '))
print('Your Grade is:',grade(marks))
print('Your Grade Point is:',point(marks))


#Programe No: 5
#Python program for simple calculator
# Function to add two numbers
def add(num1, num2):
    return num1 + num2
# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
print("Select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
if select>4 or select<=0:
    print('Invalid Selection, Please Try Again')
else:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    if select == 1:
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif select == 2:
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    elif select == 3:
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif select == 4:
        print(number_1, "/", number_2, "=", divide(number_1, number_2))