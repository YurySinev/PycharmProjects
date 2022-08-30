# упражнения со строками
# s = str(input())

s = "Hello my dear friends! I'm happy to see you again!"

print("Строка как есть: ", s)
# Отрицательный шаг позволяет развернуть строку:
print("Строка в обратную сторону: ", s[::-1])

# Встроенная функция len() позволяет узнать длину строки:
print("Длина строки: ", len(s))

# Метод find(substr), определённый для строк, позволяет находить символы и подстроки:
print(s.find('e')) # возвращает индекс

print(s.find('n!')) # в случае подстроки возвращает индекс первого символа

# Если символ или подстрока встречаются несколько раз, то возвращается индекс первого вхождения:
print(s.find('l')) # встречается в индексах 2 и 3

# Ряд функций позволяет определить, состоит ли строка из цифр, букв или одновременно из букв и цифр:
print("Строка из цифр?", s.isdigit()) # строка состоит из цифр?

print("Строка из букв?", s.isalpha()) # строка состоит из букв?

print("Строка состоит из цифр и букв?", s.isalnum()) # строка состоит из цифр и букв?

# Приведённые ниже методы позволяют привести все буквы к верхнему регистру
# (заглавным буквам) или к нижнему регистру (строчным буквам).
# Обратите внимание, что исходная строка не изменяется:

print("Верхний регистр:", s.upper())

print("Нижний регистр:", s.lower())

