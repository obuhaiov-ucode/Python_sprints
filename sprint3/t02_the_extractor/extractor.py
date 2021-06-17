def extractor(dct: dict, type = str) -> dict:
    if not isinstance(dct, dict):
        raise ValueError('The first argument must be a dict.')
    return dict(filter(lambda kv: isinstance(kv[1], type), dct.items()))
