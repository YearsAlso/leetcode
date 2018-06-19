# class Solution:
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) < 3:
#             return False
#         sub = 0
#         for i in range(1, len(nums) - 1):
#             if nums[i] - nums[i - 1] > 0:
#                 sub = nums[i] - nums[i-1]
#             else:
#                 continue

#             if sub * (nums[i + 1] - nums[i]) > 0:
#                 return True

#         return False


# class Solution:
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) < 3:
#             return False
#         j = 0
#         for i in range(0, len(nums)):
#             while nums[i] < nums[j-1] and j>=1:
#                 nums[j-1] = nums[i]
#                 j-=1
#                 if j == 0:
#                     j+=1
#                     break
#             if j >= 1:
#                 if nums[i] > nums[j-1] and nums[i] < nums[j]:
#                     nums[j], nums[i] = nums[i], nums[j]
#                     j += 1
#                 elif nums[i] == nums[j]:
#                     j+=1
#             elif j < 1:
#                 if nums[i] < nums[j]:
#                     nums[j], nums[i] = nums[i], nums[j]
#                     nums[i] = 2147483648
#                     j += 1
#
#                 elif nums[i] == nums[j]:
#                     j+=1
#                 else:
#                     nums[i] = 2147483648
#             else:
#                 nums[i] = 2147483648
#
#             if j >= 3:
#                 return True
#         return False
#


# class Solution:
#     def increasingTriplet(self, nums):
#         if len(nums) < 3:
#                 return False
#         j=[]
#         for i in range(0, len(nums)):
#             if len(j) == 0:
#                 j.append(nums[i])
#             else:
#                 n = len(j)-1
#                 while n >= 0:
#                     if nums[i] in j:
#                         break
#                     if j[-1] > nums[i]:
#                         j.pop()
#                         if len(j) == 0:
#                             j.append(nums[i])
#                             break
#                     elif j[-1]<nums[i]:
#                         j.append(nums[i])
#                     n -= 1
#             if len(j) >=3:
#                 print(j)
#                 return True
#         print(i)
#         return False

class Solution:
    def increasingTriplet(self,nums):
        if len(nums) < 3:
            return False
        m1 = 2147483648
        m2 = 2147483648
        for value in nums:
            if m1 >= value:
                m1 = value
            elif m2 >= value:
                m2 = value
            else:
                return True
        return False

sol = Solution()
nums=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,3]
print(sol.increasingTriplet(nums))
print(nums)
