# #
# # Декораторы
# #
# # Напоследок займёмся декорацией функций. Как вы наверняка помните, декораторы призваны
# # дополнять поведение функции без изменений в самой функции. Можно считать время, затраченное
# # на выполнение функции, или выводить служебную информацию о ней. Со временем мы познакомимся
# # с несколькими удобными использованиями декораторов, а сейчас рассмотрим только один, который
# # предвосхищает декоратор проверки авторизации пользователя из встроенных средств Django.
# #
# # Пусть у нас есть функция, которая должна извлекать из базы данных какую-то информацию.
# # На начальном этапе разработки мы не заботились о том, что это можно делать только при условии,
# # что пользователь программы авторизовался, но сейчас время пришло. Попробуем написать декоратор,
# # который позволяет вызвать функцию, только если она вызывается авторизованным пользователем.
#
# yesno = input("""Введите Y, если хотите авторизоваться, или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper
#
#
# @is_auth
# def from_db():
#     print("some data from database")
# from_db()
# #
# # Итак, разберём код по частям. Сначала мы спрашиваем у пользователя, хочет ли он авторизоваться.
# # При авторизации на сайтах вы, наверное, не раз встречали такую ситуацию, что браузер помнит
# # ваши логин и пароль и не нужно их вводить каждый раз. Представим, что именно это мы и сделали —
# # для авторизации достаточно ввести Y. После чего в переменную auth сохранили True, если пользователь авторизован.
# #
# # Следующий блок кода — сам декоратор, который в случае успешной авторизации выводит соответствующее
# # сообщение и выполняет функцию. Если же пользователь не авторизовался, то также получаем соответствующее
# # сообщение, но уже без вызова самой функции!
# #
# # Самая главная фишка декораторов в том, что такую обёртку можно использовать для многих функций.
# # Если в нашу программу хотим добавить ещё одну функцию, для которой мы бы хотели сначала проверить
# # авторизацию пользователя, достаточно всего лишь указать для неё декоратор.
#
# @is_auth
# def change_profile():
#     print("Profile has been changed")
# #
# # Задание 5.4.15
# # Реализуйте функцию-декоратор, которая проверяет доступ к функции по username пользователя.
# # Все username пользователей хранятся в глобальной области видимости в списке USERS.
# # При согласии пользователя на авторизацию ему предлагается ввести username, который также
# # хранится в глобальной области видимости. Функция должна использовать два декоратора:
# # один для проверки авторизации вообще (реализован выше), второй — для проверки доступа.
#
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться, или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# # Ответ:
#
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещён")
#     return wrapper
#

def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещён")
    return wrapper

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def change_profile():
    print("Profile has been changed")

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться, или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()

