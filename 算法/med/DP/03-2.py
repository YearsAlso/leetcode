class Solution:
    def coinChangeCoreII(self,coins,amount,coins_num,list_num,list_coin):
        if amount==0:
            print(list_coin,coins_num)
            if list_num[0] > coins_num:
                list_num[0] = coins_num
            return True
        elif amount<0:
            return False
        elif len(coins)==0:
            return False
        num = amount//coins[-1]+1
        for i in range(num)[::-1]:
            remainder = amount-coins[-1]*i
            list_coin.append(i)
            if coins_num+i >= list_num[0]:
                list_coin.pop()
                return
            self.coinChangeCoreII(coins[:-1],remainder,coins_num+i,list_num,list_coin)
            list_coin.pop()
    
    def coinChangeCore(self,coins,amount,coins_num,list_num):
        if amount==0:
            if list_num[0] > coins_num:
                list_num[0] = coins_num
            return True
        elif amount<0:
            return False
        elif len(coins)==0:
            return False
        num = amount//coins[-1]+1
        for i in range(num)[::-1]:
            remainder = amount-coins[-1]*i
            if coins_num+i > list_num[0]:
                return
            self.coinChangeCore(coins[:-1],remainder,coins_num+i,list_num)
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        remainder = amount - amount//coins[-1]*coins[-1]
        list_num = [21473648]
        coins.sort()
        self.coinChangeCoreII(coins, amount, 0, list_num,[])
        if list_num[0]!=21473648:
            return list_num[0]
        else:
            return -1
        
sol  = Solution()
print(sol.coinChange([243,291,335,209,177,345,114,91,313,331]
,amount=7367))