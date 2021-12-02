#3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float].
# Напишите программу, которая проверяет, является ли треугольник прямоугольным (с2=a2+b2)

side = input('Please enter side "A", side "B" and side "C": ')

x = side.split()

if float(x[2]) ** 2 == float(x[0]) ** 2 + float(x[1]) ** 2:
    print('This is right triangle')
else:
    print('This is not right triangle')



