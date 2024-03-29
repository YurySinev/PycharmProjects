#
# C2.4. Исключения
#
# Предположим, мы написали программу. Она вроде даже запустилась и вроде даже что-то сделала.
# Но в один прекрасный момент всё вылетело, а в терминале вылезло непонятное сообщение по типу:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: "odin"

# Эта ошибка относится к типу исключительных ситуаций. Исключительные ситуации порой
# возникают тогда, когда вы большой молодец, написали код правильно. Допустим, он
# запустился и отработал своё. Завтра вы решили запустить код повторно, и что же вы
# видите? Ошибка! Но как? В прошлый раз всё ведь запускалось без ошибок. Почему? Да
# дело в том, что исключения могут возникнуть не только из-за ошибок в написании кода,
# а ещё и от взаимодействия пользователя с вашей программой, от состояния системы, на
# которой она запущена, погоды или расположения луны в Юпитере, да от чего угодно, но
# только не от вашего кода. Да-да, сегодня вы узнаете, как работать с исключительными
# ситуациями или же исключениями в языке Python.
#
# Исключения — это такие ошибки, которые возникают не во время компиляции программы,
# а в процессе её исполнения, в случаях, если что-то идёт не так.
#
# После возникновения исключения программа попытается экстренно завершить работу или
# перейти к обработчику исключения, если такой есть. Поскольку Python — интерпретируемый
# язык, то, по сути, исключения и вставляют нам чаще всего палки в колёса,
# прерывая выполнение программы.
#
# Ошибки бывают двух видов:
#
#         отлавливаемые — все, что наследуются от класса Exception
#               (более подробно изучим в следующем модуле);
#         не отлавливаемые — SystemExit, KeyboardInterrupt и т. д.
#
# На самом деле заучивать их все не стоит, только зря потратите время, потому как на
# самом деле этих ошибок может быть множество, например, в отдельной библиотеке есть
# собственные исключения (писать собственные исключения мы научимся на следующем занятии).
#
# Давайте же посмотрим на пример кода, который вызывает исключение.
#
# Название исключения | Когда возникает | Название в Python
# Исключение, возникающее при делении на 0 | При делении на ноль. | ZeroDivisionError
# Ошибка значения | При невозможности привести один тип к другому. | ValueError
# Файл не найден`| Если попытаться открыть файл для чтения, который не был создан. | FileNotFoundError
# Недостаточно прав | Если попытаться открыть файл из корневых каталогов при запуске программы
# не от имени администратора. | PermissionError
#
# Это лишь несколько из них. Список всех исключений доступен в документации, можете ознакомиться с ним, чтобы быть в курсе какие ошибки могут возникнуть в простых программах.
#
# print("Перед исключением")
# c = 1 / 0  # Здесь что-то не так….
# print("После исключения")
#
# В консоли мы увидим следующий результат:
#
# Перед исключением
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
#
# Строка «После исключения» не будет выведена на экран, потому что, как только
# интерпретатор дойдёт до строчки I = 1 / 0, он экстренно завершит работу и
# выведет нам сообщение об ошибке деления на ноль.
#
# В этом примере мы чётко видим, что может возникнуть ошибка. Но в большинстве
# случаев это бывает не столь очевидно. Поэтому давайте слегка поменяем наш код:

# print("Перед исключением")
# # теперь пользователь сам вводит числа для деления
# a = int(input("a: "))
# b = int(input("b: "))
# c = a / b  # здесь может возникнуть исключение деления на ноль
# print(c)  # печатаем c = a / b если всё хорошо
# print("После исключения")

# После выполнения этого кода у пользователя может возникнуть такая же ошибка,
# если он введёт b = 0.
#
# Так как же сделать так, чтобы программа не вылетала при ошибке и продолжала
# свою работу? Это всё делается очень просто. Для этого и нужна конструкция try-except.
#
# Давайте посмотрим на следующий код:

try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Перед исключением")
    # теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b  # здесь может возникнуть исключение деления на ноль
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)  # Выводим информацию об ошибке
    print("После исключения")

print("После После исключения")

# В данном случае тоже может возникнуть ошибка деления на ноль, если пользователь
# введёт b = 0. Поэтому мы отлавливаем ошибку ZeroDivisionError. В блоке try
# помещается «опасный» кусок кода, который может вызывать исключения, а в блоке
# except указывается класс ошибки, которую мы хотим отловить, а затем помещается
# код, который нужно выполнить в случае возникновении ошибки. В данном случае
# после возникновении ошибки код в блоке try прервётся, перейдёт в блок except,
# а затем продолжит выполняться дальше, т.е. программа не вылетает, как это было
# без обработчика исключений. В этом и есть суть конструкции try-except.
#
#
# Ну конечно же, это ещё не всё. Есть также блоки finally и else. Если вы хорошо
# помните тему «Циклы», то там тоже было ключевое слово else. Код в блоке else
# выполнялся после завершения цикла. С try-except есть нечто похожее.
# Посмотрите на пример кода ниже.
#
# Можно так:

