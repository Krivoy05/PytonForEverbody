""""
Counts the number of occurrences of item 50 from a tuple

Given:

tuple1 = (50, 10, 60, 70, 50)

Expected output:

"""

tuple1 = (50, 10, 60, 70, 50)

def count_occurrencies(tuple1,value):
    result = 0
    for el in tuple1:
        if el==value:
            result+=1
    return result

def count_occurrencies_count(tuple1,value):
    return tuple1.count(value)

print(count_occurrencies_count(tuple1,50))