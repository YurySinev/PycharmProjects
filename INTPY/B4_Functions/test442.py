# Задание 4.4.2 # Задание на самопроверку.
# Создать генератор цикла, то есть в функцию на входе будет передаваться массив,
# например, [1, 2, 3], генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.

def cycle(list_):
    new_list = list_.copy()
    while True:
        value = new_list.pop(0)
        new_list.append(value)
        yield value

for i in cycle([1,2,3,4,5]):
    print(i)

# предложенное решение:
def repeat_list(list_):
   list_values = list_.copy()
   while True:
       value = list_values.pop(0)
       list_values.append(value)
       yield value

for i in repeat_list([1, 2, 3]):
   print(i)