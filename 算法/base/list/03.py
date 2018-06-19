def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    while i < k:
        n = nums.pop()
        nums.insert(0, n)
        i += 1
    return nums

print(rotate([1,2,3,4,5,6,7],4))