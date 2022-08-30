# Задание 4.3.5
#
# Дано натуральное число N. Вычислите сумму его цифр.
#
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).

# мое решение:
number = 247

def int_sum(N):
    sum_ = 0
    if N == 0:
        return sum_
    else:
        sum_ += N % 10
        return sum_ + int_sum(N // 10)

print(int_sum(number))

# предложенное решение:
def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

sum_digit(123)  # 6
print(sum_digit(258))