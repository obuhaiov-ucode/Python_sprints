import re

def check(addr: str) -> bool:
    lst = addr.split(',')

    if len(lst) == 4 and re.match(r"^Ukraine", lst[0])\
            and re.match(r"^\s*(?:[A-Z][a-z\_]+[\.]?(\s|\-))+\s*$", lst[1].__add__(' '))\
            and re.match(r"^\s*(?:[A-Z][a-z\_]+[\.]?(\s|\-)?)+\d{1,6}\s*$", lst[2])\
            and re.match(r"^\s*\d{5}\s*$", lst[3]):
        return True
    else:
        return False

def check_address(dct: dict) -> list:
    res = []

    if isinstance(dct, dict) and dct:
        for key in dct:
            if check(dct[key]):
                res.append(f'The address of {key} is valid')
            else:
                res.append(f'The address of {key} is invalid')
    return res
