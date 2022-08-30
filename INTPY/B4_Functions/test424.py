from divide_line import line

# Задание 4.2.4 # Задание на самопроверку.
# Напишите функцию, которая печатает «обратную лесенку» следующего типа:
# n = 3
# ***
# **
# *
#
# n = 4
# ****
# ***
# **
# *
line('мое решение (с while): ')


# мое решение:
def back_scale(n):
    while n != 0:
        print("*" * n)
        n -= 1


back_scale(5)

line('предложенное решение (c for in range): ')


# предложенное решение:
def reverse_stair(n):
    for i in range(n, 0, -1):
        print("*" * i)


reverse_stair(5)
