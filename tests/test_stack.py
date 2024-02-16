"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self):
        """Добавляем объект в стек и проверяем правильную последовательность"""
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')

    def test_pop_push(self):
        """Проверка правильного добавление и удаления из конца стека"""
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.pop()
        self.assertEqual(self.stack.top.data, 'data1')
        self.assertEqual(self.stack.top.next_node, None)
        self.assertEqual(self.stack.pop(), 'data1')

