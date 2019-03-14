import json, pprint, pyperclip

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


print(list(dict_generator(parsed_json)))














'''jkeys = parsed_json.keys()
jvalues = parsed_json.values()

print(parsed_json['message']['content-domain']['domain'])
print(parsed_json['message']['content-domain']['crossmark-restriction'])

print(len(parsed_json['message']))

for item in parsed_json['message']:
	message_values = parsed_json['message'][str(item)]
	for x in message_values:
	# print(item)
		print(message_values[str(item)])
	print(message_values)'''










# print(parsed_json['message']['URL'])

'''parsed_json_keys = parsed_json.keys()
print(parsed_json_keys)'''
