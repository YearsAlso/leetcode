import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_bck =[]
        self.nums_bck.extend(nums)
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        #self.nums = self.nums_bck
        return self.nums_bck

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        self.nums.insert(0, self.nums.pop(random.randint(0, len(self.nums)-1)))
        return self.nums

if __name__ == '__main__':
    sol = Solution([1,2,3])
    print(sol.shuffle())
    print(sol.reset())
    print(sol.shuffle())