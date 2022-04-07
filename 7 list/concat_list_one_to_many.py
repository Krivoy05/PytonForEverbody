"""
Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""
def concat_one_to_many_for_iteration(list1, list2):
    result = list()
    for i in list1:
        for j in list2:
            result.append(i+" "+j)
    return result
def concat_one_to_many(list1, list2):
    result = list()
    result = [i+j for i in list1 for j in list2]
    return result

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concat_one_to_many_for_iteration(list1,list2))
print(concat_one_to_many(list1,list2))
