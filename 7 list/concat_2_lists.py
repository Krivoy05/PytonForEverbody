"""
Concatenate two lists index-wise

Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

Expected output:

['My', 'name', 'is', 'Kelly']
"""
def concat(list1,list2):
    result = list()
    for i in range(len(list1)):
        result.append(list1[i]+list2[i])
    return result

def concat_zip(list1,list2):
    zipped_li = list(zip(list1,list2))
    res2 = list()
    any(res2.append("".join(element)) for element in zipped_li)
    return res2

def concat_zip_example(list1,list2):
    return [i+j for i,j in zip(list1,list2)]

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
li3 = [i + j for i, j in zip(list1, list2)]

print(concat(list1,list2))
print(concat_zip(list1,list2))
print(concat_zip_example(list1,list2))

