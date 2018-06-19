def  threeMax(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_num = -2147483648
    i = 0
    leg = len(nums)
    if leg == 0:
        return 0
    if leg == 1:
        return nums[0]
    this_num = 0
    while i < leg:
        this_num += nums[i]
        if this_num > max_num:
            max_num = this_num
        if this_num < 0:
            this_num = 0
        i += 1
    return max_num

print(maxSubArray([-2,-1]))