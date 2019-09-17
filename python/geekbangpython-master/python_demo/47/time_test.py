import time
import datetime


# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y%d%d'))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
#

print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=10)
newtime1 = datetime.timedelta(hours=11)
newtime2 = datetime.timedelta(seconds=11)
print(datetime.datetime.now()+ newtime1+newtime2)

one_day=datetime.datetime(2008,5,27)
new_date=datetime.timedelta(days=10)
print( one_day + new_date)