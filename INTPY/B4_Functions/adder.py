a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 0, 3, 7, 5]
print("Один список", a)
print("Другой список", b)
print("Два списка", a, b)
print("Значения обоих списков", *a, *b)
c = {*a, *b}
print(type(c))
print("Множество из двух списков", c)


def adder(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

print(adder(*a))
print(adder(*b))
print(adder(*c))
