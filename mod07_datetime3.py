import datetime
import json
import re

date1 = datetime.date.today()
date2 = datetime.date(2012, 3, 12)

result = date1 - date2
print(result.total_seconds())
print(type(result), result)
day = datetime.timedelta(days=1)
print(date1 + day * 3)


file = open('./ress/dump.json', encoding='utf-8').read()


date_list = re.findall(r'[0-9]{2}.[0-9]{2}.[0-9]{4}', file)
date_result = []

for date in date_list:
    date_result.append(datetime.datetime.strptime(date, '%d.%m.%Y'))
    # print(min(date_result))

print(datetime.datetime.utcnow())
print(min(date_result))
print(datetime.datetime.utcnow() - min(date_result))
