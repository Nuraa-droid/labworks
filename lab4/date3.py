import datetime
now = datetime.datetime.now()
print(now)

drop = now.replace(microsecond=0)
print(drop)