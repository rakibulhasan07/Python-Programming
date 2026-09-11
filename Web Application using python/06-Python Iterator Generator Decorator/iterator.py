list = [1, 2, 3, 4, 'Rakib', 'hablu', 'sakib']

# for i in list:
#     print(i) 

x = iter(list)

# print(x.__next__())
# print(x.__next__())

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))



# # Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
# class MyNumbers:
#     def __iter__(self):
#         self.a =1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))