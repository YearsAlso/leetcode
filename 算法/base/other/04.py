# coding=utf-8

def generate(numRows):
    if numRows==0:
        return []
    elif numRows==1:
        return [[1]]
    i=1
    l1=[[1]]
    l2=[]
    while i<=numRows:
        l3 = []
        l3.extend(l1[i-1])
        l3.insert(0,0)
        l3.append(0)

        j=0
        while j<i:
            l2.append(l3[j]+l3[j+1])
            j+=1
        l1.append(l2)
        l2=[]
        i+=1
    l1.pop(0)
    return l1

print(generate(5))