class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        str_list = list(s)
        
        num = 0
        a_hex = ord('A') - 1
        
        for i,value in enumerate(str_list):
            str_list[i] = ord(value) - a_hex
            
        print(str_list)
        num = 0
        for value in str_list:
            num = num*26 + value
            
        return num
    
sol = Solution()
print(sol.titleToNumber("A"))