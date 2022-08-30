#
# C1.5. Магический метод __init__
#
# Мы уже говорили о том, что классы задают структуру данных своих будущих экземпляров
# с помощью атрибутов. Но если у любого экземпляра можно задавать произвольные атрибуты,
# а затем совершенно независимо менять, то как это поможет нам создать кучу одинаковых
# объектов и управлять их единообразием?
#
# Для этого используется конструктор класса, магический метод __init__, который заранее
# определяет атрибуты новых экземпляров. Первым аргументом он обязательно принимает на
# вход self, а дальше — произвольный набор аргументов, как обычная функция:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

#
# Здесь __init__ — это так называемый «магический» метод-конструктор, окруженный двумя
# нижними подчёркиваниями с обеих сторон. Такие подчёркивания иногда для краткости называются
# дандерами, от «double underscore». Магические методы обычно неявно вызываются при совершении
# каких-либо операций, и мы подробнее разберём их дальше в курсе. Пока что для нас неважно,
# почему он называется именно так — достаточно запомнить, что конструктор класса всегда
# называется именно__init__.
#
# Метод-конструктор задаётся как функция внутри класса (не забудьте про отступ) и первым
# аргументом всегда принимает self. Именно с помощью этого хитрого финта в него передаётся
# объект с экземпляром, поэтому его нельзя забывать.
#
# Этот метод вызывается каждый раз, когда мы создаём экземпляр.
#
# После того как мы задали конструктор, при создании объектов в скобки вызова класса
# можно передавать аргументы, которые он принимает на вход. Чтобы не запутаться,
# можно явно указать, в какой аргумент что класть:

peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)

# Вывод:
#
# Peter Robertson
# juliadonaldson@mail.com
#
# Вроде бы выглядит похоже на то, что мы получили в прошлый раз, но есть ключевая разница:
# при создании экземпляра класса мы сразу же задаём содержимое его атрибутов. Если так
# не сделать и не передать в вызов класса нужные аргументы, мы получим ошибку:

# chris = User()

# Вывод:
#
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'email'
#
# Мы видим, что конструктор класса способен задавать строгую структуру для создаваемых
# экземпляров — уже одно это способно здорово помочь с обеспечением единообразия большого
# количества однотипных объектов. У каждого, как минимум, будет одинаковый набор атрибутов.

# Задание 1.5.1
# Выберите правильные утверждения (множественный выбор).
#   Без разницы, как называть метод-конструктор. Главное, чтобы он был определён внутри
#       класса и принимал на вход self.
#   Аргумент self может идти любым по порядку, главное, чтобы он назывался self.
#   Чтобы задать атрибут для объектов класса в конструкторе, нужно просто придумать
#       название и приписать его после self: self.attr_name = "value". Больше ничего не требуется.
#       верно
#   Атрибуты, заданные в методе __init__, будут доступны у всех объектов класса.
#       верно

# Задание 1.5.2
# Выберите верное(-ые) утверждение(-я) (подумайте, одно или несколько).
#   Если окружить переменную двойными подчёркиваниями с обеих сторон, она станет приватной.
#   Приватные переменные нельзя импортировать.
#   Название переменной может представлять из себя просто одинарный знак подчёркивания.
#       верно
#   Метод, который работает с экземпляром класса, называется магическим.

# ( см. дальше C1_6_incapsulation.py )

