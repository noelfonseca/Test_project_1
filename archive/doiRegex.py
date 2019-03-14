#! python3
#doi detector

import pyperclip, re

doiRegex = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'])\S)+)\b')

text = str(pyperclip.paste())
matches = []

for items in doiRegex.findall(text):
	print(items)
print('\n\n\n----------------')
print('There are ' + str(len(doiRegex.findall(text))) + ' dois within the text you copied')
print('----------------\n\n\n')