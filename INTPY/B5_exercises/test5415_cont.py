#
# Задание 5.4.15
#
# Реализуйте функцию-декоратор, которая проверяет доступ к функции по username пользователя.
# Все username пользователей хранятся в глобальной области видимости в списке USERS.
# При согласии пользователя на авторизацию ему предлагается ввести username,
# который также хранится в глобальной области видимости. Функция должна использовать
# два декоратора: один для проверки авторизации вообще (реализован выше), второй — для проверки доступа.

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""\tВведите Y, если хотите авторизоваться, или N,
\tесли хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y" or 'y'

if auth:
    username = input("Введите ваш username: ")


def is_auth(func):
    def wrapper(*args, **kwargs):
        if auth:
            return func
        else:
            print("Пользователь не авторизован. В доступе отказано.")

    return wrapper


def has_access(func):
    def wrapper(*args, **kwargs):
        if username in USERS:
            print("Авторизован как ", username)
            func()
        else:
            print("Доступ пользователю ", username, " запрещен")

    return wrapper


# @is_auth
@has_access
def from_db():
    print("some data from database")


from_db()


# (см. дальше test551_map.py)