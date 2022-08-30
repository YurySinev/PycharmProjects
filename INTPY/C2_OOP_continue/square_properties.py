class Square:
    _side = None

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            print("Сторона квадрата не может быть 0 и меньше.")

    @property
    def area(self):
        return self._side ** 2

sq = Square()
sq.side = 6
print(sq.side, sq.area)
