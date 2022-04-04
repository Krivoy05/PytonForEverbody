"""
Removal all characters from a string except integers

Given:

str1 = 'I am 25 years and 10 months old'

Expected Output:

2510
"""
import re

def remove_all_alphas(input_string):
    result_str = ""
    for symbol in str1:
        if symbol.isdigit():
            result_str += symbol
    return result_str

def remove_all_alphas_regex(input_string):
    result_str = re.sub(r'[\D]',"",input_string)
    return result_str

str1 = 'I am 25 years and 10 months old'
print(remove_all_alphas(str1))
print(remove_all_alphas_regex(str1))