import os
helloFile = open(str(os.getcwd() + '/hello.txt'), 'w')
helloFile.write('Hello world!\n')
helloFile.close()

helloFile = open(str(os.getcwd() + '/hello.txt'), 'a')
helloFile.write('Bacon is not a vegetable')
helloFile.close()

helloFile = open(str(os.getcwd() + '/hello.txt'))
helloContent = helloFile.read()
helloFile.close()
print(helloContent)