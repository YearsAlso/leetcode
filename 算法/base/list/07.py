def plusOne1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digit = 0
    for value in digits:
        digit =digit*10+value

    digit+=1

    digit_list=[]
    digit_h=int(digit/100000)
    digit_l=int(digit%100000)
    i = 0
    while digit_l>0:
        digit_list.append(int(digit_l%10))
        digit_l=int(digit_l/10)
        i+=1

    if digit_h!=0:
        i = 5-i
        while i:
            digit_list.append(0)
            i-=1
        while digit_h>0:
            digit_list.append(int(digit_h%10))
            digit_h=int(digit_h/10)


    digit_list.reverse()
    return digit_list

def plusOne(digits):
    digits.reverse()
    add = False
    i=0
    length = len(digits)
    digits[0]+=1

    while i<length:
        if add:
            digits[i]+=1
        if digits[i]>9:
            digits[i]=int(digits[i]%10)
            add=True
        else:
            add=False
        i+=1
    if add:
        digits.append(1)
    return digits[::-1]

print(plusOne([8,9,9,9]))