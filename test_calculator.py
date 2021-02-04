import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition_1(self):
        self.assertEqual(calculator.addition(2, 3), 5)

    def test_addition_2(self):
        self.assertEqual(calculator.addition(-2, -3), -5)

    def test_addition_3(self):
        self.assertEqual(calculator.addition(3.5, 4.5), 8.0)

    def test_subtraction_1(self):
        self.assertEqual(calculator.subtraction(10, 3), 7)

    def test_subtraction_2(self):
        self.assertEqual(calculator.subtraction(-2, 4), -6)

    def test_subtraction_3(self):
        self.assertEqual(calculator.subtraction(25.5, 10.5), 15.0)

    def test_multiplication_1(self):
        self.assertEqual(calculator.multiply(2, 5), 10)
    
    def test_multiplication_2(self):
        self.assertEqual(calculator.multiply(0, 45), 0)

    def test_multiplication_3(self):
        self.assertEqual(calculator.multiply(2.5, 4.0), 10.0)

    def test_division_1(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_division_2(self):
        self.assertEqual(calculator.divide(15, 2.5), 6.0)

    def test_division_3(self):
        self.assertEqual(calculator.divide(-2, 4), -0.5)

    def test_division_4(self):
        #self.assertEqual(calculator.divide(10, 0), 0)
        self.assertRaises(ZeroDivisionError, calculator.divide, 10, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

