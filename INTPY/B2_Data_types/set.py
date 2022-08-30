# S = list(set(input()))
# S.sort()

Zen = "The Zen of PythonBeautiful is better than ugly." \
      "Explicit is better than implicit.Simple is better than complex." \
      "Complex is better than complicated.Flat is better than nested." \
      "Sparse is better than dense." \
      "Readability counts." \
      "Special cases aren't special enough to break the rules." \
      "Although practicality beats purity." \
      "Errors should never pass silently." \
      "Unless explicitly silenced." \
      "In the face of ambiguity, refuse the temptation to guess." \
      "There should be one-- and preferably only one --obvious way to do it." \
      "Although that way may not be obvious at first unless you're Dutch." \
      "Now is better than never." \
      "Although never is often better than *right* now." \
      "If the implementation is hard to explain, it's a bad idea." \
      "If the implementation is easy to explain, it may be a good idea." \
      "Namespaces are one honking great idea -- let's do more of those!"
symbols = list(set(Zen))
print(symbols)
print("Количество уникальных символов: ", len(symbols))

# Задание 2.6.14 Найти ошибку в коде и исправить
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

# a_and_b = a_set.union(b_set) правильно так:
a_and_b = a_set.intersection(b_set)
print(a_and_b)