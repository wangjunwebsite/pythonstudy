#2.日期类型的 time 、datetime

import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
now_time = datetime.datetime.now()
print(now_time)
newtime = datetime.timedelta(minutes=10)
print(newtime + now_time)

one_day = datetime.datetime(2008,5,27)
newdata = datetime.timedelta(days=10)
print(one_day + newdata)