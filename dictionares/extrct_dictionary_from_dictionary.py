"""
Create a dictionary by extracting the keys from a given dictionary

Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Expected output:

{'name': 'Kelly', 'salary': 8000}

"""
def extract_dictionary(list_to_extract,dictionary_to_extract):
    result = dict()
    for value in list_to_extract:
        result[value] = dictionary_to_extract.get(value)

    return result

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
result = extract_dictionary(keys,sample_dict)
print(result)