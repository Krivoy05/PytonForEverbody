"""
Split a string on hyphens

Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist

Expected Output:

Displaying each substring

Emma
is
a
data
scientist
"""

def find_and_replace_symbol(input_string, replace_any_symbol_that_meet_here, replace_value):
    result_string = ""
    for symbol in input_string:
        if any(symbol.__contains__(char) for char in replace_any_symbol_that_meet_here):
            result_string += replace_value
        else:
            result_string += symbol
    return result_string

#str1 = "Emma-is-a-data-scientist"
#print(find_and_replace_symbol(str1,"-","\n"))
