def moveZeroes(nums):
    length = len(nums)
    i = 0
    while i < length:
        if nums[i] == 0:
            nums.pop(i)
            nums.insert(length-1,0)
            length-=1
        else:
            i += 1
    print(nums)

moveZeroes([0,0,1])