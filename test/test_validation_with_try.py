import unittest
from topic4 import validation_with_try
from topic4.validation_with_try import average


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()
