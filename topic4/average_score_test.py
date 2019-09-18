import unittest
from topic4 import average_score_2


class MyTestCase(unittest.TestCase):
    def test_input_validation(self):
        self.assertEqual(-1, average_score_2.average(-90, 90, 85))


if __name__ == '__main__':
    unittest.main()
