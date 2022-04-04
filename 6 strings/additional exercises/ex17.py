"""
Replace each special symbol with # in the following string

Given:

str1 = '/*Jon is @developer & musician!!'

Expected Output:

##Jon is #developer # musician##
"""
import string

from ex12 import find_and_replace_symbol

str1 = '/*Jon is @developer & musician!!'

#result = find_and_replace_symbol(str1,string.punctuation,"#")
for char in string.punctuation:
    str1 = str1.replace(char,"#")

print(str1)
