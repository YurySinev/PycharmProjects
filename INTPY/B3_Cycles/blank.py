a = "Юрий Синёв"
b = ''

it = iter(a)
try:
    while True:
        b += next(it) + '..'
        print(b)
except StopIteration:
    pass

# print(b)
