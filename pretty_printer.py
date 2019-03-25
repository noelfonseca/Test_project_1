from crossref.restful import Works
import pprint, pyperclip

works = Works()
enter_doi = input('pretty print the DOI: ')
#enter_doi = '10.1016/j.gfs.2018.01.001'
#enter_doi = '10.3390/genes10010030'
#enter_doi = 'http://dx.doi.org/10.3390/su10061732'
#enter_doi = 'http://dx.doi.org/10.20944/preprints201808.0493.v1'
#enter_doi = '10.1111/dpr.12387'
#enter_doi = '10.1007/978-981-10-7461-5_17'

json_file = works.doi(enter_doi)

new_json = json_file.pop('reference')

pprint.pprint(json_file)