# Program no: 1
# Experiment : create a dictionary in Python
#Creating a dictionary with {} and Dict()
my_dict_one = {}    # creating an empty dictionary with {}
my_dict_two = dict()    # creating an empty dictionary with dict()
print("Empty dictionary using {}:", my_dict_one)
print("Empty dictionary using dict():", my_dict_two)

# Program no: 1
my_dict_One ={'one':1, 'two':2, 'three':3}   # with curly brackets
print('My dict one:', my_dict_One)

my_dict_two = dict({'one':1, 'two':2, 'three':3})   # with dict()
print('My dict two:', my_dict_two)

my_dict_three = dict(one=1, two=2, three=3)   # with dict() without curly brackets
print('My dict three:', my_dict_three)

my_dict_four = dict([('one',1), ('two',2), ('three',3)])   # with dict() with list of tuples
print('My dict four:', my_dict_four)

my_dict_five = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # with dict() with zip()
print('My dict five:', my_dict_five)    