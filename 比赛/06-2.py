def fun(n, list_n1):
    if n == 1:
        return list_n1[0]
    elif n == 2:
        return (list_n1[n-1])
    elif n == 3:
        return list_n1[0] + list_n1[1] + list_n1[2]
    else:
        return fun(n - 2, list_n1) + min(2 * list_n1[0] + list_n1[n - 1] + list_n1[n - 2],
                                  2 * list_n1[1] + list_n1[0] + list_n1[n - 1])


n = int(input())
list_n1 = []
list_n2 = []
for value in input().split(" "):
    list_n1.append(int(value))
list_n1.sort()

print(fun(n, list_n1))