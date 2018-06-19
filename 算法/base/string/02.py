def reverse(x):
    list = []
    num = x
    if x<0:
        num=num*(-1)
    while num > 0:
        list.append(num % 10)
        num = int(num / 10)

    while list[0] == 0:
        list.pop(0)

    num = 0
    for value in list:
        num = num * 10 + value
    if x < 0:
        num=num*(-1)
    return num

print(reverse(-120))