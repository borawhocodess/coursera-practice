import datetime as dt
import time as tm

print(tm.time())

dtnow = dt.datetime.fromtimestamp(tm.time())

print(dtnow)

today = dt.date.today()

print(today)