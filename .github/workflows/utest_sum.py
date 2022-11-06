import unittest
import suma


class SumTest(unittest.TestCase):
    def test_sumowanie(self):
        self.assertEqual(suma.sumowanie(2,2), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()

