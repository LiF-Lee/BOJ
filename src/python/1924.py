import calendar
week = ["MON","TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, input().split())

day = calendar.weekday(2007, x, y)
print(week[day])