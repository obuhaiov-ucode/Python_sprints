def make_unique(dict_of_lists: dict) -> dict:
    result = dict()

    for key in dict_of_lists:
        value = sorted(list(set(dict_of_lists.get(key))))
        result.update({key: value})
    return result
