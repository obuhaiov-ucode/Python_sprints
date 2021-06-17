sign = input('There are 3 signs in front of you. Which one would you like to read? ')
if sign == 'right':
    print('The right sign says: "DEAD PEOPLE ONLY"')
elif sign == 'left':
    print('The left sign says: "BEWARE!"')
elif sign == 'middle':
    print('The middle sign says: "CERTAIN DEATH"')
else:
    print(f'There is no {sign} sign')
