import queue

class Solution:
    def isSign(self,value):
        list_sign = ["+", "-", "*", "/"]
        for sign in list_sign:
            if sign==value:
                return True
        return False
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        num_list = []
        for value in tokens:
            if self.isSign(value):
                val2 = int(num_list.pop())
                val1 = int(num_list.pop())
                print("%s %s %s" % (val1,value,val2))
                num_list.append({"+":val1+val2,"-":val1-val2,"*":val1*val2,"/":int(val1/val2) if val2!=0 else 0 }.get(value))
            else:
                num_list.append(int(value))
        return num_list[0]
    
sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))