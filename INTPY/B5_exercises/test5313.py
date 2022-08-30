# Задание 5.3.13
# При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.

mult_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for i in mult_table:
    print(i)
