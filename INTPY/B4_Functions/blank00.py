l = ['s', 'd', 'f', 'g', 'r', 't', 'y', 'h', 'b', 'n', 'qwerty']

print(l)
print(l.pop())  # метод pop не только удаляет последний элемент, но и возвращает его
print(l)

age = 25
my_age = "I'm " + str(age)
print(my_age)



def get_my_func():
    def hello_world():
        print("Hello!")
    return hello_world


hello_world_func = get_my_func()  # получить функцию в качестве результата
print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello
