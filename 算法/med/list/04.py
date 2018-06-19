def lengthOfLongestSubstring(strings):
    if len(strings)==0:
        return None
    str_all_list=[]
    i = 0
    while i < len(strings):
        j=i
        substring_list = []
        while j<len(strings):
            char = strings[j]
            if len(substring_list)==0:
                substring_list.append(char)
            elif char in substring_list:
                if not (substring_list in str_all_list):
                    str_all_list.append(substring_list)
                break
            else:
                substring_list.append(char)
            j+=1
        str_all_list.append(substring_list)
        i += 1


    max_len = 0
    for str_list in str_all_list:
        if len(str_list)>max_len:
            max_len = len(str_list)

    return max_len


print(lengthOfLongestSubstring("asjrgapa"))