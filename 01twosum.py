def twoSum(nums, target):
    list = []
    list.extend(nums)
    sum = -1
    while sum != target:
        max_num = max(list)
        min_num = min(list)
        sum = max_num + min_num
        if sum > target:
            list.remove(max_num)
        elif sum < target:
            list.remove(min_num)

    return [nums.index(min_num), len(nums)-1-nums[::-1].index(max_num)]


print(twoSum([0,4,3,0], 0))
