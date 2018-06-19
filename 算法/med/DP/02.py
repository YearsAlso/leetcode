class Solution:
    def uniquePathsCore(self, i,j,m, n,list_path):
        if i>m or j>n:
            #list_path.append(False)
            return
        elif i==m and j==n:
            list_path.append(True)
            return
        else:
            self.uniquePathsCore(i+1,j,m,n,list_path)
            self.uniquePathsCore(i,j+1,m,n,list_path)
            return
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # list_path = []
        # self.uniquePathsCore(1,1,m,n,list_path)
        # return sum(list_path)
        list_path = [[1],[1,2]]
        
        max_num = max(m,n)
        min_num = min(m,n)
        if max_num<3:
            return list_path[max_num-1][min_num-1]
        for i in range(2,max_num):
            for j in range(i+1):
                if j == i:
                    list_path[i].append(list_path[i][j-1]*2)
                elif j == 0:
                    list_path.append([])
                    list_path[i].append(1)
                else:
                    list_path[i].append(list_path[i-1][j] + list_path[i][j-1])
        print(list_path)
        return list_path[max_num-1][min_num-1]

    
sol = Solution()
while True:
    m,n = [int(a) for a in input().split(" ")]
    if m==n and m==0:
        break
    print(sol.uniquePaths(m,n))