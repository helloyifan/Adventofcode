import unittest
from aoc_2023_01 import solution

class TestMyFunction(unittest.TestCase):
    def test_example(self):
        print("hello world")
        solution()
        self.assertEqual(solution(), 1)

if __name__ == '__main__':
    unittest.main()
