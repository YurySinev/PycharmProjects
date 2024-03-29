from playground import field

def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_coord:
        symbols = []
        for j in i:
            symbols.append(field[j[0]][j[1]])
        if symbols == ["X", "X", "X"]:
            print("\t\t\tВыиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("\t\t\tВыиграл 0!!!")
            return True
    return False
