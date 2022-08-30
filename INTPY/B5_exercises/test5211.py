#  Задание 5.2.11
#
# Найдите ошибку в коде и запишите исправленную строку полностью в форму ответа.
# Представленная ниже программа должна находить множество символов, которые
# встречаются в двух строках одновременно.
#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.union(b_set)
#
# print(a_and_b)
#

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)
new_list = list(a_and_b)
print("Пересечение:", sorted(a_and_b))

# a_and_b = a_set.union(b_set)
# print("Объединение:", a_and_b)
#
# a_and_b = a_set.difference(b_set)
# print("Разность:", a_and_b)
#
# a_and_b = a_set.symmetric_difference(b_set)
# print("Симметричная разность:", a_and_b)



