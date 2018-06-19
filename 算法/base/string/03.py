def firstUniqChar(strs):
    l = list(strs)
    l.sort()
    i=0
    length = len(l)
    index_list=[]
    while i<length:
        count = l.count(l[i])
        if count==1:
            index_list.append(strs.index(l[i]))
        i+=count
    if len(index_list)>0:
        return min(index_list)
    else:
        return -1




print(firstUniqChar(""))