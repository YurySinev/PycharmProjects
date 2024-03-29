# Генераторы и итераторы

# В прошлом модуле мы разобрали сложный, но очень полезный механизм создания
# бесконечных последовательностей — функции-генераторы.
#
# Задание 5.4.12
# Каким ключевым словом нужно заменить return, чтобы функция стала генератором?

# yield

# Теперь попробуем написать генератор для приближённого вычисления числа e = 2.718.
# Для нахождения числа, удовлетворяющего необходимой точности,
# будем использовать следующий цикл:

# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение

# Для вычисления числа e с определённой точностью можно использовать формулу:
#
# e_n = (1 + 1/n)**n
#
# В этой формуле число n — натуральное (1, 2, 3 и т. д.).
#
# Задание 5.4.13
# Реализуйте функцию-генератор, каждое значение которого — приближение числа e с некоторым числом n.

def e():
    n = 1

    while True:
        yield (1 + 1 / n) ** n
        n += 1

last = 0

for a in e():  # e() - генератор
    if (a - last) < 0.00000001:  # ограничение на точность
        print(a)
        break  # после достижения которого завершаем цикл
    else:
        last = a  # иначе - присваиваем новое значение

# И в качестве актуализации темы итераторов давайте вспомним, какого вида исключение
# появляется при попытке выйти за пределы итерируемого объекта. Чтобы вспомнить,
# можно запустить следующий код:

iter_obj = iter("Hello!")

print(next(iter_obj)) # на седьмом повторении строки ошибка StopIteration

# И повторить последнюю строку столько раз, сколько необходимо для получения нужного эффекта.

# см. дальше test5415.py
