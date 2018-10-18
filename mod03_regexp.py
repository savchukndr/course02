import re

# ^ - start of a string
# $ - end of a string



text = 'Ala ma 3 koty i 2 psy'


# re.IGNORCASE - flag for case ignore
print(re.search('^a', text, re.IGNORECASE)) # ^ - start of a string
print(re.search('y$', text)) # $ - end of a string
print(re.search('m', text))
print(re.search('^[AB]', text)) # [AB] - can be A or B on one position
print(re.search('^[^AB]', text)) # [^AB] - can be everything instead oa A and B
print(re.search('^[^A-K]', text)) # [^A-K] - zakres od A do K
print(re.search('[0-9]', text)) # moze byc od 0 do 9
print(re.search('[01-67]', text)) # moze byc 0, lub od 1 do 6, lub 7
print(re.search(r'[0-9][0-9]-[0-9][0-9][0-9]', '00-234')) # lub tamplate '\d\d-\d\d\d' lub '\d{2}-\d{3}'
print(re.search(r'\d\d-\d\d\d', 'test 00-234 test'))
print(re.search(r'\d{2}-\d{3}', 'test 00-234 test'))
print(re.findall(r'\d{1,4}', 'test 0 test 123 dd 1234 dd 24324324132')) # from 1 to 4
print(re.findall(r'\d{1,}', 'test 0 test 123 dd 1234 dd 24324324132')) # 1 or more
print(re.findall(r'\d+', 'test 0 test 123 dd 1234 dd 24324324132')) # + form 1 or more
print(re.findall(r'\d{2}\W?\d{3}', 'test 11-222 12333 ddsdsa 13 444 45d544 444555'))



