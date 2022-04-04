"""
Remove special symbols / punctuation from a string

Given:

str1 = "/*Jon is @developer & musician"

Expected Output:

"Jon is developer musician"
"""
import string
import re
def filter_alpha_regex (input_string):
    result_str =re.sub(r'[^\w\s]',"",input_string)
    return result_str


def filter_alpha_manualy (input_string):
    result_str =""
    for symbol in str1:
        if symbol.isalpha() or symbol == " ":
            result_str += symbol
    return result_str

def filter_alpha_translate(input_string):
    result_str = ""
    dictionary = input_string.maketrans("","",string.punctuation)
    result_str = input_string.translate(dictionary)
    return result_str

str1 = "/*Jon is @developer & musician"
#print(filter_alpha_manualy(str1))
#print(filter_alpha_translate(str1))
print(filter_alpha_regex(str1))

