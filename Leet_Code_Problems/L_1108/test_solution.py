import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def test_defangIPaddr(self):
        self.assertEqual(Solution().defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")
