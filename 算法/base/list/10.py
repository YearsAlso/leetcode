def isValidSudoku(board):
    i=0
    while i<9:
        j=0
        list = []
        while j<9:
            list.append(board[j][i])
            j+=1
        n = 1
        while n<=9:
            try:
                con = list.count(str(n))
                if con >1:
                    return False
            except:
                pass
            n+=1
        i+=1

    j = 0
    while j<9:
        n = 1
        while n<=9:
            try:
                con = board[j].count(str(n))
                if con > 1:
                    return False
            except:
                pass
            n+=1
        j+=1
    i+=9


    g=0
    while g<9:
        list=[]
        i = 0
        while i<3:
            j = 0
            while j<3:

                list.append(board[i+int(int(g/3)*3)][j+int(int(g%3)*3)])
                j+=1
            i+=1
        n = 1

        while n<=9:
            try:
                con = list.count(str(n))
                if con > 1:
                    print(con)
                    return False
            except:
                pass
            n+=1

        g+=1
        print(g)
    return True

print(isValidSudoku([[".","8","7","6","5","4","3","2","1"],
                     ["2",".",".",".",".",".",".",".","."],
                     ["3",".",".",".",".",".",".",".","."],
                     ["4",".",".",".",".",".",".",".","."],
                     ["5",".",".",".",".",".",".",".","."],
                     ["6",".",".",".",".",".",".",".","."],
                     ["7",".",".",".",".",".",".",".","."],
                     ["8",".",".",".",".",".",".",".","."],
                     ["9",".",".",".",".",".",".",".","."]]))