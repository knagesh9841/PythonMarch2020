from datetime import date, time, datetime, timedelta


"""
When an object of this class is instantiated, it represents a date in the format YYYY-MM-DD. 
Constructor of this class needs three mandatory arguments year, month and date.

"""

my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

"""
Current date
To return the current local date today() function of date class is used. today() function comes with several attributes 
(year, month and day). These can be printed individually.
"""

today = date.today()

print("Today's date is", today)

# Printing date's components

print("Date components", today.year, today.month, today.day)

Time = time(13, 24, 56)

print("Entered time", Time)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

my_time = time(minute=12)
print("Time with one argument", my_time)

my_time = time()
print("Time without argument", my_time)

a = datetime(1999, 12, 12)
print(a)

# Initializing constructor
# with time parameters as well

a = datetime(1999, 12, 12, 12, 12, 12)
print(a)

print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

# Current date and time

today = datetime.now()

print("Current date and time is", today)


"""
Timedelta class
Python timedelta() function is present under datetime library which is generally used for calculating differences in dates and also can be used for date manipulations in Python. It is one of the easiest ways to perform date manipulations.

Constructor syntax:

class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

Returns : Date

"""

ini_time_for_now = datetime.now()

print("initial_date", str(ini_time_for_now))

# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + timedelta(days=730)

future_date_after_2days = ini_time_for_now + timedelta(days=2)

past_date_before_2days = ini_time_for_now + timedelta(days=-2)

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))
print('past_date_before_2days', past_date_before_2days)

# Compare two Dates

if future_date_after_2days > past_date_before_2days:
    print("future_date_after_2days is Greater than past_date_before_2days")
else:
    print("future_date_after_2days is Less than past_date_before_2days")


"""
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""


formats = "%Y %B %d %I %M %S %p %Z"         # The format
past_date_before_2days = past_date_before_2days.strftime(formats)

print(past_date_before_2days)


