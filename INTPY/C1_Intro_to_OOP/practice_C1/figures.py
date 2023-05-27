class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


class Square:
    def __init__(self, size):
        self.size = size

    def get_area_square(self):
        return self.size ** 2
    def __str__(self):
        return f"Сторона квадрата: {self.size}. Площадь: {self.get_area_square()}"


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return self.r ** 2 * 3.14


class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)

