
from crossref.restful import Works
import pprint, csv, json

works = Works()
enter_doi = input('Enter doi: ')

json_file = works.doi(enter_doi)

print(json_file)

'''
with open('123123123.csv', 'w') as f:
	w = csv.DictWriter(f, json_file.keys())
	w.writeheader()
	w.writerow(json_file)'''