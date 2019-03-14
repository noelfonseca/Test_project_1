import pyperclip, re
phoneRegex = re.compile(r'''((\d{3}|\(\d{3}\))?
	(\s|-|\.)?							# area code
	\d{3}								# separator
	(\s|-|\.)							# first 3 digits
	\d{4}								# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?		# extension
	)''', re.VERBOSE)

#Create email regex.
emailRegex = re.compile(r'''(
	[a-zA-z-09._%+-]+	#username
	@					#@ symbol
	[a-zA-Z0-9.-]+		#domain name
	(\.[a-zA-Z]{2,4})	#dot something
	)''', re.VERBOSE)
#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]