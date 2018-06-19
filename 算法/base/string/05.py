def isPalindrome(strs=''):
    strs=strs.lower()
    new_strs = ""
    for str in strs:
        if str.isalpha() or str.isdigit():
            new_strs=new_strs+str
    if new_strs == new_strs[::-1]:
        return True
    else:
        return False

print(isPalindrome("ab"))