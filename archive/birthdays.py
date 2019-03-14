birthdays = {'Alice': 'April 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	name = input('Enter a name: (or blank to quit)')
	if name == '':
		break
	if name in birthdays:
		print(name + "'s birthday is on " + birthdays[name])
	else:
		print('I do not have birthday information for ' + name)
		bday = input('What is their birthday? ')
		birthdays[name] = bday
		print('Birthday database updated')
		print(birthdays)