class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxarea = 0
        while start < end:
            maxarea = max(maxarea, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxarea
    
sol = Solution()
print(sol.maxArea([1,1]))