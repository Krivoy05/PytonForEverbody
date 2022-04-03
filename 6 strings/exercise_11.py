"""
Exercise 5: Take the following Python code that stores a string:`

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character
 and then use the float function to convert the extracted string into a floating point number."""

str = 'X-DSPAM-Confidence:0.847llll54544'

colon_character_position = str.find(":")
str_number_from_str = str[colon_character_position + 1:]
exeption_str = ""
try:
    float_from_str = float(str_number_from_str)
    print(float_from_str)
except:
    print("Can't convert to float to end of line, try to parse parsial")
    symbol_counter = 0
    for symbol in str_number_from_str:
        if symbol.isnumeric():
            exeption_str += symbol
            symbol_counter += 1
        else:
            if symbol == '.':
                exeption_str += symbol
                symbol_counter += 1
            else:
                break
    print("Parsed str is: "+exeption_str)
