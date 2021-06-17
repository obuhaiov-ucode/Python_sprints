f_str = input('Enter your first string: ')
s_str = input('Enter your second string: ')
if f_str == '' or s_str == '':
    print('One of the strings is empty.')
else:
    cmd = input('Enter your command: ')
    if cmd == 'find':
        if f_str.find(s_str) >= 0:
            print(True)
        else:
            print(False)
    elif cmd == 'concat':
        print(f'Your string is: {f_str} {s_str}')
    elif cmd == 'beatbox':
        f_num = int(input('Enter your first beatbox number: '))
        s_num = int(input('Enter your second beatbox number: '))
        print(f_str * f_num + s_str * s_num)
    else:
        print('usage: command find | concat | beatbox')