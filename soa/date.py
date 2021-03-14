from datetime import timedelta as delt
from datetime import time
from datetime import datetime as dt
import datetime

then = dt.now()

print(f'now is {then}')

# https://docs.python.org/release/2.6/library/datetime.html#datetime.timedelta
# class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
# 60s * 60 = 1m * 60 = 1h
delta = delt(hours=1)

future = then + delta

print(f'through 1h will be {future}')
