class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        nums = set(nums)
        list_nums = list(nums)
        list_nums.sort()
        i = 1
        for value in list_nums:
            if value <= 0:
                continue
            if value ^ i != 0:
                return i
            i += 1
        return i


sol = Solution()
print(sol.firstMissingPositive([1, 1000]))
