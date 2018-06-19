n,m = input().split(" ")
n = int(n)
m = int(m)
list_n = []
for value in input().split(" "):
    list_n.append(int(value))

time = 0
list_n.sort()
i= 0
while i< len(list_n)-1:
    if list_n[i+1] - list_n[i] < m:
        time+=1
        i+=2
    else:
        i+=1

print(time)
