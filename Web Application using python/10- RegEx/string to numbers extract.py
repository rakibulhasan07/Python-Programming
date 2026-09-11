import re

my_string = "the price of item 1 is 100 dollars, item 2 is 200 dollars, and item 3 is 300 dollars."

# \d+ matches one or more digits
numbers = re.findall(r'\d+', my_string)
print(' nischasito number gulo: ', numbers)