#23.Create a date-time variable in python and display the current date and time.
from datetime import date
from datetime import datetime

today = date.today()
print("\nToday's date: ",today)

now = datetime.now()
print("\nnow =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("\ndate and time =", dt_string)