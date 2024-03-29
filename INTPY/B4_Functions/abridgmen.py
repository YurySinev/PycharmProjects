from divide_line import line

# Функция высшего порядка — в программировании это функция, принимающая в качестве
# аргументов другие функции или возвращающая другую функцию в качестве результата.
#
# Основная идея состоит в том, что функции имеют тот же статус, что и другие объекты данных.
#
print("Функция высшего порядка:")


def twice_func(inside_func):
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    inside_func()


def hello():
    print("Hello")


# имя одной функции передается другой в качестве аргумента. Более того,
# даже и сами функции запускаются в виде присвоения переменной значения
test = twice_func(hello)
# Hello
# Hello
line()
#
print('Замыкание функций:')


# Замыкание функций
#
# Замыкание в программировании — это функция, в теле которой присутствуют ссылки на переменные,
# объявленные вне тела этой функции в окружающем коде и не являющиеся её аргументами.
#
# Вспомните нелокальную (nonlocal) область видимости, на этом принципе работает замыкание функций.
#

def info(func):
    print("Функция, которая будет к любому числу прибавлять пятёрку")
    print("(сообщение от функции-декоратора до выполнения осн.функции)")
    return func

@info
# Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и то же число x:
def make_adder(x):
    def adder(n):
        return x + n  # захват переменной "x" из nonlocal области

    return adder  # возвращение функции в качестве результата


add_5 = make_adder(5)
print("10 + 5 = ", add_5(10))  # 15
print("100 + 5 = ", add_5(100))  # 105


line()
