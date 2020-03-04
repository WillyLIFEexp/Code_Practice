import unittest

from sol_1108 import Solution

class TestL1108(unittest.TestCase):
    def test_defangIPaddr(self):
        self.assertEqual(Solution().defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")


if __name__ == '__main__':
    unittest.main()