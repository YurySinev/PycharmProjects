from cats_n_dogs import Cat, Dog, Client

cat1 = Cat("Барон", "мальчик", 2)
cat2 = Cat("Сэм", "мальчик", 2)

print(cat1.get_age())

dog1 = Dog("Sharik", "boy", 4)

print(dog1.get_pet())

client1 = Client("Иван", "Петров", "Москва", 50)
client2 = Client("Прохор", "Баульский", "Тамбов", 39)
client3 = Client("Степан", "Голодубцев", "Урюпинск", 41)
client4 = Client("Евгения", "Бурдовченко", "Пермь", 28)
client5 = Client("Валентина", "Коврижкина", "Москва", 45)
client6 = Client("Сидор", "Пантелеймонов", "Тверь", 53)

guests = [client1, client2, client3, client4, client5, client6]
for g in guests:
    print(g.get_guest())
