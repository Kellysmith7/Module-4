import unittest
from topic3 import calculate_order


class MyTestCase(unittest.TestCase):
    def test_under_ten(self):
        self.assertEqual(8.65, calculate_order.calculate_order(8, 5, .10))
        self.assertEqual(8.50, calculate_order.calculate_order(8, 5, .15))
        self.assertEqual(8.35, calculate_order.calculate_order(8, 5, .20))
        #self.assertEqual(0, calculate_order(8, 10, .10))
        #self.assertEqual(0, calculate_order(8, 10, .15))
        #self.assertEqual(0, calculate_order(8, 10, .20))


if __name__ == '__main__':
    unittest.main()
