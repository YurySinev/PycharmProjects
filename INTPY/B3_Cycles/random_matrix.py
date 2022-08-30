from divide_line import line
# мое решение:

random_matrix = [
    [9, 2, 1, 8, 4],
    [2, 5, 3, 3, 0],
    [4, 8, 5, 7, 1],
    [4, 6, 8, 9, 7],
    [2, 1, 5, 8, 3]
]

ROWS = 5
COLS = 5

for i in range(ROWS):
    max_elem = random_matrix[i][0]
    max_index = 0
    min_elem = random_matrix[i][0]
    min_index = 0
    for j in range(COLS):
        if random_matrix[i][j] > max_elem:
            max_elem = random_matrix[i][j]
            max_index = j
        if random_matrix[i][j] < min_elem:
            min_elem = random_matrix[i][j]
            min_index = j
    print(f"Строка {i}: макс: {max_elem} - индекс: {max_index}, мин: {min_elem} - индекс: {min_index}")

line()

# предложенное решение:

random_matrix = [
    [9, 2, 1, 8, 4],
    [2, 5, 3, 3, 0],
    [4, 8, 5, 7, 1],
    [4, 6, 8, 9, 7],
    [2, 1, 5, 8, 3]
]
# Создадим списки, где мы будем хранить ответ на наш вопрос:
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []

# напишем цикл, в котором пройдём по всем строкам матрицы:
for row in random_matrix:
    # Создадим две переменные:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    # Индексы можно перебрать так:
    for index_col in range(len(row)):
        # Теперь сравниваем элемент с индексом index_col и нашего кандидата в соответствии с алгоритмом:
        if row[index_col] < min_value:
            # Если он оказался меньше, то теперь кандидат — это сам текущий элемент:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)


