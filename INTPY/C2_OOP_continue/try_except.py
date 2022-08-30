try:
    print("Перед исключением")
    a = int(input())
    b = int(input())
    c = a / b
    print(c)
except ZeroDivisionError as e:
    # print("На ноль делить низзя!")
    # print(e)
    print("После исключения")
else:
    print("Всё ништяк!")
finally:
    print("Finally на месте!")

print("После всех исключений или не исключений")


