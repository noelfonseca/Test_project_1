import shelve

my_stuff = shelve.open('stuffData')
gadgets = ['Macbook pro', 'Ipad', 'Samsung Galaxy J Prime']
toiletries = ['toothbrush', 'toothpaste', 'mouthwash', 'floss']
bikes = ['roadbike', 'brompton']
my_stuff['toiletries'] = toiletries
my_stuff.close()

my_stuff = shelve.open('stuffData')
print(my_stuff['toiletries'])
my_stuff.close()