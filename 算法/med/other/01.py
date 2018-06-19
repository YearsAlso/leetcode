class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while a != 0:
            tmp = (a & b) << 1
            b = a ^ b
            a = tmp
        
        return b


print(Solution().getSum(-1, 1))
