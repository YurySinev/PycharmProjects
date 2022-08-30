a = 10
list_ = []
while a < 50:
    a += 5
    if a == 25 or a == 35:
        b = a ** 2
        list_.append(b)
    list_.append(a)

print(list_)
