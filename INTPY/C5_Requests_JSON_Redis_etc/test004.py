import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree
html = requests.get('https://www.python.org/').content
# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.htm', lxml.html.HTMLParser())  # попытаемся спарсить наш файл
# с помощью html-парсера. Сам html - это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')
    print(a.text)  # из этого тега забираем текст, это и будет нашим названием