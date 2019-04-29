import unittest

class TestSum(unittest.TestCase):

    def test_score1(self):
        self.assertEqual(score( [2, 3, 4, 6, 2] ), 0,"Should be 0")
    def test_score2(self):
        self.assertEqual(score( [4, 4, 4, 3, 3] ), 400,"Should be 400")
    def test_score3(self):
        self.assertEqual(score( [2, 4, 4, 5, 4] ), 450,"Should be 450")


def score(dice):
    final_score = 0
    for x in range(1,7):
        ck = dice.count(x)
        remain = ck - 3
        if x != 1 and ck >=3:
            final_score += x * 100
        elif x == 1 and ck >= 3:
            final_score += x * 1000
        if remain > 0:
            if x == 5:
                final_score += remain * 50
            elif x == 1:
                final_score += remain * 100
        elif ck > remain:
            if x == 5:
                final_score += ck * 50
            elif x == 1:
                final_score += ck * 100
    return final_score
           


if __name__ == "__main__":
    unittest.main()
    #score([ 2,3,4,6,5])
