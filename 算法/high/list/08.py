import collections
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==0:
        #     return
        # dict_num = collections.Counter(nums)
        # return sorted(dict_num.items(),key=lambda x:x[1],reverse=True)[0][0]
        if len(nums) == 0:
            return 0
        slow = nums[0]
        fast = nums[nums[0]]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow
    
    
sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))
        