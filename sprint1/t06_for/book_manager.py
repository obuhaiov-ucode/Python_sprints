def get_anonymous(lst):
    res = []

    for elem in lst:
        if elem.find(' by ') < 0:
            res.append(elem)
    return res