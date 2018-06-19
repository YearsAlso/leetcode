class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = 1
        for value in nums:
            if value != 0:
                num *= value
        
        list_num = len(nums) * [num]
        if 0 in nums:
            if nums.count(0) == 1:
                for i, value in enumerate(nums):
                    if value != 0:
                        list_num[i] = 0
            elif nums.count(0)==len(nums):
                return nums
            else:
                return len(nums) * [0]
        else:
            for i, value in enumerate(nums):
                list_num[i] = list_num[i] // value
        return list_num
    
    
sol = Solution()
print(sol.productExceptSelf([0,4,0]))