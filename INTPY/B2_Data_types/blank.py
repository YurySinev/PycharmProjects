my_list = [1, 4, 6, 3, 7, 4, 4, 34, 67, 23, 75, 63, 46, 43, 32]
print(my_list)
print(my_list[len(my_list)-1])  # можно
print(my_list[-1])              # но так лучше

my_list.pop()
print(my_list)
my_list.append(123)
print(my_list, len(my_list))
print(my_list[-1:-4:-1])
print(list(map(float, my_list)))

# Напишите программу, которая на вход получает последовательность чисел,
# а выводит модифицированный список:
#
#         Первое и последнее числа последовательности должны поменяться местами.
#         В конец списка нужно добавить сумму всех чисел.

# string_ = input("Введите числа через пробел:")
# list_of_strings = string_.split()
# list_of_numbers = list(map(int, list_of_strings))
# print(list_of_numbers)
# a, b = list_of_numbers[0], list_of_numbers[-1]
# a = a - b
# b = a + b
# a = b - a
# list_of_numbers[0], list_of_numbers[-1] = a, b
# list_of_numbers.append(sum(list_of_numbers))
# print(list_of_numbers)

N = list(map(int, input("Введите числа через пробел: ").split()))
print(N)
N[0], N[-1] = N[-1], N[0]
N.append(sum(N))
print(N)


