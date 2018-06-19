def addTwoNum1(l1,l2):
    l1 = l1[1:-1]
    l2 = l2[1:-1]
    num_l1 = [int(v.strip()) for v in l1.split('->')]
    num_l2 = [int(v.strip()) for v in l2.split('->')]
    num1=0
    num2=0
    for num in num_l1:
        num1=num1*10+num
    for num in num_l2:
        num2=num2*10+num

    sum = (num1 + num2)
    ptr = ''
    while sum>0:
        ptr+=str(int(sum%10))
        if sum > 10:
            ptr += ' -> '
        sum = int(sum / 10)
    print(ptr)


def addTwoNum(l1,l2):
    num1=0
    num2=0
    for num in l1:
        num1=num1*10+int(num)
    for num in l2:
        num2=num2*10+int(num)

    sum = (num1 + num2)
    sum_list = []
    while sum>0:
        sum_list.append(int(sum%10))
        sum = int(sum / 10)
    print(sum_list)

#addTwoNum("(2 -> 4 -> 3)","(5 -> 6 -> 4)")
addTwoNum([2,4,3],[5,6,4])