version = [0, 0, 1, 1]


def isBadVersion(n):
    return bool(version[n - 1])


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    
    if n < 3:
        if isBadVersion(1):
            return 1
        else:
            return 2
    
    head = 1
    tail = n
    
    while head < tail:
        half = (head + tail) // 2
        if isBadVersion(half):
            if not isBadVersion(half - 1):
                return half
            else:
                tail = half - 1
        else:
            if isBadVersion(half + 1):
                return half + 1
            else:
                head = half
    return head


print(firstBadVersion(4))
