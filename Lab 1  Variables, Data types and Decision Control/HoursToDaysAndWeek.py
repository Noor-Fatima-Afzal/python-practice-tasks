hours = int(input("Enter hours: "))
days = hours // 24
remaining_hours = hours % 24
weeks = days // 7
remaining_days = days % 7
print(hours, "are equal to", weeks, "weeks,", remaining_days, "days, and", remaining_hours, "hours")
