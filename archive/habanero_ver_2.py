
from crossref.restful import Works
import pprint, csv, json

works = Works()
enter_doi = input('Enter doi: ')
json_file = works.doi(enter_doi)
filename = input('Enter filename:')
with open(filename, 'w') as f:
	w = csv.DictWriter(f, json_file.keys())
	w.writeheader()
	w.writerow(json_file)