def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    sum = 0
    while i < len(s):
        if dict.get(s[i]) >= 0:
            if i>0 and dict[s[i - 1]] < dict[s[i]]:
                sum -= 2*dict[s[i - 1]]
            sum += dict[s[i]]
        i += 1
    return int(sum)

print(romanToInt("DCXXI"))