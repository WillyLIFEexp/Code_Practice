class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        # This is the worst case scenario
        if num == 1:
            return 1

        if (num % 2) == 0:
            return 1 + self.numberOfSteps(num / 2)
        else:
            return 1 + self.numberOfSteps(num - 1)
