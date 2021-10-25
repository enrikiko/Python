import time
import datetime
timeString = "2019-05-16 14:45:00"
date_time_obj = datetime.datetime.strptime(timeString, '%Y-%m-%d %H:%M:%S')
print(date_time_obj.strftime("%s"))
# dt = datetime.fromtimestamp(mktime(struct))
# def toTimeStamp(date_time_obj):
#     timestamp = 0
#     timestamp = timestamp +
#
# print(time.time())
