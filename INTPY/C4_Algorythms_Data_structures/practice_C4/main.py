from queue import Queue

def practice_queue():
    size = int(input("Определите размер очереди: "))
    q = Queue(size)

    while True:
        cmd = input("Введите команду (empty, size, add, show, do, exit): ")
        if cmd == "empty":
            if q.is_empty():
                print("Очередь пустая")
            else:
                print("В очереди есть задачи")
        elif cmd == "size":
            print("Количество задач в очереди: ", q.size())
        elif cmd == "add":
            if q.size() != q.max_size:
                q.add()
            else:
                print("Очередь переполнена")
        elif cmd == "show":
            if q.is_empty():
                print("Очередь пустая")
            else:
                q.show()
        elif cmd == "do":
            if q.is_empty():
                print("Очередь пустая")
            else:
                q.do()
        elif cmd == "exit":
            for _ in range(q.size()):
                q.do()
            print("Очередь пустая. Завершение работы")
            break
        else:
            print("Введена неверная команда")

print("Клавиши для выбора: \n 1 - очередь, 2 - стек, 3 - граф")
start = input("Ваш выбор? ")
if start == "1":
    practice_queue()