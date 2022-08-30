#
print("""
Наш список:
a = [6, 18, "Юрий", "Синёв", ["Елена", "Синёва", "жен."], (45, 87, "14"), 2, 0]
""")

a = [6, 18, "Юрий", "Синёв", ["Елена", "Синёва", "жен."], (45, 87, "14"), 2, 0]

print("-" * 25, "цикл for изнутри:", "-" * 25)
print("""
    it = iter(a)
    try:
        while True:
            print(next(it))
    except StopIteration:
        pass
""")
# Вот ТАК работает цикл FOR:
it = iter(a)
try:
    while True:
        print(next(it))
except StopIteration:
    pass

print("-" * 25, "чистый цикл for:", "-" * 25)
print("""
    for x in a:
        print(x)
""")
for x in a:
    print(x)

print("-" * 25, "'самодельный' цикл for:", "-" * 25)
print("""
    def my(l):
        it = iter(l)
        try:
            while True:
                print(next(it))
        except StopIteration:
            pass
""")

def my(l):  # можно вот так написать собственный цикл for
    it = iter(l)
    try:
        while True:
            print(next(it))
    except StopIteration:
        pass


my(a)  # и запустить его

print("-" * 20, "развернем и внутренние списки с кортежами", "-" * 20)
print("""
    for x in a:
        if type(x) == list or type(x) == tuple:
            for l in x:
                print(l)
        else:
            print(x)
""")
for x in a:
    if type(x) == list or type(x) == tuple:
        for l in x:
            print(l)
    else:
        print(x)

