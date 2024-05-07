import unittest
import sys


def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorialFunction(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
    def test_factorial_plus_number(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
    def test_factorial_minus_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)
    def test_factorial_bigINT_input(self):
        with self.assertRaises(ValueError):
            factorial(1000000)
