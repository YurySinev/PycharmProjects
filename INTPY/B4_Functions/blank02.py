# проверка объекта на итерируемость с помощью функции iter():

N = "123456789"

print(iter(N))

def my_animal_generator():
    yield "Корова"
    print('-----')
    for animal in ["Собака","Кошка","Медведь"]:
        yield animal
    print('-----')
    yield "Кит"

a = my_animal_generator()
# вызов по-штучно:
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# или сразу весь итерируемый объект
# for i in a:
#     print(i)

