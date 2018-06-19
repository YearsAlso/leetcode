class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            start = nums.index(target)
        except:
            return [-1,-1]
        end = start+nums.count(target)-1
        return [start,end]

sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))