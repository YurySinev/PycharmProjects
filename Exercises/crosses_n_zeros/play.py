from playground import field


def play():
    while True:
        coords = (input("Номер строки: "), input("Номер столбца: "))

        x, y = coords

        if not (x.isdigit()) or not (y.isdigit()):
            print("\tВведите числа! ")
            continue

        x, y = int(x) - 1, int(y) - 1  # коррекция введенных координат уже под компьютер

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("\tКоординаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("\tКлетка занята! ")
            continue

        return x, y
