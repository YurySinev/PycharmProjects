import os

f= open('test.txt', 'a', encoding='utf8')

# Запишем в файл строку
# f.write("This is a test string\n")
# f.write("This is a new string\n")
#
# f.write("Это текстовая строка\n")
# f.write("А это еще одна текстовая строка\n")
f.write("\nИ вот еще дополнительная текстовая строка\n")
f.write("Пожалуй, закроем теперь этот файл\n")
f.write("=================================")
f.close()


