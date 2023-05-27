class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Координаты точки: {self.x}, {self.y}"


d1 = Dot(22, 25)
d2 = Dot(15, 34)

print(d1 == d2)
print(str(d2))
print(d1)
var = str(d1)
print(var)