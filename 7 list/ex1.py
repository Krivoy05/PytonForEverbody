"""
Exercise 1:

Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

"""
def chop(in_list):
    del in_list[0]
    del in_list[len(in_list)-1]
    return None

def middle(in_list):
    result = in_list.copy()
    del result[0]
    del result[len(result)-1]
    return result


li = ["1","2","3","4","5"]
print("orginal list is:\n")
print(li)

print("return as new list: \n")
print(middle(li))

print("after chop function ist is: \n")
chop(li)
print(li)
