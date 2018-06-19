class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        lines = len(board)
        if lines == 0:
            return
        rows = len(board[0])
        if rows==0:
            return
        dict_change = {}
        for line in range(lines):
            for row in range(rows):
                life_num = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if line+i<0 or line+i>=lines  :
                            break
                        if row+j<0 or row+j>=rows:
                            continue
                        if board[line+i][row+j]:
                            life_num += 1
                print(line,"-",row,":",life_num)
                if life_num < 2:
                    dict_change[(line,row)] = 0
                elif life_num==2 and board[line][row]==1:
                    dict_change[(line,row)] = 1
                elif life_num==3:
                    dict_change[(line,row)] = 1
                elif life_num>3:
                    dict_change[(line,row)] = 0
                
        for key,value in dict_change.items():
            board[key[0]][key[1]] = value
        print(board)

sol = Solution()
sol.gameOfLife([[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]])