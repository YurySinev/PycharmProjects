class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


class Dog(Cat):
    def get_pet(self):
        return f"{self.name}, {self.age}"


class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."
    def get_guest(self):
        return f"{self.name} {self.surname}: г.{self.city}"

if __name__ == '__main__':
    client1 = Client("Иван", "Петров", "Москва", 50)
    print(client1.get_guest())