def merge( nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if m!=0:
        l1 = nums1[:m]
    else:
        l1 = []
    l2 = nums2[:n]
    l1.extend(l2)
    l1.sort()
    nums1.clear()
    nums1.extend(l1)
    return nums1

print(merge([0],0,[1],1))