"""
Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum
of the numbers instead of the average.
"""

list_of_numbers = []
def find_minimum_and_maximum(list):
    minimum = list[0]
    maximum = list[0]
    for value in list:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    return "Maximum value is: "+str(maximum)+"\nMinimum value is: "+str(minimum)


while True:
    inputed_value = input("Input number: ")
    try:
        list_of_numbers.append(float(inputed_value))
    except:
        print("Please input only numbers")
    if inputed_value == "done":
        print("here is list of inputted numbers:")
        print(list_of_numbers)
        print(find_minimum_and_maximum(list_of_numbers))
        break

