from datetime import datetime, timedelta

timestamp = 1693501992
from_ts = datetime.fromtimestamp(timestamp)
print(from_ts)
current_dt = datetime.today()
print(current_dt)
print(from_ts.isocalendar())
print(from_ts.strftime("%d %b %Y  %H:%M"))
delta = current_dt - from_ts
print(delta)
td = timedelta(hours=2)
print(current_dt+td)
