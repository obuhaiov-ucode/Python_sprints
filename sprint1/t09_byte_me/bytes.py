def convert_to_bytes(arg1, arg2, arg3):
    tmp_bool = arg2
    error = False

    if arg2 != 'True' and arg2 != 'False':
        error = True
    try:
        integer = int(arg1)
        boolean = bool(arg2)
        string = str(arg3)
    except ValueError:
        return False
    int_bytes = bytes(integer)
    bool_bytes = bytes(boolean)
    str_bytes = bytes(string, 'utf-8')

    print(f'-- The int value is "{integer}"\nbytes: "{int_bytes}"')
    if error:
        print(f'-- The bool value is "False"\nbytes: "b\'\'"')
    else:
        print(f'-- The bool value is "{tmp_bool}"\nbytes: "{bool_bytes}"')
    print(f'-- The string value is "{string}"\nbytes: "{str_bytes}"')