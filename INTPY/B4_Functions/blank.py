from divide_line import line
import divide_line
from pushkin import pushkin
from word_frequency import word_frequency
from char_frequency import char_frequency

print(pushkin)

line('частота слов:')

word_frequency(pushkin)

line('символы:')

char_frequency(pushkin)

line('пробы пера с семинара')


def add_to_list(list_=None, elem=0):
    if list_ is None:
        list_ = []
    list_.append(elem)
    return list_


print(add_to_list())
print(add_to_list())

line('семинар: вопрос про видимость глобальных переменных из импортированных модулей')
line('проверим...')

print(divide_line.abc)

line('получилось! Хотя я же с Пушкиным уже это проделал')
# line('способ повторять запрос к пользователю с рекурсией (так себе)')
# def ask_int():
#     t = input('Введите число: ')
#     if t.isdigit():
#         return t
#     else:
#         return ask_int()
# ask_int()
line('хороший способ повторять запрос к пользователю: ')


def ask_int():
    t = input('Введите число: ')
    while not t.isdigit():
        t = input('Это было не число. Введите число: ')

    return print(f'Вы ввели число {t}')

ask_int()