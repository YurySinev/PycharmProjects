#
# ввод сразу нескольких переменных
#
# здесь вводимые переменные надо разделять клавишей Ввода:
"""
a, b, c = [int(input()) for _ in range(3)]
print(a, b, c)

# а здесь вводимые переменные разделяются Пробелом:
a, b, c = map(int, input().split())
print(a, b, c)
"""

# Задача 9. Напишите декоратор, который печатает имя функции при ее вызове
def my_decorator(fn):
    def wrapper():
        print(fn.__name__)
        return fn()
    return wrapper

@my_decorator
def myf():
    return 1
    print(myf())

def myf2():
    return 2

myf2=my_decorator(myf2)
print(myf2())

