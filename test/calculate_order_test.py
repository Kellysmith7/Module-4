import unittest
from topic3 import calculate_order


class MyTestCase(unittest.TestCase):
    def test_ten_to_thirty(self):
        self.assertEqual(25.95, calculate_order.calculate_order(25, 5, .10))
        self.assertEqual(24.95, calculate_order.calculate_order(25, 5, .15))
        self.assertEqual(23.95, calculate_order.calculate_order(25, 5, .20))
        self.assertEqual(21.45, calculate_order.calculate_order(25, 10, .10))
        self.assertEqual(20.70, calculate_order.calculate_order(25, 10, .15))
        self.assertEqual(19.95, calculate_order.calculate_order(25, 10, .20))


if __name__ == '__main__':
    unittest.main()
