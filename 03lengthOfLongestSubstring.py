def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    s = sorted(set(s), key = s.index)
    print(s)
    return len(s)

print(lengthOfLongestSubstring("bbbbbbbbb"))
