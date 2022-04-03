"""
Find the last position of a given substring

Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."

Expected Output:

Last occurrence of Emma starts at index 43
"""
def find_last_index_optimised(input_string,searched_value):
    return input_string.rfind(searched_value)

def find_last_index_no_case_sensetive(input_string, searched_value):
    position_counter = 0
    counter = 0
    lowered_input = input_string.lower()
    searched_value_lenght = len(searched_value)
    while lowered_input.find(searched_value.lower())>-1:
        position_of_search_value = lowered_input.find(searched_value.lower())
        position_counter += position_of_search_value
        if counter > 0:
            position_counter += searched_value_lenght
        counter += 1
        lowered_input = lowered_input[position_of_search_value+searched_value_lenght:]
    return position_counter
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Last occurrence of Emma starts at index "+str(find_last_index_optimised(str1,"Emma")))
print("Last occurrence of Emma starts at index " + str(find_last_index_no_case_sensetive(str1, "Emma")))
