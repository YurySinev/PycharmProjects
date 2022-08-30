from pushkin import pushkin


def char_frequency(text):
    text = text.lower()  # привели все к нижнему регистру
    text = text.replace(" ", "")  # убрали пробелы
    text = text.replace("\n", "")  # убрали символы перевода строки

    count = {}  # для подсчета символов и их количества
    for letter in text:
        if letter in count:  # если символ уже встречался, то увеличиваем его количество на 1
            count[letter] += 1
        else:
            count[letter] = 1

    # После подсчёта применим цикл for для работы со словарем. У словаря есть метод items, который
    # возвращает кортежи состоящие из пар ключ-значение. Зная их, можно вывести статистику по тексту.
    for char, cnt in count.items():
        print(f"Символ {char} встречается {cnt} раз")


# char_frequency(pushkin)
