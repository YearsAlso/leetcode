import queue


class Solution:
    def calculate(self, s):
        num_q = queue.LifoQueue()
        num = 0
        op = ''
        for i,c in enumerate(s):
            if c.isnumeric():
                num = num*10 + int(c)
            if c in ['*', "/", '+', "-"] or i == len(s)-1:
                if op == "-":
                    num = -1 * num
                if op == '+':
                    num = num
                if op=='*':
                    num = int(num_q.get() * num)
                if op=='/':
                    num = int(num_q.get() / num)
                op = c
                num_q.put(num)
                num = 0
            
        
        while not num_q.empty():
            num += num_q.get()
        return int(num)
    

def main():
    sol = Solution()
    print(sol.calculate("14-3/2"))


if __name__ == "__main__":
    main()
