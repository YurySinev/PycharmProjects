# Задание 4.3.5 сумма цифр числа

N = 1365829342785


def recurs_num_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + recurs_num_sum(n // 10)


print(recurs_num_sum(N))
