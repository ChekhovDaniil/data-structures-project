class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.tail is not None:
            self.tail.next_node = node
            self.tail = self.tail.next_node
        else:
            self.tail = node
            self.head = node

    def dequeue(self) -> [int, float, str, None]:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            deq = self.head
            self.head = self.head.next_node
            return deq.data
        return None

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        if self.tail is None:
            return ''
        return f'{self.head.data}\n{self.head.next_node.data}\n{self.tail.data}'
