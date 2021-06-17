def list_maker(string, delim=' '):
    if delim == '':
        return string.split()
    else:
        return string.split(delim)