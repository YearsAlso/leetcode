import collections
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        dict_num = collections.Counter(nums)
        key,value = sorted(dict_num.items(),key=lambda x:x[1],reverse=True)[0]
        if value > len(nums)//2:
            return key
        else:
            return None
        
        
print(Solution().majorityElement([3,2,3]))