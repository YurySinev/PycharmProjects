class Room:
    def get_room(self):
        print("комната")

class Room1(Room):
    def get_room(self):
        print("комната один")

class Room2(Room):
    def get_room(self):
        print("комната два")

class Flat(Room1, Room2):
    def get_flat(self):
        print("двухкомнатная квартира")

print(Flat.mro())
# [<class '__main__.Flat'>, <class '__main__.Room1'>, <class '__main__.Room2'>,
# <class '__main__.Room'>, <class 'object'>]

f = Flat()
f.get_room()
# комната один

# Обратите внимание на метод mro(), он относится к методам класса, а не объекта класса,
# поэтому вызывается непосредственно от Flat. Метод mro() возвращает порядок, в котором
# будут проинспектированы родительские классы. Методы класса будут подробно рассмотрены
# в следующем модуле.
#
# На практике сложные системы наследования используются не так уж часто. Как правило,
# берутся сторонние готовые библиотеки и модули и выполняется наследование от нужных классов,
# чтобы дополнить и переопределить их логику.
