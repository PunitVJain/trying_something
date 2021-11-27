import datetime as dt
import time

current_time = dt.datetime.now() #  current time stamp
print(current_time.strftime('%d-%m-%Y'))
print(current_time.today().strftime('%d-%m-%Y')) # todays date.
#print(time())
print(time.localtime())

