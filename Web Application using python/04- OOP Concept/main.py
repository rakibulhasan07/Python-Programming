import mymodule   # module import করা

result = mymodule.add(10, 20)  # function call from module

print("যোগফল =", result)  # output

from calculator.add import add

print(add(5, 7))