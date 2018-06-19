
n = int(input())
list_n = []
for value in input().split(" "):
    list_n.append(int(value))

sub_list = []
for i in range(1,len(list_n)):
    sub_list.append(list_n[i] - list_n[i-1])

max = 0
for value in sub_list:
    if value > 0:
        max+=value

print(max)