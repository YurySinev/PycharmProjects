# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# r = json.loads(r.content)
#
# print(r[0])

################################################################
# import telebot
#
# TOKEN = "5386412319:AAGoNUgj71uclssOgkm6dsBF3BSOlTJsus8" # @integromatYS_bot
#
# bot = telebot.TeleBot(TOKEN)
#
# bot.polling(none_stop=True)

#################################################################

# import requests
# import lxml.html
# from lxml import etree
#
# html = requests.get('https://www.python.org').content
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()')
#
# print(title)
#
#
# /html/body/div[1]/div[3]/div/section/div[2]/div[1]/div/h2
# /html/body/div[1]/div[3]/div/section/div[2]/div[1]/div/ul/li[1]

##############################################################################


# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.htm', lxml.html.HTMLParser())  # попытаемся спарсить наш файл
# # с помощью html-парсера. Сам html - это то, что мы скачали и поместили в папку из браузера.
#
# ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')
#
# # создаём цикл, в котором мы будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a')
#     print(a.text)  # из этого тега забираем текст, это и будет нашим названием

#####################################################################################

import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.htm',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера

ul = tree.findall(
    'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
    # time = li.find('time')
    # print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием
    print(a.text)