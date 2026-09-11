class Student:
    def __init__(self):
        # private variable (__ is used to make variable private)
        self.__balance = 0

    # taka set korar jonno public method (setter method)
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
            print(f"{amount} taka joma hoyeche")
        else:
            print('taka poriman shothik noi')

    # taka check korar jonno public method (getter method)
    def get_balance(self):
        print(f"Current balance: {self.__balance}")

# object creation
s = Student()

# method use kore balance set kora
s.set_balance(5000)
s.get_balance()

# direct access to private variable will cause error
# print(s.__balance)  <-- ei line kaj korbe na karon __balance private variable.
