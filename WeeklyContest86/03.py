class Solution:
    def splitIntoFibonacci(self, S):
            """
            :type S: str
            :rtype: List[int]
            """
            if S[0] == '0':
                return None
            
            length = len(S) - 2
            list_num = []
            
            for start in range(length):
                for end in range(start+2,length+2)[::-1]:
                    #print(end)
                    for mid1 in range(start+1,end):
                        for mid2 in range(mid1+1,end)[::-1]:
                            if int(S[start:mid1]) + int(S[mid1:mid2]) == int(S[mid2:end]):
                                print(S[start:mid1], '+', S[mid1:mid2], '=', S[mid2:end])
                                if len(list_num) == 0:
                                    list_num.append(S[start:mid1])
                                    list_num.append(S[mid1:mid2])
                                list_num.append(S[mid2:end])
                                #end = len(str(int(S[mid1:mid2])+int(S[mid2:end])))
                                #start = mid1
            return list_num


def main():
    sol = Solution()
    print(sol.splitIntoFibonacci("123456579"))

if __name__ == '__main__':
    main()