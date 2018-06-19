class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length_row = len(grid[0])
        length_len = len(grid)
        num = 0
        for i in range(2, length_row):
            for j in range(2, length_len):
                sum = grid[j][i] + grid[j][i - 2] + grid[j][i - 1]
                
                if grid[j - 1][i] + grid[j - 2][i] + grid[j][i] == sum and grid[j - 1][i - 1] + grid[j - 2][i - 1] + \
                        grid[j][i - 1] == sum and grid[j - 1][i - 2] + grid[j - 2][i - 2] + grid[j][i - 2] == sum \
                        and grid[j - 1][i] + grid[j - 1][i - 1] + grid[j - 1][i - 2] == sum and grid[j - 2][i] + \
                        grid[j - 2][i - 1] + grid[j - 2][i - 2] == sum \
                        and grid[j - 2][i] + grid[j - 1][i - 1] + grid[j][i - 2] == sum and grid[j - 2][i - 2] + \
                        grid[j - 1][i - 1] + grid[j][i] == sum:
                    if grid[j][i] < 10 and grid[j - 1][i] < 10 and grid[j - 2][i] < 10 and grid[j][i - 1] < 10 and \
                            grid[j - 1][i - 1] < 10 and grid[j - 2][i - 1] < 10 and grid[j][i - 2] < 10 and grid[j - 1][
                        i - 2] < 10 and grid[j - 2][i - 2] < 10:
                        if grid[j][i] > 0 and grid[j - 1][i] > 0 and grid[j - 2][i] > 0 and grid[j][i - 1] > 0 and \
                                grid[j - 1][i - 1] > 0 and grid[j - 2][i - 1] > 0 and grid[j][i - 2] > 0 and \
                                grid[j - 1][i - 2] > 0 and grid[j - 2][i - 2] > 0:
                            num += 1
                            print(sum)
                            print([[grid[j - 2][i - 2], grid[j - 2][i - 1], grid[j - 2][i]],
                                   [grid[j - 1][i - 2], grid[j - 1][i - 1], grid[j - 1][i]],
                                   [grid[j][i - 2], grid[j][i - 1], grid[j][i]]])
        return num


def main():
    sol = Solution()
    print(sol.numMagicSquaresInside([[10, 3, 5], [1, 6, 11], [7, 9, 2]]))


if __name__ == '__main__':
    main()