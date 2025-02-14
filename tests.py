import unittest
from linked_list import LinkedList
from char_queue import CharQueue


class TestLinkedList(unittest.TestCase):
    """Тесты для класса LinkedList."""

    def test_insert_and_search(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        self.assertTrue(ll.search(10))
        self.assertTrue(ll.search(20))
        self.assertFalse(ll.search(30))

    def test_delete(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.delete(10)
        self.assertFalse(ll.search(10))
        self.assertTrue(ll.search(20))


class TestCharQueue(unittest.TestCase):
    """Тесты для класса CharQueue."""

    def test_is_empty(self):
        queue = CharQueue(3)
        self.assertTrue(queue.is_empty())
        queue.enqueue("a")
        self.assertFalse(queue.is_empty())

    def test_is_full(self):
        queue = CharQueue(2)
        self.assertFalse(queue.is_full())
        queue.enqueue("a")
        queue.enqueue("b")
        self.assertTrue(queue.is_full())


if __name__ == "__main__":
    unittest.main()