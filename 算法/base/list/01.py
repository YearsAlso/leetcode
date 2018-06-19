def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    length = len(nums)
    while i < length:
        num = nums[i]
        counts = nums.count(num)
        if counts > 1:
            nums2 = nums[i + counts:]
            nums = nums[:i+1]
            nums.extend(nums2)
            length=length-counts+1
        i += 1
    print(nums)
    return len(nums)

def removeDuplicates(nums):
    #return list(set(listA))

    return len(sorted(set(nums), key = nums.index))


print(removeDuplicates([1,1,2,2,5,5,5]))