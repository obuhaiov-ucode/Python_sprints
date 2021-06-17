import json
import collections

def summary(file_json, summarize_by):
    with open(file_json, 'r') as read_json:
        try:
            dicts = json.load(read_json)
            c = collections.Counter()

            for dct in dicts:
                try:
                    if dct[summarize_by] and not c[dct[summarize_by]]:
                        c.setdefault(dct[summarize_by], 1)
                    elif dct[summarize_by] or dct[summarize_by] is False\
                                            or dct[summarize_by] == '':
                        c.update({dct[summarize_by]})
                    elif dct[summarize_by] is None:
                        c.update({None})
                except KeyError:
                    c.update({None})
                except TypeError:
                    c.update({"unhashable"})
            return dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        except json.decoder.JSONDecodeError:
            return 'Error in decoding JSON.'
