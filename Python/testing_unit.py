import unittest

class CC_LEMON():
    def __init__(self):
        pass
    def times(self,a,b):
        return a * b

class CC_Test_Case(unittest.TestCase):
    def setUp(self):
        self.args = (3,2)
    def tearDown(self):
        self.args = None
    def test_plus(self):
        expected = 5;
        result = self.plus(*self.args)
        self.assertEqual(expected,result);

    def test_minus(self):
        expected = 1
        result = self.minus(*self.args)
        self.assertEqual(expected, result)

    def test_times(self):
        expected = 6
        cc_lemon = CC_LEMON()
        data = [(2,3),(3,2),(6,1),(2,2)]
        for num in data:
            result = cc_lemon.times(*num)
            self.assertEqual(expected,result)
            
        #result = cc_lemon.times(*self.args)
        #self.assertEqual(expected,result)

    def plus(self,a,b):
        return a + b

    def minus(self,a,b):
        return a - b

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CC_Test_Case('test_plus'))
    suite.addTest(CC_Test_Case('test_times'))
    suite.addTest(CC_Test_Case('test_minus'))

    unittest.TextTestRunner(verbosity=2).run(suite)

