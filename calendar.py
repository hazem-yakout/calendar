import calendar
while True:
 x = calendar.TextCalendar()
 choose = int(input("enter please the year you want to know the calendar of it:\n"))
 print(x.pryear(choose))
 choice = input("do you need to continue in the app?\n").strip().lower()
 if choice == "no":
    break
print("program is exited.")


