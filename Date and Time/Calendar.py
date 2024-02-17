import calendar

month, day, year = list(map(int, input().split()))

dayNumber = calendar.weekday(year, month, day)
     
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    
print(days[dayNumber])
