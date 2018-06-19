class Solution:
    def get_loop(self,a,b):
        pass
    
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        integer = numerator//denominator
        decimal = self.get_loop(numerator%denominator,denominator)
        