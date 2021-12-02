
id_code = '131052-308T'
while True:
    try:
        user_input = input('Please enter ID code: ')
        if len(user_input) != 11:
            raise UserWarning
    except UserWarning:
        if len(user_input) > 11:
            print('ID code is too long')
        elif len(user_input) < 11:
            print('ID code is too short')
        continue
    else:
        break
print(user_input)
condition = True
while condition:
    user_choice = input('Please choose:\n1.Get data from ID\n2.Validate\n0.Exit')
    if user_choice == '1':
        gender_num = user_input[7:10]
        by_num = user_input[4:6]
        bm_num = user_input[3:5]
        bd_num = user_input[0:2]
        check_num = user_input[10]

        # Get gender of ID owner
        if int(gender_num) % 2 == 0:
            gender_id = 'Female'
        else:
            gender_id = 'Male'

        # Get year of birth

        if id_code[6] == '+':
            by = '18'+ id_code[4:6]
        elif id_code[6] == '-':
            by = '19'+ id_code[4:6]
        elif id_code[6] == 'A':
            by = '20'+ id_code[4:6]
        else:
            print ('Your ID code is invalid')


        print(f'ID: {user_input}')
        print(f'Gender: {gender_id}')
        print(f'Date of birth: {bd_num}.{bm_num}.{by}')


    elif user_choice == '2':
        id_code = user_input

        chk = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'ABCDEFHJKLMNPRSTUVWXY']
        chk[10] = range[11:]



        cnt = 0
        result = 0
        for num in chk1:
            result += num * int(id_code[cnt])
            cnt += 1
        check_num = result % 11

        if int(id_code[-1]) == check_num:
            print(f'Your ID is {id_code}')
            print('ID is valid')
        elif check_num == 10:
            cnt = 0
            result = 0
            for num in chk2:
                result += num * int(id_code[cnt])
                cnt += 1
            check_num = result % 11
            if check_num == int(id_code[-1]):
                print(f'Your ID is {id_code}')
                print('ID is valid')
            else:
                print('Your ID is invalid.')
        else:
            print('Your ID is invalid.')
    elif user_choice == '0':
        break
    else:
        print('Choice is out of range')



