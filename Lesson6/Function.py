def squares(x):
    return x ** 2

y = 200
result = squares(y)

print(result)


def print_message(name, age, profession):
    return print(f'Hi my name is {name}, I am {age} years old. I work as a {profession}.')

user_name, user_age, user_profession = input('Enter name, age, profession' ).split(', ')

def double(x):
    y = x * 2
    return f'Double from {x} is {y}'

def triple(x):
    y = x * 3
    return y
number = 5
print(triple(triple(double(number))))

def fizz_buzz(start_num, end_num):
    for num in range(start_num, end_num):
        if num % 3 == 0 and num % 5 == 0:
            print(f'{num} FizzBuzz')
        elif num % 3 == 0:
            print(f'{num} Fizz')
        elif num % 5 == 0:
            print(f'{num} Buzz')
fizz_buzz(50, 1000)