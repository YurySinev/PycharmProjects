# Деление с остатком отрицательных чисел
a = -5
b = 2
q = a // b # хочется получить 2, как и в прошлый раз, но q = -3
r = a % b # а остаток остался тот же r = 1
print(q, r)

print ((31%2) + (-31 % 2))

print (13%-3*3-3**2)

# приведение типов
print(1.00+0.01-3.01) # ожидается -2.0
# -1.9999999999999998

print(int(1.00+0.01-3.01))
# -1

# функция round()
print(round(1.00+0.01-3.01))
# -2

# задание
print(round(11 * 2.5 / 3, 2))

# задание 2.4.4
# Напишите программу, которая вычислит половину квадрата числа Пи (pi=3.14159),
# округлив до целого. Впишите результат вычислений:

print(round(3.14159**2/2))
