"""
Exercise 3: Create a new string made of the first, middle, and last characters of each input string

Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"

Expected Output:

AJrpan
"""
import math


def get_symbols (str):
    result_str = ""
    str_max = len(str) - 1
    str_midle = math.ceil((str_max + 1) / 2) - 1
    result_str = str[0] + str[str_midle] + str[str_max]
    return result_str

def combine_str(str1,str2):
    result_str = ""
    symbol_index = 0
    while symbol_index<= len(str1)-1:
        result_str += str1[symbol_index]+str2[symbol_index]
        symbol_index +=1
    return result_str


str1 = input("Input string to convert: ")
str2 = input("Input string to convert: ")
str1_symbols = get_symbols(str1)
str2_symbols = get_symbols(str2)
result_str = combine_str(str1_symbols,str2_symbols)

print("First, middle and last symbol is: "+result_str)
