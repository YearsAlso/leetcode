#coding=utf-8
import math
import collections


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0:
            return []
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        t_dict = collections.defaultdict()
        t_list = []
        num = 0
        for i, value in enumerate(s):
            if value in t:
                if num < len(t) :
                    if t_dict.get(value) == None:
                        num += 1
                t_dict[value] = i
                if num == len(t):
                    t_list.append([v for k, v in t_dict.items()])
        if len(t_list) == 0:
            return ""
        sum_list = []
        for list in t_list:
            sum = 0
            for index in list:
                sum += abs(index - list[0])
            sum_list.append(sum)
        s += ' '
        count = sum_list.index(min(sum_list))
        t_min = min(t_list[count])
        t_max = max(t_list[count])
        return s[t_min:t_max + 1]


def main():
    sol = Solution()
    print(sol.minWindow("bbaa", "aba"))


if __name__ == "__main__":
    main()
