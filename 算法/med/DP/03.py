class Solution:
    def __init__(self):
        self.list_coin = {}
        
    def add_list_coin(self,value):
        if not self.list_coin.get(value):
            self.list_coin[value] = 1
        else:
            self.list_coin[value] += 1
    
    def coinChangeCore(self, coins,amount,num_path,list_path):
        for value in coins:
            if value > amount:
                continue
            elif value == amount:
                list_path.append(num_path+1)
                return True
            if self.coinChangeCore(coins,amount-value,num_path+1,list_path):
                self.add_list_coin(value)
                return True
        return False

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        list_path = []
        coins.sort(reverse=True)
        self.coinChangeCore(coins,amount,0,list_path)
        if len(list_path) == 0:
            return -1
        return min(list_path)
    
    # def coinChange(self, coins, amount):
    #     list_path = {}
    #     while amount>0:
    #         for coin in coins:
    #             a = amount
    #             a -= coin
    #             if a>=0:
    #                 list_path[a] = coin
    #             else:
    #                 coins.remove(coin)
    #         amount-=sorted(list_path.items(),key=lambda x:x[0])[0][1]
    #         print(amount)
            
        
            
sol  = Solution()
print(sol.coinChange([186,419,83,408],amount=6249))
print(sol.list_coin)