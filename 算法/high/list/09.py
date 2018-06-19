import queue


class Solution:
    def calculate(self, s):
        num_q = queue.LifoQueue()
        num_q.put(0)
        sign_q = queue.LifoQueue()
        num = 0
        for c in s:
            if c in ['*', "/", '+', "-"]:
                num_q.put(0)
                if c == "-":
                    num_q.put(-1 * num)
                if c == '+':
                    num_q.put(num)
            else:
                num = num*10 + int(c)
        return sum(num_q)
    

def main():
    sol = Solution()
    print(sol.calculate("14/3*2"))


if __name__ == "__main__":
    main()
