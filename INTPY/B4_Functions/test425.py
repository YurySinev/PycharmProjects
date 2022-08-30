from divide_line import line

# Задание 4.2.5 Задание на самопроверку.
# Напишите функцию, которая будет возвращать количество делителей числа а.
# Пример ввода: 5 Пример вывода программы: 2

line('мое решение')

# мое решение:
def get_mult(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    #    return count
    print(f"У числа {a} {count} делителей")

get_mult(7)

line('предложенное решение - такое же')

# предложенное решение:
def get_multipliers(a):
    count = 0
    for n in range(1, a + 1):
        if a % n == 0:
            count += 1

    return count


print(get_multipliers(5))  # 2
print(get_multipliers(4))  # 3
