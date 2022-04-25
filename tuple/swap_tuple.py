"""
Swap two tuples in Python

Given:

tuple1 = (11, 22)
tuple2 = (99, 88)

Expected output:

tuple1: (99, 88)
tuple2: (11, 22)
"""

tuple1 = (11, 22)
tuple2 = (99, 88)
print("Before")
print(tuple1)
print(tuple2)

def swap_tuple(tuple1,tuple2):
    tuple3 = tuple1
    tuple1 = tuple2
    tuple2 = tuple3
    return (tuple1,tuple2)

tuple1,tuple2 = swap_tuple(tuple1,tuple2)
print("After")
print(tuple1)
print(tuple2)