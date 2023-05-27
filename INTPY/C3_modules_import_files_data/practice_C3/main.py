from module import circle_area, rectangle_area

circle = circle_area(int(input("Введите радиус круга... ")))
rectangle = rectangle_area(int(input("Введите ширину и высоту прямоугольника... ")), int(input()))

if circle > rectangle:
    print(f"Площадь круга больше: {circle} > {rectangle}")
else:
    print(f"Площадь прямоугольника больше: {rectangle} > {circle}")
