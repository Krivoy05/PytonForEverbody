"""
Count all letters, digits, and special symbols from a given string

Given:

str1 = "P@#yn26at^&i5ve"

Expected Outcome:

Total counts of chars, digits, and symbols

Chars = 8
Digits = 3
Symbol = 4
"""
def count_chars(str):
    counter = 0
    for symbol in str:
        if symbol.isalpha():
            counter += 1
    return counter

#need to optimise,no idea how to find symbols
def count_symbols(str):
    counter = 0
    for symbol in str:
        if symbol.isdigit():
           counter = counter
        elif symbol.isalpha():
            counter = counter
        else:
            counter += 1
    return counter



def count_symbols_optimised(str):
    counter = 0
    symbols_set_to_search = "!@#$%^&*()_+=-_?.,<> "
    for symbol in symbols_set_to_search:
        for character in str:
            if character == symbol:
                counter+=1
    return counter


def count_digits(str):
    counter = 0
    for symbol in str:
        if symbol.isdigit():
            counter += 1
    return counter

str1 = "P@#yn26at^&i5ve"

"""
print("Total counts of chars, digits, and symbols")

print("Chars = " + str(count_chars(str1)))
print("Digits = " + str(count_digits(str1)))
print("Symbol = " + str(count_symbols_optimised(str1)))
"""
