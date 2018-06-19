win_dict={}
for i in range(3):
    m,n = input().split(" ")
    win_dict[n] = m

time = int(input())

j = 0
prt_list=[]
while j< time:
    inp_str = input("")
    if win_dict.get(inp_str)!=None:
        prt_list.append(win_dict[inp_str])
    else:
        prt_list.append("Fuck")
    j+=1

for value in  prt_list:
    print(value)
