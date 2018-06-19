def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # if len(prices) == 0:
    #     return 0
    # min_num = min(prices)
    # max_num = max(prices)
    # min_i = prices.index(min_num)
    # max_i = prices.index(max_num)
    # if min_i > max_i:
    #     if max_i >= 1:
    #         return max_num - min(prices[:(max_i)])
    #     else:
    #         return max(prices[min_i:]) - min_num
    # return max_num - min_num
    sub_list = []
    i=1
    while i<len(prices):
        sub_list.append(prices[i]-prices[i-1])
        i+=1

    i=0
    sum=0
    while i<len(sub_list):
        if sub_list[i] > 0:
            sum+=sub_list[i]
        i+=1
    return sum

print(maxProfit([4,1,2]))