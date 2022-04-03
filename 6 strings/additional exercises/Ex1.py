import  math
"""
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"

Expected Output:

Jms
"""

str = input("Input string to convert: ")
result_str = ""
str_max = len(str)-1
str_midle = math.ceil((str_max+1)/2)-1

result_str = str[0] + str[str_midle] + str[str_max]

print("First, middle and last symbol is: "+result_str)
