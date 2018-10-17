import re

text = 'Ala ma 4 koty i 2 psy'

# result = re.match('\d', text)
result = re.search('\d', text)
print(result)

# Find all matches in text  - findall()
result = re.findall('\d', text)
print(result)

# Chnge found template into #
print(re.sub('\d', '#', text))
# Split string by template
print(re.split('\W', text))

# Use regex template more then once
reg = re.compile('\d')

result = re.search(reg, text)
# Return indexes from and untill foud match
print(result.span())
# Return start index
print(result.start())
# Return end index
print(result.end())
# Return first success match
print(result.group())