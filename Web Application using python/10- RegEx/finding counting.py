import re
text = "Python is a programming language. Python is widely used in web development, data analysis, artificial intelligence, and more. Python's simplicity and readability make it a popular choice among developers."

word_to_Find = "is"

# Regex using finding word
matches = re.findall( word_to_Find, text)

#print 
print(f'khuja hoichey: {word_to_Find} word er count: {len(matches)}')