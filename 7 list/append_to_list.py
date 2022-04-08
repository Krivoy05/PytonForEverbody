"""
Add new item to list after a specified item

Write a program to add item 7000 after 6000 in the following Python List

Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

"""


def apend_to_list(list1,value_after_to_add,adding_value):
    i =0
    for val in list1:
        if islist(val):
            #jesli tak parsujemy liste def
            parsing_list(list1,value_after_to_add,adding_value)
        else:
            check_and_add_value(list1,val,value_after_to_add,adding_value,i)
        i += 1
    return True

def check_and_add_value(list1,cheking_value,value_after_to_add,adding_value,index):
    if cheking_value == value_after_to_add:
        list1.insert(index+1,adding_value)

def islist(list1):
    return isinstance(list1,list)

def parsing_list(list1,value_after_to_add,adding_value):
    i = 0;
    for value_from_list in list1:
        test = islist(value_from_list)
        if islist(value_from_list):
            parsing_list(value_from_list,value_after_to_add,adding_value)
        else:
            check_and_add_value(list1, value_from_list, value_after_to_add, adding_value,i)
        i += 1
    return True


list1 = [10, 20, [300, 400, [000,000, 8000], 500], 30, 6000,40]
print("Before add")
print(list1)
print("After add")
apend_to_list(list1,6000,7000)
print(list1)
