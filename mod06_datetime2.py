import datetime


date1 = datetime.date.today()
date2 = datetime.date(2012, 3, 12)

result = date1 - date2
print(result.total_seconds())
print(type(result), result)
day = datetime.timedelta(days=1)
print(date1 + day * 3)