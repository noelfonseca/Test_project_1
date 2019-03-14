from crossref.restful import Works
import pprint, json, gspread, itertools
from oauth2client.service_account import ServiceAccountCredentials


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
		for auth_initials in json_file[bib]:			
			if 'given' not in auth_initials.keys():
				Authors.append(auth_initials['family'])
				continue
			else:
				family_and_initial = auth_initials['family']+ ', ' + auth_initials['given'][0] + '.'
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

BIBLIOGRAPHY = [Authors, Title, Publisher, Volume, Issue_no, Year, Type, Page, D_O_I]
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SpreadsheetExample-b020928dcb91.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1f4qx_5JVGSdsSjfwdQM9s1NoX8saqe2w19v2nWp5faA').sheet1


new_list = ', '.join(map(str, BIBLIOGRAPHY))
print(new_list)


Authors = ', '.join(Authors)
print(type(Authors))
print(Authors)

wks.update_acell('A1', Authors)

for item in BIBLIOGRAPHY:
	if item == []:
		item.append('')

new_bibliography = Title + Publisher + Volume + Issue_no + Year + Type + Page + D_O_I

wks.append_row(new_bibliography)