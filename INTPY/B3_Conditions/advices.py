A = 46
if A % 2 == 0 or A % 3 == 0:
    print('Число А кратно 2 или 3')

# Для последовательностей (строк, списков, кортежей)
# используйте тот факт, что пустая последовательность есть False.

# Хорошо
if not seq:
if seq:

# Плохо
if len(seq)
if not len(seq)

# Примеры

if pozitive_num:  # нет смысла проверять len(pozitive_num)
   # если список не пустой печатаем его
   print("Список положительных чисел равен: ", pozitive_num)
else:
   # печатаем, если список оказался пустым
   print("Список положительных чисел пустой")

if not password:  # password строка содержащая пароль, введенный пользователем
   print("Вы забыли ввести пароль! Повторите попытку ещё раз")

# Не сравнивайте логические типы с True и False с помощью ==, иначе получается «масло масляное».
# Хорошо
if greeting:

# Плохо
if greeting == True:

# Совсем неправильно
if greeting is True: