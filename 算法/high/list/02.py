class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        min_line = 0
        max_line = len(matrix)
        min_row = 0
        max_row = len(matrix[0])
        length = max_line*max_row
        list_num = []
        step = 0
        while(len(list_num)<length):
            if(step==0):
                for i in range(min_row,max_row):
                    list_num.append(matrix[min_line][i])
                min_line+=1
                step=(step+1)%4
            elif (step == 1):
                for j in range(min_line,max_line):
                    list_num.append(matrix[j][max_row-1])
                max_row-=1
                step=(step+1)%4
            elif (step == 2):
                for i in range(min_row,max_row)[::-1]:
                    list_num.append(matrix[max_line-1][i])
                max_line-=1
                step=(step+1)%4
            elif (step == 3):
                for j in range(min_line,max_line)[::-1]:
                    list_num.append(matrix[j][min_row])
                min_row+=1
                step=(step+1)%4
        return list_num
    
sol = Solution()
print(sol.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [14,23,21,15]
]))