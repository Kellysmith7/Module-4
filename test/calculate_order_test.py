import unittest
from topic3 import calculate_order


class MyTestCase(unittest.TestCase):
    def test_thirty_to_fifty(self):
        self.assertEqual(85.50, calculate_order.calculate_order(100, 5, .10))
        self.assertEqual(80.75, calculate_order.calculate_order(100, 5, .15))
        self.assertEqual(76, calculate_order.calculate_order(100, 5, .20))
        self.assertEqual(81.00, calculate_order.calculate_order(100, 10, .10))
        self.assertEqual(76.50, calculate_order.calculate_order(100, 10, .15))
        self.assertEqual(72.00, calculate_order.calculate_order(100, 10, .20))


if __name__ == '__main__':
    unittest.main()
