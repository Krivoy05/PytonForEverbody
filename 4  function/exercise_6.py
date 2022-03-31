"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and rate).
"""
#Setting constanse
normal_time_hours = 40
multipluer_overtime = 1.5


def computepay(hours, rate):
    try:
        if hours <= normal_time_hours:
         result = hours*rate
        else:
            result = rate *normal_time_hours +(multipluer_overtime*rate*(hours-normal_time_hours))
    except: result =-1
    print_pay(result, hours, rate)
    return result


def print_pay(pay, hours, rate):
    if pay == -1:
        print("Cant calculate pay, incorrect input data")
    else:
        print("You're worked: " + str(hours) + " hours")
        print("Normal rate is count for hours: " + str(normal_time_hours) + "   | You earn: "+ str(normal_time_hours*rate) + " dollars")
        if hours >= 41:
            print("Normal 1,5 rate is count for hours: " + str(hours - normal_time_hours) + "| You earn: "
              + str((hours - normal_time_hours)*multipluer_overtime*rate) + " dollars")
        print("You're total pay is: "+str(pay))



pay = computepay(41, 10)

