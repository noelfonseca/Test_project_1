
from crossref.restful import Works
import pprint, json

works = Works()
enter_doi = input('Enter doi: ')

json_file = works.doi(enter_doi)
# pprint.pprint(json_file.keys())
# pprint.pprint(json_file)

bibkeys = ['haha','author', 'title', 'short-container-title', 'volume', 'issue', 'published-print','type', 'page', 'DOI', 'subject']

Authors = []
Title = []
Publisher = []
Volume = []
Issue_no = []
Year = []
Type = []
Page = []
Subject = []
D_O_I = []

for bib in bibkeys:
	if bib not in json_file.keys():
		continue
	if bib == 'author':
		for authInitials in json_file[bib]:			
			if 'given' not in authInitials.keys():
				Authors.append(authInitials['family'])
				continue
			else:
				family_and_initial = authInitials['family']+ ', ' + authInitials['given'][0] + '.'
				Authors.append(family_and_initial)
		continue
	if bib == 'title':
		Title.append(json_file[bib][0])
		continue
	if bib == 'short-container-title':
		Publisher.append(json_file[bib][0])
		continue
	if bib == 'volume':
		Volume.append(json_file[bib])
		continue
	if bib == 'issue':
		Issue_no.append(json_file[bib])
		continue
	if bib == 'published-print':
		Year.append(json_file[bib]['date-parts'][0][0])
		continue
	if bib == 'type':
		Type.append(json_file[bib])
		continue
	if bib == 'page':
		Page.append(json_file[bib])
		continue
	if bib == 'subject':
		Subject.append(', '.join(json_file[bib]))
	if bib == 'DOI':
		D_O_I.append(json_file[bib])

print('=====================================')
print(Year)
print(Authors)
print(Title)
print(Publisher)
print(Volume)
print(Issue_no)
print(Type)
print(Page)
print(Subject)
print(D_O_I)