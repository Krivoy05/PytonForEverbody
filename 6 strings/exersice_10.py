"""
Exercise 1: Write a while loop that starts at the last character in the string and works its
way backwards to the first character in the string, printing each letter on a separate line, except backwards.
"""
string = "Hello Wold!"
string_lenght = len(string)

while string_lenght > 0:
    print(string[string_lenght-1])
    string_lenght -= 1
"""
Exercise 3:

Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
"""

def count_a(word,counted_leter):
    count = 0
    for letter in word:
        if letter.lower() == counted_leter.lower():
            count = count + 1
    return count

seching_letter = "l"
print("Numbers of letter "+ seching_letter +" is:" +str(count_a(string,seching_letter)))

"""
Exercise 4:

There is a string method called count that is similar to the function in the previous exercise.
 Read the documentation of this method at
  https://docs.python.org/3.5/library/stdtypes.html#string-methods 
  and write an invocation that counts the number of times the letter a occurs in "banana"."""

string = "bananna"
print(string + " contains n:")
print(string.count("n"))

