# Напишите класс SquareFactory с одним статическим методом, принимающим единственный аргумент
# — сторону квадрата. Данный метод должен возвращать объект класса Square с переданной стороной
class Square:
#    side = None # это излишне
    def __init__(self, side):
        self.side = side

class SquareFactory:
    @staticmethod
    def square(side):
        return Square(side)

# sq = SquareFactory.square(3)
# print(sq.side)


