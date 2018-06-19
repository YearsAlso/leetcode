def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    length = len(matrix[0])
    i = 0
    sum_list = []
    while i < length:
        rev_list = []
        for value in matrix:
            rev_list.append(value[i])
        rev_list.reverse()
        sum_list.append(rev_list)
        i += 1
    matrix.clear()
    matrix.extend(sum_list)
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
