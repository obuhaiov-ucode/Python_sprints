def add_to_bookshelf(title, lst):
    i = 0
    n = len(lst)

    while i < n:
        if lst[i] == '---':
            lst[i] = title
            return True
        i += 1
    return False
