class Solution:
    def existCore(self,nums,i,j,str,n):
        if i<0 or j<0 or i >= len(nums) or j >= len(nums[0]):
            return False
        if nums[i][j]==str[n]:
            nums[i][j] = '*'
            if n == len(str)-1:
                return True
            ex =  (self.existCore(nums,i+1,j,str,n+1) or
            self.existCore(nums,i-1,j,str,n+1) or
            self.existCore(nums,i,j-1,str,n+1) or
            self.existCore(nums,i,j+1,str,n+1))
            nums[i][j] = str[n]
            return ex
        else:
            return False


    def exist(self, board, word):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(word)==0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.existCore(board,i,j,word,0):
                        return True
        return False

board = [
  ['a','a']
]
word = "aaa"
sol = Solution()
print(sol.exist(board,word))