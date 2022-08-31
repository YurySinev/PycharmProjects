# Задание 3.2.5
# Задание на самопроверку.
# Создать класс Square. Добавить в конструктор класса Square собственное исключение
# NonPositiveDigitException, унаследованное от ValueError, которое будет срабатывать
# каждый раз, когда сторона квадрата меньше или равна 0.


class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, side):
        if side <= 0:
            raise NonPositiveDigitException('Неправильно указана сторона!')
        self.side = side

    def area(self):
        return self.side ** 2


if __name__ == '__main__':
    sq = Square(2)
    print(sq.area())
    print(dir(sq))
    print(help(sq))

