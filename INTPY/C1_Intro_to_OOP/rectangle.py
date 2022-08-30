PI = 3.1418


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.get_area() == other.get_area()

        def get_area(self):
            return self.a * self.b  # площадь = сторона х сторона


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_area(self):
        return self.a ** 2  # площадь: сторона в квадрате


# Задание 1.9.1, добавить еще и круг
class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return PI * self.r ** 2
