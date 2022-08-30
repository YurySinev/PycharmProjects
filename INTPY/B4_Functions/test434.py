# Задание 4.3.4
#
# С помощью рекурсивной функции разверните строку.

# мое решение... Спасовал, запутался...
# def back_string(s):
#     str_ = ""
#     L = []
#     def back():
#         if s[0]:
#             return L
#         L.append(s[])
#     if s[] ==
#
#     str_.join(L)
#
# print(back_string("Hello"))

# предложенное решение:
def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])

reverse_str('test')  # tset
print(reverse_str("Ты пока не до конца разобрался с рекурсивными функциями"))