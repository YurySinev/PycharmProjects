
# ( см. C2_3_class_decorators.py )

class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if value <= 100 and value >= 0:
            self._happiness = value
        else:
            print("Значение счастья в диапазоне 0 ... 100")


jane = Dog("Jane", 5)
print(jane.human_age)
jane.happiness = 100
print(jane.happiness)
Dog.happiness = 50
print(Dog.happiness)

