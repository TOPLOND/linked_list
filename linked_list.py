class Node:
    """Класс узла списка."""

    def __init__(self, data):
        """
        Конструктор узла списка.

        :param data: Данные, хранящиеся в узле.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Класс односвязного списка."""

    def __init__(self):
        """
        Конструктор односвязного списка.

        :ivar head: Указатель на первый элемент списка.
        """
        self.head = None

    def insert(self, new_data):
        """
        Вставка нового узла в начало списка.

        :param new_data: Данные для вставки.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        """
        Поиск элемента в списке.

        :param item: Элемент для поиска.
        :return: True, если элемент найден, иначе False.
        """
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def delete(self, key):
        """
        Удаление первого встреченного узла с заданным ключом.

        :param key: Ключ для удаления.
        """
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        """
        Вывод содержимого списка.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")