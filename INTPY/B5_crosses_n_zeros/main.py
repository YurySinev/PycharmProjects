from greeting import greeting
from playground import playground
from playground import field
from play import play
from check_win import check_win

greeting()

count = 0
while True:
    count += 1
    playground()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = play()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break
