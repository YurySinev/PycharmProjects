def word_frequency(text):
    text = text.lower()  # все слова - в нижний регистр
    symbols = ['.', ',', ';', ':', '!', '?', '...', '--', ' ']  # список знаков препинания
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

