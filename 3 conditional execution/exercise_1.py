#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours= 45
rate = 10
if hours >= 41:
    pay= rate*40 +(hours-40)*1.5*rate
else:
    pay = hours*rate

print(pay)
