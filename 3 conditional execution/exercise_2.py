#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by
# printing a message and exiting the program. The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours= 45
rate = "nine"
pay = -1
try:
    if hours >= 41:

        pay = rate*40 +(hours-40)*1.5*rate

    else:
        pay = hours*rate
except:
    print("Error, please enter numeric input")
if pay == -1:
    print("Pay can't be calculated, wrong input")
else:
    print("Calculaded pay is: "+str(pay))
