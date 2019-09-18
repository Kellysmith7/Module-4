import unittest
from topic4 import validation_with_if


class MyTestCase(unittest.TestCase):
    def test_input_validation(self):
        self.assertEqual(-1, validation_with_if.average(90, 90, -85))


if __name__ == '__main__':
    unittest.main()
