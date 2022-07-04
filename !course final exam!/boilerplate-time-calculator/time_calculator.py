#class for parsing data purporse
class Time:
    def __init__(self, hours, minutes, period):
        self.period = period
        self.minutes = minutes
        self.hours = hours

#class for get result
class TimeDays:
    def __init__(self, hours, minutes, period, days_later, day_of_week):
        self.day_of_week = day_of_week
        self.days_later = days_later
        self.period = period
        self.minutes = minutes
        self.hours = hours

def add_time(start, duration, *day):
    new_time = ""
    start_time = parse_time(start)
    duration_time = parse_time(duration)
    result_timedays = adder(start_time, duration_time, *day)

    #type issues, sometes return day of week as tuple
    if isinstance(result_timedays.day_of_week,tuple):
        result_timedays.day_of_week = result_timedays.day_of_week[0]

    #forming result string
    if (result_timedays.day_of_week is not None) and (result_timedays.days_later is None):
        new_time = str(result_timedays.hours) + ":" + str(
            minute_fixer(result_timedays.minutes)) + " " + result_timedays.period + ", "+result_timedays.day_of_week
    elif result_timedays.days_later is None:
        new_time = str(result_timedays.hours)+":"+str(minute_fixer(result_timedays.minutes))+" "+result_timedays.period
    elif (result_timedays.days_later == 1) and (result_timedays.day_of_week is None):
        new_time = str(result_timedays.hours) + ":" + str(
            minute_fixer(result_timedays.minutes)) + " " + result_timedays.period + " (next day)"
    elif (result_timedays.days_later == 1) and (result_timedays.day_of_week is not None):
        new_time = str(result_timedays.hours) + ":" + str(
            minute_fixer(result_timedays.minutes)) + " " + result_timedays.period + ", " \
                   + result_timedays.day_of_week + " (next day)"
    elif int(result_timedays.days_later) > 1:
        if result_timedays.day_of_week is None:
            new_time = str(result_timedays.hours) + ":" + str(
                minute_fixer(result_timedays.minutes)) + " " + result_timedays.period +\
                    " ("+str(result_timedays.days_later)+" days later)"
        else:
            new_time = str(result_timedays.hours) + ":" + str(
                minute_fixer(result_timedays.minutes)) + " " + result_timedays.period + ", " +\
                       result_timedays.day_of_week + " (" + str(result_timedays.days_later) + " days later)"
    return new_time


def minute_fixer(minutes):
    if int(minutes) <= 9:
        return "0"+minutes
    else:
        return minutes


def parse_time(start):
    hours = ""
    minutes = ""
    period = ""
    raw_data = start.split(":")
    if "AM" in start:
        period = "AM"
    elif "PM" in start:
        period = "PM"
    else:
        period = None
    hours = raw_data[0]
    minutes = raw_data[1][0:2]
    return Time(hours, minutes, period)


def adder(start, duration, *day_of_week):
    days_later = None
    period = start.period
    result_minutes_time = minute_adder(start.minutes, duration.minutes)
    h1 = int(start.hours)
    h2 = int(duration.hours)
    h3 = int(result_minutes_time.hours)
    result_hours = h1 + h2 + h3
    if result_hours >= 12:
        calculating_hours = result_hours
        while calculating_hours >= 12:
            period = opposite_period(period)
            calculating_hours = calculating_hours - 12

        #need to change 00 to 12
        if calculating_hours != 0:
            hours = calculating_hours
        else:
            hours = 12
    else:
        hours = str(result_hours)

    #count days if more 24 hours
    if result_hours >= 24:
        days_later = result_hours // 24
        if start.period == "PM":
            if period == "AM":
                days_later = days_later + 1
    else:
    #add one dy more, PM was changet to AM
        if start.period == "PM":
            if period == "AM":
                days_later = 1
    if days_later is None:
        if len(day_of_week) > 0:
            result_day_of_week = day_of_week
        else:
            result_day_of_week = None
    else:
        result_day_of_week = calculate_day(day_of_week, days_later)
    return TimeDays(hours, result_minutes_time.minutes, period, days_later, result_day_of_week)

def calculate_day(day, days_later):
    if len(day) == 0:
        return None
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    days_lowercase = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_number = days_lowercase.index(day[0].lower())
    index = (day_number+days_later) % 7
    result_day = days[index]
    return result_day

def opposite_period(period):
    if period == "AM":
        return "PM"
    elif period == "PM":
        return "AM"
    else:
        return None


def minute_adder(minutes1, minutes2):
    m1 = int(minutes1)
    m2 = int(minutes2)
    result_minutes = m1+m2
    if result_minutes >= 60:
        minutes = str(result_minutes % 60)
        hours = str(result_minutes//60)
    else:
        minutes = str(result_minutes)
        hours = "0"
    return Time(hours, minutes, None)

