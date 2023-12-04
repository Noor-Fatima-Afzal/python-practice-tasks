hours=int(input("enter hours"))

hours_in_a_day = 24
days = hours // hours_in_a_day
remaining_hours = hours % hours_in_a_day

days_in_a_week = 7
weeks = days // days_in_a_week
remaining_days = days % days_in_a_week


print(hours,"are",weeks,"weeks",remaining_days,"days and",remaining_hours,"hours")