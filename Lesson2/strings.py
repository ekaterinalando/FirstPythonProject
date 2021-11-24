string_sample1 = 'Hello world!'
string_sample2 = 'firSt letter is loWer case'
string_sample3 = ' extral whitespace string'
string_sample4 = 'der fluß'

print(len(string_sample1))
# [start_index:stop_index:step]
print(string_sample1[:17])
print(string_sample1[::3])
print(string_sample1[-5:-1])

sliced_string = string_sample1[6:14]
print(string_sample1.upper())
print(string_sample4.casefold())
print(string_sample2.capitalize())
print(string_sample3.strip())
print(string_sample1.replace(' ', '*'))
print(string_sample1.split('w'))
print(string_sample1.count('o', 1, 10))
print(string_sample1.find('world'))