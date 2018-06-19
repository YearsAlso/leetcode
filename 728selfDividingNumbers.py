def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    list = []
    i = left
    while i <= right:
        j = i
        is_div = 0
        div_time = 0
        n=1
        while j > 0:
            n = int(j % 10)
            if (n != 0):
                if (int(i % n)==0):
                    is_div += 1
            j = int(j / 10)
            div_time += 1
        if div_time == is_div:
            list.append(i)
        i += 1
    return list

print(selfDividingNumbers(1,22))