def playground():
    print()
    print("    | 1 | 2 | 3 | ")  # исправил номера столбцов для "человекочитабельности"
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i + 1} | {' | '.join(row)} | "  # то же и для номеров столбцов
        print(row_str)
        print("  --------------- ")
    print()

field = [[" "] * 3 for i in range(3)]