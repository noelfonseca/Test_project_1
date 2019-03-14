import shutil, os, send2trash

# PATHS
#############################################################
python_folder = '/home/nfonseca/Pythonprograms'
sample_folder = '/home/nfonseca/Pythonprograms/sample_folder'
bacon_file = sample_folder + '/bacon.txt'
inner_folder = sample_folder + '/inner_folder'
waffles_folder = inner_folder + '/delicious/walnut/waffles'
#os.makedirs(waffles_folder)
#############################################################
print(os.getcwd())
os.chdir(sample_folder)

#os.makedirs(waffles_folder)








# NOTES
#############################################################
# permanently deleting files and folders
#SHUTILS: COPY, MOVE AND REMOVE TREE
# shutil.move() will rename a file if you do not choose a specific folder to move your file.
# shutil.copy() can also rename the file being removed IF YOU WISH SO.
# shutil.rmtree() - will remove folders and the files it contains.

########################
'''def go_to_folder_folder(path):
	os.chdir(path)
	print(os.getcwd())'''
########################

########################
'''
os.chdir(sample_folder)
print(os.getcwd())

for filename in os.listdir(sample_folder):
	if filename.endswith('.txt'):
		os.unlink(filename) # always make sure that we are working in the current directory
'''
########################


# SEND2TRASH MODULE
########################
'''create_bacon = open('bacon.txt', 'w')
create_bacon.write('bacon')
create_bacon.close()
create_spam = open('spam.txt', 'w')
create_spam.write('spam')
create_spam.close()
create_eggs = open('eggs.txt', 'w')
create_eggs.write('eggs')
create_eggs.close()

create_bacon = open('bacon.txt', 'a')
create_bacon.write('\nbacon is not a vegetable')
create_bacon.close()
send2trash.send2trash('bacon.txt')'''
########################