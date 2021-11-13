import datetime as dt

current_time = dt.datetime.now() #  current time stamp
print(current_time.strftime('%d-%m-%Y'))
print(current_time.today().strftime('%d-%m-%Y')) # todays date.


