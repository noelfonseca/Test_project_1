import shelve

shelf_file = shelve.open('my_data')
print(shelf_file['gadgets'])