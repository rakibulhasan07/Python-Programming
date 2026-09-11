import re

my_string = "The price of the product is $100. The discount is 20%."

#\d+ matches one or more digits
numbers = re.findall(r'\d+', my_string)
print(f"Extracted numbers: {numbers}")  # Output: ['100', '20']