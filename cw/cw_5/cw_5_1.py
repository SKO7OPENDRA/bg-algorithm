# Counter

from collections import Counter


a = Counter()
b = Counter('abrakadabra')
c = Counter({'red': 2, 'Blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')
print(b['z'])
b['z']=0
print(b)

print (list(b.elements()))
print(b.most_common(2))

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
g.subtract(f)
print(g)

print('*' * 50)
print(set(g))
print(dict(g))
