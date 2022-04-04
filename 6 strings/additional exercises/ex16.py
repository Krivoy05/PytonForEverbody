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
            contains_alpha = False
            for sub_symvol in word_until_whitespace:
                if sub_symvol.isalpha():
                    contains_alpha = True
                if sub_symvol.isdigit() and contains_alpha:
                    result.append(word_until_whitespace)
                    break
            word_until_whitespace = ''
        else:
            word_until_whitespace += symbol
    return result

def find_alphanumerical_split_test(input_string):
    result = []
    words = input_string.split()
    for word in words:
        if any(char.isalpha() for char in word) and any(char.isdigit() for char in word):
            result.append(word)
    return result


str1 = "Emma25 is Data scientist50 and AI Expert 50a"
print(find_alphanumerical(str1))
print(find_alphanumerical_split_test(str1))
