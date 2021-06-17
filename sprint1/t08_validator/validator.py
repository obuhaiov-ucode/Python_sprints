def validator(string):
    lst = string.split(' ')

    try:
        lst[0] = float(lst[0])
        lst[2] = float(lst[2])
    except ValueError:
        return False
    if (lst[1] == '>=' or lst[1] == '<=' or lst[1] == '=='\
            or lst[1] == '<' or lst[1] == '>') and len(lst) == 3:
        if (lst[0] >= lst[2] and lst[1] == '>=')\
                or (lst[0] <= lst[2] and lst[0] == '<='):
            return True
        elif (lst[0] > lst[2] and lst[1] == '>')\
                or (lst[0] < lst[2] and lst[1] == '<'):
            return True
        elif lst[0] == lst[2] and lst[1] == '==':
            return True
        elif lst[0] >= lst[2] and lst[1] == '<=':
            return f'{lst[0]} >= {lst[2]}'
        elif lst[0] <= lst[2] and lst[1] == '>=':
            return f'{lst[0]} <= {lst[2]}'
        elif lst[0] > lst[2] and lst[1] == '<':
            return f'{lst[0]} > {lst[2]}'
        elif lst[0] < lst[2] and lst[1] == '>':
            return f'{lst[0]} < {lst[2]}'
        elif lst[0] == lst[2] and lst[1] != '==':
            return f'{lst[0]} == {lst[2]}'
    return False
