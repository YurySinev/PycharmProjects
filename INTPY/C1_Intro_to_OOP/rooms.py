class Room1:
    def get_room(self):
        print("комната 1")

class Room2:
    def get_room(self):
        print("комната 2")
    def get_room2(self):
        print("двухкомнатная квартира")

class Kitchen:
    def get_kitchen(self):
        print("кухня")

class Flat(Kitchen, Room1, Room2):
    def get_flat(self):
        print(self.get_room2())

f = Flat()
f.get_kitchen()
f.get_room()
f.get_room2()
f.get_flat()