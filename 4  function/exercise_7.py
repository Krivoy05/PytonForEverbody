"""
Exercise 7: Rewrite the grade program from the previous chapter using a function called
computegrade that takes a score as its parameter and returns a grade as a string.
"""
def computegrade(score):
    result = ""
    try:
        if float(score) < 0:
            result = "Bad score"
        elif float(score) > 1:
            result = "Bad score"
        elif float(score) >= 0.9:
            result = "A"
        elif float(score) >= 0.8:
            result = "B"
        elif float(score) >= 0.7:
            result = "C"
        elif float(score) >= 0.6:
            result = "D"
        elif float(score) < 0.6:
            result = "F"
    except:
        result = "Bad score"
    return result


score = input("Enter score: ")
print("You score is: " + computegrade(score))