# try:
#     *ваш код*
# except Ошибка:
#     *Код отлова*
# else:
#     *Код, который выполнится если всё хорошо прошло в блоке try*
# finally:
#     *Код, который выполнится по любому*
#
# ВАЖНО!  Обратите внимание на отступы! Код внутри конструкции сдвинут на второй уровень вложенности.
#
# Рассмотрим применение этих блоков на примере:
try:
    print("Перед исключением")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:
    print("После исключения")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения)
    print("Всё ништяк")
finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Finally на месте")

print("После После исключения")

# Здесь результат работы программы будет зависеть от ввода пользователя. Если
# пользователь введёт всё правильно, то он должен увидеть следующее:
#
# Перед исключением
# *результат деления a/b*
# Всё ништяк
# Finally на месте
# После После исключения
#
# Если же ошибка возникнет, то пользователь увидит следующее:
#
# Перед исключением
# После исключения
# Finally на месте
# После После исключения
#
# Т.е. код в блоке else не выполнится, т.к. было исключение, а код в блоке
# finally выполняется в обоих случаях.
#
# Ну и конечно же, мы можем вызывать ошибки самостоятельно, с помощью конструкции raise.
# Используется это, как правило, для отладки кода и остановки программы в критических ситуациях.
#
# Например:
age = int(input("Сколько тебе лет?"))

if age > 100 or age <= 0:
    raise ValueError("Тебе не может быть столько лет")

print(f"Тебе {age} лет!")  # Возраст выводится только если пользователь ввёл правильный возраст.

# Здесь ошибка ValueError возникнет, если пользователь ввёл неправильный возраст,
# и остановит работу программы выдав в консоль:
# raise ValueError("Тебе не может быть столько лет")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: Тебе не может быть столько лет
#
# Сообщение в консоль выводится именно то, которое вы передадите в аргумент конструктора
# класса вашего исключения. Если не хотите никаких сообщений, то просто оставьте скобки
# пустыми. Ну и конечно же стоит отметить, что отлавливать вызываемые
# с помощью raise ошибки тоже можно.
#
# Например:

try:
    age = int(input("Сколько тебе лет?"))

    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")

    # Возраст выводится только если пользователь ввёл правильный возраст.
    print(f"Тебе {age} лет!")
except ValueError:
    print("Неправильный возраст")

#
#
# Давайте кратко подведём итоги:
#
#         Исключения — это ошибки, которые выбрасываются при неправильной работе
#             программы и останавливают её выполнение, если они не обработаны.
#         Конструкция try-except выглядит следующим образом и служит для обработки исключений:

        # try:
        #     *код, который может вызвать ту или иную ошибку*
        # except *ошибка*:
        #     *код, который выполнится в случае возникновения ошибки*
        # else:
        #     *код, который выполнится только в случае, если в try ничего не сломалось*
        # finally:
        #     *код, который выполнится по-любому*

        # Блоки finally и else, являются необязательными, но могут быть использованы
    # для вашего удобства. Код из блока finally выполняется в любом случае, независимо
    # от исхода в блоках try-except. Код из блока else выполняется только в случае
    # успешного выполнения кода в try.
    #     Выбрасывать ошибки можно и по своему желанию с помощью конструкции
#     raise *Тип ошибки* (сообщение, которое нужно вывести в консоль).

#  Задание 2.4.1
# Просмотрите основные виды встроенных исключений в документации. Найдите
# исключение, которое возникает при проблемах с оперативной памятью.
# MemoryError

# Задание 2.4.2
# Исключения – это...
# Ошибки, возникающие в результате работы программы и всегда приводящие к её завершению.
# Ошибки, возникающие в результате выполнения программы и завершающие её работу, если не предусмотрен их отлов.
#     верно
# Особая сущность в языке Python, которая останавливает работу программы в любом месте.
#

#  Задание 2.4.3
# Для отлова исключений используется конструкция...
# try-except

#  Задание 2.4.4
# В блоке try помещается...
# Безопасный код, который не вызывает исключений.
# Код, который обязательно вызывает хотя бы одно исключение.
# Любой код, который может либо вызвать, либо не вызвать исключение. # верно

#  Задание 2.4.5
# В блоке except должен находиться...
# Безопасный код.
# Код, который вызывает исключения.
# Любой код, который выполнится после возникновения той или иной ошибки. # верно
# Код, который выполнится после блока try.

# Задание 2.4.6
# Сопоставьте ответ с блоком.
# Выполняется в любом случае после выхода из try-except # finaly
# Выполняется только при удачном завершении кода в блоке try, # else
#

#  Задание 2.4.7
# Конструкция raise *имя ошибки* используется для...
# Вызова этой ошибки, которую можно в дальнейшем отловить. # верно
# Вызова этой ошибки и прекращения работы программы.
# Отлова ошибки.

# Задание 2.4.8
# Создать скрипт, который будет в input() принимать строки, и их необходимо
# будет конвертировать в числа, добавить try-except на то, чтобы строки
# могли быть сконвертированы в числа.
# В случае удачного выполнения скрипта написать: «Вы ввели правильное число».
# В конце скрипта обязательно написать: «Выход из программы».
# Примечание: для отлова ошибок используйте try-except, а также блоки finally и else.
#
# Примеры входов и выходов:
# Входные данные: 	                    Выходные данные:
# 1                 Вы ввели 1                      Выход из программы
# -3                Вы ввели -3                     Выход из программы
# razdvatri         Вы ввели неправильное число     Выход из программы

