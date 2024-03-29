# снова про неизменяемость

s1 = "foo"
s2 = "bar"

# Допишем вторую строку к первой:

s1 = s1+s2
print(s1)
# foobar

# Может показаться, что мы к существующей переменной s1 «приклеили» справа вторую
# переменную — модифицировали её. Это так и не так одновременно. Давайте посмотрим
# на эти строки немного глубже. Для этого воспользуемся встроенной функцией id(),
# которая возвращает уникальный идентификатор любого объекта.

s1 = "foo"
print(id(s1), s1) #проверяем идентификатор
# 139953609727144, foo

s2 = "bar"
print(id(s2), s2) #проверяем идентификатор
# 139953609727088, bar

s1 = s1+s2
print(id(s1), s1) #проверяем идентификатор
# 139953459591296, foobar