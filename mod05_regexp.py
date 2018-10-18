import re

import requests

data = requests.get('http://www.nbp.pl/').text

match = re.search(r'<div>Tabela z dnia (\d{4})-(\d{2})-(\d{2})</div>', data)

# print(match.group(1))
print(match.groups())