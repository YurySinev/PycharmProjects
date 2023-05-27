from figures import Rectangle, Square, Circle, SquareFactory

r1 = Rectangle(17, 28)
r2 = Rectangle(17, 28)
r3 = Rectangle(21, 14)
s1 = Square(15)
s2 = Square(39)
c1 = Circle(13)
c2 = Circle(41)

figures = [s2, c2, r1, c1, s1, r2]

for fig in figures:
    if isinstance(fig, Square):
        print("Площадь квадрата:", fig.get_area_square())
    elif isinstance(fig, Circle):
        print("Площадь круга:", fig.get_area_circle())
    else:
        print("Площадь прямоугольника:", fig.get_area())

# print(r1 == r2)
# print(r2 == r3)

sq1 = SquareFactory.create_square(15)
print(sq1)
print(sq1.size)