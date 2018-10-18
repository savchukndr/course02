import re

text = "Wiosenna 9/4, 00-122 Warszawa"

match = re.search(r'^(\w*)\s.*\s(\w*)$', text)

print(match.groups())
print(match.group(0))  # The whole string
print(match.group(1))  # First group
print(match.group(2))  # secong droup


html = '''
<code>test</code>
<city>Warszawa</city>
'''

# Returns all matches re.findall()
match = re.findall(r'<([a-z]+)>(.*)</(\1)>', html)  # repeat group (\1) - one, (\0) - all
print(match)


# Returns just first match re.search()
match = re.search(r'<([a-z]+)>(.*)</(\1)>', html)  # repeat group (\1) - one, (\0) - all
print(match.groups())


# Returns group by group name
match = re.search(r'<([a-z]+)>(?P<value>.*)</(\1)>', html)  # (?P<group name>pattern)
print(match.group('value'))