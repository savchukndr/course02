import json
import re


class RegIterator:

    def __init__(self, file):
        self.file = open(file, encoding='windows-1250')

    def __iter__(self):
        print('start iterator')
        return self

    def __next__(self):
        value = self.file.readline()
        if value == '':
            raise StopIteration
        return value

    def __del__(self):
        self.file.close()
        print('file is closed')

dt = []
for row in RegIterator('res/dump.dat'):
        # print(row)
        match = re.search(r'(.+)\s\((\d{2}.\d{2}.\d{4})\):\s(.+)\s(\d+,\d{2})\s\w{2}\n$', row)
        # print(match.groups())
        data = {}
        keys = ['nazwisko', 'data', 'miasto', 'wartosc']
        for x in keys:
            data[x] = match.groups()[keys.index(x)]
        dt.append(data)
json_data = json.dump(dt, open('res/dt.json', 'w', encoding='windows-1250'), ensure_ascii=False, indent=4)