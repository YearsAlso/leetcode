import math


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        num = 0
        while n > 0:
            num += n // 5
            n = n // 5
        
        return num


print(Solution().trailingZeroes(3678))
