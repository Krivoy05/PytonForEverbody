"""
Write a program to count occurrences of all characters within a string

Given:

str1 = "Apple"

Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""
from ex7 import find_str_optimised
str1 = "Appppllle"
searched_symbols = ""
for symbol in str1:
    contains = searched_symbols.find(symbol)
    if searched_symbols.find(symbol) == -1:
        print("\'"+symbol+":\' " + str(find_str_optimised(str1,symbol))+", ")
        searched_symbols += symbol
