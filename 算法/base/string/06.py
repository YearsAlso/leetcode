def myAtoi(str):
    str = str.strip()
    if len(str)<=0:
        return 0
    f = 1
    have_num=False
    num = 0
    if str[0] == '+':
        f = 1
        str = str[1:]
    elif str[0] == '-':
        f = -1
        str = str[1:]
    for s in str:
        if s.isdigit():
            num =num*10+int(s)
            have_num=True
        else:
            if have_num:
                break
            return 0
    num = num*f
    if num >2147483647:
        return 2147483647
    if num<(-2147483648):
        return -2147483648
    return num


print(myAtoi('2147483648'))