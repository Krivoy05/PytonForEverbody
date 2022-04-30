"""
Replace all occurrences of 5 with five for the given string.

>>> ip = 'They ate 5 apples and 5 oranges'
"""
import re

def replace(string_to_chage, value, newvalue):
    return re.sub(value,newvalue,string_to_chage)

ip = 'They ate 5 apples and 5 oranges'
result = replace(ip,"5","five")
print(result)


