# Возможности языка позволяют выполнить определённые действия для каждого элемента списка.
# Такую операцию можно проделать с помощью функции map():
#
# map(function, list)
#
# Первый аргумент map() — функция, которую нужно применить к каждому элементу списка,
# а сам список — второй аргумент. Возвращаемое значение этой функции — объект map,
# который можно преобразовать, например, обратно в список. Пример:

# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6]

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]


# Область применения функции очень большая, но мы остановимся на одном её применении
# — ввод данных. Вспомним, что даже при вводе чисел во время выполнения функции input(),
# они все равно остаются в строковом представлении. Если ввести сразу несколько чисел
# через пробел, то тем более они останутся в таком виде.
#
# Однако, пользуясь функциями split() и map(), можно выполнить нужное преобразование:

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(float, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка (с шагом 3)

