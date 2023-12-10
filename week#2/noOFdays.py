from datetime import date

firstdate = date(2004, 8, 7)
lastdate = date(2023, 12, 10)
days = lastdate - firstdate

print(days.days)  # Access the 'days' attribute to get the number of days
