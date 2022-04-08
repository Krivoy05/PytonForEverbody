"""
terate both lists simultaneously

Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:

10 400
20 300
30 200
40 100

"""
def iterate_and_reverse(l1,l2):
    result = list()
    l= zip(l1,l2[::-1])
    for x,y in l:
        result.append(str(x)+" "+str(y))
    return result

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
l3 = iterate_and_reverse(list1,list2)
for i in l3:
    print(i)
