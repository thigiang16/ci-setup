import unittest
from src.main import add, subtract, mul, poweroftwo, squareroot

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)

    def test_poweroftwo(self):
        self.assertEqual(poweroftwo(6), 36)

    """new test"""
    def test_squareroot(self):
        self.assertEqual(squareroot(25), 5)

if __name__ == '__main__':
    unittest.main()
