def isPowerOfThree(n):
    if n==1:
        return True
    elif n==0:
        return False
    n=int(n)
    while n>3:
        if int(n%3)!=0:
            return False
        n=int(n/3)
    if n!=3:
        return False
    else:
        return True

print(isPowerOfThree(19684))