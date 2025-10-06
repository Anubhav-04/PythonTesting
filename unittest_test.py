import calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5,6),11)
    def test_sub(self):
        self.assertEqual(calculator.sub(10,6),4)
    def test_mul(self):
        self.assertEqual(calculator.mul(5,6),30)
    def test_div(self):
        self.assertEqual(calculator.div(12,6),2)
    def test_divByZero(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            calculator.div(10, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero")

    