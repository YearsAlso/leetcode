def init(n):
    pre = [-1] * n
    for i in range(len(pre)):
        pre[i] = i
    return pre


def find(pre, x):
    while x != pre[x]:
        x = pre[x]
    return pre[x]


def union(pre, x, y):
    x = find(pre, x)
    y = find(pre, y)
    while x != y:
        pre[x] = y
        
        
def main():
    n  =int(input())
    m = input()
    pre = init(n)
    list1 = [(1, 2), (2, 3), (4, 5)]
    for x, y in list1:
        union(pre, x, y)
    num=0
    for i,value in enumerate(pre):
        if i == value:
            num+=1
    print(num)
    
if __name__ == '__main__':
    main()
