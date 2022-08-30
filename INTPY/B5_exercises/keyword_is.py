a = 42
b = 42
print(a == b)
print(a is b)

c = -123456789
d = -123456789
print(c == d)
# True
print(c is d)
# False

print("----------------------")

L = ['Hello', 'world']
M = L

print(M is L)
# True

M = L.copy()
print(M is L)
# False
print("--------------------------")

L = ['Hello', 'world']
M = L

# print(M is L)
# True
# M.append('!')

print(L)
# ['Hello', 'world', '!']

M = L.copy()
print(M)
print(M is L)
