# Write a code to return "Hero" from given string
example_string1 = "Hello bro"

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"

# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

# Write a code to return byte_string text value
byte_string = b"\316\273"

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000.00$"


print(example_string1[:2] + example_string1[7:])
print(example_string2.capitalize())
print(example_string3.strip('*'))

example_string4 = "hello my name is "
print(example_string4.capitalize()+var1.capitalize())
print(var2.capitalize()+',', var3.lower(), var1.capitalize())
print(byte_string.decode())

cost = 1000.00
example_string5 = f"It cost me {cost}$"
if cost >= 500: print('True')
