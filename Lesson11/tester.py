import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ]\ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
Mr. Jones
Mr Smith
Mrs. Robinson
Ms. T
Mrs

abc
ball mall hall tall
'''

sentence = 'Start a sentence and then bring it to an end Start'

pattern = re.compile(r'M(rs|s|r)\.? [A-Z][a-z]*')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
    
