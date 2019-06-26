#Students are asked to stand in non-decreasing order of heights for an annual photo.

#Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for x in zip(heights,sorted(heights)):
            if x[0] != x[1]:
                res += 1
        return res

if __name__ == '__main__':
    S = Solution()

