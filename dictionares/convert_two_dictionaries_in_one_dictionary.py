"""
Convert two lists into a dictionary

Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
"""
def convert_two_list_to_dictionary(keys, values):
    result = dict()
    i=0
    for key in keys:
        result[key] = values[i]
        i+=1
    return result

def convert_two_list_to_dictionary_zip(keys, values):
    result = dict(zip(keys,values))
    return result

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = convert_two_list_to_dictionary_zip(keys,values)
print(result)
