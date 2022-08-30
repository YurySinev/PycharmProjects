# из вебинара
def rounder(func):
    def wrap(*args):
        # result = func(*args)
        # return round(result, 2)
        return round(func(*args), 2)
    return wrap


@rounder
def area(height, width):
    return height * width


@rounder
def hypot(a, b):
    return (a ** 2 + b ** 2) ** 0.5


print(area(1.234, 1.72))
print(hypot(10, 3))
