"""
npack the tuple into 4 variables

Write a program to unpack the following tuple into four variables and display each variable.

Given:

tuple1 = (10, 20, 30, 40)

Expected output:

tuple1 = (10, 20, 30, 40)
# Your code
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40

"""
def tuple_to_list(tup):
    res = list()
    for el in tup:
        res.append(el)
    return res

def print_result(li):
    charecter_counter = ord(u"a")
    for el in li:
        print("print("+chr(charecter_counter) +") # should print "+ str(el))
        charecter_counter += 1

tuple1 = (10, 20, 30, 40)
result = tuple_to_list(tuple1)
print_result(result)