# Задание 4.3.2 Задание на самопроверку.
# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

# мое решение:
def mult_all(*nums):
    sum_ = 1
    for i in nums:
        sum_ *= i
    return sum_

print(mult_all(2, 3, 5))

# предлагаемое решение - такое же:
def mul(*nums):
    p = 1
    for n in nums:
        p *= n

    return p