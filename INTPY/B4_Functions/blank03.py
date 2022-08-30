def decor(f):
    def wrapper():
        print("Обертка: ДО выполнения")
        result = f()
        print("Обертка: ПОСЛЕ выполнения")
        # return result
    return wrapper

def decor2(f):
    def wrapper():
        print("Запустим обертку другим способом...")
        result = f()
        print("Если успешно, то видим это сообщение")
    return wrapper

# @decor
@decor2
def my_func():
    print("ОСНОВНАЯ функция")

# print(my_func())

decor2(my_func())


