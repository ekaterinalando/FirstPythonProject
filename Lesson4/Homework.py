id_code = input('Please enter your ID code: ')

chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

cnt = 0
result = 0

for num in chk1:
    result += num * int(id_code[cnt])
    cnt += 1

check_num = result % 11

if int(id_code[-1]) == check_num:
   print(f'Your ID {id_code} is valid')
elif check_num  == 10:
    cnt = 0
    result = 0
    for num in chk2:
        result += num * int(id_code[cnt])
        cnt += 1
        check_num = result % 11
        if check_num == int(id_code[-1]):
            print(f'Your ID {id_code} is valid')
        else:
            print('Your ID is invalid')
else:
    print('Your ID is invalid')
