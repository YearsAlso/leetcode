class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = set(nums)
        list_num = list(nums)
        list_num.sort()
        list_length = []

        j = 0
        length = len(list_num)
        while j<length:
            i = list_num[j]
            start = i
            while i^list_num[j]==0:
                i+=1
                j+=1
                if j >= length:
                    break
            list_length.append(i - start)
        return max(list_length)
        
    
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))