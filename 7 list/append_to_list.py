"""
Add new item to list after a specified item

Write a program to add item 7000 after 6000 in the following Python List

Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

"""
def apend_to_list(list1,value):
    result = list()
    for val in list1:
        if list_inside_list(val):
            check_for_searched_value(value)
### do to
    return result

def check_for_searched_value(value):


def list_inside_list(value):
    return any(x for x in value)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(apend_to_list(list1,6000))