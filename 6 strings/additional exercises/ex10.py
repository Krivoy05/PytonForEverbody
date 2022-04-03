"""
Reverse a given string

Given:

str1 = "PYnative"

Expected Output:

evitanYP
"""
def revers_str(str):
    counter = len(str) - 1
    result_str =""
    while counter >= 0:
        result_str += str[counter]
        counter -= 1
    return result_str

str1 = "PYnative"
print(revers_str(str1))
