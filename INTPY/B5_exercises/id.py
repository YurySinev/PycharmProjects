L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 0
b = 0
print(id(a))
print(id(b))

while id(a) == id(b):
    a -= 1
    b -= 1
print(a, id(a), b, id(b))
