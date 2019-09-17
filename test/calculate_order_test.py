import unittest
from topic3 import calculate_order


class MyTestCase(unittest.TestCase):
    def test_ten_to_thirty(self):
        self.assertEqual(14.50, calculate_order.calculate_order(20, 5, .10))
        self.assertEqual(17.75, calculate_order.calculate_order(20, 5, .15))
        self.assertEqual(17, calculate_order.calculate_order(20, 5, .20))
        self.assertEqual(9, calculate_order.calculate_order(20, 10, .10))
        self.assertEqual(8.5, calculate_order.calculate_order(20, 10, .15))
        self.assertEqual(8, calculate_order.calculate_order(20, 10, .20))


if __name__ == '__main__':
    unittest.main()
