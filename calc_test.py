import unittest
import calc

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.addition(7,3),10)
        self.assertEqual(calc.addition(10,3),13)


    def test_divide(self):
        self.assertEqual(calc.divide(9,3),3)


if __name__=="__main__":
    unittest.main()


