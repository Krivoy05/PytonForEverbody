"""
Initialize dictionary with default values

In Python, we can initialize the keys with the same values.

Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

Expected output:

{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
"""
def initialise_wit_default(list_to_initialise, default_values_dictionary):
    result = dict()
    for name in list_to_initialise:
        result[name] = default_values_dictionary
    return result

def initialise_wit_default_fromkeys(list_to_initialise, default_values_dictionary):
    result = dict.fromkeys(list_to_initialise,default_values_dictionary)
    return result

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = initialise_wit_default_fromkeys(employees,defaults)
print(result)