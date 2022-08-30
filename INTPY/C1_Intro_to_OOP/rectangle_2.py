from rectangle import Rectangle, Square, Circle

# создаем два прямоугольника
rect1 = Rectangle(5, 12)
rect2 = Rectangle(12, 5)

# # выводим площади этих прямоугольников
# print(rect1.get_area())
# print(rect2.get_area())

# создаем два квадрата
square1 = Square(5)
square2 = Square(10)

# # выводим площади этих квадратов
# print(square1.get_sq_area(),
#       square2.get_sq_area())

# создадим два круга, Задание 1.9.1
circ1 = Circle(7)
circ2 = Circle(11)

# создаем коллекцию объектов
# и добавим в нее наши два круга (Задание 1.9.1)
figures = [square2, circ1, rect1, circ2, square1, rect2]

# пройдемся циклом по этой коллекции
for figure in figures:
    if isinstance(figure, Square):
        print("Площадь квадрата: ", figure.get_sq_area())
    elif isinstance(figure, Circle):
        print("Площадь круга: ", figure.get_circle_area())
    else:
        print("Площадь прямоугольника", figure.get_area())

print("Равны ли по площади эти прямоугольники?")
print(rect1 == rect2)
