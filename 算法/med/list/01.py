def threeSum1(nums):
    nums.sort()
    print(nums)
    h = 0
    length = len(nums)
    t = length - 1
    num_list = []
    while h < t:
        sub = (nums[h] + nums[t])
        j = h + 1
        while j < t:
            if nums[j] == (sub * -1):
                l = sorted([nums[h], nums[t], (sub * -1)])
                if not num_list.count(l):
                    num_list.append(l)
                h = 0
                break
            j += 1
        if sub < 0:
            h += 1
        elif sub >= 0:
            t -= 1

    return num_list

def threeSum2( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
        """
    length = len(nums)
    nums.sort()
    num_list = []
    i = 0
    while i < length:
        j = i + 1
        r = length - 1
        while j < r:

            sub = nums[i] + nums[j] + nums[r]
            if sub == 0:
                l = sorted([nums[i], nums[j], nums[r]])
                l.sort()
                num_list.append(l)

                while j > 0 and nums[j] == nums[j - 1]:
                    j += 1
                while r < (length - 1) and nums[r] == nums[r + 1]:
                    r -= 1
            if sub <= 0:
                j += 1
            elif sub > 0:
                r -= 1
        while i < (length - 1) and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return num_list

def threeSum(nums):
    length = len(nums)
    nums.sort()
    num_list = []
    i = 0
    l = [None,None,None]
    while i < length:
        sub = 0-nums[i]
        j = i + 1
        r = length - 1
        l[0] = nums[i]
        while j < r:
            if sub == nums[j] + nums[r]:
                l[1] = nums[j]
                j+=1
                l[2] = nums[r]
                r-=1
                num_list.append(l)
                while (j<r) and (nums[j]==nums[j-1]):
                    j+=1
                while (j<r) and (nums[r]==nums[r+1]):
                    r-=1
            if (nums[j] + nums[r]) < sub:
                j += 1
            else:
                r -= 1
        while i<(length-1) and nums[i]==nums[i+1]:
            i += 1
        i += 1
    return num_list


#print(threeSum1([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
print(threeSum([-1,0,1,2,-1,-4]))
# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
