alienDictionary = {"we": "vorag", "come": "thang", "in": "zon", "peace": "argh", "hello": "kodar", "can": "znak", "i": "az", "borrow": "liftit", "some":"zum", "rocket": "upgoman", "fuel": "kakboom", "please": "selpin", "don't": "baaaaaaaaarn", "about": "flabil", "welcome":"inkip", "our": "mandig", "new": "brang", "alien": "marangin", "overlords": "bap" }

englishPhrase = input("Please enter an English word or phrase to translate: ")

englishWords = englishPhrase.lower().split()
alienWords = []

for word in englishWords:
	if word in alienDictionary:
		alienWords.append(alienDictionary[word])
print(alienWords)