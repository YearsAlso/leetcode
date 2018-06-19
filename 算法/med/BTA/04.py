class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # list_s = [[]]
        # for i in range(len(nums)):
        #     for j in range(len(list_s)):
        #         for value in nums:
        #             list_p = [value] + list_s[j]
        #             list_p.sort()
        #             if (not list_p in list_s )and(not value in list_s[j]) :
        #                 list_s.append(list_p)
        # return list_s

        res = []
        for index in range(1 << len(nums)):  # n^2
            item = []
            for j in range(len(nums)):
                if (index & (1 << j)):
                    item.append(nums[j])
            res.append(item)
        return res

sol = Solution()
print(sol.subsets([1,2,3,4]))


