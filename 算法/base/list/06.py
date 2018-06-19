def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    list = []
    for value in nums2:
        try:
            i = nums1.index(value)
            if i>=0:
                list.append(value)
                nums1.pop(i)
        except:
            pass
    return list

print(intersect([1],[1,1]))