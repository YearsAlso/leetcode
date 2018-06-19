class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if len(S)==0:
            
            if len(T)==0:
                return True
            return False
        elif len(T)==0:
            return False
        str1 = ""
        str2 = ""
        for value in S:
            if value == "#":
                if len(str1) > 0:
                    str1 = str1[:-1]
                continue
            str1+=value
            
        for value in T:
            if value == "#":
                if len(str2)>0:
                    str2 = str2[:-1]
                continue
            str2+=value
            
        if str1 == str2:
            return True
        return False
            



def main():
    sol = Solution()
    print(sol.backspaceCompare("a##c","#a#c"))

if __name__ == '__main__':
    main()