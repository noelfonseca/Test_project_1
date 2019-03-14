
number = int(input())
while number > 1:
	if number % 2 == 0:
		number = int(number) // 2
		print(number)
	elif number % 2 == 1:
		number = 3 * int(number) + 1
		print(number)
