x = 100

if x != 100:
    print('X is not equal to 100')
elif x == 100:
    print('X is equal to 100')
else:
    print(x)

id_code = input('Please enter ID: ')

if len(id_code) == 11:
    print('ID code is correct')
elif len(id_code) > 11:
    print('ID code is too long')
else:
    print('ID code is too short')

if len(id_code) == 11:
    print('ID code is correct')
else:
    if len(id_code) > 11:
        print('ID code is too long')
        if len(id_code) > 15:
            print('ID is more than 15 symbols')
    else:
        print('ID is too short')