"""
Change value of a key in a nested dictionary

Write a Python program to change Brad’s salary to 8500 in the following dictionary.

Given:

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

Expected output:

{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
"""
def change_valeue(di,parent_category,value_to_change, new_value):
    result = dict.copy(di)
    sub_di = result.get(parent_category)
    test = sub_di.copy()
    test[value_to_change] = new_value
    result.pop(parent_category)
    result[parent_category] = test
    return result

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

result = change_valeue(sample_dict,'emp3','salary',8500)
print(result)
