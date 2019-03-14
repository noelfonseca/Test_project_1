import pprint

cats = [{'name':'Zophie', 'description': 'chubby'},{'name': 'Pooka', 'description': 'fluffy'}]

fileObj = open('myCats.py', 'w')
fileObj.write('myCats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats
print(cats)