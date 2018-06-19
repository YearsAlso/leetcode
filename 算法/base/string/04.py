def isAnagram(s, t):
    l1 = list(s)
    l1.sort()
    l2 = list(t)
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

print(isAnagram("a","b"))