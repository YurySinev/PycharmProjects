import time

print(time.time())
print(time.ctime())

i = 10
while i != 0:
    print(i, end="\t->\t", flush=True)
    time.sleep(1)
    i -= 1
print("Время вышло!")