from cat import Cat


# Задание 1.8.2
#
# Создайте класс Dog с помощью наследования класса Cat. Создайте метод get_pet()
# таким образом, чтобы он возвращал только имя и возраст.
#
# Далее сделайте вывод этой информации в консоль.

class Dog(Cat):
    def get_pet(self):
        return f'Dog: {self.name}, {self.age}'


dog1 = Dog("Жучка", "самка", 8)
dog2 = Dog("Барбос", "самец", 4)
dog3 = Dog("Мухтар", "самец", 11)
dog4 = Dog("Белка", "самка", 5)

dogs = [dog4, dog3, dog1, dog2]

for _ in dogs:
    print(_.get_pet())

