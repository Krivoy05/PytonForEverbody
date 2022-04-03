"""
Calculate the sum and average of the digits present in a string

Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"

Expected Outcome:

Sum is: 38 Average is  6.333333333333333
"""
from ex4 import count_digits

def count_sum(str1):
    sum = 0
    for symbol in str1:
        if symbol.isdigit():
            sum += int(symbol)
    return sum


str1 = "PYnative29@#8496"



print("Sum is: " +str(count_sum(str1))+ " Average is: " +str(count_sum(str1)/count_digits(str1)))
