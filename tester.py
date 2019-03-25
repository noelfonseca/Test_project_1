l = ['a', 'b', 'c', 'd']
l.insert(-1, 'and')
l[-2:] = [' '.join(l[-2:])]
print(l)
