from C1_10_praktikum import Rectangle, Client

client1 = Client("Иван","Петров","Москва",50)
print(client1.get_client())
print(1)
client2=Client("Мария","Селедкина","Самара",150)
client3=Client("Николай","Вяткин","Брянск", 400)
client4=Client("Елена","Хлопьева","Тверь", 850)
client5=Client("Геннадий","Борисов","Мурманск", 1200)
client6=Client("Екатерина","Голышева","Астрахань", 915)

clients=[client6, client2, client5, client1, client3, client4]
print("Список гостей:")
for i in clients:
    print(i.get_client_info())
