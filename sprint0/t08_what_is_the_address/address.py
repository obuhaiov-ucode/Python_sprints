first_var = 1000
second_var = first_var
third_var = 999
print(f'first_var = {first_var}, address is', id(first_var))
print(f'second_var = {second_var}, address is', id(second_var))
print(f'third_var = {third_var}, address is', id(third_var))
print(f'{first_var} is {second_var} =', first_var is second_var)
print(f'{second_var} is {third_var} =', second_var is third_var)