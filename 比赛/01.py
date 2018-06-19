
def find_num(list_n,n):
    for i in range(n):
        if i in list_n:
            continue
        else:
            return(i)
    return None

n = int(input())
list_n = []
for value in input().split(" "):
    list_n.append(int(value))
list_n.sort()
num = find_num(list_n,n)
if num:
    print(num)

