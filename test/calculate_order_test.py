import unittest
from topic3 import calculate_order


class MyTestCase(unittest.TestCase):
    def test_thirty_to_fifty(self):
        self.assertEqual(47.95, calculate_order.calculate_order(45, 5, .10))
        self.assertEqual(45.95, calculate_order.calculate_order(45, 5, .15))
        self.assertEqual(43.95, calculate_order.calculate_order(45, 5, .20))
        self.assertEqual(43.45, calculate_order.calculate_order(45, 10, .10))
        self.assertEqual(44.25, calculate_order.calculate_order(48, 10, .15))
        self.assertAlmostEqual(42.35, calculate_order.calculate_order(48, 10, .20))


if __name__ == '__main__':
    unittest.main()
