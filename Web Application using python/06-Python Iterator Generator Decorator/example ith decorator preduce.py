# 1. decorator function
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

# 2. mul functioner upor decorator use kora hocche
@smart_divide
def divide(a, b):
    print(f" division is: {a/b}")

# 3 function call 
divide(10,2)
divide(10,0)    

