class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        list_sub = []
        for i in range(1, len(A)):
            if A[i] - A[i - 1] > 0:
                list_sub.append(1)
            elif A[i] - A[i - 1] < 0:
                list_sub.append(-1)
            else:
                list_sub.append(0)
        
        mountain = []
        isLow = False
        mountains = [0]
        for i, value in enumerate(list_sub):
            if value > 0 and isLow == False:
                mountain.append(value)
            elif value < 0 and len(mountain) > 0:
                isLow = True
                mountain.append(value)
            elif isLow == True and value > 0:
                mountains.append(len(mountain) + 1)
                mountain = []
                mountain.append(value)
                isLow = False
            elif value == 0 and isLow:
                mountains.append(len(mountain) + 1)
                mountain = []
                isLow = False
            elif value == 0 and isLow == False:
                mountain = []
                isLow = False
        if isLow == True:
            mountains.append(len(mountain) + 1)
        return max(mountains)


def main():
    sol = Solution()
    print(sol.longestMountain([2,1,4,7,3,2,5]))


if __name__ == '__main__':
    main()
