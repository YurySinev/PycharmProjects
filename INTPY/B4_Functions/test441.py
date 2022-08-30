# Задание 4.4.1 # Задание на самопроверку.
# Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
# По умолчанию она начинается с единицы, её шаг равен 1, но пользователь может указать любой шаг
# и любое число в качестве аргумента функции, с которого будет начинаться последовательность.

# def infinit_natural_numbers(a):
#
#     while True:
#         print(a)
#         a += 3
#         yield a
#
# print(infinit_natural_numbers(5))

#
def count(start, step):
    counter = start
    yield counter
    while True:
        yield counter
        counter += step
        if counter == 5:
            raise StopIteration

my_gen_func = count(100, 10)

for i in range(10):
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))
    print(next(my_gen_func))

# предложенное решение
def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step



