# изменится ли id?
L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
# нет
print("---------------")

a = 4
b = 2+2
print(id(a))
print(id(b))