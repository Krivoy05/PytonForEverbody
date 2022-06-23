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

"""
Replace all occurrences of note irrespective of case with X.
ip = 'This note should not be NoTeD'

"""

def replace_case_not_sensitive_compile(input_value,expresion_to_replace,new_expresion):
    import re
    patern = re.compile(expresion_to_replace, re.IGNORECASE)
    return patern.sub(new_expresion,input_value)

def replace_case_not_sensitive(input_value,expresion_to_replace,new_expresion):
    import re
    return re.sub(expresion_to_replace,new_expresion,input_value,flags=re.I)

ip = 'This note should not be NoTeD'
result = replace_case_not_sensitive(ip,"note","X")
print(result)