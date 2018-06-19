class Solution:
    def isPalindrome(self, strings1, strings2, center):
        length = min(len(strings1), len(strings2))
        i = 0
        while i < length:
            if strings1[i] != strings2[i]:
                break
            center = strings1[i] + center + strings1[i]
            i += 1
        return center

    def longestPalindrome(self, strings):
        """
        :type strings: str
        :rtype: str
        """
        if len(strings) == 0:
            return 0
        if len(strings) == 1:
            return strings
        i = 0
        substring_list = []
        length = len(strings)
        max_str = ''
        while i < length-1:
            pal_str= ''
            if i>=1 and strings[i - 1] == strings[i+1]:
                pal_str2 = self.isPalindrome(strings[i-1::-1], strings[i+1:], strings[i])
                if len(pal_str2)>len(pal_str):
                    pal_str = pal_str2
            if strings[i] == strings[i + 1]:
                pal_str1 = self.isPalindrome(strings[i::-1], strings[i+1:], "")
                if len(pal_str1)>len(pal_str):
                    pal_str = pal_str1
            if len(max_str) == 0:
                max_str = strings[i]
            if len(pal_str) > len(max_str):
                max_str = pal_str
            i+=1
        return max_str


sol = Solution()

print(sol.longestPalindrome("a"*10))
print("a"*10)