# Задача
#
# Вам нужно сделать кнопку возврата назад для браузера.
# Вы используете стек для хранения ссылок на веб-сайты,
# которые вы посетили. Каждая новая посещенная ссылка
# добавляется в стек.
# Кнопка возврата назад должна удалять верхнюю ссылку
# из стека и переходить по ней.
#
# Данный код объявляет класс Browser в качестве стека и
# реализует некоторые его методы. Дальше в стек добавляется
# несколько ссылок.
# Цикл while используется для возврата назад ко всем ссылкам
# и выводит их.
#
# Реализуйте требуемый метод pop() для Browser, чтобы
# данный код работал, как требуется.

class Browser:
    def __init__(self):
        self.links = []

    def is_empty(self):
        return self.links == []

    def push(self, link):
        self.links.insert(0, link)

    # ваш код
    def pop(self):
        return self.links.pop(0)

x = Browser()
x.push('about:blank')
x.push('www.sololearn.com')
x.push('www.sololearn.com/courses/')
x.push('www.sololearn.com/courses/python/')

while not x.is_empty():
    print(x.pop())
