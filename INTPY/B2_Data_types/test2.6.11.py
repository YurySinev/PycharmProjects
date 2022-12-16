# Напишите программу, которая получает на вход название книги - title,
# фамилию автора - author и год выпуска - year.

# Полученные данные должны быть преобразованы в словарь book с ключами:
# title, author, year. Причем year нужно преобраовать в тип int.

title = input("Введите название книги:\t")
author = input("Фамилия автора:\t")
year = int(input("Введите год выпуска:\t"))

book = {'title' : title,
        'author' : author,
        'year' : year }

print(book)