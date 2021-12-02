#2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам.
# (с = sqrt(a * a  +  b * b))

a = int(input('Please enter side "A": '))
b = int(input('Please enter side "B": '))
c = (a * a + b * b) ** 0.5
print(f'Side "C" is {c}')
