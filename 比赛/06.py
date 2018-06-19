# def bridg(nums):
#     time = 0
#     if len(nums) == 1:
#         return nums[0]
#     elif len(nums) == 2:
#         return max(nums)
#     elif len(nums) == 3:
#         return nums[0] +nums[1]+nums[2]
#     list1 = nums
#     list2 = nums
#     list1.pop(0)
#     list2.pop(0)
#     list2.pop()
#     time += min(bridg(list1),bridg(list2))
#     return time

n = int(input())
list_n1 = []
list_n2 = []
for value in input().split(" "):
    list_n1.append(int(value))


if n == 1:
    print(list_n1[0])
elif n == 2:
    print(max(list_n1))
elif n == 3:
    print(list_n1[0] + list_n1[1] + list_n1[2])
else:

    list_n1.sort()
    head1 = min(list_n1)
    list_n1.remove(head1)

    fun1_time = 0
    for value in list_n1:
        fun1_time+=value
        fun1_time+=head1

    fun1_time-=head1
    print(fun1_time)

    head2 = min(list_n1)
    list_n1.remove(head2)

    i = 1
    time = 0

    while i < len(list_n1):
        list_n2.append(list_n1[i])
        time += 1
        i += 2

    add = 0
    for value in list_n2:
        add += value
    fun2_time = add + (n - 1) * head2 + time * head1
    print(fun2_time)

    print(min(fun2_time,fun1_time))
