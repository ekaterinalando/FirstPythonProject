# 1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#         Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

user_data = input('Please enter your surname, name and age: ')
x = user_data.split()
print(f'Hello {x[0].capitalize()} {x[1].capitalize()}. Your age is {x[2]}.')