list_str = []

for str in input().split(','):
    list_str.append(str)

min_str = ""
min_length = 10000
for value in list_str:
    if min_length > len(value):
        min_length = len(value)
        min_str = value

char_num = 0
i = 0
prt =""
length = len(list_str)
while i<len(min_str):
    j=0
    char_num = 0
    while j<len(list_str):
        if list_str[j][i] == min_str[i]:
            char_num+=1
        j+=1
    if char_num == length:
        prt+=min_str[i]
    else:
        break
    i+=1
print(prt)

