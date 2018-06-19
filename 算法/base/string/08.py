def longestCommonPrefix(strs):
    if len(strs)==0:
        return ""
    str=""
    i=0
    while i<len(strs[0]):
        str+=strs[0][i]
        j= 1
        while j<len(strs):
            if strs[j].startswith(str):
                pass
            else:
                return str[:-1]
            j+=1
        i+=1
    return str

print(longestCommonPrefix([]))