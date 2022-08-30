# Задание 3.8.1 (на самопроверку)
# Напишите цикл, который ищет наибольший элемент в матрице.
# Пример матрицы:
test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]
max_value_rows = []
max_index_rows = []
for row in test_matrix:
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Maximal elements:", max_value_rows) # максимальные элементы
print("Their indices:", max_index_rows) # их индексы