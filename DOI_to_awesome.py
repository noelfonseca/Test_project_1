from crossref.restful import Works
import pprint, json, gspread, itertools
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SpreadsheetExample-b020928dcb91.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1f4qx_5JVGSdsSjfwdQM9s1NoX8saqe2w19v2nWp5faA').sheet1

works = Works()

enter_doi = input('Enter doi: ')
#enter_doi = '10.1016/j.gfs.2018.01.001'
#enter_doi = '10.1016/j.catena.2018.05.010'
#enter_doi = '10.1016/j.eja.2018.03.006' # Sudhir-Yadav - no given name
#enter_doi = 'http://dx.doi.org/10.1111/pbi.13087' #for checking
#enter_doi = '10.3390/genes10010030'
#enter_doi = 'http://dx.doi.org/10.20944/preprints201808.0493.v1' #NO CROSSREF
#enter_doi = '10.1111/dpr.12387'
#enter_doi = '10.1007/978-981-10-7461-5_17' #this is a book

json_file = works.doi(enter_doi)

bibkeys = ['author', 'title', 'short-container-title', 'volume', 'issue', 'published-print','type', 'page', 'DOI', 'subject', 'published-online']

# to add in bibkeys for books: 'container-title', 

last_name_list = []
given_name_list = []
Volume = ''
Issue_no = ''
Subject = ''
Page = ''
Year = ''
Publisher = ''


for bib in bibkeys:
	if bib not in json_file.keys():
		continue
	elif bib == 'author':
		for auth_initials in json_file[bib]:			
			if 'given' not in auth_initials.keys():
				family_name_only = auth_initials['family']
				#family_name_only_list.append(family_name_only)
			elif len(json_file[bib]) == 1:
				family_and_initial = auth_initials['family'] + ', ' + auth_initials['given']
				Authors = family_and_initial
			else:
				last_name_first = auth_initials['family'] + ', ' + auth_initials['given']
				last_name_list.append(last_name_first)				
				given_name_first = auth_initials['given'] + ' ' + auth_initials['family']
				given_name_list.append(given_name_first)				
				first_author = last_name_list[0]
				proceeding_authors = given_name_list[1:]
				proceeding_authors.insert(0, first_author)
				Authors = proceeding_authors
	elif bib == 'title':
		Title = json_file[bib][0]
	elif bib == 'short-container-title':
		if bib not in bibkeys:
			continue
		elif json_file[bib] == []:
			continue
		else:
			Publisher = json_file[bib][0] + ', '	
	elif bib == 'volume':
		if bib not in bibkeys:
			continue
		else: 
			Volume = 'Volume ' + str(json_file[bib]) + ', '	
	elif bib == 'issue':
		if bib not in bibkeys:
			continue
		else:
			Issue_no = 'no. ' + json_file[bib] + ', '
	elif bib == 'published-print':
		if bib not in bibkeys:
			Year = ''
			continue
		else:
			Year = str(json_file[bib]['date-parts'][0][0])
	elif bib == 'published-online':
		if bib not in bibkeys:
			Year = ''
			continue
		else:
			Year = str(json_file[bib]['date-parts'][0][0])
	elif bib == 'type':
		Type = json_file[bib]
		if json_file[bib] == 'journal-article':
			json_file[bib] = 'Journal'
			Type = json_file[bib]
		elif json_file[bib] == 'book-chapter':
			json_file[bib] = 'Book'
			Type = json_file[bib]
		else:
			Type = json_file[bib]
	elif bib == 'page':
		if bib not in bibkeys:
			Page = ''
			continue
		else:
			Page = 'p. ' + json_file[bib]
	elif bib == 'subject':
		Subject = ', '.join(json_file[bib])
	else:
		D_O_I = json_file[bib]

if 'given' not in auth_initials.keys():
	Authors.append(family_name_only)

Source = Publisher + Volume + ' ' + Issue_no + Page

print(type(json_file['type']))
print(json_file['short-container-title'])
print(Authors)
print(len(Authors))
if len(Authors) > 1:
	Authors.insert(-1, 'and')
	Authors[-2:] = [' '.join(Authors[-2:])]
	Authors = ', '.join(Authors)

BIBLIOGRAPHY = [Year, Authors, Title, Source, Type, D_O_I, Publisher]

# List values
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
print('=====================================')
new_list = ', '.join(map(str, BIBLIOGRAPHY))
print(new_list)
print('=====================================')


for affiliation in json_file['author']:
	for s in affiliation['affiliation']:
		if s['name'].startswith('International Rice'):
			pprint.pprint(affiliation['given'] + ' ' + affiliation['family'])
			pprint.pprint(s['name'])
	#pprint.pprint(affiliation['affiliation'])

for item in BIBLIOGRAPHY:
	if item == Year:
		wks.update_acell('A1', Year)
	elif item == Authors:
		wks.update_acell('E1', Authors)
	elif item == Title:
		wks.update_acell('F1', Title)
	elif item == Source:
		wks.update_acell('G1', Source)
	elif item == Type:
		wks.update_acell('I1', Type)
	elif item == D_O_I:
		wks.update_acell('J1', D_O_I)
	else:
		wks.update_acell('L1', Publisher)

#wks.insert_row('1', 'hello!', index=2)