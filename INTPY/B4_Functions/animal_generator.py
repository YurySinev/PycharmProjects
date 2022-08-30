from divide_line import line
#
# пример из видео, 10:00
# та же фигня

def my_animal_generator():
    yield 'корова'
    for animal in ['кот','собака','медведь']:
        yield animal
    yield 'кит'

a = my_animal_generator()
print(next(a))
print(next(a))
for i in a:
    print(i)

line()
#
# пример из видео с числами Фибоначчи, 11:30:
def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

# num = 2
for i in fib():
    print(i)
