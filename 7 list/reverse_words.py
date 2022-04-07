"""
Reverse each word of a string

Given:

str = 'My Name is Jessa'

Expected Output

yM emaN si asseJ
"""

def reverse_each_words(data):
    li = list()
    result_li = list()
    li += data.split(" ")
    for word in li:
        result_li.append(word[::-1])
    result = " ".join(result_li)
    return result

str = 'My Name is Jessa'
reverse = reverse_each_words(str)
print(reverse)