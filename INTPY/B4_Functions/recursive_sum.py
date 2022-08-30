# Задание 4.3.3

def recursum(n):
    if n == 1:
        return 1
    return n + recursum(n - 1)

print(recursum(44))
