import unittest

from sol_1342 import Solution

class TestL1342(unittest.TestCase):
    def test_numberOfSteps(self):
        self.assertEqual(Solution().numberOfSteps(14), 6)

if __name__ == '__main__':
    unittest.main()
