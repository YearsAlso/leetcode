def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums==[0]:
        return 1
    nums_list = []
    i = 0
    length = len(nums)
    while i < (length+1):
        nums_list.append(0)
        i += 1
    i=0
    while i < length:
        nums_list[nums[i]]=1
        i += 1
    i = 0
    while i <= length:
        if nums_list[i] != 1:
            return i
        i+=1


print(missingNumber([0,1]))