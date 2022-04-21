"""
Check if a value exists in a dictionary

We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary.

Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}

Expected output:

200 present in a dict
"""
def value_is_exist_in_dictionary(dictionary,value):
    result = False
    for di_value in dictionary.values():
        if di_value==value:
            result=True
    return result
def convert_result_to_output_production(value,is_exist):
    if is_exist:
       return ""+str(value)+" present in a dict"
    else:
        return "" +str(value) + " is NOT present in a dict"

sample_dict = {'a': 100, 'b': 200, 'c': 300}
value_to_find = 100
result = value_is_exist_in_dictionary(sample_dict,value_to_find)
print(convert_result_to_output_production(value_to_find,result))