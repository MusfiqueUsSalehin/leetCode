class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res
        