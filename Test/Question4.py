#4 Пользователь вводит некоторый произвольный список list.
# Написать программу, выводящую элементы списка в обратном порядке.

list = input('Please enter your items: ')
x = list.split()
print(' '.join(x[::-1]))
