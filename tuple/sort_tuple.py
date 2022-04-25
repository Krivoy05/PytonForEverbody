"""
Sort a tuple of tuples by 2nd item

Given:

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))
"""

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

def sort_tuple_by_second_value(tuple1):
    di = list()
    result_li = list()
    di.extend( (v,k) for k,v in tuple1)
    di.sort()
    result_li.extend((v,k) for k,v in di)
    return tuple(result_li)

result = sort_tuple_by_second_value(tuple1)
print(result)
