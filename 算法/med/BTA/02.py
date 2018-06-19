import copy
class Solution:
    # def generateParenthesisCore(self,n,str,list_str):
    #     get_str = "".join(str)
    #     if n==0:
    #         if list_str.count(get_str)>0:
    #             return
    #         print(get_str)
    #         list_str.append(get_str)
    #         return
    #     mid = len(str)//2
    #     temp = copy.copy(str)
    #     str.insert(mid, ')')
    #     str.insert(mid, '(')
    #     self.generateParenthesisCore(n-1,str,list_str)
    #
    #     str = copy.copy(temp)
    #     str.insert(mid - 1, ')')
    #     str.insert(mid - 1, '(')
    #     self.generateParenthesisCore(n - 1, str, list_str)
    #
    #     str = copy.copy(temp)
    #     str.insert(mid + 1, ')')
    #     str.insert(mid + 1, '(')
    #     self.generateParenthesisCore(n - 1, str, list_str)
    #
    #
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     if n==1:
    #         return ["()"]
    #     if n==0:
    #         return []
    #     lis_str = []
    #     self.generateParenthesisCore(n-1,["(",")"],lis_str)
    #     return lis_str

    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack:
                return False
            elif c == ')' and stack.pop() != '(':
                return False
            elif c == '}' and stack.pop() != '{':
                return False
            elif c == ']' and stack.pop() != '[':
                return False
        return not stack

    def generateParenthesisCore(self, n1,n2,list_str,ele_str):
        if n1==0 and n2==0:
            list_str.append(ele_str)
        if n1 :
            self.generateParenthesisCore(n1-1, n2, list_str, ele_str+"(")
        if n1 < n2:
            self.generateParenthesisCore(n1, n2 - 1, list_str, ele_str+")")

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1:
            return ["()"]
        if n==0:
            return []
        list_str = []
        self.generateParenthesisCore(n,n,list_str,"")

        return list_str


sol = Solution()
print(sol.generateParenthesis(4))