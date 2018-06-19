def maxProfit1(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0

    num_max = max(prices)
    ind_max = prices.index(num_max)
    while ind_max==0:
        prices.pop(ind_max)
        if len(prices)==0:
            return 0
        num_max = max(prices)
        ind_max = prices.index(num_max)


    num_min = min(prices)
    ind_min = prices.index(num_min)
    while ind_min==(len(prices)-1):
        prices.pop(ind_min)
        num_min = min(prices)
        ind_min = prices.index(num_min)


    sub_max = num_max - min(prices[:ind_max])
    sub_min = max(prices[ind_min:]) - num_min
    if sub_max >= sub_min:
        return sub_max
    else:
        return sub_min


def maxProfit(prices):
    if len(prices) < 2:
        return 0
    sub_prices = []
    i=1
    while i<len(prices):
        sub_prices.append(prices[i]-prices[i-1])
        i+=1

    max_sum = 0
    i=0
    while i<len(sub_prices):
        add_flag = False
        sum=0
        while sub_prices[i]>0:
            sum +=sub_prices[i]
            add_flag = True
            i+=1
        if add_flag:
            if sum > max_sum:
                max_sum = sum
        else:
            i+=1

    return max_sum

print(maxProfit([7,1,5,3,6,4]))