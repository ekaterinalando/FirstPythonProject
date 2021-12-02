condition = True
while condition:
    user_choice = input('Please choose:\n1:Print message\n0:Exit\n-->')
    if user_choice == '1':
        print('Hello world')
    elif user_choice == '0':
        print('Good bye2')
        break
    print('test')

print('Good bye')