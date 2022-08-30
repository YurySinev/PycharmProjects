# Задание 4.5.2
# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.

def count_func_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        print(f"Вызовов функции {func }: {count}")
        # return result
    return wrapper

@count_func_calls
def my_func(word):
    print(word)

while True:
    wrd = input("Введи слово или фразу: ")
    if wrd == "stop":
        break
    else:
        my_func(wrd)


