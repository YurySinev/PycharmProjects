import time
# Декораторы предназначены для подключения любого дополнительного поведения к основной функции,
# называемой декорируемой функцией, которое может выполняться до, после или даже вместо основной
# функции. При этом исходный код декорируемой функции никак не затрагивается.
#
# В качестве дополнительного поведения может выступать подсчёт времени выполнения функции,
# проверка дополнительных условий, разрешающих выполнение указанной функции.

# Давайте посмотрим на примере, как добавить дополнительное поведение к основной функции.

def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обёртку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, который будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper


# Наш декоратор будет печатать строку «Я буду выполнен до основного вызова!» перед основным
# вызовом, а строка «Я буду выполнен после основного вызова!» соответственно после основного
# вызова. Если необходимо, то не забываем вернуть результат исходной функции.

def my_function():
    print("Я - оборачиваемая функция!")
    return ''


print(my_function())
# Я - оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я - оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0

# Видим, что задекорировав my_function, мы добавили к ней новый функционал,
# не меняя исходный код самой функции.
#
# Зачем это нужно? Например, декораторы могут замерять время выполнения функции
# либо количество запусков конкретной функции, также можно сохранять результаты
# вычисления (кеширование).
#
# Давайте попробуем замерить время выполнения системной функции для возведения числа
# в степень 2 и соответствующего оператора.

# import time перенесем в начало скрипта

def decorator_time(fn):
    def wrapper():
        print(f"Запустилась функция {fn}")
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы

    return wrapper


def pow_2():
    return 87654321 ** 2


def in_build_pow():
    return pow(87654321, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458

# Чтобы замерить время, будем использовать модуль time, в котором есть функция time(),
# возвращающая текущее время. Зная время до начала выполнения и сразу после, можно
# вычислить время работы функции.
#
# Видим, что наша функция работает быстрее, но один раз это не показатель. Нужно
# выполнить серию запусков и найти среднее время, тогда можно делать какие-то выводы.
