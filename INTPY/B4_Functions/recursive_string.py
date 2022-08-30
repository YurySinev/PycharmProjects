# Задание 4.3.4 см. test434

def recurs_str(string_):
    if len(string_) == 0:
        return ''
    else:
        return string_[-1] + recurs_str(string_[:-1])

print("Введите текст: ")
print(recurs_str(input()))
# str_ = input()
# print(str_[:-5])
