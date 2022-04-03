"""
Find all occurrences of a substring in a given string by ignoring the case

Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"

Expected Outcome:

The USA count is: 2
"""
def find_str(input_string , searched_value):
    counter = 0
    lowered_input = input_string.lower()
    searched_value_lenght = len(searched_value)
    while lowered_input.__contains__(searched_value):
        position_of_search_value = lowered_input.find(searched_value)
        counter +=1
        lowered_input = lowered_input[position_of_search_value+searched_value_lenght:]
    return counter

def find_str_optimised(input_string, searched_value):
    return input_string.lower().count(searched_value.lower())

str1 = "Welcome to USA. usa awesome, isn't it?"
search = input("Input text to search: ")

print("\""+search+"\" was writed "+str(find_str_optimised(str1,search))+" times in text")

