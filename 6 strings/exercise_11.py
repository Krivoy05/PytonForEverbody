"""
Exercise 5: Take the following Python code that stores a string:`

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character
 and then use the float function to convert the extracted string into a floating point number."""

str = 'X-DSPAM-Confidence:0.84754544'

colon_character_position = str.find(":")
str_number_from_str = str[colon_character_position + 1:]
try :
    float_from_str = float(str_number_from_str)
    print(float_from_str)
except:
    print("Can't convert to float")