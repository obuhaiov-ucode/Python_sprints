from itertools import groupby

def get_one_level(l_dct: list, k: str) -> dict:
    l_dct = sorted(l_dct, key=lambda x: x[k])
    res = {}

    for dct in l_dct:
        an_iterator = groupby(l_dct, lambda x: dct[k])
        for key, group in an_iterator:
            res_lst = []
            for item in group:
                if item[k] == key:
                    tmp = dict(item)
                    tmp.pop(k)
                    res_lst.append(tmp)
            res.update({key: res_lst})
    return res

def group(l_dct: list, lst: list) -> dict:
    if isinstance(l_dct, list) and isinstance(lst, list):
        i = 0
        res = get_one_level(l_dct, lst[i])

        # i = 1
        # while i < len(lst):
        #     l_dct = list(res.values())
        #     for dct in l_dct:
        #         tmp = (get_one_level(dct, lst[i]))
        #         for k, v in res.items():
        #             res.update({k: tmp})
        #     i += 1
        return res
    raise ValueError('The arguments must be a dict and a list.')
