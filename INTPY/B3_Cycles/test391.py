from divide_line import line

#  Задание 3.9.1
# Начинающий разработчик написал программу, которая находит индекс последнего
# отрицательного элемента в списке.
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i in range(len(list_)):
#     if list_[i] < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# Но он не знал, что есть функция enumerate. Ваша задача — подправить код так,
# чтобы он работал с помощью функции enumerate.


list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число: ", list_[i])
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", list_[i])
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

line()
# а вот так я решил это в новую единицу времени:

my_list = [-5, 2, 4, 8, 12, -7, 5, 2, 8, 5, 7, 9, -15, 7, 5]
last_negative = None
for i, value in enumerate(my_list):
    last_negative = i if value < 0 else last_negative
print(f"Индекс последнего отрицательного элемента: {last_negative}")

line()

print(type(enumerate(my_list)))
print(len(my_list))
