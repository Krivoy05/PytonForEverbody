"""
Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
"""
def convert_two_dictionaries_in_one_dictionary(dict1,dict2):
    result_di = dict()
    result_di.update(dict1)
    result_di.update(dict2)
    return result_di
def convert_two_dictionaries_in_one_dictionary_copy(dict1,dict2):
    result_di = dict1.copy()
    result_di.update(dict2)
    return result_di
def convert_two_dictionaries_in_one_dictionary_3(dict1,dict2):
    result_di = {**dict1,**dict2}
    return result_di

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

result = convert_two_dictionaries_in_one_dictionary_3(dict1,dict2)
print(result)