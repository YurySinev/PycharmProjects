from divide_line import line
# Задание 3.8.2
# Напишите код, который определяет, является ли матрица квадратной
# (то есть количество строк равно количеству столбцов). В конце программа должна
# выводить на экран значение True или False в зависимости от заданной матрицы.

matrix = [
    [9, 2, 1, 8, 4],
    [2, 5, 3, 3, 0],
    [4, 8, 5, 7, 1],
    [4, 6, 8, 9, 7],
    [2, 1, 5, 8, 3]
]
row_lenth = 0
col_lenth = 0

for row in matrix:
    row_lenth += 1
for row in matrix:
    for col in row:
        col_lenth += 1
print(row_lenth == col_lenth / row_lenth)
# col_lenth /= row_lenth
print(f"Рядов: {row_lenth}, столбцов: {col_lenth}")

line()

rows = len(matrix)
cols = len(matrix[0])
print(rows, cols)






