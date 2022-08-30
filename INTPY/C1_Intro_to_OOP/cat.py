class Cat:
    color = None

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

    @property
    def set_color(self, color):
        self.color = color
        return color


if __name__ == "__main__":
    cat_ = Cat("Плюша", "самка", 3)
    print(cat_.get_name(), cat_.get_gender(), cat_.get_age())
    cat_.color = "белая и пушистая"
    print(cat_.color)
