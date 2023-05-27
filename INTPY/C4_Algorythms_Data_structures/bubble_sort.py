array = [2, 3, 1, 4, 6, 5, 9, 8, 4, 5, 6, 7, 8, 9, 2, 9, 5, 7, 6, 8, 4, 6, 5, 77]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
