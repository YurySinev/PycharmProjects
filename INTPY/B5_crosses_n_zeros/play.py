from playground import field

def play():
    while True:
        cords = input("         Ваш ход: ").split()
        # почему не сделать сразу так?
        # cords = int(input("Ваш ход: ").split()
        # потому-что тогда при вводе не-чисел программа просто сбойно завершится!
        # А нам надо, чтобы она продолжала работать. Вот почему не стоит сразу приводить к типу int.

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x) - 1, int(y) - 1   # коррекция введенных координат уже под компьютер

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
