import re

def contains(string: str, lst: list) -> list:
    res = list()

    if isinstance(string, str) and isinstance(lst, list):
        for substring in lst:
            if isinstance(substring, str)\
                    and re.search(substring, string, re.IGNORECASE):
                res.append(substring)
    return res
