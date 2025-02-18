import datetime

date1str = input("enter first date: ")
date2str = input("enter second date: ")

date1 = datetime.datetime.strptime(date1str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2str, "%Y-%m-%d %H:%M:%S")

difference = abs((date1 - date2).total_seconds())
print(difference)
