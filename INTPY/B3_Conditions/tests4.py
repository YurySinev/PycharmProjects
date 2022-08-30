# Задание 3.2.2
# Дано n-значное целое число N. Определите, начинается ли оно с чётной цифры.
# мое решение:
N = input()
firstnum = int(N[0])%2
print(firstnum==0)

# предлагаемое решение:
N = 123
N_str = str(N) # преобразуем число в строку
first_digit = int(N_str[0]) # берём самый левый элемент строки и преобразуем его в число
print(first_digit % 2 == 0) # выводим True в случае, если цифра делится на 2, иначе False
# False

# Задание 3.2.3 Каков результат выполнения кода ниже?
# 1
list_1 = [1, 2]
list_2 = [1, 2, 3]
val = list_2.pop()
print(list_1 == list_2)

# 2
list_1 = [1, 2]
list_2 = [1, 2, 3]
val = list_2.pop()
print(id(list_1) == id(list_2))