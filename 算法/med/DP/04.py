class Solution:
    def lengthOfLISII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dict_num = {}
        for value in nums:
            dict_num[value] = nums.index(value)
            
        
        list_value  = sorted(dict_num.items(),key=lambda x:x[0])
        print(list_value)
        list_num = [list_value[0][1]]
        for i in range(1,len(list_value)):
            list_num.append(max(list_value[i][1],list_num[i-1]))
        print(list_num)
        return len(set(list_num))

    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            res = max(res,dp[i])
        return res
    
sol = Solution()
print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))