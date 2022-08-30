# Задание 4.2.6 Задание на самопроверку.
# Напишите функцию, которая проверяет,
# является ли данная строка палиндромом или нет,
# и возвращает результат проверки. Пример:
# сheck_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True

# мое решение:
def check_palindr(s):
    s = s.lower()
    for i in [" ", "\n", "-", ",", ".", "!", "?", ":", ";", "=", "+", "/"]:
        s = s.replace(i, "")
    if s[0:len(s)] == s[::-1]: # мой вот этот срез [0:len(s)] НЕ НУЖЕН
        return True
    else:
        return False

str1 = "test"
str2 = "Кит на море не романтик"
str3 = "abcdefedcba"

print(check_palindr(str2))

# предложенное решение:
def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True