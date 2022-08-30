from divide_line import line

# Изменяемые типы данных как аргументы по умолчанию
#
# Разберём один случай, который может вызвать не совсем ожидаемое поведение функции.
# Основная идея состоит в том, что функция должна вести себя одинаково на одних и тех же входных данных
# и выдавать результат, который соответствует этим входным данным. Это одна из основных идей
# функционального программирования, то есть такого стиля написания кода, где всё опирается на функции.
#
# Аргументы по умолчанию создаются один раз в момент инициализации функции (первого прочтения
# интерпретатором инструкции def), а не при каждом вызове функции. Если в качестве аргументов
# по умолчанию использовать изменяемые типы данных (списки, словари), то они создаются один раз
# и будут использоваться на протяжении времени жизни функции. Так как при передаче словаря передаются
# не все его значения, а указатель на первый его элемент.
#
# Создадим неправильную функцию incorrect_func с указанием аргумента по умолчанию в виде списка.
# И вызовем эту функцию два раза.
line('некорректная функция')


def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


# вызовем два раза одну и ту же функцию
line('первый вызов функции')
incorrect_func()
line('второй вызов функции, значения изменились')
incorrect_func()

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [1]
# Аргумент после изменения [1, 1]
line('исправление этой ситуации')


# Видим, что при одних и тех же входных данных функция выдаёт разные результаты,
# что в дальнейшей разработке может вводить в заблуждение. Если вдруг внутри функции
# нужно использовать списки, то этот момент можно обойти следующим образом:

# установим аргумент name_arg пустым, а внутри функции будем проверять его
def correct_func(name_arg=None):  # по умолчанию name_arg пустой
    if name_arg is None:  # если пользователь его не переопределил
        name_arg = []
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


# вызовем два раза одну и ту же функцию
line('первый вызов функции')
correct_func()
line('второй вызов, изменений нет')
correct_func()  # дважды - никаких проблем
line()
line('вызов функции со значением')
correct_func([123])  # если передаем аргумент - тоже без проблем
line('вызов функции с именнованным аргументом, тоже без проблем')
correct_func(name_arg=[123])  # если передаем именованный аргумент - тоже нет проблем

# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]

# Чтобы избежать такого, создадим функцию correct_func, где в качестве значения по умолчанию
# укажем значение None. А вот уже внутри функции будем проверять, если пользователь не поменял
# это значение, то будем инициализировать, например, пустой список. И тогда всё будет хорошо,
# при каждом вызове функции, если это необходимо, этот пустой список будет инициализироваться
# вместе со всеми остальными аргументами функции.
