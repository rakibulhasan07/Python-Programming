# 1. re.findall() - Find all occurrences of a pattern in a string

import re

res = re.findall("ai", 'The rain in Spain stays mainly in the plain.')
print(res)  # Output: ['ai', 'ai', 'ai']


#2. re.search() - Search for the first occurrence of a pattern in a string
import re

res2 = re.search("\s", "Helloiii World in bangladesh")
print('space paoa gese position: ', res2.start())  # Output: <re.Match object; span=(5, 6), match=' '>

#3. re.split() - Split a string by the occurrences of a pattern
import re

res3 = re.split("\s", "Helloiii World in bangladesh")
print(res3)  # Output: ['Helloiii', 'World', 'in', 'bangladesh']    

#4. re.sub() - Replace occurrences of a pattern in a string with a specified replacement
import re       

res4 = re.sub("\s", "__", "Helloiii World in bangladesh")
print(res4)  # Output: 'Helloiii__World__in__bangladesh'

#5. re.compile() - Compile a regular expression pattern into a regex object for reuse
import re   

res5 = re.compile("\s")
res6 = res5.sub("__", "Helloiii World in bangladesh")

print(res6)  # Output: 'Helloiii__World__in__bangladesh'

#6. re.match() - Determine if the beginning of a string matches a pattern
import re

res7 = re.match("Helloiii", "Helloiii World in bangladesh")
if res7:
    print("Match found:", res7.group())  # Output: Match found: Helloiii    

    