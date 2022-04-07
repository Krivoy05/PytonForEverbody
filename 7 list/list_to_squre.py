"""
Turn every item of a list into its square

Given a list of numbers. write a program to turn every item of a list into its square.

Given:

numbers = [1, 2, 3, 4, 5, 6, 7]

Expected output:

[1, 4, 9, 16, 25, 36, 49]
"""
def list_to_square(numbers):
    result = list()
    try:
        result = [i*i for i in numbers]
    except:
        print("there some not numeric value in list")
    return result
numbers = [1, 2, 3, 4, 5, 6, 7]

print(list_to_square(numbers))
