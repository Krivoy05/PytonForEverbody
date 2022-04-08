"""
Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

Expected output:

["Mike", "Emma", "Kelly", "Brad"]

"""
def remove_empty_from_list(l):
    result = list()
    for value in l:
        if value:
            result.append(value)
    return result
def remove_empty_from_list_none(l):
    result = list(filter(None,l))
    return result


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#print(remove_empty_from_list(list1))
#print(remove_empty_from_list_none(list1))
