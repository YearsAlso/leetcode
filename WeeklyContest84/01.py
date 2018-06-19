class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A)==0:
            return []
        
        for value in A:
            value.reverse()
            
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        return A
                    
                    
sol = Solution()
A =  [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(sol.flipAndInvertImage(A))