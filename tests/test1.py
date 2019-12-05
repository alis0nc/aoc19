import unittest
from ..day1 import fuel_required

class Test1(unittest.TestCase):
    def test12(self):
        self.assertEqual(fuel_required(12), 2)

    def test14(self):
        self.assertEqual(fuel_required(14), 2)

    def test1969(self):
        self.assertEqual(fuel_required(1969), 654)

    def test100756(self):
        self.assertEqual(fuel_required(100756), 33583)

if __name__ == '__main__':
    unittest.main()