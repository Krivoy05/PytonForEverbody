"""
Modify the tuple

Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

Given:

tuple1 = (11, [22, 33], 44, 55)

Expected output:

tuple1: (11, [222, 33], 44, 55)
"""

tuple1 = (11, [22, 33], 44, 55)

def modify_tuple(tuple1,positon,new_value):
    result= list(tuple1)
    result[positon][1] = new_value
    return tuple(result)

tuple1 = modify_tuple(tuple1,1,222)
print(tuple1)
