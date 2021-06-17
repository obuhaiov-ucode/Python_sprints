def print_str_analytics(string):
    printables = alpha = num = lower = upper = white = 0

    for c in string:
        if c.isprintable():
            printables += 1
        if c.isalpha():
            alpha += 1
        if c.isdigit():
            num += 1
        if c.islower():
            lower += 1
        if c.isupper():
            upper += 1
        if c.isspace():
            white += 1
    print('|------------------------------------------------|')
    print('|                String analytics                |')
    print('|------------------------------------------------|')
    print(f"| '{string}'\n|------------------------------------------------|")
    print('| Number of printable characters is:', printables)
    print('| Number of alphanumeric characters is:', alpha + num)
    print('| Number of alphabetic characters is:', alpha)
    print('| Number of decimal characters is:', num)
    print('| Number of lowercase letters is:', lower)
    print('| Number of uppercase letters is:', upper)
    print('| Number of whitespace characters is:', white)
    print('|------------------------------------------------|')