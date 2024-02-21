from src.queue import Queue

if __name__ == '__main__':
    queue = Queue()

    # Магический метод __str__ возвращает пустую строку
    assert str(Queue()) == ""

    # Добавляем данных в очередь
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    # Проверяем очередность хранения данных
    print(queue.head.data)
    assert queue.head.data == 'data1'
    print(queue.head.next_node.data)
    assert queue.head.next_node.data == 'data2'
    print(queue.tail.data)
    assert queue.tail.data == 'data3'
    print(queue.tail.next_node)
    assert queue.tail.next_node is None

    # print(queue.tail.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'

    # Проверяем магический метод __str__
    print(str(queue))
    assert str(queue) == "data1\ndata2\ndata3"
