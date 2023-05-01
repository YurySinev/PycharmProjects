txt1 = "Москва"
txt2 = "москвА"

a = txt1.casefold()
b = txt2.casefold()

print(f'{txt1} == {txt2}')
print(txt1 == txt2)

print(f'{a} == {b}')
print(a == b)

