"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Queue()
        self.stack.enqueue('data1')
        self.stack.enqueue('data2')
        self.stack.enqueue('data3')

    def test_enqueue(self):
        """Тестирование правильно работы метода enqueue"""
        self.assertEqual(self.stack.head.data, 'data1')
        self.assertEqual(self.stack.head.next_node.data, 'data2')
        self.assertEqual(self.stack.tail.data, 'data3')

    def test_dequeue(self):
        """Тестирование правильно работы метода dequeue"""
        self.assertEqual(self.stack.dequeue(), 'data1')
        self.assertEqual(self.stack.dequeue(), 'data2')
        self.assertEqual(self.stack.dequeue(), 'data3')
        self.assertEqual(self.stack.dequeue(), None)

    def test__str__(self):
        """Тестирование правильного вывода __str__"""
        self.assertEqual(str(self.stack), "data1\ndata2\ndata3")
