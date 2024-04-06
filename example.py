import datetime 

current_date=datetime.datetime.now()


print(current_date.strftime("Today's Date    : %d"))
print(current_date.strftime("Current Month   : %B"))
print(current_date.strftime("Current Year    : %Y"))
print(current_date.strftime("Hours           : %H"))
print(current_date.strftime("Minutes         : %M"))
print(current_date.strftime("Seconds         : %S"))
print(current_date.strftime("Day             : %A"))
print(current_date.strftime("Weekday in decimal number : %w"))
