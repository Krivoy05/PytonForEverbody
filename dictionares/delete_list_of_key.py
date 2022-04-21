"""
Delete a list of keys from a dictionary

Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

Expected output:

{'city': 'New york', 'age': 25}
"""
def remove_list_of_keys(list_to_remove,dictionary):
    result = dict.copy(dictionary)
    for value in list_to_remove:
        result.pop(value)
    return result

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

#result = remove_list_of_keys(keys,sample_dict)
#print(result)