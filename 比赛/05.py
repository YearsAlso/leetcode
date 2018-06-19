str = input()
str_list=[]
for s in str:
    if str.count(s) == 1:
        str_list.append(s)

str_list.sort()
print(str_list[0])