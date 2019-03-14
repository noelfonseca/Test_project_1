
import pprint, json



json_file = {'reference-count': 67, 'references-count': 67, 'DOI': '10.1016/j.jag.2018.11.007', 'alternative-id': ['S0303243418306329'], 'issn-type': [{'value': '0303-2434', 'type': 'print'}], 'deposited': {'date-time': '2019-01-23T19:23:51Z', 'date-parts': [[2019, 1, 23]], 'timestamp': 1548271431000}, 'funder': [{'name': 'Indonesia Endowment Fund for Education', 'award': []}, {'name': 'ITC, University of Twente', 'award': []}], 'created': {'date-time': '2018-12-04T04:08:10Z', 'date-parts': [[2018, 12, 4]], 'timestamp': 1543896490000}, 'short-title': [], 'update-policy': 'http://dx.doi.org/10.1016/elsevier_cm_policy', 'issued': {'date-parts': [[2019, 4]]}, 'publisher': 'Elsevier BV', 'source': 'Crossref', 'content-domain': {'crossmark-restriction': True, 'domain': ['elsevier.com', 'sciencedirect.com']}, 'page': '143-153', 'subject': ['Computers in Earth Sciences', 'Earth-Surface Processes', 'Global and Planetary Change', 'Management, Monitoring, Policy and Law'], 'license': [{'start': {'date-time': '2019-04-01T00:00:00Z', 'date-parts': [[2019, 4, 1]], 'timestamp': 1554076800000}, 'delay-in-days': 0, 'content-version': 'tdm', 'URL': 'https://www.elsevier.com/tdm/userlicense/1.0/'}], 'language': 'en', 'relation': {}, 'member': '78', 'type': 'journal-article', 'short-container-title': ['International Journal of Applied Earth Observation and Geoinformation'], 'author': [{'authenticated-orcid': False, 'family': 'Fikriyah', 'given': 'Vidya Nahdhiyatul', 'affiliation': [], 'ORCID': 'http://orcid.org/0000-0003-2869-3657', 'sequence': 'first'}, {'family': 'Darvishzadeh', 'given': 'Roshanak', 'sequence': 'additional', 'affiliation': []}, {'family': 'Laborte', 'given': 'Alice', 'sequence': 'additional', 'affiliation': []}, {'family': 'Khan', 'given': 'Nasreen Islam', 'sequence': 'additional', 'affiliation': []}, {'family': 'Nelson', 'given': 'Andy', 'sequence': 'additional', 'affiliation': []}], 'URL': 'http://dx.doi.org/10.1016/j.jag.2018.11.007', 'container-title': ['International Journal of Applied Earth Observation and Geoinformation'], 'is-referenced-by-count': 0, 'link': [{'content-version': 'vor', 'intended-application': 'text-mining', 'content-type': 'text/xml', 'URL': 'https://api.elsevier.com/content/article/PII:S0303243418306329?httpAccept=text/xml'}, {'content-version': 'vor', 'intended-application': 'text-mining', 'content-type': 'text/plain', 'URL': 'https://api.elsevier.com/content/article/PII:S0303243418306329?httpAccept=text/plain'}], 'assertion': [{'name': 'publisher', 'value': 'Elsevier', 'label': 'This article is maintained by'}, {'name': 'articletitle', 'value': 'Discriminating transplanted and direct seeded rice using Sentinel-1 intensity data', 'label': 'Article Title'}, {'name': 'journaltitle', 'value': 'International Journal of Applied Earth Observation and Geoinformation', 'label': 'Journal Title'}, {'name': 'articlelink', 'value': 'https://doi.org/10.1016/j.jag.2018.11.007', 'label': 'CrossRef DOI link to publisher maintained version'}, {'name': 'content_type', 'value': 'article', 'label': 'Content Type'}, {'name': 'copyright', 'value': '© 2018 Elsevier B.V. All rights reserved.', 'label': 'Copyright'}], 'subtitle': [], 'original-title': [], 'score': 1.0, 'ISSN': ['0303-2434'], 'volume': '76', 'title': ['Discriminating transplanted and direct seeded rice using Sentinel-1 intensity data'], 'prefix': '10.1016', 'indexed': {'date-time': '2019-01-23T19:40:54Z', 'date-parts': [[2019, 1, 23]], 'timestamp': 1548272454487}, 'published-print': {'date-parts': [[2019, 4]]}}

# pprint.pprint(json_file.keys())



bibkeys = ['haha','author', 'title', 'short-container-title', 'volume', 'published-print', 'page', 'DOI']

for bib in bibkeys:
	if bib not in json_file.keys():
		continue
	'''json_finder = json_file[bib]
				if bib == 'author':
					for authInitials in json_file[bib]:
						print(authInitials['family']+ ', ' + authInitials['given'][0] + '.')
					continue
				if bib == 'published-print':
					print(json_file[bib]['date-parts'])
					continue'''
	print(json_file[bib][0])

	














'''Author = json_file['author']
for authInitials in Author:
	print(authInitials['family']+ ', ' + authInitials['given'][0] + '.')
Title = json_file['title']
Publisher = json_file['short-container-title']
Volume = json_file['volume']
Year = json_file['published-print']['date-parts'][0][0]
Page = json_file['page']
D_O_I = json_file['DOI']

bibkeys = [Title, D_O_I, Publisher, Volume, Year, Page]

for key in bibkeys:
	print(key)'''