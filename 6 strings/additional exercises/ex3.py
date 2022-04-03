"""
Exercise 4: Arrange string characters such that lowercase letters should come first

Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive

Expected Output:

yaivePNT
"""
def get_lower(str):
    result_str = ""
    for symbol in str:
        if symbol.islower():
            result_str += symbol
    return result_str

def get_upper(str):
    result_str = ""
    for symbol in str:
        if symbol.isupper():
            result_str += symbol
    return result_str

str = "PyNaTive"

result_str = get_lower(str)+get_upper(str)

print(result_str)
