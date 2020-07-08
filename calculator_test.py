import unittest  # import unit test module
import pytest

from calculator import Calculator  # import calculator from calculator.py

class CalculatorTest(unittest.TestCase):  # Calculator test with test case being run, make sure file has '_test'

    calculator_instance = Calculator()  # Make instance of the calculator instance

    def test_add(self):
        self.assertEqual(self.calculator_instance.addition(4, 4), 8)  # Test addition ((number1, number2), expected)

    def test_subtract(self):
        self.assertEqual(self.calculator_instance.subtraction(20, 5), 15)

    def test_multiply(self):
        self.assertEqual(self.calculator_instance.multiplication(8, 10), 80)

    def test_divide(self):
        self.assertEqual(self.calculator_instance.division(100, 10), 10)

    def test_modulo(self):
        self.assertEqual(self.calculator_instance.modulo(60, 7), 4)

    def test_quotient(self):
        self.assertEqual(self.calculator_instance.quotient(100, 12), 8)

    def test_exponentiation(self):
        self.assertEqual(self.calculator_instance.exponentiation(4, 5), 1024)

    # Trying out pyTest module too
    def func(self, x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 4

