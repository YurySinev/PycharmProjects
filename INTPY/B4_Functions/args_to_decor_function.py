def u_line():
    print("-" * 20," следующий пример","-" * 20)

# декоратор, в котором встроенная функция умеет принимать аргументы
def do_it_twice(func):
   def wrapper(*args, **kwargs):
       func(*args, **kwargs)
       func(*args, **kwargs)
   return wrapper

@do_it_twice
def say_word(word):
   print(word)

say_word("Да ну нах!!!")
# Oo!!!
# Oo!!!
u_line()
# Подведём итог по декораторам:
#
#         1. Декораторы добавляют дополнительное поведение функции без изменения её исходного кода.
#         2. Декораторы —  вызовы дополнительных функций, поэтому они немного замедляют ваш код.
#         3. Для передачи аргументов декорируемой функции используйте *args и **kwargs.
#
print( """
# Вот универсальный шаблон для декоратора:
def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper
""")
u_line()
# Задание 4.5.2 Задание на самопроверку.
# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.
# предложенное решение:

def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)
       count += 1
       print(f"Функция {func} была вызвана {count} раз")
   return wrapper

@counter
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз
