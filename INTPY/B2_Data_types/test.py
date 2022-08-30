a = 3.14
b = "3.14"
c = True
# примененик функции type() для выяснения типа данных переменной
print(type(a))
print(type(b))
print(type(c))

x = 0.1
y = 21.5
print(y / x)

print (0.1+0.1*5-0.3*4)

print ((3.14+0.3)/2+0.15)

a = -13
b = 7

# способ взаимной замены значений переменных:
a = a - b
b = a + b
a = b - a
print(a, b)

# работа со строками
s = "python"
print(s[0])
# p
print(s[1:4])
# yth

# логические выражения как возвращаемые значения:
print(3 > 10)
# False
print(3 < 10)
# True
print(3 == 10)
# False

# проверка есть ли какой-то символ в строке:
print('r' in 'world') # проверяем отдельный символ
# True

print('th' in 'python') # проверяем целую подстроку
# True

print('the' in 'python')
# False

# Истинно или ложно?
print(1.57*3/1.5==3.14)

# кортеж
date = (1, 'january', 2020)
print(date[0])
# 1
print(date[1])
# january
print(date[2])
# 2020
print(date)
