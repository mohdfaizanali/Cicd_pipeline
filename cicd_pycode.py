# tests/test_app.py
import unittest
from my_module import add_numbers

class TestMyModule(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

# my_module.py
def add_numbers(a, b):
    return a + b