"""
Find words with both alphabets and numbers

Write a program to find words with both alphabets and numbers from an input string.

Given:

str1 = "Emma25 is Data scientist50 and AI Expert"

Expected Output:

Emma25
scientist50
"""
import re

def find_alphanumerical(input_string):
    result = []
    word_until_whitespace = ''
    for symbol in input_string:
        if symbol ==' ':
            for sub_symvol in word_until_whitespace:
                if sub_symvol.isdigit():
                    result.append(word_until_whitespace)
                    break
            word_until_whitespace = ''
        else:
            word_until_whitespace += symbol
    return result

str1 = "Emma25 is Data scientist50 and AI Expert"
#print(find_alphanumerical(str1))
