import json, pprint, pyperclip, csv

json_string = str(pyperclip.paste())

parsed_json = json.loads(json_string)


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, [key] + pre):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, [key] + pre):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


rows = str(pprint.pprint(list(dict_generator(parsed_json))))

with open('random4.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)