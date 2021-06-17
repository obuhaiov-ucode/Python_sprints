f_val = int(input("---- Simple calculator ----\nLet's add some numbers\nInput your first value: "))
op_val = input('Input your operator: ')
if op_val == '+' or op_val == '-' or op_val == '*' or op_val == '/':
    s_val = int(input('Input your second value: '))
    if op_val == '+':
        print(f'{f_val} + {s_val} =', f_val + s_val)
    elif op_val == '-':
        print(f'{f_val} - {s_val} =', f_val - s_val)
    elif op_val == '*':
        print(f'{f_val} * {s_val} =', f_val * s_val)
    else:
        print(f'{f_val} / {s_val} =', f_val / s_val)
else:
    print("usage: the operator must be '*' or '+' or '-' or '/'")
print("---- Simple calculator ----")