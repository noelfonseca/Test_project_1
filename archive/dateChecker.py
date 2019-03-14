def date(text): #checks date pattern XX/XX/XXXX
	if len(text) != 10:
		return False
	for i in range(0,1):
		if not text[i].isdecimal():
			return False
	if text[2] != '/':
		return False
	for i in range(3,4):
		if not text[i].isdecimal():
			return False
	if text[5] != '/':
		return False
	for i in range(6,9):
		if not text[i].isdecimal():
			return False
	return True


print(date('12/24/1984'))



