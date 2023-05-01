L = [1, 3, 4, 6, 7, 8, 19]
print(L)
M = L[::-1]
print(M)
if 19 in L:
    print("Ага, есть такое дело")
else:
    print("Не-а, нет такого")
print(True if L is M else False)

print("5" in str('12346789678678'))

n = 1234686950762354

print(('7' and '3') in str(n))