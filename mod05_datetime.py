

# date, time, datetime, deltatime, timezone
import datetime
import locale

today = datetime.datetime.today()

print(type(today))
print(today)
print(today.strftime('%a %b %d %Y %m'))

# locale.setlocale(locale.LC_TIME, 'pl')
print(today.strftime('$A %B %d %Y %m'))
print(f'{today:%c}')

# date1 = datetime.date()
date1 = datetime.datetime.strptime('03/20/2012', '%m/%d/%Y')
print(date1)
print(date1.year, date1.month, date1.day)
