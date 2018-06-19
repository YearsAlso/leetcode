def countAndSay(n):
    count_str = "1"

    if n == 1:
        return count_str
    i = 2
    while i <= n:
        temp_str = ""
        v=0
        counts = 0
        length = len(count_str)
        # 算下一个数的字符串
        while v<length:
            j=0
            count_str = count_str[counts:]
            counts = 0
            # 从上一个数字的字符串算现在的

            while j<len(count_str):
                if count_str[j]==count_str[0]:
                    counts+=1
                else:
                    break
                j+=1
            temp_str += (str(counts) + count_str[0])
            v+=counts
        count_str=temp_str
        i+=1
    return count_str


while True:
    n = int(input())
    if n == 0:
        break

    print(countAndSay(n))
