import sys
import math
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        m = abs(dividend)
        n = abs(divisor)

        if m<n:
            return 0
        res = 0
        while (m >= n):
            t = n
            p = 1
            while (m > (t << 1)):
                t <<= 1
                p <<= 1
                print(p)
            res += p
            m -= t

        if (divisor<0)^ (dividend<0):
            res *= -1
        return res if res<=2147483647 else 2147483647
    
sol = Solution()
print(sol.divide(-2147483648,-1))