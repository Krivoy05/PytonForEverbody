"""
Reverse a list in Python

Given:

list1 = [100, 200, 300, 400, 500]

Expected output:

[500, 400, 300, 200, 100]
"""

def list_reverse(list_to_reverse):
    result_li = list()
    result_li += list_to_reverse
    result_li.reverse()
    return result_li

def list_revers_as_string_solution(list_to_reverse):
    result_li = list()
    result_li += list_to_reverse
    result_li[::-1]
    return result_li

list1 = [100, 200, 300, 400, 500]

li2 = list_reverse(list1)
print(li2)

li3 = list_reverse(list1)
print(li3)
