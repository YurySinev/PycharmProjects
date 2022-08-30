# Задание на самопроверку
# При помощи цикла for можно подсчитывать не только буквы но и слова. Для этого нужно
# использовать метод split() строки, которой разделяет строку на слова по пробельным
# символам. Напишите программу которая берет text из предыдущего примера и
# подсчитывает количество слов в нём.


text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

text = text.lower()  # все слова - в нижний регистр
symbols = ['.', ',', ';', ':', '!', '...', '--', '  ']  # список знаков препинания
for s in symbols:  # убираем из текста все знаки препинания
    text = text.replace(s, '')

count = {}  # заводим словарь-счетчик
word_list = list(text.split())  # разбиваем текст на список
for wrd in word_list:  # добавляем слова в словарь и ведем их счет
    if wrd in count:
        count[wrd] += 1
    else:
        count[wrd] = 1

for w, c in count.items():  # выводим окончательную информацию
    print(f'Слово "{w}" встречается {c} раз')
