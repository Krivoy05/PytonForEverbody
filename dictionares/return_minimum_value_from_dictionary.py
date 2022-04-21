"""
Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,

  'history': 75
}

Expected output:

Math
"""
def find_max_value_from_dicionary(di):
    result = None
    conter = None
    for value in di:
        if result == None:
            result  = value
            counter = di.get(value)
        elif counter > di.get(value):
            result = value
            counter = di.get(value)
    return result

def find_max_value_from_dicionary_items(di):
    result = None
    for key,value in di.items():
        if result == None:
            result = key
            counter = value
        elif counter > value:
            result = key
            counter = value
    return result

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'Maath': 6,
  'history': 75
}

result = min(sample_dict, key=sample_dict.get)
print(result)
