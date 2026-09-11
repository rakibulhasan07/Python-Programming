# ### RegEx ব্যবহার করে নির্দিষ্ট Word খোঁজা এবং গণনা করার প্রোগ্রাম

# # **Python প্রোগ্রাম:**

# from os import times
# import re

# text = input("Enter a text: ")
# word = input("Enter the word to search: ")

# result = re.findall(r'\b' + re.escape(word) + r'\b', text)

# print("Word found:", len(result), "times")


# # ### উদাহরণ

# # **Input:**

# # ```text
# # Enter a text: I love Python. Python is easy. I learn Python.
# # Enter the word to search: Python
# # ```

# # **Output:**

# # ```text
# # Word found: 3 times
# # ```

# # ### ব্যাখ্যা

# # * `re.findall()` → নির্দিষ্ট Word খুঁজে বের করে।
# # * `\b` → পুরো Word মিলছে কি না নিশ্চিত করে।
# # * `len(result)` → Word-টি কতবার পাওয়া গেছে তা গণনা করে।
# # * `re.escape()` → Word-এর বিশেষ চিহ্ন থাকলেও নিরাপদে search করতে সাহায্য করে।

# import re
# text = 'Python is poerful, python is easy to learn. Python is popular.'

# word_to_find = 'Python'

# #RegEx using find out ord
# matches = re.findall(r'\b' + re.escape(word_to_find) + r'\b', text, flags=re.IGNORECASE)
# #\
# #fulaful prodoshon
# print(f"The word '{word_to_find}' was found {len(matches)} times in the text.")




import re

text = ' python is powerful, python is easy to learn. Python is popular.'

find_word = 'python'
matche = re.findall(find_word, text)
print(f"the word '{find_word}' was found {len(matche)} times in the text.")