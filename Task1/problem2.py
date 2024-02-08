#write a program that takes today’s date and print tomorrow
day=int(input("Enter Day:"))
month=int(input("Enter Month:"))
year=int(input("Enter Year:"))
if day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
    month += 1
    day = 1
elif day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
    month += 1
    day = 1
elif month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    if day == 29:
        month += 1
        day = 1
    else:
        day+=1
elif month == 2 and ((year % 4 != 0 and year % 100 == 0) or (year % 400 != 0)):
     if day == 28:
        month += 1
        day = 1
     else:
        day += 1
elif  day == 31:
     if month == 12:
        year += 1
        month = 1
        day=1
else:
    day+=1



print(f"Day={day}  Month={month}  Year={year}")