class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.task_num = 0
        self.tasks = [0 for _ in range(self.max_size)]
        self.head = 0
        self.tail = 0

    def push(self):  # Вставка элемента в хвост очереди
        ...

    def top(self):  # Получение элемента из начала очереди
        ...

    def pop(self):  # Удаление элемента из начала очереди
        ...

    # Проверка наличия элементов в очереди
    def is_empty(self):  # очередь пуста? да, если указатели совпадают и в ячейке нет задачи
        return self.head == self.tail and self.tasks[self.head] == 0

    # Получение размера очереди
    def size(self):
        if self.is_empty():  # если она пуста,
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # если она не пуста, но указатели совпадают, з
            return self.max_size  # значит очередь заполнена
        elif self.head > self.tail:  # если хвост левее начала
            return self.max_size - self.head + self.tail
        else:  # или если хвост правее начала
            return self.tail - self.head

    # добавление задачи в очередь
    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")
        self.tail = (self.tail + 1) % self.max_size  # увеличиваем указатель на 1
        # по модулю максимального числа элементов для зацикливания очереди в списке

    # Выполнение очередного пункта и удаление его из очереди
    def do(self):
        print(f"Задача №{self.tasks[self.head]} выполнена")
        self.tasks[self.head] = 0  # после выполнения зануляем элемент по указателю
        self.head = (self.head + 1) % self.max_size  # и циклично перемещаем указатель

    def show(self):
        print(f"Задача №{self.tasks[self.head]} в приоритете")
