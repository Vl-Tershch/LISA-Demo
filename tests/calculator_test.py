import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(Calculator.divide(4, 2), 2)

    def test_square(self):
        self.assertEqual(Calculator.square(2), 4)
