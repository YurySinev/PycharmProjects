a = 123456789
b = 123456789
print(a == b)
print(a is b)


L = ["Hello", "World"]
M = L
print(L is M)

M.append("!")
print(L)

M = L.copy()
print(M is L)