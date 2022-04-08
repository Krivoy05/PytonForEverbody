"""
 Replace list’s item with new value if found

You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

Given:

list1 = [5, 10, 15, 20, 25, 50, 20]

Expected output:

[5, 10, 15, 200, 25, 50, 20]

"""
from remove_empty import remove_empty_from_list

def replace_in_list(list_to_change, value_to_change,new_value):
    index = list_to_change.index(value_to_change)
    list1.remove(value_to_change)
    list1.insert(index, new_value)


list1 = [5,"",None, 10, 15, 20, 25, 50, 20]
replace_in_list(list1,20,200)
replace_in_list(list1,15,150)
list1 = remove_empty_from_list(list1)
print(list1)
