"""
Download a copy of the file from www.py4e.com/code3/romeo.txt

Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
"""
text_file = open("romeo.txt","r")
ls =[]
ls1 = []

for line in text_file:
    words_list = line.split()
    ls = ls + words_list
set1 = set(ls)
elements_from_set = list()
for element in set1:
    elements_from_set.append(element)
elements_from_set.sort()

test = list()
while len(set1)>=1:
    test.append(set1.pop())
test.sort()
print(set1)

print(test)
print(elements_from_set)
