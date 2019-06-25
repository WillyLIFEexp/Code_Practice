#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

#Return the element repeated N times.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # My solution
        tmp = dict()
        for a in A:
            if a in tmp.keys():
                return a
            else:
                tmp[a] = 1

        # Other solutions
        for a in A:
            if A.count(a) > 1:
                return a
