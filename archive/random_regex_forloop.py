import re

regex1 = re.compile(r'Robocop')
regex2 = re.compile(r'ROBOCOP')
regex3 = re.compile(r'robOcop')
regex4 = re.compile(r'RobocOp')

regexes = [regex1, regex2, regex3, regex4]

for r in regexes:
	mo = r.search('robOcop')
	if mo == None:
		print('none!')
	else:
		print(mo.group())