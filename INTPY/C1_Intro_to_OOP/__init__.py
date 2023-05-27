from C1_6_incapsulation import *


class User:
    ...


L = [4, 6, 7, 8, 4, 5, 3, 4, 2, 3, 4, 5]
U = User()
U.name = "Юра"
U.list = L
print(U.name, U.list)
print(Human)


class MyData:
    L = [4, 5, 6, 7, 8, 3, 4, 10, 2]
    txt = "тут какой-то текст"
    T = (4, 5, 3, 4, 5)
    D = {"печка": "лавочка",
         "кошка": "балабошка"}
    def __init__(self, name=None):
        self.name = name

print(MyData.D.keys())

md = MyData("моё!")

print(md.name, md.txt)
