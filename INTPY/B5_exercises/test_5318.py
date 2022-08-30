# Задание 5.3.18
# Реализуйте программу, которая сжимает последовательность символов.
# На вход подаётся последовательность вида:
#
# aaabbccccdaa
#
# Необходимо вывести строку, где каждая последовательность из одинаковых символов,
# идущих подряд, заменяется на один символ, и длину этой последовательности
# (включая последовательности единичной длины). Вывод должен выглядеть так:
#
# a3b2c4d1a2

# Опять я помучился и подглядел решение... см. ниже

# txt = input()
# new_txt = []
# counter = 0
# for i in txt:
#     if new_txt[::-1] == None:
#         new_txt.append(i)
#         counter = 1
#     if new_txt[::-1] == i:
#         counter += 1
#     if new_txt[::-1] != i:
#         new_txt.append(counter)
#         new_txt.append(i)
#         counter = 1
#
# print(new_txt)

txt = input()   # вводим текст
last = txt[0]   # сохраняем в переменную самый первый символ, он же пока и крайний
counter = 0     # заводим счетчик
result = ''     # создаем результирующую строку

for i in txt:
    if i == last:   # если символ такой же как и предыдущий,
        counter += 1    # то просто увеличиваем счетчик
    else:   # если же он отличается от предыдущего, то
        result += last + str(counter)   # записываем/дописываем в результат предыдущий символ и его счетчик
        last = i    # заменяем крайний символ на новый
        counter = 1 # сбрасываем старый счетчик

result += last + str(counter)   # дописываем в результат заключительный символ с его счетчиком
print(result)
