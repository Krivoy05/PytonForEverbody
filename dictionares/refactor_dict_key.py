"""
Rename key of a dictionary

Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

Expected output:

{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
"""

#ImportError: attempted relative import with no known parent package
#from .delete_list_of_key import remove_list_of_keys
def refactor_dict(di,key_to_refactor,new_name):
    result = dict.copy(di)
    key_to_refactr_value = result.pop(key_to_refactor)
    result[new_name] = key_to_refactr_value
    return result


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

result = refactor_dict(sample_dict,"city","location")
print(sample_dict)
print(result)