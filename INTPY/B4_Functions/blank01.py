def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step

my_count = count(11, 2)

for i in range(10):
    print(next(my_count))

a = input()
a = input("123")
b = input("hh")
b = input()

print(a + b)
