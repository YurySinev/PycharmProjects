import time

i = 10
while i >= 0: # поправка 1: было i != 0
    print(i)
    time.sleep(1)   # поправка 2: было sleep(1)
    i -= 1
print("Время вышло!") # поправка 3: строка была с отступом
