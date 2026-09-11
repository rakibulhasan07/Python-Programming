### RegEx ব্যবহার করে Email Address Valid করার প্রোগ্রাম


# import re

# email = input("Enter your email address: ")

# pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

# if re.match(pattern, email):
#     print("Valid Email Address")
# else:
#     print("Invalid Email Address")


# ### উদাহরণ

# # **Input:**

# ```text
# Enter your email address: rakib@gmail.com
# ```

# **Output:**

# ```text
# Valid Email Address
# ```

# **Input:**

# ```text
# Enter your email address: rakib@gmail
# ```

# **Output:**

# ```text
# Invalid Email Address
# ```

# **সংক্ষেপে:** `re.match()` ব্যবহার করে নির্দিষ্ট Regular Expression-এর সাথে Email Address মিলিয়ে দেখা হয়েছে। মিললে **Valid**, না মিললে **Invalid** দেখাবে।




# -------------------------------------------
# revision 2

import re

email = input('enter your email address: ') # input email address: rakib12@gmail.com

pattern = r'^[A-Za-z0-9_%+-]+@[gmail]+\.[A-Za-z]{2,}$'

if re.match(pattern, email):
    print('Valid Email Address')
else:
    print('Invalid Email Address')