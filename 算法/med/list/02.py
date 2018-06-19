def setRowZeroesCore(matrix, row):
    i = 0
    j = 0
    while i < len(matrix[0]):
        if i == row:
            j = 0
            while j < len(matrix):
                matrix[j][i] = 0
                j += 1
        i += 1


def setLineZeroesCore(matrix, line):
    i = 0
    j = 0
    while i < len(matrix):
        if i == line:
            j = 0
            while j < len(matrix):
                matrix[i][j] = 0
                j += 1
        i += 1


def setZeroes(matrix):
    ignore_rows = []
    ignore_lines = []
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == 0:
                if not i in ignore_lines:
                    ignore_lines.append(i)
                if not j in ignore_rows:
                    ignore_rows.append(j)
            j += 1
        i += 1
    for row in ignore_rows:
        setRowZeroesCore(matrix, row)

    for line in ignore_lines:
        setLineZeroesCore(matrix, line)


zero = [
    [1, 1, 1], [1, 0, 1], [1, 1, 1]
]


setZeroes(zero)
for value in zero:
    print(value)
