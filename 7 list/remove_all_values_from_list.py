"""
Remove all occurrences of a specific item from a list.

Given a Python list, write a program to remove all occurrences of item 20.

Given:

list1 = [5, 20, 15, 20, 25, 50, 20]

Expected output:

[5, 15, 25, 50]
"""
def remove_all_from_list(list1, value_to_delete):
    for element in list1:
        if element == value_to_delete:
            index = list1.index(value_to_delete)
            del list1[index]

def remove_from_list(list1,value):
    while True:
        try:
            list1.remove(value)
        except:
            break

list1 = [5, 150,20, 25, 50,20]
remove_from_list(list1,20)
print(list1)