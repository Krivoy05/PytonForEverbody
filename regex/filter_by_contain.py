"""
 For the given list, filter all elements that do not contain e.

>>> items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
"""


def filter_by(li,must_contain_symbol):
    import re
    result_li = list()
    for el in li:
        if not re.findall(must_contain_symbol,el):
            result_li.append(el)
    return result_li


items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
result = filter_by(items,"e")
print(result)