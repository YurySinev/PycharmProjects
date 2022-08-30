# При работе со строками часто возникает необходимость разделить строку на несколько подстрок.
# Python и здесь предлагает удобный способ для реализации такой идеи — метод split():
colors = 'red blue green'
print(colors.split())
# # ['red', 'blue', 'green'] результат: список

# другой пример, с указанным разделителем
path = '/home/user/documents/file.txt'
print(path.split('/')) # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']

# объединение элементов списка в новую строку
colors_split = colors.split() # список цветов по отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue