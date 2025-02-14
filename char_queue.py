class CharQueue:
    """Класс очереди для работы с символьными значениями."""

    def __init__(self, size):
        """
        Конструктор очереди.

        :param size: Максимальный размер очереди.
        """
        self.size = size
        self.queue = []

    def is_empty(self):
        """
        Проверка очереди на пустоту.

        :return: True, если очередь пуста, иначе False.
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Проверка очереди на заполнение.

        :return: True, если очередь заполнена, иначе False.
        """
        return len(self.queue) == self.size

    def enqueue(self, item):
        """
        Добавление элемента в очередь.

        :param item: Элемент для добавления.
        :raises: OverflowError, если очередь заполнена.
        """
        if self.is_full():
            raise OverflowError("Очередь заполнена.")
        self.queue.append(item)

    def dequeue(self):
        """
        Удаление элемента из очереди.

        :return: Удаленный элемент.
        :raises: IndexError, если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("Очередь пуста.")
        return self.queue.pop(0)

    def show(self):
        """
        Отображение всех элементов очереди на экран.
        """
        print("Очередь:", " -> ".join(self.queue))