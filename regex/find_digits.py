"""
Write a regular expression to search digit inside a string
"""

import re

def get_numbers(str):
    return re.findall("\d+",target_str)
    #return re.findall("[0-9]+",target_str)


target_str = "My roll number is 25 and 23"

result = get_numbers(target_str)
print(result)


