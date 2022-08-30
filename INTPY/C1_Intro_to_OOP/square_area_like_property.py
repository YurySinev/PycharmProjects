#
# Задание 2.3.4
# Создать вычисляемое свойство для класса Square. Сделайте метод по вычислению площади свойством.
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер. В сеттере
# добавьте проверку условия, что сторона должна быть неотрицательной.

class Square:
    _side = None
    # def __init__(self, side): # не вижу смысла в этом блоке
    #     self.side = side      # без него работает, с ним - нет
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, side):
        if side > 0:
            self._side = side
        else:
            print("Это значение не может быть отрицательным числом")
    @property
    def area(self):
        return self.side**2

# sq = Square()
# sq.side = 22
# print(sq.side)