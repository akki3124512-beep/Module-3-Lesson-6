from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is ", today)
print("\nRight now it is ", now)

print("\nThe different components are: ", today.month, today.year, today.day)
