s = {1, 2, 3, 4, 5}
s.remove(3)
s.discard(3)

#================================

a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {2, 4, 6, 8, 10}
c = {1, 3, 5, 7, 9}

#3.1
print(a.intersection(b))
#3.2
print(a.difference(b))
#3.3
print(b.union(c))
#3.4
a.clear()
b.clear()
c.clear()
print(a, b, c)

