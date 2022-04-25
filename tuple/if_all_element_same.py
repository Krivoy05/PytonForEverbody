"""
Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

Expected output:

True
"""
tuple1 = (45, 45, 45, 45,4)

def is_all_elements_same(tuple1):
    result = False
    for i in range(len(tuple1)):
        if i+1>=len(tuple1):
            break
        if tuple1[i] == tuple1[i+1]:
            result = True
        else:
            result = False
    return result

def is_all_elements_same_all(tuple1):
    result = all(i == tuple1[0] for i in tuple1)
    return result


print(is_all_elements_same_all(tuple1))
