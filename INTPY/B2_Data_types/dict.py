# Задание 2.6.11
# Напишите программу, которая получает на вход
# название книги, фамилию автора и год выпуска.
# Полученные данные должны быть преобразованы в словарь
# и в таком представлении выведены в консоль.
title = input("Название книги: ")
author = input("Автор: ")
year = input("Год издания: ")
book = {'title' : title,
        'author' : author,
        'year' : year }
print(book)