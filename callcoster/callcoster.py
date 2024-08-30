day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
minutes = int(input("Enter the duration of the call (in minutes): "))

cost = 0
day = day.lower()

if day in ("sat", "sun"):
    cost = minutes * 0.15
else:
    if time < 8000 or time > 1800:
        cost = minutes * 0.25
    else:
        cost = minutes * 0.40


print("This call will cost $%2.2f" % (round(cost, 2)))
