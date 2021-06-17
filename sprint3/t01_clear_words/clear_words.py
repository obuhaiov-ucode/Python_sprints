import re

def clear_words(string: str) -> list:
    if isinstance(string, str) and string and not re.match(r"^\s+$", string):
        return list(map(lambda s: re.sub(r"(!|\?|\.|,|:|;|-)", "", s),
                        re.split("\s", string)))
    return list()
