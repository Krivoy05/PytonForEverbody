"""
Copy specific elements from one tuple to a new tuple

Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Given:

tuple1 = (11, 22, 33, 44, 55, 66)

Expected output:

tuple2: (44, 55)
"""
tuple1 = (11, 22, 33, 44, 55, 66)


def get_elements_from_tuple(tuple1, position, lenght):
    counter_in_tuple = 0
    result = list()
    for el in tuple1:
        if counter_in_tuple>= position and lenght>0:
            result.append(el)
            lenght -= 1
        counter_in_tuple +=1

    return tuple(result)

result = get_elements_from_tuple(tuple1,3,2)
print(result)

print(tuple1[3:5])